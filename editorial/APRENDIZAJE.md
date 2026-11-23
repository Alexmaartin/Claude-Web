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

- **Opinión en primera persona** («en mi opinión», «creo», «mi lectura», «para mí»), en cierres y bloques de análisis. Aparece en 3 artículos publicados (`como-funciona-draft-nba-sorteo-picks-rondas`, `top-10-rookies-temporada-2026-27` y `miami-heat-2026-27-plantilla-rotacion-claves-arranque`) y en 8 ediciones humanas (2026-11-08 a 2026-11-12). Coincide con `ESTILO.md` §2. Se aplica.
- **Quitar cifras salariales y bloques de salario cuando la fuente no las confirma.** Dos artículos: Nets (FAQ de salarios, 2026-11-07) y Heat (sección «Contratos y margen salarial», 2026-11-12). Coincide con la regla de no inventar cifras. Se aplica.

## Patrones observados (pendientes de confirmar)

- **Etiquetas recortadas** (2026-11-07, 1 artículo, Nets). Del borrador (`nba, plantillas, brooklyn-nets, michael-porter-jr, julius-randle, traspasos`) se publicaron `NBA`, `Michael Porter Jr.` y `traspasos`. Pendiente de ver si se repite.
- **Categoría publicada: solo «Brooklyn Nets»** (2026-11-07, 1 artículo). Pendiente de confirmar.
- **Quitar el calendario de próximos partidos** (2026-11-12, 1 artículo, Heat). Pendiente de confirmar.
- **Quitar frases de fuentes del cuerpo** (2026-11-12, Heat: «Las cifras proceden de…» fuera de la intro). Pendiente de confirmar.
- **Lista en líneas sueltas, no en prosa** (2026-11-12, 1 artículo, rookies: las cuatro variables en líneas separadas). Tensión leve con `ESTILO.md` §1 («las listas van en prosa»). No se aplica hasta que Alejandro lo decida.

**Basketball-Reference solo para verificar, no como fuente del texto.** Aparece en tres correcciones con motivo «Instrucción de Alejandro» (`ed-20261108-draft-v3-01`, `ed-20261109-heat-07`, `ed-20261111-heat-03`). Es una instrucción explícita recogida en las ediciones, no un patrón. Se propone como preferencia expresa para que Alejandro la confirme en `ESTILO.md`. Mientras tanto, la redacción la aplica (no se cita Basketball-Reference en el cuerpo).

**Cifras de la guía de los Nets: correcciones del Verificador, no cambios de Alejandro ni patrones.** La versión publicada procede de las correcciones del Verificador contrastadas con Basketball-Reference (ediciones `ed-20261107-nets-01` a `08`). No se registra como patrón.

## Patrones que contradicen ESTILO.md (alerta, no se aplican)

- **Ironía y sarcasmo sobre jugadores** («su salario bien pagado está», «siempre y cuando no busque más sanciones como la del otro día», «deja mucho que desear», «sería raro que mejorase el tiro libre»). Dos artículos (rookies y Heat). `ESTILO.md` §2 prohíbe el sarcasmo sobre personas. Alerta de incertidumbre a Alejandro.
- **Segunda persona y «vosotros»** («Tranquilo, yo también…», «tu zona», y «sacar vosotros mismos vuestras propias conclusiones» en la guía de los Nets ya publicada). `ESTILO.md` §4.5 pone «vosotros» entre lo que hay que evitar. Alerta de incertidumbre a Alejandro.

## Historial

- 2026-10-30: archivo creado. Primera versión sin patrones.
- 2026-11-07: pasada de comprobación y aprendizaje de la guía de los Nets (encargo de JalandBot). Ver alerta técnica en `editorial/alertas/2026-11-07-nets-comprobacion.md`. Se añaden cuatro patrones observados. Ninguno confirmado todavía.
- 2026-11-23: pasada semanal (encargo de JalandBot). Ediciones humanas desde el 2026-11-07 a las 03:45 UTC (8 documentos, 3 artículos publicados; las correcciones del Verificador no se cuentan). Corpus: 9 artículos nuevos de Alejandro guardados en `editorial/corpus/nuevos/` y añadidos a `corpus/AUTORES.tsv` (total 41 de Alejandro en WordPress). Se confirman dos patrones y se añaden cinco observados. Dos patrones contradicen `ESTILO.md` y pasan a alerta. `ESTILO.md` no se ha modificado.

## Jerarquía y encargos de JalandBot

Autorizado por Alejandro el 2026-11-07. Orden de mando: Alejandro es el máximo responsable y su palabra manda siempre. Justo debajo está JalandBot, su asistente y orquestador (sesión `session_01TFZkNHTz9Lscwonw8q2JdY`, ver `editorial/ORQUESTADOR.md`). Debajo, los agentes de `editorial/AGENTES.md`. Los encargos que llegan desde la sesión de JalandBot son tareas de Alejandro: ejecútalos dentro de los límites de esta instrucción. Si un encargo de JalandBot contradice algo que Alejandro haya dicho directamente, manda Alejandro. Lo que ningún encargo cambia: no apruebas ni publicas borradores, no amplías tus permisos, no tocas credenciales y no te saltas la lista prohibida. Al terminar un encargo, deja el resultado en el panel (alerta `tecnica`) o en el repo, para que JalandBot lo revise.
