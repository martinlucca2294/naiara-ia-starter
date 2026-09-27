# Hola, Naiara

No hace falta que entiendas todo hoy. El primer objetivo es que una IA pueda trabajar en una carpeta tuya y explicarte lo que hace. Después vamos a crear una pieza de contenido y recién entonces sumar conexiones.

## 1. Guardá este kit

En la página de GitHub tocá el botón **Code → Download ZIP**. En Windows abrí Descargas, hacé clic derecho sobre el ZIP y elegí **Extraer todo**. Entrá a la carpeta extraída: adentro tienen que verse `README.md`, `INICIO-IA.md` y la carpeta `docs`.

Mové esa carpeta a un lugar fácil de encontrar. Por ejemplo, dentro de tu carpeta de usuario creá `IA` y guardala como `naiara-ia-starter`. No necesitás una cuenta de GitHub para descargar el ZIP público.

Si ya usás Git, en PowerShell podés descargarla así:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\IA" | Out-Null
Set-Location "$env:USERPROFILE\IA"
git clone https://github.com/martinlucca2294/naiara-ia-starter.git
Set-Location .\naiara-ia-starter
```

Si una carpeta con ese nombre ya existe, no borres nada. Abrila y pedile a la IA que determine si es el kit anterior o un proyecto diferente.

## 2. Elegí una IA para empezar

Si ya tenés **Codex o Claude Code instalado y con sesión iniciada**, pasá al punto 3. Si sólo usás ChatGPT o Claude en una pestaña del navegador, eso no significa que el programa de terminal esté instalado. Abrí [Windows desde cero](docs/01-windows.md); instalá primero uno de los dos.

También podés darle el enlace de este repositorio a la IA que ya usás:

> Quiero empezar con este kit en Windows. Leé EMPEZA-AQUI.md e INICIO-IA.md del repositorio y ayudame a instalar una sola IA primero. No sé usar la terminal. Mostrame una acción, qué tendría que ver y cómo comprobarla.

Si no puede acceder a GitHub, adjuntale esos dos archivos descargados. No des por hecho que leyó el repositorio: pedile que te nombre el primer paso de la guía.

## 3. Abrí la terminal en la carpeta

Dentro de la carpeta del kit, hacé clic derecho en un espacio vacío y elegí **Abrir en Terminal**, si aparece. Otra opción: hacé clic en la barra de dirección del Explorador, escribí `powershell` y presioná Enter.

La terminal es una ventana donde podés dar instrucciones al sistema. Primero escribí:

```powershell
Get-Location
Get-ChildItem
```

El primero muestra dónde estás; el segundo, los archivos. Tenés que ver `INICIO-IA.md`. Si no aparece, todavía no estás en la carpeta correcta. No pegues el siguiente comando hasta ubicarla.

Escribí **uno** de estos comandos, según lo que hayas instalado:

```powershell
codex
```

o:

```powershell
claude
```

Se abre una conversación. Iniciá sesión en el navegador si te lo pide. Las contraseñas se escriben en la página del proveedor, nunca en el chat.

## 4. Pegá tu primer mensaje

> Soy Naiara y quiero aprender a crear videos hiperrealistas, contenido para Instagram y páginas web. Leé INICIO-IA.md. Empecemos por la etapa 0. No des por hecho que tengo programas, cuentas o conexiones. Explicame sin jerga, preguntame como máximo tres cosas juntas y ayudame a comprobar cada paso. Quiero usar mi propia memoria en Obsidian y, más adelante, Codex y Claude juntos.

Tu IA debería decirte qué carpeta está leyendo, qué encontró instalado y qué falta. Todavía no necesita tus datos de Gmail, tarjetas o claves de API.

## 5. Primera meta, pequeña y visible

Elegí una idea: por ejemplo, una cafetería inventada. Pedí un guion de 15 segundos, tres escenas y una propuesta de estilo. Guardalo, cerrá la conversación y abrí una nueva. Si la IA puede retomar desde la nota guardada, ya aprendiste una de las partes más útiles de este sistema.

Podés decir **“más despacio”**, **“mostrame dónde hago clic”**, **“no entiendo esa palabra”** o **“hagamos una cosa por vez”**. El kit está diseñado para adaptarse a tu ritmo.
