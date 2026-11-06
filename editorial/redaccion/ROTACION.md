# Rotación de franquicias: un artículo al día

Cada día sale un artículo, y cada franquicia tiene su turno en orden. Este archivo indica cuál toca.

**Regla:** la pieza del día es de la franquicia del turno, salvo que haya una noticia bomba de otra de las diez, que tiene prioridad ese día. Una noticia bomba es una lesión grave, un traspaso confirmado, una renovación o una decisión que cambia la temporada de la franquicia. En ese caso, la franquicia del turno pasa al día siguiente y no se pierde.

## Ritmo

Franquicia, franquicia, evergreen, y así siempre. Los días evergreen no consumen turno. Se calcula contando los días desde el 6 de noviembre de 2026 (día 0): si el resto de dividir entre 3 es 2, toca evergreen.

## Orden

| Turno | Franquicia | ID de categoría | Estado |
| --- | --- | --- | --- |
| 1 | Minnesota Timberwolves | 29 | en pausa (a petición de Alejandro) |
| 2 | Brooklyn Nets | 16 | siguiente |
| 3 | Miami Heat | 33 | pendiente |
| 4 | Los Angeles Clippers | 26 | pendiente |
| 5 | Milwaukee Bucks | 13 | pendiente |
| 6 | Oklahoma City Thunder | 32 | pendiente |
| 7 | Philadelphia 76ers | 31 | pendiente |
| 8 | Sacramento Kings | 42 | pendiente |
| 9 | Utah Jazz | 40 | pendiente |
| 10 | Chicago Bulls | 18 | pendiente |

Tras el turno 10 se vuelve al 1.

## Cómo se actualiza

Cuando se publica el artículo del día, se marca la franquicia del turno como `cubierta` con la fecha, y el siguiente pasa a `siguiente`. Si el día fue una noticia bomba de otra franquicia, la del turno sigue como `siguiente`.

## Historial

- 2026-11-06: archivo creado. Ningún artículo publicado todavía con esta rotación.
