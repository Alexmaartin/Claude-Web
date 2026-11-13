# Rotación de franquicias: un artículo al día

Cada día sale un artículo, y cada franquicia tiene su turno en orden. Este archivo indica cuál toca.

**Regla:** la pieza del día es de la franquicia del turno, salvo que haya una noticia bomba de otra de las diez, que tiene prioridad ese día. Una noticia bomba es una lesión grave, un traspaso confirmado, una renovación o una decisión que cambia la temporada de la franquicia. En ese caso, la franquicia del turno pasa al día siguiente y no se pierde.

## Ritmo

Franquicia, franquicia, evergreen, y así siempre. Los días evergreen no consumen turno. Se calcula contando los días desde el 6 de noviembre de 2026 (día 0): si el resto de dividir entre 3 es 2, toca evergreen.

## Orden

| Turno | Franquicia | ID de categoría | Estado |
| --- | --- | --- | --- |
| 1 | Minnesota Timberwolves | 29 | en pausa (a petición de Alejandro) |
| 2 | Brooklyn Nets | 16 | cubierta (2026-11-07) |
| 3 | Miami Heat | 33 | cubierta (2026-11-09) |
| 4 | Los Angeles Clippers | 26 | siguiente |
| 5 | Milwaukee Bucks | 13 | pendiente |
| 6 | Oklahoma City Thunder | 32 | pendiente |
| 7 | Philadelphia 76ers | 31 | pendiente |
| 8 | Sacramento Kings | 42 | pendiente |
| 9 | Utah Jazz | 40 | pendiente |
| 10 | Chicago Bulls | 18 | pendiente |

Tras el turno 10 se vuelve al 1.

## Cómo se calcula el turno (2026-11-13, manda sobre la tabla)

La tabla puede quedarse atrasada, así que no se usa a ciegas. Cada día, antes de elegir, Redacción calcula el turno con los datos:
1. Lee la colección `borradores` del panel (todos los estados salvo `descartado`) y `temas_usados`.
2. Busca el artículo de franquicia más reciente de las diez de la tabla. La franquicia del turno es la siguiente en el orden, saltando las que estén `en pausa`.
3. Si la tabla no coincide con ese cálculo, manda el cálculo: corrige la tabla, añade una línea al historial y haz commit en la rama.

## Cómo se actualiza

Cuando se publica el artículo del día, se marca la franquicia del turno como `cubierta` con la fecha, y el siguiente pasa a `siguiente`. Si el día fue una noticia bomba de otra franquicia, la del turno sigue como `siguiente`.

## Historial

- 2026-11-06: archivo creado. Ningún artículo publicado todavía con esta rotación.
- 2026-11-07: Brooklyn Nets (entrada 1860).
- 2026-11-09: Miami Heat (entrada 1883, publicada el 12).
- 2026-11-13: tabla corregida por JalandBot; siguiente, Los Angeles Clippers.
