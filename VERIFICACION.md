# Verificación del kit

Preparado el 27/09/2026. Este archivo registra pruebas del material distribuido; no certifica cuentas o servicios de Naiara.

## Alcance

- Pruebas Python sin red para Telegram: vinculación por código, exclusión de chats, archivos, errores sin secretos y ausencia de reintentos de envíos.
- Integridad de las cuatro skills y sus copias para ambos clientes; enlaces relativos y notas semilla.
- Prueba PowerShell en carpeta temporal: creación de memoria, repetición sin sobrescribir notas, diagnóstico, sincronización y preservación de copias editadas.

## Ejecución

```powershell
py -3 -m unittest discover -s tests -v
& .\tests\windows-smoke.ps1
```

El flujo de GitHub Actions `.github/workflows/verify.yml` ejecuta pruebas sin secretos en Windows, con Windows PowerShell 5.1 y PowerShell 7. Consultá el resultado del commit que descargaste en la pestaña **Actions**; la presencia del workflow no demuestra que haya pasado.

## Límites

No se iniciaron sesiones, instalaron suscripciones ni usaron créditos de Naiara. Las pruebas de Telegram son simuladas. El funcionamiento con sus cuentas requiere completar las pruebas de las guías. Una revisión de archivos no demuestra calidad de un video futuro ni acceso real a Gmail.

La revisión independiente del kit se hizo con agentes Codex. Claude no estaba autenticado en la máquina de preparación y no participó; el protocolo para que ambas IAs colaboren se incluye para su configuración posterior.
