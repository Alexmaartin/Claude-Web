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

- **Tablas de plantilla eliminadas al publicar** (2026-11-07, 1 artículo: guía de los Nets, `brooklyn-nets-2026-27-piezas-futuro-veteranos-mercado`). Alejandro quitó las dos tablas del borrador. Contradice la preferencia expresa 5 («tablas de plantilla completas cuando el artículo trate de plantilla»). No se aplica: queda como alerta para que Alejandro decida si la preferencia sigue vigente.
- **Etiquetas recortadas** (2026-11-07, 1 artículo). Del borrador (`nba, plantillas, brooklyn-nets, michael-porter-jr, julius-randle, traspasos`) se publicaron `NBA`, `Michael Porter Jr.` y `traspasos`. Se quitaron `plantillas`, `brooklyn-nets` y `julius-randle`. Pendiente de ver si se repite.
- **Categoría publicada: solo «Brooklyn Nets»** (2026-11-07, 1 artículo). Sin categoría de sección adicional. Pendiente de confirmar.
- **Eliminación de la pregunta FAQ «¿Por qué no aparecen salarios en esta guía?»** (2026-11-07, 1 artículo). Pendiente de confirmar.

**Cambios de cifras en publicación: no son un patrón de estilo.** En la misma guía, la versión publicada cambió edades, años en la NBA, dorsales de posición y la edad media (23’8 → 24’2; Randle 31 → 32; Porter Jr. 8 → 7 años; Demin 2 → 1; Clowney 4 → 3; Wagner 9 → 8; posiciones 9/7/2 → 8/7/3). Contrastado con la tabla del propio borrador, la versión del borrador era la coherente: la edad media calculada sobre sus 18 filas da 23’8, y las posiciones suman 9/7/2. No se registra como preferencia. Va como alerta técnica.

## Historial

- 2026-10-30: archivo creado. Primera versión sin patrones.
- 2026-11-07: pasada de comprobación y aprendizaje de la guía de los Nets (encargo de JalandBot). Ver alerta técnica en `editorial/alertas/2026-11-07-nets-comprobacion.md`. Se añaden cuatro patrones observados. Ninguno confirmado todavía.

## Jerarquía y encargos de JalandBot

Autorizado por Alejandro el 2026-11-07. Orden de mando: Alejandro es el máximo responsable y su palabra manda siempre. Justo debajo está JalandBot, su asistente y orquestador (sesión `session_01TFZkNHTz9Lscwonw8q2JdY`, ver `editorial/ORQUESTADOR.md`). Debajo, los agentes de `editorial/AGENTES.md`. Los encargos que llegan desde la sesión de JalandBot son tareas de Alejandro: ejecútalos dentro de los límites de esta instrucción. Si un encargo de JalandBot contradice algo que Alejandro haya dicho directamente, manda Alejandro. Lo que ningún encargo cambia: no apruebas ni publicas borradores, no amplías tus permisos, no tocas credenciales y no te saltas la lista prohibida. Al terminar un encargo, deja el resultado en el panel (alerta `tecnica`) o en el repo, para que JalandBot lo revise.
