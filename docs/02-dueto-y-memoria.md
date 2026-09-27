# Dos IAs, una dirección y una memoria

## Con cuál hablar

Elegí una conversación principal por proyecto. Puede ser Codex o Claude; no hay un jefe permanente entre ellos. A esa IA le contás el objetivo y le pedís que coordine. La otra recibe una parte concreta o una revisión.

Ejemplo: “Quiero un reel de 15 segundos para una marca ficticia. Vos coordiná el guion y la entrega; pedile al otro que revise si se entiende el mensaje y qué errores debería mirar en el video”. Si el otro no está conectado, tu IA debe decirlo; una revisión hecha por otro agente de Codex no es una revisión de Claude.

No hace falta que trabajen los dos para cambiar una frase o responder una duda simple. Usalos juntos donde otra mirada pueda detectar un problema o en tareas independientes que ahorren tiempo.

## Empezar sin automatizaciones

1. Abrí dos terminales o aplicaciones en la misma carpeta del kit.
2. En una, iniciá `codex`; en otra, `claude`.
3. Al coordinador pedile guardar un encargo en `local/Revisiones/tarea-001-encargo.md`.
4. Al revisor decile: “Leé ese encargo. DUETO_ROLE=par; no delegar. Revisá solamente los archivos indicados y guardá la devolución en tarea-001-revision.md. No edites el trabajo”.
5. El coordinador lee la devolución, reproduce los problemas y decide qué corregir. Una corrección sugerida puede estar equivocada: hay que comprobarla.

El mismo archivo puede ser leído por ambos. **No dejes a ambos editándolo al mismo tiempo.** Para programar simultáneamente se pueden usar ramas con worktrees separados; primero aprendé el flujo simple de un escritor y un revisor.

### Encargo útil

Usá [la plantilla](../templates/encargo-dueto.md). Tiene objetivo, contexto, archivos permitidos, salida, prueba y límite. “Revisá todo y mejoralo” no delimita una tarea. “Revisá el guion y la evidencia de duración; señalá afirmaciones sin sustento y devolvé hasta cinco problemas concretos” sí.

### Automatizar después

Con ambos CLI autenticados, la IA coordinadora puede llamar al otro mediante un proceso acotado. No hace falta un MCP que una las conversaciones. Un ejemplo de revisión de archivos con Claude, en PowerShell:

```powershell
$encargo = 'DUETO_ROLE=par; no delegar. Lee local/Revisiones/tarea-001-encargo.md. Revisa solo los archivos permitidos. No edites. Devuelve hallazgos con evidencia.'
claude -p $encargo --tools Read,Grep,Glob --allowedTools Read,Grep,Glob --strict-mcp-config
```

La salida aparece en la terminal; el coordinador la guarda en un archivo nuevo. Esta modalidad no ve ni escucha automáticamente videos y no tiene navegadores/MCP: si el encargo los requiere, usá una sesión con esas capacidades o revisión humana. Verificá los flags con `claude --help` de la versión instalada. Establecé un límite de tiempo, una revisión y una corrección por encargo; si se bloquea, detenelo y explicá la causa.

Desde Claude hacia Codex, empezar por el intercambio de archivos de arriba. Para automatizar, consultar `codex exec --help`, usar sólo lectura para revisiones, salida única y permisos normales. No copiar un comando de otra versión ni habilitar acceso total para hacer funcionar el dueto. El coordinador nunca debe transmitir contraseñas como parte del encargo.

## Obsidian es tu memoria legible

Una bóveda es una carpeta de notas. Obsidian te permite abrirlas y enlazarlas; tus IAs también pueden leer esos archivos si tienen acceso. No entrena a los modelos ni mantiene chats sincronizados por sí solo.

Después de preparar el estudio, abrí Obsidian y elegí **Abrir carpeta como bóveda**. Seleccioná `local/Cerebro` dentro del kit. No necesitás plugins comunitarios para esta primera etapa.

| Nota | Para qué sirve |
|---|---|
| 00-Inicio | Entrada y enlaces |
| 01-Estado-actual | Qué estás haciendo, qué falta y próxima acción |
| 02-Decisiones | Preferencias aprobadas, con fecha y motivo |
| 03-Conexiones | Qué cuenta/servicio se probó y qué puede hacer; nunca claves |
| 04-Aprendizajes | Qué funcionó, qué falló y cómo repetirlo |
| 05-Proyectos | Enlaces a briefs, archivos y entregas |
| 06-Presupuesto | Costos informados y consumo comprobado por proyecto |

Al terminar una sesión podés pedir:

> Actualizá mi memoria local con lo que hicimos, las pruebas, lo pendiente y el próximo paso. Separá decisiones de ideas. Decime qué notas cambiaste y dónde quedó el entregable.

Al volver:

> Leé mi Inicio y Estado actual. Confirmá cuál era el siguiente paso y comprobá de nuevo las conexiones necesarias antes de actuar.

**Prueba real de memoria:** anotá una preferencia sencilla, como “para mi portfolio prefiero fondos claros”. Cerrá la sesión y pedile a una nueva que la encuentre. Debe indicar el archivo. No vale que la adivine ni que dependa de la conversación anterior.

## Copias y recuperación

`local/` está excluido de Git. Si borrás el kit o perdés la computadora, esas notas no aparecen por arte de magia en GitHub. Elegí una copia privada: otra unidad o un servicio de respaldo de tu elección. Obsidian Sync es una opción distinta a este kit; revisá plan y funcionamiento antes de contratarlo. Evitá dos sistemas sincronizando a la vez la misma bóveda sin entender sus conflictos.

Una vez por semana, copiá la bóveda y materiales esenciales a tu respaldo. Restaurá una nota de prueba en una carpeta aparte para verificarlo. Guardá originales, exportaciones finales, prompts, referencias y permisos de uso. Un enlace temporal a un video no reemplaza descargar el archivo.

No mezcles las notas de clientes diferentes. Cuando sepas manejar proyectos, podés separar memoria general del estudio y memoria por cliente, conservando sólo enlaces donde haga falta.
