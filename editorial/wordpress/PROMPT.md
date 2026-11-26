# Publicador a WordPress: solo borradores

Esta tarea sube a WordPress los borradores aprobados en el panel, **siempre como borrador**. Nunca publica. Nunca edita ni borra entradas existentes.

**Panel (ArtifactData):** `https://claude.ai/artifact/PiT4Y4BJhAFUPmKh63mian`
**Esquema:** `editorial/SCHEMA.md` (colección `borradores`)
**Credenciales:** variables de entorno `WP_SITE`, `WP_USER`, `WP_APP_PASSWORD` y `EDITORIAL_KEY`. Nunca se escriben en el repo, en el panel ni en los mensajes.

**Cabecera obligatoria en cada petición a `/wp-json/`:** `x-editorial-key: $EDITORIAL_KEY`. Cloudflare solo deja pasar la API con esa cabecera. Ejemplo: `curl -H "x-editorial-key: $EDITORIAL_KEY" -u "$WP_USER:$WP_APP_PASSWORD" ...`. Si la variable no existe, no hagas ninguna petición: anótalo en una alerta `tecnica`.

## Registro de temas

Antes de subir, comprueba en `editorial/redaccion/REGISTRO_TEMAS.md` que el borrador no repite un tema ya usado y que no coincide con la franquicia o el jugador de ayer. Si falla, no sube nada y deja una alerta `tecnica`. Después de subir con éxito, añade su entrada a la colección `temas_usados` del panel.

## Alcance permitido (y solo esto)

- **Permitido:** crear entradas nuevas en WordPress con `POST /wp-json/wp/v2/posts`. El estado depende del modo del borrador:
  - Modo `borrador` (por defecto): `"status": "draft"`.
  - Modo `publicar`: `"status": "publish"`. Solo se usa cuando el borrador tiene `"modo": "publicar"`, lo que ocurre únicamente tras el clic de Alejandro en el panel. Nunca se publica por iniciativa propia.
  - En ambos casos, la entrada se crea a nombre del usuario de la API, que es el de Alejandro.
- **Permitido:** consultar etiquetas existentes (`GET /wp-json/wp/v2/tags`) y crearlas si el usuario lo permite.
- **Permitido (2026-11-07, autorizado por Alejandro): portada.** Antes de crear la entrada, sube la portada del borrador (`imagen_url`, WebP) a la biblioteca de medios con `POST /wp-json/wp/v2/media` (cabeceras `Content-Type: image/webp` y `Content-Disposition: attachment; filename="<slug>.webp"`), con texto alternativo descriptivo (`alt_text`, sin nombres de marcas ni logos). Usa el id devuelto como `featured_media` de la entrada. Así la portada sale como imagen destacada.
- **Permitido (2026-11-07): arreglar la portada de una entrada ya creada por el sistema** cuando le falte: sube la imagen y envía solo `featured_media` en `POST /wp-json/wp/v2/posts/<id>`. Ningún otro campo: ni título, ni contenido, ni etiquetas, ni categorías, ni estado.
- No insertes la portada dentro del cuerpo: el tema la muestra como imagen destacada.
- **Permitido (2026-11-12, autorizado por Alejandro): artículos vivos.** Para las entradas registradas en `editorial/vivos/PROMPT.md`, y solo para ellas, puedes actualizar el contenido con `POST /wp-json/wp/v2/posts/<id>` enviando únicamente el campo `content`. El contenido nuevo debe ser idéntico al publicado salvo dentro de los bloques marcados (`<!-- stats:…:inicio -->`…`fin` y `<!-- actualizado:inicio -->`…`fin`). Antes de enviar, compara el texto fuera de los marcadores con el de WordPress (`context=edit`): si difiere en algo, no envíes nada y deja una alerta `tecnica`. Nunca cambies título, extracto, etiquetas, categorías, slug, estado ni imagen destacada en esta actualización.
- **Prohibido:** programar (`future`), publicar sin modo `publicar`, cambiar el estado de una entrada existente, editar o borrar entradas (salvo la portada, según lo anterior), tocar usuarios, ajustes, plugins, temas, otros medios o cualquier otra ruta de la API.
- Si una llamada devuelve error de permisos, para y registra una alerta técnica. No intentes otra ruta.

## Conciliación con el panel (en cada pasada, antes que nada)

