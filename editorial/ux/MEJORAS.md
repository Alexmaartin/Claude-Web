# Registro de mejoras del panel (Diseño y UX)

Encargo de JalandBot (autorizado por Alejandro): iterar el panel por rondas, máximo 5.
Una ronda = un cambio con sentido, verificado en 400 px y escritorio con el arnés (`editorial/ux/arnes/`, datos de ejemplo) antes de publicar.

## Rondas hechas

| Ronda | Cambio | Commit | Versión publicada |
|---|---|---|---|
| 1 | Hoy: bloque «Estado del ciclo» (pasada diaria, borrador más reciente, verificación, alertas abiertas) | d771ae1 | v23 |
| 2 | Borradores: bloque «Verificación» (confirmadas, corregidas, sin comprobar, pendientes para el humano) e «Historial de cambios» (colección `ediciones`) | cfabe53 | v24 |
| 3 | Hoy: contraste de la etiqueta «Propuesta de hoy» sobre la portada | ab0a761 | v25 |
| 4 | Hoy: degradado del hero más oscuro para que el titular se lea entero (propuesta 1 de la siguiente tanda) | 9ff606e | v26 |
| 5 | Hoy: «1 pendiente» en singular y «Último borrador» como etiqueta (propuesta 2) | d21e23a | v27 |
| 6 | Confirmación dentro del panel antes de Aprobar, Devolver y Solicitar publicación en WordPress (propuesta 3 de la tanda 2). El primer toque pide confirmar; el segundo ejecuta la misma acción, sin cambiar qué se escribe ni cuándo. Probado: un toque no escribe, dos sí. | f4e42ce | v28 |
| 7 | Métricas en 400 px: los KPIs quedan en cuadrícula 2x2 sin hueco; la última etiqueta del gráfico ya no se recorta (propuesta 4) | 2aaf6a2 | v29 |
| 8 | Borradores: la selección lleva `aria-pressed` y el foco pasa al titular del detalle al abrir (propuesta 5) | 6ab883b | v30 |

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

## Tanda 2 (aprobada por JalandBot): cerrada

Propuestas 3, 4 y 5 hechas en las rondas 6, 7 y 8. Con esto se cierra la tanda.

Nota sobre la propuesta 3: la aprobación de JalandBot pedía solo añadir un paso de confirmación. Se cumple: el primer toque muestra la pregunta y el segundo ejecuta la misma escritura de siempre.

## Siguiente tanda (propuesta, pendiente de aprobación)

1. **Dos capturas de pantalla reales en el informe.** Hoy el arnés usa datos de ejemplo. Falta un arnés de métricas con histórico real para revisar gráficas y tablas de CWV en 400 px.
2. **Estado vacío y error de la base de datos.** Ahora solo aparece «Sin acceso a los datos» cuando no hay db; falta un estado para cuando la lectura falla a mitad de sesión.
3. **Vista previa limpia del artículo.** En móvil el artículo se muestra con todo el HTML; un modo «leer» con tipografía del artículo ayudaría a revisar.
4. **Revisión por lotes.** Aprobar o devolver varios borradores a la vez; hoy es uno a uno.

Impacto y esfuerzo: 1 medio/bajo, 2 medio/bajo, 3 medio/medio, 4 alto/medio. Ordenado por impacto dividido entre esfuerzo: 2, 1, 3, 4.
