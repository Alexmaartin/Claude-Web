# Registro de mejoras del panel (Diseño y UX)

Encargo de JalandBot (autorizado por Alejandro): iterar el panel por rondas, máximo 5.
Una ronda = un cambio con sentido, verificado en 400 px y escritorio con el arnés (`editorial/ux/arnes/`, datos de ejemplo) antes de publicar.

## Rondas hechas

| Ronda | Cambio | Commit | Versión publicada |
|---|---|---|---|
| 1 | Hoy: bloque «Estado del ciclo» (pasada diaria, borrador más reciente, verificación, alertas abiertas) | d771ae1 | v23 |
| 2 | Borradores: bloque «Verificación» (confirmadas, corregidas, sin comprobar, pendientes para el humano) e «Historial de cambios» (colección `ediciones`) | cfabe53 | v24 |
| 3 | Hoy: contraste de la etiqueta «Propuesta de hoy» sobre la portada | ab0a761 | v25 |

Sin cambios en la lógica de aprobación, publicación ni comprobaciones. No se han tocado colecciones ni nombres de campos.

## Errores y hallazgos

- **Error (corregido en el arnés, no en el panel):** en la vista móvil de Borradores parecía que la columna de detalle vacía aplastaba la lista. Causa: el arnés local no tenía la etiqueta `viewport`, así que se renderizaba a 980 px. En 400 px el panel se ve bien.
- **Error (pendiente):** el título de la propuesta de Hoy se pierde en su primera línea sobre la portada clara, porque el degradado solo cubre a partir del 20 %. Esfuerzo bajo, impacto medio.
- **Mejora (pendiente):** el bloque «Estado del ciclo» pluraliza mal («1 pendientes»); el titular largo del borrador ocupa demasiado sitio en la columna de valor.
- **Mejora (pendiente, prioridad 3 del encargo):** Aprobar, Devolver y Publicar en WordPress no piden confirmación dentro del panel. Cambiar esto toca la lógica de aprobación: requiere aviso a JalandBot antes de hacerlo.
- **Mejora (pendiente, prioridad 4):** revisar métricas en 400 px con datos reales (tablas de Core Web Vitals con scroll interno).
- **Mejora (pendiente, prioridad 5):** accesibilidad: el área de Borradores no anuncia el borrador seleccionado a lectores de pantalla.

## Propuesta para la siguiente tanda

1. Corregir el degradado del hero (error, esfuerzo bajo, impacto medio).
2. Pluralización y ancho del titular en «Estado del ciclo» (mejora, esfuerzo bajo, impacto bajo).
3. Confirmaciones dentro del panel para Aprobar, Devolver y Publicar (mejora, esfuerzo medio, impacto alto). Pendiente de aprobación de JalandBot porque toca la lógica de aprobación.
4. Revisión de métricas en 400 px con datos reales.
5. Accesibilidad de la selección en Borradores.
