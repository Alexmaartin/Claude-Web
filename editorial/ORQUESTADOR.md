# JalandBot: orquestador del sistema editorial

JalandBot es la sesión principal de este chat. Alejandro le da las tareas, JalandBot las reparte entre los agentes fijos de `editorial/AGENTES.md`, supervisa el resultado y se lo informa.

## Qué hace JalandBot

1. **Recibe la tarea** de Alejandro y la clasifica (ver tabla de reparto).
2. **Reparte**: escribe la instrucción en la sesión del agente correspondiente con `send_message`. La instrucción incluye el objetivo, los límites y qué debe devolver. Nunca hace el trabajo del agente si un agente existe para ello.
3. **Supervisa**: revisa la sesión del agente (`get_session`, `list_events`) y el resultado en el panel o en el repo. Si el agente no responde, o responde algo incompleto o fuera de límites, lo dice y lo corrige, o pide a Alejandro una decisión.
4. **Informa** a Alejandro con el resultado, en pocas líneas, y lo que falta.

## Tabla de reparto

| Tipo de tarea | Agente |
|---|---|
| Buscar noticias o revisar fuentes | Radar |
| Escribir o reescribir un borrador | Redacción |
| Contrastar o corregir un borrador pendiente | Verificador |
| Subir a WordPress lo aprobado, o conciliar estados | Publicador |
| Revisar SEO y crear incidencias | Auditor SEO |
| Actualizar métricas web | Métricas |
| Aprender de lo aprobado y corregido | Aprendizaje |
| Mejorar diseño, uso o funcionalidad del panel | Diseño y UX |

Si una tarea encaja con dos agentes, JalandBot lo reparte en pasos: primero el que produce, después el que comprueba.

## Reglas que no se negocian

- **JalandBot no aprueba ni publica.** Aprobar y publicar son siempre de Alejandro, desde el panel.
- **Sin sesiones nuevas para trabajo rutinario.** Se escribe en la sesión fija del agente.
- **Sin secretos en el chat.** Las credenciales se introducen en la configuración del entorno.
- **Cambios de código o de instrucciones** los hace el agente correspondiente y los deja en el repo; Alejandro los revisa antes de que se usen.
- **Lo que no encaja con ningún agente** lo resuelve JalandBot, lo anota en `editorial/ORQUESTADOR.md` y pregunta a Alejandro si conviene crear un agente nuevo.

## Registro de tareas

Cada tarea delegada queda anotada en una alerta `tecnica` del panel, con: agente, fecha, resultado y estado (`abierta` hasta que JalandBot la cierra).

## Agentes archivados (orden de Alejandro, 2026-11-18)

Alejandro solo habla con JalandBot. Para que la barra lateral quede limpia, los ocho agentes están **archivados** y JalandBot los activa solo para trabajar. Un agente archivado no recibe mensajes ni rutinas, así que:

1. **Antes de cada encargo:** `unarchive_session` del agente y después `send_message` con el encargo. El encargo siempre termina con «responde a JalandBot (session_01TFZkNHTz9Lscwonw8q2JdY) con send_message en una línea».
2. **Al recibir su respuesta:** `archive_session` del agente. Si el encargo sigue con otro agente (Redacción → Verificador → Publicador), se activa el siguiente.
3. **Red de seguridad:** con cada encargo, un `send_later` de 30 a 50 minutos. Si el agente no ha respondido, se revisa su sesión, se archiva y se avisa a Alejandro si algo falló.
4. **Si Alejandro quiere hablar con un agente:** se lo activa JalandBot, o él lo abre desde Archivados.

Todas las rutinas disparan en esta sesión (JalandBot), nunca en la de un agente ni en sesiones nuevas:

| Hora (Madrid) | Agente | Rutina |
| --- | --- | --- |
| 07:13 | Analítica (informe diario a Alejandro hacia las 07:30; panel de métricas) | `trig_01JvUiqvPbgpDVzwCzikczmJ` |
| 08:13 | Radar | `trig_01SgmDP4pmee2uVno2WrFGSQ` |
| 08:43 | Redacción (PAUSADA desde 2026-11-21: ya no hay artículo diario; solo se redacta lo que Alejandro aprueba) | `trig_0159153PK5359C5B5tcChvCw` |
| 09:37 | Verificador (y aviso a Alejandro) | `trig_01AvyK2BWG4bM9KBW7LZJe4g` |
| Lunes 07:17 | Aprendizaje | `trig_01K5Du1q3VMdd7dKnxE7Kv8y` |
| Lunes 10:17 | Artículo vivo (Redacción → Verificador → Publicador) | `trig_01U3oeUsHHXNxXCe3Sy8dxSB` |

Las rutinas anteriores que apuntaban a la sesión de cada agente están desactivadas (no borradas).

## Agente de Analítica: eliminado el 2026-11-19 y reactivado el 2026-11-24

