# Windows desde cero

## Antes de instalar

Trabajamos con **Windows nativo y PowerShell**. WSL es una alternativa para proyectos que necesitan Linux; no es requisito inicial. Instalá de a una herramienta. Usá tus cuentas; una suscripción a un chat y el consumo de una API pueden tener facturación distinta.

Abrí Inicio, escribí **PowerShell** y abrilo normalmente. No hace falta empezar como administradora. Si es una computadora laboral administrada y una instalación está bloqueada, consultá a quien la administra.

Los bloques de esta guía se pegan en PowerShell, excepto los mensajes para conversar con la IA. No copies las líneas `PS C:\...>` que puedas ver en ejemplos de otras páginas. Enter ejecuta el comando; Ctrl+C detiene uno que sigue trabajando. En una conversación de IA, escribís pedidos en castellano.

## A. Ver qué ya existe

```powershell
$PSVersionTable.PSVersion
Get-Command git, node, npm, codex, claude, py -ErrorAction SilentlyContinue |
    Select-Object Name, Source
```

Si falta un nombre no implica que tu PC esté rota. Sólo indica que esa terminal no lo encontró. Cerrá y abrí una terminal nueva después de instalar.

## B. Instalar lo necesario

Elegimos Git para guardar versiones, Node.js LTS para herramientas web/CLI y una IA. Obsidian y Python se suman cuando llegues a memoria y Telegram. Descargá desde estas páginas oficiales:

| Herramienta | Descarga | Verificación |
|---|---|---|
| Git para Windows | https://git-scm.com/downloads/win | `git --version` |
| Node.js LTS | https://nodejs.org/en/download | `node --version` y `npm.cmd --version` |
| Obsidian | https://obsidian.md/download | Abrir la aplicación |
| Python 3.10 o posterior, para Telegram | https://www.python.org/downloads/windows/ | `py -3 --version` |
| GitHub CLI, opcional para publicar | https://cli.github.com/ | `gh --version` |

LTS significa una versión con soporte prolongado. En Python, si el instalador ofrece agregar Python a PATH, esa opción permite encontrarlo desde terminal; verificá siempre el comando final. Si `py` no existe pero `python --version` funciona y dice 3.10 o posterior, usá `python` en los ejemplos de Telegram. No necesitás comprar otra suscripción para estas herramientas; las IAs y servicios creativos tienen sus propios planes.

### Codex

Para usarlo por terminal, con Node instalado:

```powershell
npm.cmd install -g @openai/codex
codex --version
```

Si PowerShell bloquea el archivo `codex.ps1`, probá `codex.cmd --version` y usá `codex.cmd` para iniciarlo. No cambies la política global de Windows para resolver ese caso. Verificá el método npm en la pestaña correspondiente de la [guía oficial de CLI](https://learn.chatgpt.com/docs/codex/cli); si el proveedor cambia el método, seguí la guía actual.

Abrí la carpeta del kit y ejecutá `codex`. Completá el ingreso con tu cuenta de ChatGPT si esa opción está disponible. Revisá permisos y acceso del plan en la pantalla. Alternativa visual: [aplicación de escritorio para Windows](https://learn.chatgpt.com/docs/windows/windows-app); también tenés que seleccionar esta carpeta como proyecto. El nombre o menú puede variar según versión.

**Prueba:** pedile que lea README.md y diga los tres primeros pasos. Una versión impresa sólo confirma instalación; una respuesta leyendo tu archivo confirma que esa sesión puede trabajar aquí.

### Claude Code

Si tu Windows dispone de WinGet:

```powershell
winget install --id Anthropic.ClaudeCode --exact
```

Cerrá y abrí la terminal, luego:

```powershell
claude --version
claude
```

Seguí el ingreso en navegador con tu cuenta. Si WinGet no existe, usá la alternativa oficial para Windows de [Claude Code Quickstart](https://code.claude.com/docs/en/quickstart), acompañada por tu IA. No pegues instaladores encontrados en comentarios de redes.

Git para Windows también le permite utilizar Git Bash. Si aparece un error de shell, consultá [configuración Windows](https://code.claude.com/docs/en/setup) sin adivinar rutas. WinGet no actualiza Claude automáticamente: la actualización correspondiente es `winget upgrade Anthropic.ClaudeCode` cuando decidas actualizar.

**Prueba:** pedile leer el mismo README y verificar qué tarea dejó Codex en la memoria. Iniciar sesión en Claude web no demuestra que Claude Code tenga una sesión válida.

## C. Preparar tu espacio

Desde la carpeta del kit:

```powershell
Get-Content .\scripts\Preparar-Estudio.ps1
```

Esto sólo muestra el script. Tu IA puede explicarlo. Después ejecutá:

```powershell
& .\scripts\Preparar-Estudio.ps1
```

Si Windows lo bloquea por política, no la desactives. Tu IA puede hacer las mismas operaciones: crear `local/Cerebro`, copiar allí las notas de `vault-template` que falten y crear `local/Proyectos`, `local/Entregas` y `local/Revisiones`. Si se trata de un archivo descargado bloqueado y tu política permite scripts locales, pedile revisar el archivo y explicar `Unblock-File` sólo para ese archivo; no usar una excepción global.

**Prueba:** abrí `local/Cerebro/00-Inicio.md` y `01-Estado-actual.md`. La segunda ejecución debe conservar cualquier texto que ya escribiste. Luego seguí [memoria y dueto](02-dueto-y-memoria.md).

## D. Diagnóstico sencillo

```powershell
& .\scripts\Diagnostico.ps1
```

Este script no instala ni conecta nada y no lee claves. Muestra herramientas encontradas y presencia de archivos. Las conexiones deben comprobarse por separado.
