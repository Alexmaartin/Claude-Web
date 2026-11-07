# Alerta técnica · comprobación de producción y aprendizaje · guía de los Nets

- Agente: Aprendizaje
- Encargo: JalandBot, de parte de Alejandro (2026-11-07)
- Borrador: b-20261107-nets · slug `brooklyn-nets-2026-27-piezas-futuro-veteranos-mercado` · ID WordPress 1860
- Estado: abierta, para revisión de JalandBot

## Corrección (JalandBot, 2026-11-07, tras la alerta original)

- **Cifras:** no son errores ni cambios de Alejandro. Son correcciones del Verificador contrastadas con Basketball-Reference (ediciones `ed-20261107-nets-01` a `08`, según JalandBot; no verificado desde este repo). La versión de producción es la correcta. Punto 2 de prioridad alta: resuelto.
- **Tablas:** la preferencia expresa 5 ya dice «Sin tablas» desde el commit `90944a0`. Quitar las tablas no contradice ninguna regla. Punto 3 y decisión (a): resueltos.
- **Frase del cierre:** es de Alejandro y es intencionada; no es una nota interna. Punto 1 y decisión (c): resueltos.
- **Pendiente:** etiquetas (punto 4), salvo que JalandBot indique lo contrario.

## 1. Problemas en producción (prioridad alta)

1. **Frase con tono de nota interna, publicada.** En la sección «Julius Randle» / última sección de cierre aparece: «El punto a destacar de brooklyn es que Julius Randle es su máximo asistente, sacar vosotros mismos vuestras propias conclusiones, las mías ya os lo adelanto, no son para nada buenas.» No está en el borrador. Parece un fragmento de nota, con una errata («brooklyn» en minúscula) y una afirmación («máximo asistente») que no he podido verificar. Revisar y corregir antes de que se quede.
2. **Cifras distintas de las del propio borrador.** El borrador (con su tabla de plantilla, sacada de ESPN) era coherente; la versión publicada no. Diferencias:
   - Edad media: 23’8 → 24’2. Calculada sobre las 18 filas de la tabla del borrador, la media es 23’8.
   - Posiciones: 9 aleros / 7 bases-escoltas / 2 pívots → 8 / 7 / 3. La tabla da 9 / 7 / 2.
   - Randle: 31 años y 13 temporadas → 32 años y 12 temporadas.
   - Porter Jr.: 8 temporadas → 7. Demin: 2 → 1. Clowney: 4 → 3. Wagner: 9 → 8.
   Todas las temporadas bajan una unidad. Parece un cambio sistemático, no un error puntual. Hay que decidir cuál es la versión correcta antes de dejarla.
3. **Tablas de plantilla eliminadas.** La versión publicada no tiene ninguna tabla (el borrador tenía dos). Ver el punto de la preferencia expresa 5 más abajo.
4. **Etiquetas incompletas.** Publicadas: `NBA`, `Michael Porter Jr.`, `traspasos`. Faltan `plantillas`, `brooklyn-nets` y `julius-randle` del borrador.

## 2. Comprobación de producción (sin credenciales, solo lectura)

- API pública (`/wp-json/wp/v2/posts?slug=…&_embed`): 200. Estado `publish`, modificado 2026-11-07 03:41 UTC.
- Página pública: 200. Canonical correcto. Título SEO «… — Undrafted Zone». Meta description = extracto. Imagen destacada y `og:image` presentes (`/wp-content/uploads/2026/11/1000096287.webp`).
- Imagen destacada: **presente** (ID 1865). No hace falta que el Publicador la arregle en esta entrada.
- Enlaces internos del cuerpo: 4 (`rookie-scale-…`, `brooklyn-nets-mikel-brown-jr-michael-porter-jr`, `julius-randle-brooklyn-minnesota-traspaso`, `sign-and-trade-…`). Los cuatro responden 200. Ningún enlace externo en el cuerpo.
- Categorías: solo `Brooklyn Nets` (ID 16).
- Restos de formato: sin `&nbsp;`, sin `**`, sin párrafos vacíos. Decimales con apóstrofo tipográfico (’). Sin «salary cap». Sin tablas. Sin restos de placeholders.

## 3. Cambios de Alejandro detectados (diff borrador → publicado)

- **Estructura:** tablas eliminadas (×2). FAQ «¿Por qué no aparecen salarios…?» eliminada. Se conservan las tres preguntas restantes.
- **Texto:**
  - Párrafo de introducción ampliado («…si acaban decidiendo reconstruir sobre su núcleo más joven»).
  - Párrafo de plantilla reescrito («…y te será útil para entender el margen de maniobra real que tienen los Nets en el futuro»).
  - Párrafo de traspasos: «reconstruir con una base aún más joven que la actual» (quitado «si decidiera»).
  - Cierre de la guía: nuevo párrafo informal (ver punto 1 de prioridad alta). Se pierde el aviso «Esta guía se actualizará…».
- **Cifras:** ver punto 2 de prioridad alta.
- **Metadatos:** título, slug y extracto iguales al borrador.

## 4. Patrones para APRENDIZAJE.md

Registrados como **observados** (un artículo, no confirmados):
- Tablas de plantilla eliminadas (contradice la preferencia expresa 5; no se aplica, se propone como alerta).
- Etiquetas recortadas (quita `plantillas`, `brooklyn-nets`, `julius-randle`).
- Categoría única «Brooklyn Nets».
- Eliminación de la FAQ sobre salarios.

**No registrado como patrón:** los cambios de cifras. Parecen errores, no preferencias de estilo.

## 5. Decisiones que necesita Alejandro

- ¿Se mantiene la preferencia expresa 5 (tablas de plantilla completas), o la de hoy sustituye a esa regla para esta guía?
- ¿Qué cifras son las correctas: las del borrador (coherentes con su tabla) o las publicadas?
- ¿Retirar o corregir la frase del cierre?

Ninguna de estas decisiones la tomo yo. No he escrito en WordPress ni he modificado ESTILO.md.
