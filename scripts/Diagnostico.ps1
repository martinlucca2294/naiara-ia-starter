[CmdletBinding()]
param()
$ErrorActionPreference = 'Stop'
$kitRoot = Split-Path -Parent $PSScriptRoot
Write-Output 'Diagnostico local: presencia, no autenticacion ni acceso a servicios.'
Write-Output "PowerShell: $($PSVersionTable.PSVersion)"
Write-Output "Kit: $kitRoot"
foreach ($name in @('git', 'node', 'npm', 'codex', 'claude', 'py', 'python', 'gh')) {
    $found = Get-Command $name -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($found) { Write-Output "$name : encontrado" }
    else { Write-Output "$name : no encontrado en PATH" }
}
foreach ($file in @('INICIO-IA.md', 'local/Cerebro/00-Inicio.md', 'local/Cerebro/01-Estado-actual.md')) {
    $exists = Test-Path -LiteralPath (Join-Path $kitRoot $file) -PathType Leaf
    Write-Output "$file : $exists"
}
Write-Output 'No se leyeron credenciales ni se enviaron datos por red.'