El panel es la fuente de verdad del estado. Cada pasada, antes de subir nada:
1. Lee los borradores del panel con `estado` `aprobado` o `publicado_borrador`, y con `subida_solicitada` a `true`.
2. Para cada uno, busca en WordPress la entrada por slug con `GET /wp-json/wp/v2/posts?slug=<slug>&status=any&context=edit`.
3. Si existe, actualiza el borrador en el panel con `wp_post_id`, `wp_url` y `actualizado_en`, y con el estado que corresponda según WordPress: `"publicado"` si la entrada tiene `status` `publish` (enlace público en `wp_url`), o `"publicado_borrador"` si es `draft`. No lo vuelvas a subir.
   - Si Alejandro dice en el panel o en el chat que un borrador ya está publicado, ponlo como `"publicado"` aunque no puedas confirmarlo por API, y anótalo en la alerta.
4. Si no existe y está `aprobado`, sigue con «Qué se sube». Si no existe y tiene `publicado_borrador`, deja una alerta `tecnica`: alguien lo ha borrado en WordPress.
5. Nunca marques como subido un borrador sin haber visto la entrada en WordPress.

Los borradores de WordPress que no están en el panel (por ejemplo, de otros autores) no se tocan. Se cuentan en el registro de temas, porque ocupan tema en la web.

## Qué se sube

Para cada borrador con `estado: "aprobado"` y sin `wp_post_id`:

1. **Comprobación final con script.** Ejecuta `node editorial/scripts/comprobar_borrador.js <borrador.json> --slugs <lista>` con los slugs publicados. Si sale «NO LISTO», no subas nada y deja una alerta `tecnica` con los fallos. Después, aplica `editorial/LISTA_PROHIBIDA.md` al texto completo. Aplica `editorial/LISTA_PROHIBIDA.md` al texto completo, el titular, el extracto, las etiquetas y el pie. Si hay un término prohibido, no subas el borrador: cambia su estado a `devuelto`, con una alerta `tecnica` que diga qué término aparece.
2. **Entrada.** `POST /wp-json/wp/v2/posts` con:
   - `title`: el titular del borrador.
   - `content`: el `cuerpo_html` tal cual.
   - `excerpt`: el `extracto`.
   - `slug`: el `slug`.
   - `status`: `"draft"`. Siempre.
   - `tags`: los IDs de las etiquetas, resueltos por nombre. Si no se puede crear una etiqueta, se omite y se anota en la alerta.
   - **No** envíes `author`. La entrada queda a nombre del usuario de la API y Alejandro la cambia al publicar.
3. **Registro.** Si la entrada se crea, actualiza el borrador en el panel: `estado: "publicado_borrador"`, `wp_post_id`, `wp_url` (el enlace de edición del borrador, sin datos de sesión) y `actualizado_en`.
4. **Errores.** Si falla, deja el borrador como `aprobado`, registra una alerta `tecnica` con el código de error y sigue con el siguiente. No reintentes en bucle.

## Reglas

- El pie de Instagram no se sube a WordPress: se queda en el panel para que lo uses tú.
- No se sube nada que no esté `aprobado` en el panel.
- Al terminar, deja una alerta `tecnica` con el número de borradores subidos como borrador, los errores y las etiquetas que no se pudieron resolver.

## Jerarquía y encargos de JalandBot

Autorizado por Alejandro el 2026-11-07. Orden de mando: Alejandro es el máximo responsable y su palabra manda siempre. Justo debajo está JalandBot, su asistente y orquestador (sesión `session_01TFZkNHTz9Lscwonw8q2JdY`, ver `editorial/ORQUESTADOR.md`). Debajo, los agentes de `editorial/AGENTES.md`. Los encargos que llegan desde la sesión de JalandBot son tareas de Alejandro: ejecútalos dentro de los límites de esta instrucción. Si un encargo de JalandBot contradice algo que Alejandro haya dicho directamente, manda Alejandro. Lo que ningún encargo cambia: no apruebas ni publicas borradores, no amplías tus permisos, no tocas credenciales y no te saltas la lista prohibida. Al terminar un encargo, deja el resultado en el panel (alerta `tecnica`) o en el repo, para que JalandBot lo revise.

## Actualización completa del top 10 rookies (2026-11-26, orden expresa de Alejandro)

