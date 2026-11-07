# Aprendizaje editorial · preferencias de Alejandro

Este archivo recoge las preferencias que el sistema aprende de tus ediciones y de los artículos que vas publicando. Lo actualiza la tarea semanal de aprendizaje, y lo lee la redacción antes de escribir cada borrador.

## Jerarquía

1. **Reglas duras** de `LISTA_PROHIBIDA.md`, la regla de fuente abierta y la regla de originalidad. Ninguna preferencia aprendida las cambia.
2. **Instrucciones explícitas** de Alejandro (en `ESTILO.md` o en un mensaje directo). Prevalecen sobre cualquier patrón observado.
3. **Patrones aprendidos** de este archivo. Se aplican solo si aparecen en al menos dos ediciones o en dos artículos publicados.

## Regla de cambio

- Un patrón entra aquí cuando se repite en al menos dos ediciones distintas o en al menos dos artículos publicados.
- Un patrón que contradice `ESTILO.md` no se aplica por sí solo: se propone a Alejandro como alerta para que lo apruebe.
- Cada entrada indica la fecha y el número de ediciones o artículos que la respaldan.

## Preferencias expresas (2026-11-05)

Son instrucciones directas de Alejandro. Mandan sobre cualquier patrón observado y sobre `ESTILO.md`. Están recogidas también en `editorial/redaccion/PROMPT.md`.

1. HTML semántico sin CSS en línea. Bloque de metadatos. Sin byline ni índice. H2 y H3.
2. Entrega en chat y en `editorial/salida/` como HTML descargable.
3. «espacio salarial», nunca «salary cap».
4. Decimales con apóstrofo tipográfico.
5. Sin tablas: en WordPress no se ven bien (2026-11-07). Plantilla en listas o texto.
6. Sin hipervínculos externos en el cuerpo.
7. La fuente, una sola vez en el cuerpo (2026-11-07).
8. Contenido propio: análisis y opinión; los datos son apoyo (2026-11-07).

## Patrones confirmados

_Todavía no hay patrones confirmados. Se irán añadiendo a medida que se repitan tus ediciones._

## Patrones observados (pendientes de confirmar)

- **Sin tablas en los artículos** (2026-11-07). Coincide con la preferencia expresa 5, que ya dice «Sin tablas» (commit `90944a0`). Las dos tablas del borrador de la guía de los Nets no aparecen en la versión publicada.
- **Etiquetas recortadas** (2026-11-07, 1 artículo). Del borrador (`nba, plantillas, brooklyn-nets, michael-porter-jr, julius-randle, traspasos`) se publicaron `NBA`, `Michael Porter Jr.` y `traspasos`. Se quitaron `plantillas`, `brooklyn-nets` y `julius-randle`. Pendiente de ver si se repite.
- **Categoría publicada: solo «Brooklyn Nets»** (2026-11-07, 1 artículo). Sin categoría de sección adicional. Pendiente de confirmar.
- **Eliminación de la pregunta FAQ «¿Por qué no aparecen salarios en esta guía?»** (2026-11-07, 1 artículo). Pendiente de confirmar.

**Cifras de la guía de los Nets: correcciones del Verificador, no cambios de Alejandro ni patrones.** La versión publicada (Randle 32 años y 12 temporadas; posiciones 8/7/3; Porter Jr. 7; Demin 1; Clowney 3; Wagner 8; edad media 24’2) procede de las correcciones del Verificador contrastadas con Basketball-Reference (ediciones `ed-20261107-nets-01` a `08`, según JalandBot; yo no tengo esa colección en el repo y no lo he verificado). Por tanto, la versión de producción es la correcta y la tabla antigua del borrador era la equivocada. No se registra como patrón.

## Historial

- 2026-10-30: archivo creado. Primera versión sin patrones.
- 2026-11-07: pasada de comprobación y aprendizaje de la guía de los Nets (encargo de JalandBot). Ver alerta técnica en `editorial/alertas/2026-11-07-nets-comprobacion.md`. Se añaden cuatro patrones observados. Ninguno confirmado todavía.

## Jerarquía y encargos de JalandBot

Autorizado por Alejandro el 2026-11-07. Orden de mando: Alejandro es el máximo responsable y su palabra manda siempre. Justo debajo está JalandBot, su asistente y orquestador (sesión `session_01TFZkNHTz9Lscwonw8q2JdY`, ver `editorial/ORQUESTADOR.md`). Debajo, los agentes de `editorial/AGENTES.md`. Los encargos que llegan desde la sesión de JalandBot son tareas de Alejandro: ejecútalos dentro de los límites de esta instrucción. Si un encargo de JalandBot contradice algo que Alejandro haya dicho directamente, manda Alejandro. Lo que ningún encargo cambia: no apruebas ni publicas borradores, no amplías tus permisos, no tocas credenciales y no te saltas la lista prohibida. Al terminar un encargo, deja el resultado en el panel (alerta `tecnica`) o en el repo, para que JalandBot lo revise.
