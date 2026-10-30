# Publicador a WordPress: solo borradores

Esta tarea sube a WordPress los borradores aprobados en el panel, **siempre como borrador**. Nunca publica. Nunca edita ni borra entradas existentes.

**Panel (ArtifactData):** `https://claude.ai/artifact/PiT4Y4BJhAFUPmKh63mian`
**Esquema:** `editorial/SCHEMA.md` (colección `borradores`)
**Credenciales:** variables de entorno `WP_SITE`, `WP_USER`, `WP_APP_PASSWORD` y `EDITORIAL_KEY`. Nunca se escriben en el repo, en el panel ni en los mensajes.

**Cabecera obligatoria en cada petición a `/wp-json/`:** `x-editorial-key: $EDITORIAL_KEY`. Cloudflare solo deja pasar la API con esa cabecera. Ejemplo: `curl -H "x-editorial-key: $EDITORIAL_KEY" -u "$WP_USER:$WP_APP_PASSWORD" ...`. Si la variable no existe, no hagas ninguna petición: anótalo en una alerta `tecnica`.

## Alcance permitido (y solo esto)

- **Permitido:** crear entradas nuevas en WordPress con `POST /wp-json/wp/v2/posts`, siempre con `"status": "draft"`.
- **Permitido:** consultar etiquetas existentes (`GET /wp-json/wp/v2/tags`) y crearlas si el usuario lo permite.
- **Prohibido:** publicar, programar (`future`), cambiar el estado de una entrada existente, editar o borrar entradas, tocar usuarios, ajustes, plugins, temas, medios o cualquier otra ruta de la API.
- Si una llamada devuelve error de permisos, para y registra una alerta técnica. No intentes otra ruta.

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
