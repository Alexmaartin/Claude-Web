# Guías, SEO y verificación: norma vinculante desde el 6 de noviembre de 2026

Estas reglas salen de la analítica de undraftedzone.com y mandan sobre cualquier otra instrucción de redacción, salvo las preferencias expresas de Alejandro (ver `editorial/redaccion/PROMPT.md`) y la lista prohibida.

## 1. Guías, no última hora

- Las noticias del día rinden 9–11 visitas. Las guías rinden mucho más: la guía de la NCAA hizo 223 visitas en 18 días, y las de WikiUndrafted rinden el doble que la media.
- Por eso el artículo de una franquicia **no es una crónica de la noticia**. Es una guía de la franquicia (plantilla, rotación, contratos, calendario, qué mirar), que sigue sirviendo meses después.
- Una noticia bomba (lesión grave, traspaso confirmado, decisión que cambia la temporada) puede sustituir la guía del día, pero se redacta como guía del tema: contexto, qué cambia y qué no sabemos.

### Lista de ideas de guías

Franquicia (una por equipo, en el turno de `ROTACION.md`):
- Timberwolves: plantilla y roles 2026-27, con tabla completa.
- Nets: plantilla, contratos y margen salarial.
- Heat: plantilla y rotación, con tabla completa.
- Clippers: plantilla y margen salarial.
- Bucks: plantilla, contratos y qué espera la temporada.
- Thunder: plantilla, bajas y calendario.
- 76ers: plantilla, contratos y claves de la temporada.
- Kings: plantilla y proyecto de juego.
- Jazz: plantilla, contratos y proyecto.
- Bulls: plantilla, margen salarial y agencia libre.

Evergreen (banco en `TEMAS_EVERGREEN.md`): contratos two-way, draft (lotería y picks), sorteo del draft, espacio salarial, luxury tax y aprons, regla Harry Giles, glosario de la NCAA, agencia libre paso a paso, agencia libre restringida, Summer League, roster y G League, pick protegido, estadísticas avanzadas, guía de la temporada NCAA.

## 2. Titular

- Mayúsculas normales (sin todo en mayúsculas).
- Entre 50 y 65 caracteres.
- Palabra clave al principio, y la temporada (2026-27) en el titular.

## 3. Título SEO y descripción (Yoast)

- Título SEO y meta descripción propios, distintos del titular, con la palabra clave.
- Objetivo de clic: 2–4 %. Las guías actuales rinden 0,5–1 %, así que el título SEO tiene que prometer algo concreto.

## 4. Estructura

- **Entradilla** que responde a la pregunta del artículo en 2–4 frases.
- **Un H2 cada 250–400 palabras.** H3 dentro de cada H2 si hace falta.
- **Tablas** cuando haya datos: plantilla, contratos, calendario, glosario.
- **Sección «Preguntas frecuentes»** al final, con preguntas reales y respuestas cortas.
- **Longitud:** guías de 1.500–3.000 palabras. Las noticias bomba pueden ser más cortas, pero nunca menos de 600.

## 5. Enlaces internos

- **3–5 enlaces internos obligatorios** a otros artículos publicados. Se eligen de la lista de publicados (`editorial/corpus/INDICE.md`, o el panel).
- Si no hay suficientes artículos para enlazar, se anota en una alerta `tecnica`, pero el artículo no se bloquea por eso.

## 6. Fuentes y cifras

- **Ninguna cifra sin comprobar.** Cada cifra se comprueba en la fuente antes de escribirla. Si no se puede comprobar, no se escribe.
- Las fuentes se citan y se enlazan. **Pendiente de decisión:** la preferencia de Alejandro dice «sin hipervínculos externos en el cuerpo», con las fuentes en un dossier aparte. Hasta que lo decida, las fuentes van en el campo `fuentes` del borrador, sin enlaces en el cuerpo.

## 7. Estilo de la casa

- Siempre «espacio salarial», nunca «salary cap» ni «cap space».

## 8. Prohibido siempre

- Apuestas y cuotas, en cualquier forma (ver `LISTA_PROHIBIDA.md`).
- Datos personales de jugadores, familiares o terceros que no sean públicos y relevantes.
- Copiar o parafrasear otros medios. Ver la regla de originalidad.

## 9. Portada

- Formato **1600×900 px, WebP, menos de 300 KB**.
- Sin fotos de agencias, sin fotos de jugadores reconocibles y sin logos ni escudos.
- Portada generada con la plantilla (dato destacado, símbolo del tema y pista de cancha, con el color de la franquicia). Si es ilustrada con IA, lleva su leyenda.

## 10. Categoría, etiquetas y slug

- **Categoría:** una existente (franquicia o temática), como máximo dos.
- **Etiquetas:** 3–6, con las que ya existen en WordPress.
- **Slug:** minúsculas, guiones, sin fechas salvo la temporada si es necesaria, y con la palabra clave.

## 11. Autoría y transparencia

- Todo artículo lo **aprueba un redactor humano** antes de publicarse. Hoy lo aprueba Alejandro desde el panel.
- Cada artículo indica que el texto está generado con IA y que lo revisa un redactor. La redacción de ese aviso se añade al pie del artículo.
- Referencia legal: el Reglamento de IA de la UE establece obligaciones de transparencia para el texto generado por IA que se publica para informar al público. Lo que sigue es una interpretación de trabajo, no un dictamen jurídico: conviene que lo confirme un abogado antes de publicar sin revisión humana.

## 12. Actualización por temporada

- Las guías se actualizan cada temporada. Al actualizar, se añade el aviso «Actualizado» con la fecha y la temporada.
- Una guía antigua no se borra: se actualiza con su URL.

## 13. Lista de comprobación antes de publicar

El sistema la verifica antes de dejar el borrador como `pendiente_revision`. Todo tiene que cumplirse:

- [ ] Titular en mayúsculas normales, 50–65 caracteres, palabra clave al principio, temporada incluida.
- [ ] Título SEO y meta descripción presentes, distintos del titular, con la palabra clave.
- [ ] Entradilla de 2–4 frases que responde a la pregunta.
- [ ] Un H2 cada 250–400 palabras (medido por el texto).
- [ ] Al menos una tabla si el artículo trata de plantilla, contratos, calendario o glosario.
- [ ] Sección «Preguntas frecuentes» al final.
- [ ] Longitud dentro del rango (guía 1.500–3.000 palabras; noticia bomba mínimo 600).
- [ ] 3–5 enlaces internos a artículos publicados, sin enlaces externos en el cuerpo.
- [ ] Todas las cifras comprobadas en la fuente; las fuentes en el campo `fuentes`.
- [ ] «espacio salarial» en vez de «salary cap».
- [ ] Ninguna mención a apuestas, cuotas, datos personales ni copia de otros medios.
- [ ] Portada 1600×900 WebP, menos de 300 KB, sin fotos de agencias ni logos, con leyenda si es ilustrada con IA.
- [ ] Categoría, etiquetas y slug según el punto 10.
- [ ] Aviso de texto generado con IA y revisión humana.
- [ ] Si es actualización de temporada, aviso «Actualizado» con fecha.

Si una casilla no se cumple, el borrador no pasa a `pendiente_revision`: se deja una alerta `tecnica` con la casilla que falla.