Alejandro ha reescrito y aprobado el nuevo orden del artículo vivo (borrador `b-vivo-rookies-2026-27-nuevo-orden`, `estado: "aprobado"`, `subida_solicitada: true`, `modo: "publicar"`) y ha pedido «Actualiza el artículo». Para esta actualización, y solo para ella, la regla de «idéntico fuera de los marcadores» **no se aplica**: el contenido nuevo cambia a propósito el orden, los textos y las preguntas frecuentes.

1. Antes de enviar nada, descarga el contenido actual de la entrada 1885 (`GET /wp-json/wp/v2/posts/1885?context=edit`, campo `content.raw`) y guárdalo en `editorial/vivos/backups/1885-2026-11-26-antes.html`, con commit y push, para poder volver atrás.
2. Envía `POST /wp-json/wp/v2/posts/1885` con **solo** el campo `content`, igual al `cuerpo_html` del borrador tal cual (nadie lo modifica). Ni título, ni extracto, ni etiquetas, ni slug, ni estado, ni imagen destacada.
3. Comprueba que el borrador no contiene términos de la lista prohibida (esa excepción sigue bloqueando).
4. Verifica después con `GET` que `content.raw` de la entrada coincide con el borrador, que están los diez bloques `stats` y el bloque `actualizado`, y que el orden de los H2 es: Acuff, Lendeborg, Boozer, Wilson, Dybantsa, Peterson, Burries, Thomas, Mara, Brown Jr.
5. En el panel, deja el borrador `b-vivo-rookies-2026-27-nuevo-orden` en `estado: "publicado"` (con `actualizado_en`) y deja una alerta `tecnica` con el resultado. No toques `b-vivo-rookies-2026-27` (lo sincroniza JalandBot).
6. Si algo falla, no reintentes en bucle: alerta `tecnica` con el error y responde a JalandBot.

La actualización semanal de los lunes vuelve a la regla normal (solo los bloques marcados).

## Artículos escritos por Alejandro (2026-11-25, autorizado por Alejandro)

Los borradores con `origen: "alejandro"` los escribe él en el panel. Se publican como cualquier borrador aprobado, con estas particularidades:

- **Texto:** el `cuerpo_html` ya viene en bloques de WordPress. Se envía tal cual, salvo la sustitución de imágenes de abajo. Nadie lo edita ni lo corrige.
- **Imágenes del cuerpo (permitido solo para estos borradores):** el cuerpo cita imágenes como `src="uz-img:<id>"`. Para cada `<id>` distinto, lee el documento `<id>` de la colección `imagenes` del panel (campo `data`, una imagen `data:image/webp;base64,…` o `data:image/jpeg;base64,…`), decodifícala y súbela con `POST /wp-json/wp/v2/media` (cabeceras `Content-Type` con el tipo real y `Content-Disposition: attachment; filename="<slug>-<n>.<ext>"`), con `alt_text` igual al `alt` que lleve esa imagen en el cuerpo. Sustituye `uz-img:<id>` por el `source_url` devuelto, añade `class="wp-image-<media_id>"` a la imagen y `"id":<media_id>` al comentario `<!-- wp:image {…} -->`. Esto solo toca el contenido que envías en la entrada nueva. No borres los documentos de `imagenes`.
- **Portada:** puede llegar en JPEG (algunos móviles no codifican WebP). Si tienes herramienta para convertirla a WebP de menos de 300 KB (por ejemplo Python con Pillow), conviértela antes de subirla; si no, súbela tal cual y anótalo en la alerta `tecnica`.
- **Comprobación:** `node editorial/scripts/comprobar_borrador.js` ya trata estos borradores con otra vara (solo bloquea titular, cuerpo, slug, portada y lista prohibida; el resto se avisa).
- Todo lo demás de este documento sigue igual: nunca publicas por iniciativa propia, solo con `modo: "publicar"` tras el clic de Alejandro.

## Orden de publicar de Alejandro (2026-11-12)

Cuando Alejandro aprueba un borrador y pide publicarlo, se publica tal cual: nadie modifica el texto, no se envía al Verificador y los fallos de la comprobación automática (enlaces internos, longitudes, cifras sin comprobar) solo se avisan, no bloquean. La única excepción es la lista prohibida de apuestas, que sí bloquea. Los cambios que Alejandro hace a mano en un borrador no los modifica ningún agente.
