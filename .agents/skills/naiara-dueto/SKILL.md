---
name: naiara-dueto
description: Coordinar un encargo sustantivo entre Codex y Claude, o una revisión independiente pedida, con contexto mínimo, un escritor por archivo y devolución comprobable. No usar para saludos o ajustes triviales.
---

# Coordinación por tarea

Leer docs/02-dueto-y-memoria.md. Quien recibe el pedido coordina; no hay roles fijos entre proveedores. Si el encargo ya indica DUETO_ROLE=par, realizarlo y devolver resultados sin delegar ni invocar al coordinador.

Comprobar que el otro agente está disponible y autenticado. Si no, informar y completar trabajo independiente; no atribuirle una revisión. Subagente Codex y Claude son identidades diferentes.

Crear encargo único con templates/encargo-dueto.md: objetivo, contexto necesario, rutas permitidas, lectura/escritura, salida, criterio de éxito y límite. Paralelizar sólo partes independientes; un escritor por archivo, o worktrees separados para código. Revisión normalmente de lectura. No pasar credenciales.

Supervisar una revisión y una corrección por encargo. No encadenar reintentos frente a bloqueo. Integrar hallazgos reproduciendo los fallos. Guardar qué contribución fue real y qué quedó pendiente. No cambiar modelos/esfuerzos o el alcance autorizado.
