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
- **Prohibido:** programar (`future`), publicar sin modo `publicar`, cambiar el estado de una entrada existente, editar o borrar entradas, tocar usuarios, ajustes, plugins, temas, medios o cualquier otra ruta de la API.
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

1. **Comprobación final.** Aplica `editorial/LISTA_PROHIBIDA.md` al texto completo, el titular, el extracto, las etiquetas y el pie. Si hay un término prohibido, no subas el borrador: cambia su estado a `devuelto`, con una alerta `tecnica` que diga qué término aparece.
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
