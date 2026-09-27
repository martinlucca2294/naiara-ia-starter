# Naiara · Estudio creativo con IA

Un punto de partida para crear videos, contenido para Instagram y páginas web con **Codex + Claude**, en Windows. No necesitás saber programar para empezar.

Este kit transforma una forma de trabajar en un recorrido que podés aprender: explicar bien una idea, producir una primera versión, revisar, guardar lo aprendido y mejorar. Las cuentas y conexiones se configuran con vos; descargarlo no las activa.

**¿Es tu primera vez? Abrí [EMPEZA-AQUI.md](EMPEZA-AQUI.md).** Tiene los pasos para descargarlo, abrir la terminal y darle la primera instrucción a tu IA.

**¿Ya tenés Codex o Claude funcionando en una terminal?** Descargá este repositorio, abrí la terminal en su carpeta, ejecutá `codex` o `claude` y pegá:

> Soy Naiara. Leé INICIO-IA.md y acompañame desde cero. Primero comprobá dónde estás trabajando y qué tengo instalado. Haceme como máximo tres preguntas cortas. Explicame una sola etapa por vez y verificá conmigo el resultado antes de continuar. No conectes cuentas ajenas ni generes contenido pago hasta que definamos la prueba y su presupuesto.

## Qué vas a encontrar

| Quiero… | Abrir |
|---|---|
| Instalar y entender la terminal | [Windows, paso a paso](docs/01-windows.md) |
| Trabajar con ambas IAs y conservar memoria | [Dueto y Obsidian](docs/02-dueto-y-memoria.md) |
| Conectar Higgsfield, Gmail, Drive y GitHub | [Conexiones y pruebas](docs/03-conexiones.md) |
| Crear mi propio bot | [Telegram](docs/04-telegram.md) |
| Producir videos e Instagram | [Estudio creativo](docs/05-estudio-creativo.md) |
| Agregar habilidades y especialistas | [Skills y agentes](docs/06-skills-y-agentes.md) |
| Crear una web y publicarla | [Web de principio a fin](docs/07-web-y-publicacion.md) |
| Resolver un problema o actualizar | [Ayuda y mantenimiento](docs/08-ayuda.md) |
| Saber qué aprender primero | [Recorrido por etapas](docs/09-recorrido.md) |
| Comprobar de dónde sale una instrucción | [Fuentes oficiales](docs/FUENTES.md) |

## Lo que incluye y lo que falta configurar

- Guías, plantillas, cuatro skills originales para ambas IAs y dos perfiles de revisión para Claude Code.
- Preparación local en PowerShell: crea tu memoria inicial y conserva tus notas si lo ejecutás otra vez.
- Bot de Telegram en Python: identificación, vinculación privada, envío y captura de ideas. **No ejecuta órdenes de la computadora ni tiene un modelo de IA incorporado.**
- Pruebas automáticas del kit. La evidencia concreta se publica en [VERIFICACION.md](VERIFICACION.md).
- Conexiones externas pendientes de tus cuentas, permisos y pruebas reales. No incluye suscripciones, créditos, tokens ni acceso a las cuentas de otra persona.

## Separá el kit de tu trabajo

El repositorio es material compartible. `local/` será tu espacio de trabajo, excluido de Git: `local/Cerebro`, `local/Proyectos` y los datos locales del bot. Esa exclusión evita agregados accidentales, pero **no cifra ni respalda** tus archivos. Prepará una copia privada según la guía de memoria.

No hagas un fork público para guardar material de clientes. Cuando quieras versionar un proyecto real, creá un repositorio **privado independiente** y revisá los archivos antes de subirlos. No compartas un ZIP de toda la carpeta después de empezar a trabajar: podría incluir `local/`.

## Una sesión normal

1. Contás el resultado que buscás y mostrás referencias.
2. La IA revisa la memoria del proyecto y arma una primera propuesta.
3. Una IA produce; la otra revisa un encargo acotado cuando suma valor.
4. Mirás el resultado real y comprobás que cumple lo pedido.
5. Se guarda la versión, su evidencia y el siguiente paso.

El mismo archivo de memoria puede ser leído por ambas IAs. Sus conversaciones y sesiones no se sincronizan automáticamente.

Versión inicial: **27 de septiembre de 2026**. Las interfaces, modelos y planes cambian; las fuentes oficiales prevalecen sobre una captura vieja. Este kit es independiente de OpenAI, Anthropic, Higgsfield y los demás proveedores.
