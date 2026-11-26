# Acciones en Cloudflare y en la web (las aplicas tú)

Cloudflare es de solo lectura para el sistema, y el CSS de la web no está en este repositorio. Estos son los pasos exactos, en orden de impacto. Cada uno se puede deshacer.

## 1. Portada «/» con 410 (prioridad)

Analítica ve respuestas 410 en «/» y también a Googlebot. Desde fuera, con tres navegadores distintos, la portada devuelve 200, así que hay que encontrar qué peticiones reciben el 410.

1. Cloudflare → tu dominio → **Analytics & Logs → Traffic**. Filtra por `Path = /` y `Edge status code = 410`. Mira qué **User agent**, **país** y **ASN** se repiten.
2. Revisa **Security → WAF → Custom rules** y **Rules → Redirect/Transform rules**: busca una regla con «Block» y respuesta personalizada 410. Es la causa más probable si solo afecta a ciertos bots.
3. Si no es de Cloudflare, el origen (WordPress) lo envía: revisa plugins de seguridad o de redirecciones (estado 410 para «gone»).
4. Para ver qué recibe Googlebot de verdad: **Search Console → Inspección de URLs → «/» → Probar URL publicada**. Si dice «No se puede acceder» o muestra 410, ya está confirmado.

## 2. Caché del HTML y de los JSON

La portada sale con `cf-cache-status: DYNAMIC` y `cache-control: public, max-age=300`: el origen lo permite, pero Cloudflare no lo guarda.

**Rules → Cache Rules → Create rule**, nombre «HTML público»:

- Expresión: `(http.host eq "undraftedzone.com") and not starts_with(http.request.uri.path, "/wp-admin") and not starts_with(http.request.uri.path, "/wp-login.php") and not http.cookie contains "wordpress_logged_in" and not http.cookie contains "wp-postpass"`
- Acción: **Eligible for cache**. Edge TTL: **Use cache-control header if present**, si no, 5 minutos.

Segunda regla, «JSON de datos»: `starts_with(http.request.uri.path, "/data/wp/")` → Eligible for cache, Edge TTL 10 minutos.

Después de crearlas, comprueba con `curl -sI https://undraftedzone.com/ | grep -i cf-cache-status` dos veces: la segunda debe decir `HIT`.

## 3. Escáneres y xmlrpc

El plan Free permite 5 reglas personalizadas. Una sola cubre lo principal. **Security → WAF → Custom rules → Create rule**, acción **Block**:

```
(http.request.uri.path eq "/xmlrpc.php")
or (http.request.uri.path.extension eq "php" and not http.request.uri.path in {"/index.php" "/wp-login.php" "/wp-cron.php"} and not starts_with(http.request.uri.path, "/wp-admin/") and not starts_with(http.request.uri.path, "/wp-includes/") and not starts_with(http.request.uri.path, "/wp-content/plugins/") and not starts_with(http.request.uri.path, "/wp-content/themes/"))
or (http.request.uri.path.extension in {"zip" "sql" "tar" "gz" "bak" "old" "7z" "rar"} and not starts_with(http.request.uri.path, "/wp-content/uploads/"))
or (http.request.uri.path contains "/.env")
or (http.request.uri.path contains "/.git")
```

La expresión no usa expresiones regulares, así que funciona en el plan Free. Cubre lo que Analítica ha visto: `/a.php`, `/222.php`, `/pi.php`, `/test.php`, `/wp-content/uploads/error.php`, `.env` y las copias de seguridad.

Si usas la app de WordPress o Jetpack, que necesitan `xmlrpc.php`, quita esa primera línea. Opcional: una regla de límite de peticiones para `/wp-login.php` (10 peticiones cada 10 segundos por IP).

## 4. Tablas en el móvil (CSS de la web)

La hoja de estilos aplica `overflow-wrap: anywhere` al contenido, y las tablas de más de 4 columnas se deshacen. En **Apariencia → Personalizar → CSS adicional** (o al final de `style.css`):

```css
.post-content .wp-block-table { overflow-x: auto; max-width: 100%; }
.post-content .wp-block-table td,
.post-content .wp-block-table th { overflow-wrap: normal; word-break: normal; white-space: nowrap; padding: .5rem .75rem; }
```

Con eso se podrían volver a usar tablas anchas (la tabla se desplaza en horizontal).

## 5. Search Console

Ver `editorial/analitica/SEARCH_CONSOLE.md`.
