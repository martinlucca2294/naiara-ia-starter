# Una web que se vea bien y funcione

## Antes de tocar código

Definí qué tiene que lograr la página: mostrar un portfolio, recibir una consulta o vender una propuesta. Guardá texto aprobado, marca, imágenes con permiso, contacto y destinos de cada botón en un brief. Una referencia visual sirve para comunicar estilo; no autoriza copiar material de otra marca.

Primera práctica: una página de un estudio ficticio, sin pagos ni datos reales. Pedile a la IA que la cree dentro de `local/Proyectos/mi-primera-web` con HTML/CSS/JavaScript sencillo o una tecnología que ya tengas. Que explique cómo abrirla. No hace falta una base de datos para una portada, servicios y contacto.

> Armá una web de portfolio con una portada clara, tres trabajos ficticios y contacto. Mostrame primero la propuesta visual. Cada enlace debe tener destino identificable. Si no definimos recepción de consultas, usá una demostración rotulada y no afirmes que el formulario envía. Probá en celular y escritorio antes de entregarla.

## Revisar en un navegador

- Abrí la página desde el servidor local que indique la IA, no sólo desde una captura.
- Probá escritorio y anchos móviles, por ejemplo 390 y 768 píxeles; revisá también en tu celular cuando tengas una URL accesible.
- Recorré todos los enlaces, menú, botones, filtros y modales si existen.
- Verificá texto, precios y condiciones contra la fuente aprobada.
- Revisá teclado, foco visible, contraste, etiquetas de formularios e imágenes con descripción útil.
- Mirá si las fotos están deformadas, cortadas o desalineadas. Compará las páginas internas con la portada.
- Si hay formulario, comprobá validación, error y recepción real de un envío de prueba en el destino previsto. No publicar secretos en JavaScript del navegador.

`localhost` apunta a la computadora desde donde lo abrís. Un enlace local que funciona en Windows no se vuelve público por mandártelo al celular. Para compartir, usá una vista previa publicada o un método de red específico que la IA configure y explique.

## Guardar y publicar

1. Guardá una versión local y registrá qué se probó.
2. Elegí repositorio privado propio para el código y revisá la lista de archivos que se suben.
3. Elegí alojamiento. Al preparar este kit, la [guía oficial de Cloudflare](https://developers.cloudflare.com/pages/get-started/) recomienda Workers para proyectos nuevos; también documenta Pages para proyectos que usan ese servicio. Pedile a tu IA elegir según el sitio, tu cuenta y la guía vigente. No presupongas que cualquier backend funciona allí sin adaptación.
4. Conectá tu cuenta por el flujo oficial. La IA verifica cuenta, proyecto, salida de compilación si existe y vista previa antes de publicar.
5. Autorizá una publicación concreta cuando estés conforme. Si ya pediste publicar esa versión en ese destino, no hace falta reiterar esa autorización.
6. Abrí la URL pública en incógnito y en el celular, comprobá HTTPS, imágenes, navegación y formulario. Registrá URL, fecha y versión del código desplegado.

**Un push a GitHub no siempre publica la web.** La integración Git puede desplegar automáticamente si está configurada; una carga directa es otro flujo. La IA debe verificar qué mecanismo existe y cómo volver a la versión anterior.

## Dominio propio, cuando el sitio ya esté listo

El dominio es la dirección; el alojamiento guarda el sitio y el DNS lo conecta. No son la misma cuenta necesariamente. Entrá vos a los portales para autorizar. Antes de tocar DNS, guardar los registros actuales y comprobar si hay correo u otros servicios que deban seguir funcionando. Agregar el dominio al alojamiento, seguir los valores que ese proyecto asigna y verificar DNS/HTTPS al finalizar. No reutilizar nameservers o destinos de otra cuenta por una guía vieja.

La propagación puede tardar. “Configuración guardada” y “dominio accesible desde Internet” son estados diferentes. No seguir cambiando valores correctos porque todavía no se ve en un dispositivo.

## Entrega a futuro

Dejá un README del proyecto con objetivo, comandos de inicio, carpetas, contactos de destino sin secretos, procedimiento de publicación y reversión, y límites conocidos. Incluí fuentes de imágenes/tipografías y la memoria de decisiones. Ese archivo evita reconstruir el proyecto desde cero dentro de unos meses.
