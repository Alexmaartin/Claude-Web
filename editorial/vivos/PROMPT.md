# Artículos vivos (se actualizan solos)

Un artículo vivo se publica una vez y después se actualiza de forma periódica. El texto y la opinión son de Alejandro; las cifras se refrescan solas.

## Registro

| Artículo | Borrador | Frecuencia | Qué se actualiza solo |
|---|---|---|---|
| Top 10 rookies de la temporada 2026-27 (entrada 1885, https://undraftedzone.com/top-10-rookies-temporada-2026-27/) | `b-vivo-rookies-2026-27` | Semanal (lunes) | Las cifras de cada jugador y la fecha de «Actualizado» |

## Estructura obligatoria

- Cada jugador tiene su sección (H2 o H3) con: valoración propia (texto fijo) y una línea de cifras dentro de un bloque marcado:
  `<!-- stats:<slug-jugador>:inicio -->` … `<!-- stats:<slug-jugador>:fin -->`
- Al principio del cuerpo, una línea con la fecha dentro de `<!-- actualizado:inicio -->` … `<!-- actualizado:fin -->`, con el texto «Actualizado el D de mes de AAAA con los partidos hasta esa fecha».
- Las cifras van en lista o en una línea, nunca en tabla: partidos, minutos, puntos, rebotes, asistencias, % de tiros de campo y % de triples. Decimales con apóstrofo (15’2).
- La fuente se menciona una vez en el cuerpo, fuera de los bloques marcados.

## Actualización semanal

1. **Datos.** Las cifras de los diez jugadores se toman de ESPN (estadísticas de rookies o ficha de cada jugador) y se contrastan con Basketball-Reference, solo para verificar. Si una cifra no cuadra entre las dos, no se cambia y se deja una alerta.
2. **Solo bloques marcados.** Se sustituye el contenido de cada bloque `stats` y del bloque `actualizado`. Nada fuera de los marcadores cambia de forma automática.
3. **Propuesta de cambios de opinión.** Si un jugador sube o baja con claridad (por ejemplo, otro rookie le supera en puntos y minutos durante dos semanas seguidas) o una valoración ya no cuadra con sus cifras, se deja una alerta `incertidumbre` en el panel con la propuesta de nuevo orden o de nueva frase. No se aplica sin la aprobación de Alejandro.
   - **Jugador nuevo en el top (regla de Alejandro, 2026-11-12).** Si la propuesta mete a un jugador que no estaba en el top 10, el análisis escrito de ese jugador lo redacta Alejandro. Ningún agente escribe ni reescribe ese análisis. La alerta lo dice claramente («entra X, sale Y: falta tu análisis de X») e incluye solo sus cifras verificadas como apoyo. Hasta que Alejandro lo escriba, la entrada no cambia de orden y se siguen actualizando solo las cifras.
4. **Publicación.** El Publicador actualiza en WordPress solo los bloques marcados de la entrada registrada (ver `editorial/wordpress/PROMPT.md`).
5. **Registro.** Alerta `tecnica` con las cifras que cambiaron y la entrada actualizada.
