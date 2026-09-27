# Habilidades y agentes sin complicarte

## Cuatro skills propias, listas para leer

| Skill | Cuándo sirve | Resultado |
|---|---|---|
| naiara-onboarding | Empezar o retomar una etapa del kit | Un paso explicado y una prueba observable |
| naiara-brief-creativo | Convertir una idea en un encargo de contenido | Brief, propuesta, límites y criterios de aceptación |
| naiara-dueto | Coordinar una tarea sustantiva entre dos IAs | Encargo acotado, revisión y decisión integrada |
| naiara-verificar-entrega | Revisar un video, web o archivo antes de entregarlo | Evidencia y límites, sin anunciar éxitos no comprobados |

Las fuentes originales están en `skills/`. Se distribuyen copias idénticas en `.agents/skills/` para Codex y `.claude/skills/` para Claude Code. Se usan dentro de la carpeta del kit. No se modifican tus skills globales ni se reemplazan las existentes.

**No copies una carpeta de skill sola a otro proyecto:** estas habilidades usan recursos de `docs/`, `templates/` e `INICIO-IA.md`. Para usarlas fuera, tu IA debe preparar una adaptación que incluya los recursos necesarios y corrija las rutas, o mantener un enlace explícito a la raíz de este kit y comprobar permiso de lectura allí. Después debe probar tanto el descubrimiento como la apertura de cada recurso con un caso real. Nunca copiar `local/` a un repositorio compartido para resolver esa dependencia.

En Codex CLI, consultá `/skills`; en Claude Code escribí `/` y buscá sus nombres. Si no aparecen, iniciá una sesión nueva desde la raíz del kit. También podés pedir: “Leé skills/naiara-brief-creativo/SKILL.md y aplicala a esta idea”; esto permite utilizar el método aun si la interfaz cambió. Las ubicaciones de descubrimiento se documentan en [Codex](https://learn.chatgpt.com/docs/build-skills) y [Claude Code](https://code.claude.com/docs/en/skills).

**Prueba:** invocá la skill con una idea ficticia. Tiene que entregar un brief que distinga datos confirmados y faltantes; no inventar precios ni iniciar una generación. Instalar una skill no mejora por sí solo todos los resultados ni agrega herramientas que tu cuenta no tiene.

## Agentes: repartir una responsabilidad

Un agente es una sesión con un encargo. Puede ser la misma familia de modelo, otra IA o un perfil con herramientas limitadas. No necesariamente es un producto que debas contratar aparte.

Este kit incluye en `.claude/agents/` dos perfiles de revisión de lectura: `revisor-creativo` y `revisor-web`. No publican, no gastan créditos y no corrigen archivos. Revisan los materiales escritos y evidencias disponibles; sus herramientas de lectura no reemplazan abrir el video o navegar el sitio. Pedile al coordinador que les pase sólo lo necesario.

En Codex, si tu versión tiene subagentes disponibles, el coordinador puede asignar esos roles mediante un encargo equivalente. Si no tiene esa capacidad, usá otra conversación con el archivo de encargo. No se incluye una configuración interna de subagentes de Codex porque esa superficie cambia; verificar la ayuda de la versión instalada antes de configurarla.

## Catálogo para ampliar después

No hace falta instalar todos estos repositorios. Son fuentes para inspeccionar, elegir una habilidad útil, revisar sus permisos/licencia, fijar la versión y probar un caso:

- [anthropics/skills](https://github.com/anthropics/skills): ejemplos de skills y flujos. Revisar la licencia específica de cada carpeta antes de copiar o redistribuir; no asumir una licencia única para todo.
- [obra/superpowers](https://github.com/obra/superpowers): prácticas de desarrollo y verificación. Tiene sentido cuando empieces a construir webs más complejas; no es requisito de un primer reel.
- [higgsfield-ai/skills](https://github.com/higgsfield-ai/skills): companion skills que enlaza el proveedor para su integración CLI. Seguir la instalación vigente del proveedor, después de revisar lo que se va a agregar.

No se redistribuye código de esos repositorios en este kit. La guía [de integración Higgsfield](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-connect-higgsfield-to-ai-agent) propone `npx skills add higgsfield-ai/skills`; antes de ejecutarlo, pedirle a la IA que revise el repositorio y la herramienta instaladora, explique destinos y seleccione el alcance del proyecto. No contestar “sí a todo”.

Para una nueva skill, pedile:

> Este proceso se repite y quiero convertirlo en una habilidad. Definí cuándo se usa, qué entrada necesita, qué entrega y qué no hace. Revisá si ya hay una que lo cubra. Si la creás, probala con un caso real y registrá sus límites.

## Mantenimiento de las copias

Si editás una skill, la IA debe editar `skills/<nombre>/SKILL.md` y ejecutar `scripts/Sync-Skills.ps1`. El script se detiene si detecta una copia distinta que pudo haber sido editada por otra persona. Resolver esa diferencia antes de regenerar. Las pruebas comprueban que las tres ubicaciones no diverjan.
