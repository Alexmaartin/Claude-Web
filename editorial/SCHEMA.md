# Sistema editorial UndraftedZone: esquema de datos

Este documento define las colecciones de la base de datos del panel (`ArtifactData`) y las reglas de cada campo. Lo usan el radar, la redacción, el auditor SEO y el propio panel.

## Principios

- **Nada se publica sin aprobación.** El panel marca un borrador como `aprobado`; la publicación en WordPress es un paso posterior y deja el artículo como borrador en WordPress.
- **Cada dato lleva su fuente.** Sin fuente oficial o dos independientes, la noticia se marca como `sin_confirmar`.
- **Los cambios en fichas son propuestas.** Se aplican solo cuando alguien las acepta en el panel.
- **Una noticia, una entrada.** Las coincidencias se agrupan con `grupo_id`; no se crean tareas duplicadas.

## Colecciones

| Colección | Qué guarda | Quién escribe |
| --- | --- | --- |
| `noticias` | Noticias detectadas y verificadas | Radar |
| `borradores` | Artículos listos para revisar, con sus metadatos | Redacción (crea), panel (aprueba o devuelve) |
| `fichas` | Estado actual de jugadores y equipos | Panel (al aceptar cambios) |
| `cambios_ficha` | Propuestas de cambio sobre una ficha, con valor anterior y nuevo | Radar |
| `incidencias_seo` | Problemas SEO priorizados | Auditor SEO |
| `alertas` | Asuntos que requieren criterio humano | Cualquier agente |

## `noticias`

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `titulo` | texto | Titular provisional, en español |
| `url` | texto | URL de la fuente original (solo `https://`) |
| `fuente` | texto | Medio o entidad (NBA.com, Shams Charania, etc.) |
| `tipo_fuente` | `oficial` \| `periodista` \| `medio` \| `rumor` | Naturaleza de la fuente |
| `confianza` | `alta` \| `media` \| `baja` | Según tipo de fuente y número de fuentes independientes |
| `resumen` | texto | Dos o tres frases, sin copiar texto de medios |
| `grupo_id` | texto | Identificador de la historia agrupada |
| `fecha` | ISO 8601 | Fecha de publicación de la fuente |
| `detectada_en` | ISO 8601 | Momento en que el radar la capturó |
| `estado` | `nueva` \| `para_redactar` \| `descartada` \| `sin_confirmar` \| `redactada` | Estado de la noticia |

## `borradores`

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `titulo` | texto | Titular final propuesto |
| `slug` | texto | Ver reglas abajo |
| `extracto` | texto | Ver reglas abajo |
| `etiquetas` | lista de texto | Ver reglas abajo |
| `pie_instagram` | texto | Ver reglas abajo |
| `cuerpo_html` | texto | Artículo en HTML, listo para pegar en WordPress |
| `noticia_id` | texto | Noticia de origen |
| `fuentes` | lista de texto | URLs de todas las fuentes citadas |
| `confianza` | `alta` \| `media` \| `baja` | Heredada de la noticia o rebajada por la redacción |
| `estado` | `pendiente_revision` \| `aprobado` \| `devuelto` \| `publicado_borrador` | Ciclo del borrador |
| `fecha` | ISO 8601 | Creación del borrador |
| `actualizado_en` | ISO 8601 | Última modificación |

### Reglas de los metadatos

**`slug`**
- Solo minúsculas, números y guiones: `^[a-z0-9]+(-[a-z0-9]+)*$`.
- Sin acentos ni artículos sobrantes. Entre 3 y 8 palabras.
- Si la noticia gira en torno a un jugador, incluye su apellido.
- Único dentro de `borradores`. Si ya existe, añade el año o la fecha.
- Ejemplo: `lesion-tatum-tobillo-playoffs-2027`

**`extracto`**
- Entre 140 y 160 caracteres. Sirve de descripción para buscadores y para la portada.
- Dice qué pasó y a quién afecta. Sin adjetivos que la fuente no respalde.
- No empieza por "En este artículo" ni por preguntas retóricas.

**`etiquetas`**
- Entre 3 y 6, en minúsculas, sin acentos, separadas por guiones si son compuestas.
- Una etiqueta de competición (`nba`, `ncaa`, `draft`, `europa`), una de tipo (`lesiones`, `traspasos`, `renovaciones`, `mercado`, `declaraciones`) y las de jugadores o equipos implicados (`celtics`, `jayson-tatum`).
- No repetir la misma etiqueta con distinta forma (`lesion` y `lesiones`).

**`pie_instagram`**
- Máximo 2.200 caracteres, pero para leerse de un vistazo busca unos 150–250.
- Estructura: gancho en la primera línea, dato clave, fuente si es relevante, y entre 3 y 5 hashtags al final.
- Sin emojis salvo que el tono de la cuenta lo pida; sin mencionar cuentas ajenas salvo que la fuente lo exija.
- El pie se escribe a partir de los hechos del borrador, nunca de la especulación.

## `fichas`

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `tipo` | `jugador` \| `equipo` | Entidad |
| `nombre` | texto | Nombre completo |
| `equipo` | texto | Equipo actual |
| `posicion` | texto | Posición |
| `contrato` | texto | Situación contractual, solo con fuente fiable |
| `verificado_en` | ISO 8601 | Última verificación de cualquier campo |
| `fuente_ultima` | texto | Fuente del último cambio aceptado |

Los campos de la ficha son de primer nivel (sin anidar), para que el panel pueda aplicar un cambio con una sola escritura.

## `cambios_ficha`

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `ficha_id` | texto | Identificador de la ficha afectada |
| `entidad` | texto | Nombre visible (p. ej. "Jayson Tatum") |
| `campo` | texto | Nombre del campo, de primer nivel (p. ej. `equipo`) |
| `valor_anterior` | texto | Valor que hay ahora |
| `valor_nuevo` | texto | Valor propuesto |
| `fuente` | texto | URL o referencia de la fuente |
| `motivo` | texto | Una frase: qué ha pasado |
| `estado` | `propuesto` \| `aceptado` \| `rechazado` | Estado de la propuesta |
| `fecha` | ISO 8601 | Cuándo se propuso |

## `incidencias_seo`

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `pagina` | texto | URL afectada |
| `problema` | texto | Enlace roto, no indexada, contenido obsoleto, rendimiento, etc. |
| `prioridad` | `alta` \| `media` \| `baja` | Según impacto y confianza |
| `impacto` | texto | Por qué importa, con datos si existen (clics, impresiones) |
| `sugerencia` | texto | Acción concreta |
| `estado` | `abierta` \| `resuelta` \| `ignorada` | |
| `fecha` | ISO 8601 | Detección |

## `alertas`

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `tipo` | `noticia_importante` \| `incertidumbre` \| `seo` \| `tecnica` | |
| `mensaje` | texto | Qué necesita tu criterio, en una frase |
| `contexto` | texto | Enlace o referencia a la noticia, borrador o incidencia |
| `estado` | `abierta` \| `resuelta` | |
| `fecha` | ISO 8601 | |

## Reglas de escritura

- Las fechas van en ISO 8601 con zona horaria.
- Cada escritura desde un agente pone `actualizado_en` (o `detectada_en` / `fecha` al crear).
- Antes de crear una noticia, buscar por `grupo_id` y por `url`; si existe, actualizar en lugar de duplicar.
- Antes de crear un borrador, comprobar que el `slug` no existe.
- El panel es la única superficie que cambia `estado` de borradores y fichas.
- **Ningún documento contiene contenido sobre apuestas ni juego de azar.** Todo texto se contrasta con `editorial/LISTA_PROHIBIDA.md` antes de escribirse.
