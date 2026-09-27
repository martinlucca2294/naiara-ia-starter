# Conexiones, una por vez

Una **API** es una interfaz para que programas hablen con un servicio. **MCP** es un protocolo que permite a una IA descubrir y usar herramientas. Un **conector** resuelve el acceso a un servicio; un **plugin** puede reunir herramientas y skills. Una **skill** explica cómo trabajar, pero no da acceso a una cuenta.

Empezá por la conexión que necesites para tu proyecto. No conectes todo sólo porque aparece en una lista. No se transfieren las cuentas de otra persona al descargar este kit.

## Prueba común a todas

1. Identificá el proveedor oficial y el cliente desde donde lo vas a usar: Codex CLI, aplicación, Claude Code o Claude web.
2. Instalá o agregá la integración desde el catálogo oficial que tenga ese cliente.
3. Iniciá sesión en la ventana del proveedor y revisá cuenta y permisos solicitados.
4. Abrí una nueva sesión si el cliente lo requiere.
5. Hacé una lectura pequeña de algo preparado por vos.
6. Compará el resultado con el original. Registrá fecha, cliente, alcance probado y limitaciones en `local/Cerebro/03-Conexiones.md`.

Estados útiles: **pendiente → instalada → autenticada → lectura probada → escritura probada para una acción concreta**. No los saltees.

## Higgsfield: primero creación y control de créditos

Consultá la [guía oficial de integración](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent), verificada para este kit el 27-sep-2026. Indica caminos diferentes:

- **ChatGPT/Codex compatible con plugins:** buscar el plugin oficial Higgsfield e iniciar sesión; comprobar su disponibilidad en la sesión concreta.
- **Claude web/escritorio:** Settings → Connectors → agregar el conector `https://mcp.higgsfield.ai/mcp` y autorizar en el navegador.
- **Claude Code:** la guía del proveedor propone su CLI. Con Node disponible: `npm.cmd i -g @higgsfield/cli`, luego `higgsfield auth login`. Revisar las skills de `higgsfield-ai/skills` antes de instalarlas.

La disponibilidad depende de cuenta, plan, cliente y herramientas expuestas. Si una función no aparece, usar la web oficial o dejarla pendiente. No asumir paridad entre clientes, ni que pagar una suscripción al chat paga generaciones en Higgsfield.

### Prueba sin generación

Pedile a tu IA:

> Comprobá la conexión a mi cuenta de Higgsfield con una consulta de lectura. Mostrame qué capacidades están disponibles y el saldo si hay una herramienta para consultarlo. No generes nada. Si no podés consultar alguno de esos datos, marcá ese dato como pendiente.

Después creá una prueba concreta: duración, referencia, modelo disponible, formato, voz y máximo de intentos. Usá la estimación que informe la herramienta en ese momento. Si no ofrece costo previo, decilo y definí con Naiara cómo acotar el gasto desde el panel; nunca inventes una tarifa.

**Prueba completa posterior:** generación autorizada, identificador del trabajo, archivo descargado, duración/dimensiones/audio comprobados y costo registrado. Un estado `completed` no verifica que la frase se entienda o que el rostro sea consistente: eso se revisa viendo y escuchando.

## Gmail y Google Drive

Para Codex, la documentación vigente describe el catálogo de plugins; en CLI se abre con `/plugins`. Buscar Gmail y Google Drive, conectar cuenta propia y abrir una sesión nueva. En Claude, usar los conectores de Google Workspace desde configuración. Ver [plugins de OpenAI](https://learn.chatgpt.com/docs/plugins) y [Google Workspace en Claude](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors).

### Primera prueba de Drive

1. Creá manualmente una carpeta `Estudio creativo - pruebas`.
2. Adentro, un documento `Prueba IA` con una frase inventada que reconozcas.
3. Pedí a la IA leer ese documento específico y devolver la frase con enlace.
4. Si querés probar escritura, autorizá crear un único documento de prueba ahí y abrilo para comprobar el contenido.

No confundas autorizar toda la cuenta con limitar técnicamente el conector a una carpeta: inspeccioná el permiso real. No uses documentos de clientes en la primera prueba.

### Primera prueba de Gmail

1. Mandate vos un correo con un asunto único, por ejemplo `PRUEBA-ESTUDIO-001`.
2. Pedí buscar sólo ese mensaje y confirmar asunto y una frase del cuerpo.
3. Probá luego crear un borrador si la herramienta lo permite. Revisalo en Gmail.
4. Para probar envío, especificá destinatario propio y texto exacto. Un borrador creado no equivale a enviado; la IA debe comprobar la respuesta del servicio.

Leer correos no demuestra que se puedan descargar adjuntos o enviar archivos. Probá cada función que necesites. Si un plugin no ofrece la operación, la IA debe decirlo y proponer una alternativa oficial; no improvisar un MCP desconocido con acceso a todo tu correo.

## GitHub para archivos y versiones

Git guarda cambios localmente; GitHub permite alojar repositorios. Para tus proyectos reales, empezá con un repositorio privado en tu cuenta. Este kit puede descargarse sin conectar GitHub.

Cuando necesites publicar código o tener respaldo remoto, instalá el CLI oficial y ejecutá:

```powershell
gh auth login
gh auth status
```

Elegí GitHub.com y el inicio mediante navegador cuando se ofrezca. No pegues tokens en el chat. La IA debe confirmar la cuenta antes de crear un repositorio. Autenticarse con `gh` no configura automáticamente un plugin de GitHub en otra aplicación: probá el camino que realmente vayas a usar.

**Prueba:** repositorio privado vacío propio, archivo de prueba, commit, push y apertura de ese archivo en GitHub. Verificá qué se va a subir con `git status` y la lista de archivos preparados. No subir videos pesados al repositorio de código; usar almacenamiento elegido para material multimedia.

## Cloudflare y publicación web

Conectalo cuando haya un sitio listo. Usá tu cuenta y un proyecto separado para cada web. Primero publicá una vista previa; agregá dominio propio después de confirmar el destino correcto. No necesitás compartir contraseñas de registradores en un chat. [Guía de publicación](07-web-y-publicacion.md).

## Otros MCP: agregar con propósito

Antes de agregar uno, la IA tiene que explicar: quién lo mantiene, para qué hace falta, qué permisos pide, cómo se autentica, qué prueba lo verifica y cómo se quita. Preferir integración oficial o herramienta nativa cuando cubra la necesidad. No instalar un paquete por popularidad ni copiar configuraciones completas de otra computadora.

Para un servidor HTTP oficial que aún no esté configurado, primero consultar `codex mcp --help` o `claude mcp --help`. Los formatos no son idénticos. No ejecutar un ejemplo con una URL inventada. No agregar el mismo servicio por plugin y MCP sin necesidad: puede duplicar herramientas y complicar la cuenta utilizada.

## Desconectar o cambiar cuenta

Usá el panel de conexiones del cliente y, cuando corresponda, el de aplicaciones autorizadas del proveedor. Cerrá/reabrí la sesión y verificá que ya no haya acceso. Revocar una integración no borra los archivos que ya descargaste; revisá esos archivos aparte. Actualizá la memoria sin guardar tokens.