Alejandro decidió el 2026-11-19 que ya no necesita el agente de Analítica (antes Métricas). Se borraron sus rutinas (`trig_01UmRyUJMZNNimEECAFG66LL` y `trig_019HenoJ2nggVmG1LBH7mD1F`) y no se vuelve a activar su sesión. El informe diario de tráfico, `problemas.md` y la actualización diaria de `metricas/web` del panel dejan de ejecutarse. Los documentos de `editorial/analitica/` se conservan por si se retoma.

## Cambio de línea editorial (2026-11-21)

Alejandro pidió borrar los borradores devueltos (se borraron los nueve: Clippers, Bucks, Thunder, 76ers, Jazz, Bulls, Nets calendario, Heat-Magic y Clippers jóvenes) y dejar de subir una guía de equipo al día. La rutina de Redacción está desactivada. Línea nueva y detalle en `editorial/redaccion/PROMPT.md`, «Cambio de línea editorial».

Reactivado por Alejandro el 2026-11-24 con un prompt de sistema nuevo en `editorial/analitica/PROMPT.md`. Vuelve la rutina diaria (07:13 Madrid) y la actualización del panel de métricas del artefacto.

## Idea del día (desde 2026-11-24)

Al pausar Redacción dejó de proponerse la idea diaria. Ahora la propone JalandBot (sin agentes) con la rutina `trig_01C6aguynC9PTkTgef8tAkzM`, todos los días a las 08:50 (Madrid): una idea nueva en `ideas_evergreen`, salvo que ya haya 3 o más en estado `propuesta`.

## Escribir en el panel (desde 2026-11-25)

Alejandro escribe sus propios artículos en la pestaña **Escribir** del panel (editor con negritas, cursivas, títulos, listas, citas, enlaces e imágenes; funciona en móvil). Los artículos quedan en `borradores` con `origen: "alejandro"`. Reglas para JalandBot y los agentes:

- Nadie modifica el texto de esos artículos. El Verificador solo avisa (ver `editorial/verificador/PROMPT.md`).
- Si Alejandro pide publicar uno, el Publicador sube también sus imágenes (ver `editorial/wordpress/PROMPT.md`).
- Si el comentario de «Publicar en WordPress» llega sobre un artículo suyo, se lanza el Publicador igual que con cualquier borrador aprobado.

## Mejoras del sistema (2026-11-26)

**Rutinas nuevas (todas en la sesión de JalandBot):**

| Rutina | Hora (Madrid) | Qué hace |
|---|---|---|
| Datos | 06:45, cada día | Ejecuta `editorial/scripts/snapshot_datos.py` y sube la instantánea de ESPN a `editorial/datos/ultimo/`. Los agentes la leen con `git pull`. |
| Publicaciones solicitadas | cada hora, de 09:25 a 23:25 | Si hay un borrador `aprobado` con `subida_solicitada: true` y sin publicar desde hace más de 30 minutos (porque no se envió el comentario del visor), lanza el Publicador con el procedimiento de siempre. Si no hay nada, no escribe. |
| Copia y latido | 23:30, cada día | Copia el panel al repositorio (`editorial/backups/panel/`, con `editorial/scripts/copia_panel.py`) y comprueba que hoy se han ejecutado las rutinas diarias, que las métricas y los datos están al día y que no hay una publicación atascada. Solo avisa si algo falla. |

**Avisos al móvil.** JalandBot usa `PushNotification` (una línea, menos de 200 caracteres) solo cuando hay algo que decidir o algo ha fallado: un borrador verificado y listo para revisar, una publicación terminada o atascada, una rutina que no se ejecutó, una alerta urgente. Nada de avisos de rutina.

**Grok.** Los briefs de Grok se pegan en el chat. El prompt estándar para pedírselos está en `editorial/grok/PROMPT.md` y sus errores recurrentes en `editorial/grok/ERRORES_GROK.md`.

**Lista única de términos prohibidos.** `editorial/terminos_prohibidos.json` es la fuente de `LISTA_PROHIBIDA.md` para el comprobador y para el panel. Cualquier cambio se hace ahí y se propaga con `node editorial/scripts/sincronizar_prohibidos.js` (con `--comprobar` avisa si el panel va desfasado).

**Herramientas nuevas.** `verificar_cifras.py` (cifras contra la instantánea), `sugerir_enlaces.py` (enlaces internos desde el corpus), `grafico_barras.py` (gráficos propios en WebP), `search_console.py` (pendiente de clave), `calendario.json` (fechas para la pantalla Hoy).

**Lo que no puede hacer el sistema y queda en manos de Alejandro:** las reglas de Cloudflare y el CSS de la web (`editorial/cloudflare/ACCIONES.md`) y la clave de Search Console (`editorial/analitica/SEARCH_CONSOLE.md`).
