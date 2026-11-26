# Conectar Google Search Console (solo lectura) a Analítica

**Para qué.** Cloudflare dice cuánta gente entra, pero no por qué búsquedas ni en qué posición sale cada artículo. Con Search Console, Analítica podría informar de clics, impresiones y posición del top 10 rookies, que es lo que mide el objetivo de «el artículo más leído».

**Qué tienes que hacer tú** (el sistema no puede crear accesos):

1. En Google Cloud, crea un proyecto y activa **Google Search Console API**.
2. Crea una **cuenta de servicio** y descarga su clave en JSON.
3. En Search Console → Configuración → Usuarios y permisos, añade el correo de esa cuenta de servicio como usuario **«Restringido»** (solo lectura) de la propiedad `undraftedzone.com`.
4. En el entorno del agente Analítica (Radar `env_01A4kWNnDQNZC9y6vm4grn3E`), añade la clave como secreto de red o variable `GSC_SERVICE_ACCOUNT_JSON` y permite los hosts `oauth2.googleapis.com` y `searchconsole.googleapis.com`.

**Qué hará el sistema después.** `editorial/scripts/search_console.py` (ya escrito, sin probar porque falta la clave) pide un token de solo lectura y consulta clics, impresiones, CTR y posición por página y por consulta. Analítica lo añadirá al informe diario y al panel, y Aprendizaje lo cruzará con las ediciones y los temas.

Nunca se guarda la clave en el repositorio, en el panel ni en el chat.
