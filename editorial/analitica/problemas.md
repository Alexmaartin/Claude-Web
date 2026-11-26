# Problemas abiertos · undraftedzone.com

Lo mantiene el agente de Analítica cada día (ver `PROMPT.md` y `CONTEXTO.md`, sección 3). Última actualización: 26/11/2026, con datos hasta el 25/11.

| Problema | Detectado | Último visto | Días abierto | Estado | Nota |
|---|---|---|---|---|---|
| 410 en la portada «/» (también a Googlebot) | 15/11 | 25/11 | 11 | abierto, empeora | 25/11 (día de Madrid): 198 respuestas 410 en el día (38 el 24/11). En la muestra de «/», 194 de 602 (32 %). Googlebot recibe 410 en 32 de 310 peticiones de la muestra (10 %). Prioridad alta. |
| Caché casi apagada | 14/11 | 25/11 | 12 | abierto | 25/11: 15,8 % en el día de Madrid (24/11: 10,4 %; media de 7 días UTC: 18,6 %). Mejora, pero sigue por debajo de lo normal. |
| xmlrpc.php accesible | 14/11 | 25/11 | 12 | abierto | 25/11: en la muestra, 9 respuestas 403 y 2 respuestas 200. Hay que bloquearlo del todo. |
| 404 en `/data/wp/posts/boston-celtics.json` | 22/11 | 25/11 | 4 | abierto | Una petición 404 en la muestra del 22, del 24 y del 25. Revisar si la ficha de los Celtics pide un archivo que no se genera. |

## Resueltos

| Problema | Detectado | Resuelto | Nota |
|---|---|---|---|
| Falta favicon.ico | 15/11 | 22/11 | Responde 200 en la muestra del 22, del 23, del 24 y del 25. |
| 404 imagen Celtics | 17/11 | 23/11 | No aparece en la muestra del 22 ni del 23. Causa probable: la raya «–» del nombre de archivo. Revisar si reaparece. |

## Recurrentes

- 403 en un artículo legítimo sobre el draft.
- 429 en las fuentes y el logo de la propia web.
- 503, 429 y 504 entre `/wp-json` y el Worker de respaldo.
- Los PNG se llevan buena parte del ancho de banda.
- Escáneres que buscan `.env`, `.php` sueltos, `/wp-admin/` y copias de seguridad (`.zip`, `.sql`). 23/11: 1.236 de las 1.320 respuestas de las 17:00 (Madrid) fueron 4xx. 24/11: oleadas a las 09:00 y las 11:00 (Madrid), con 292 y 262 respuestas 4xx. 25/11: oleadas a las 02:00 y las 11:00 (Madrid), con 442 y 447 respuestas 4xx; en la muestra, EE. UU. aporta el 76 % de las peticiones.
