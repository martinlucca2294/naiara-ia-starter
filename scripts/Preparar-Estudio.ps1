# Compatible with Windows PowerShell 5.1 and PowerShell 7.
# No network, installs, credentials, or global configuration changes.
[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$kitRoot = Split-Path -Parent $PSScriptRoot
$privateRoot = Join-Path $kitRoot 'local'
$vaultRoot = Join-Path $privateRoot 'Cerebro'
$templateRoot = Join-Path $kitRoot 'vault-template'
if (-not (Test-Path -LiteralPath $templateRoot -PathType Container)) {
    throw 'No se encuentra vault-template. Ejecuta el script desde el kit completo.'
}
foreach ($directory in @($privateRoot, $vaultRoot, (Join-Path $privateRoot 'Proyectos'), (Join-Path $privateRoot 'Entregas'), (Join-Path $privateRoot 'Revisiones'))) {
    if (Test-Path -LiteralPath $directory) {
        $item = Get-Item -LiteralPath $directory -Force
        if (-not $item.PSIsContainer -or ($item.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
            throw "Ruta existente inesperada; no se modifica: $directory"
        }
    } else {
        New-Item -ItemType Directory -Path $directory | Out-Null
    }
}
$created = 0
$preserved = 0
foreach ($source in Get-ChildItem -LiteralPath $templateRoot -File -Filter '*.md') {
    $destination = Join-Path $vaultRoot $source.Name
    if (Test-Path -LiteralPath $destination) {
        $preserved++
    } else {
        # overwrite=false also protects against a file created after Test-Path.
        [IO.File]::Copy($source.FullName, $destination, $false)
        $created++
    }
}
Write-Output "Notas creadas: $created. Archivos existentes conservados: $preserved."
Write-Output "Abri esta carpeta como boveda en Obsidian: $vaultRoot"
Write-Output 'No se instalaron programas ni se conectaron cuentas. local/ requiere respaldo privado.'
