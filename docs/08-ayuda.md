# Cuando algo no funciona

Copiá el texto del error y contá qué estabas intentando. Antes de compartir una captura, ocultá claves, códigos de acceso y datos personales. No borres carpetas ni reinstales todo como primer intento.

| Lo que ves | Primer paso útil |
|---|---|
| “Comando no reconocido” | Abrir terminal nueva; `Get-Command nombre`; revisar instalación y PATH |
| PowerShell bloquea npm.ps1 | Usar `npm.cmd`; no cambiar política global |
| No se puede ejecutar un script del kit | Revisar contenido y política; pedir a la IA las operaciones manuales equivalentes |
| La IA dice no ver mis archivos | Confirmar si está en navegador, nube o Windows local; indicar carpeta real |
| Instalé un plugin y no aparece | Abrir sesión nueva, comprobar cuenta/cliente y herramientas disponibles |
| Higgsfield conectado, pero no genera | Verificar sesión, plan, saldo y parámetros sin repetir generaciones |
| El trabajo quedó “pending” | Consultar su ID, no enviar otra generación idéntica |
| Gmail encuentra un correo pero no descarga el adjunto | Revisar capacidades reales del conector; no asumir acceso a adjuntos |
| El bot Telegram no responde | PC/proceso encendido, token válido, chat vinculado y única instancia; ver guía del bot |
| `409` en Telegram | Puede haber otro consumidor o webhook; no borrarlo sin revisar |
| Git muestra local/ para subir | Revisar .gitignore y si se agregó forzadamente; detener publicación y retirar del staging preservando archivos |
| Obsidian aparece vacío | Abrir la carpeta local/Cerebro correcta, no crear una bóveda nueva encima |
| Un archivo fue editado por ambos agentes | Detener escrituras, conservar ambas versiones y comparar; no elegir la última ciegamente |
| Un enlace web no abre desde el celular | Distinguir localhost/vista previa privada/URL pública |

## Pedir ayuda con contexto

> Estoy en Windows, dentro de esta carpeta: [ruta]. Quería [resultado]. Ejecuté [comando sin secretos] y salió [error]. Revisá primero en lectura. Decime qué pudiste comprobar y proponé el siguiente paso más pequeño.

## Antes de actualizar

Guardá trabajo y copia privada de `local/`. Anotá versiones actuales. Actualizá una herramienta por vez desde su método oficial, abrí sesión nueva y repetí una prueba pequeña. No cambies simultáneamente modelo, configuración, skills y servidor MCP: después cuesta saber qué rompió el flujo.

Si descargaste ZIP, extraé la versión nueva en **otra carpeta**, conservá la anterior y trasladá `local/` con ayuda de la IA. No arrastres carpetas de configuración global ni credenciales. Si clonaste con Git, revisá `git status` antes de `git pull`; resolver cambios propios preservándolos.

## Costos y tiempos

Las IAs de coordinación, los créditos creativos, almacenamiento y alojamiento pueden ser cargos diferentes. La plantilla de presupuesto distingue costo estimado, consumo informado por el proveedor y saldo comprobado. No elijas automáticamente lo más caro: probá una muestra con la calidad que permita evaluar el aspecto importante.

No repitas una generación o un envío con resultado incierto hasta consultar si la operación ya existe. Una notificación de error de red no garantiza que no se haya cobrado o enviado.

## Qué no hace este kit

No mantiene tu PC encendida, no ejecuta trabajo 24/7, no transfiere suscripciones, no publica Instagram automáticamente, no sincroniza chats y no garantiza la calidad creativa. Te da procedimientos, plantillas y herramientas pequeñas para construir esas capacidades gradualmente y verificar lo que funciona.
