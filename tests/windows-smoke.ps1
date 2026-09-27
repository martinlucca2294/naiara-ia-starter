$ErrorActionPreference = 'Stop'
$kitRoot = Split-Path -Parent $PSScriptRoot
$testRoot = Join-Path ([IO.Path]::GetTempPath()) ('naiara-kit-' + [guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $testRoot | Out-Null
try {
    foreach ($name in @('scripts', 'vault-template', 'skills', '.agents', '.claude')) {
        Copy-Item -LiteralPath (Join-Path $kitRoot $name) -Destination $testRoot -Recurse
    }
    & (Join-Path $testRoot 'scripts/Preparar-Estudio.ps1')
    $state = Join-Path $testRoot 'local/Cerebro/01-Estado-actual.md'
    if (-not (Test-Path $state)) { throw 'No creo la memoria' }
    [IO.File]::AppendAllText($state, "`nMI DECISION PERSONAL`n")
    $before = (Get-FileHash $state).Hash
    & (Join-Path $testRoot 'scripts/Preparar-Estudio.ps1')
    if ((Get-FileHash $state).Hash -ne $before) { throw 'Sobrescribio memoria existente' }
    & (Join-Path $testRoot 'scripts/Diagnostico.ps1')
    & (Join-Path $testRoot 'scripts/Sync-Skills.ps1')
    $source = Join-Path $testRoot 'skills/naiara-onboarding/SKILL.md'
    $copy = Join-Path $testRoot '.claude/skills/naiara-onboarding/SKILL.md'
    [IO.File]::AppendAllText($source, "`nCambio autorizado de fuente`n")
    & (Join-Path $testRoot 'scripts/Sync-Skills.ps1')
    if ((Get-FileHash $source).Hash -ne (Get-FileHash $copy).Hash) { throw 'No sincronizo fuente' }
    [IO.File]::AppendAllText($copy, "`nCambio ajeno en copia`n")
    $modified = (Get-FileHash $copy).Hash
    $blocked = $false
    try { & (Join-Path $testRoot 'scripts/Sync-Skills.ps1') } catch { $blocked = $true }
    if (-not $blocked -or (Get-FileHash $copy).Hash -ne $modified) { throw 'No preservo copia editada' }
    Write-Output 'PASS: creacion, repeticion sin perdida, diagnostico, sincronizacion y conflicto.'
} finally {
    # Deletes only the uniquely created temporary test directory.
    Remove-Item -LiteralPath $testRoot -Recurse -Force
}
