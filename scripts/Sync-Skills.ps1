# Maintainer helper. Sources: skills/. Targets: repo-local copies only.
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$kitRoot = Split-Path -Parent $PSScriptRoot
$manifestPath = Join-Path $kitRoot 'skills/manifest.json'
$old = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json
$next = [ordered]@{}
$copies = @()
foreach ($skill in Get-ChildItem -LiteralPath (Join-Path $kitRoot 'skills') -Directory) {
    $source = Join-Path $skill.FullName 'SKILL.md'
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw "Falta SKILL.md: $($skill.Name)" }
    $newHash = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()
    $property = $old.PSObject.Properties[$skill.Name]
    $oldHash = if ($property) { $property.Value } else { $null }
    foreach ($base in @('.agents/skills', '.claude/skills')) {
        $target = Join-Path (Join-Path (Join-Path $kitRoot $base) $skill.Name) 'SKILL.md'
        if (Test-Path -LiteralPath $target) {
            $targetHash = (Get-FileHash -LiteralPath $target -Algorithm SHA256).Hash.ToLowerInvariant()
            if ($targetHash -ne $newHash -and $targetHash -ne $oldHash) {
                throw "Copia editada fuera de skills/. Resolver antes de sincronizar: $target"
            }
        }
        $copies += [pscustomobject]@{ Source = $source; Target = $target }
    }
    $next[$skill.Name] = $newHash
}
# All conflicts are checked before any copy is updated.
foreach ($copy in $copies) {
    $directory = Split-Path -Parent $copy.Target
    if (-not (Test-Path -LiteralPath $directory)) { New-Item -ItemType Directory -Path $directory -Force | Out-Null }
    Copy-Item -LiteralPath $copy.Source -Destination $copy.Target -Force
}
$json = ($next | ConvertTo-Json) + "`n"
[IO.File]::WriteAllText($manifestPath, $json, (New-Object Text.UTF8Encoding($false)))
Write-Output "Skills sincronizadas: $($next.Count). No se modificaron carpetas globales."
