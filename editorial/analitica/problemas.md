# Problemas abiertos · undraftedzone.com

Lo mantiene el agente de Analítica cada día (ver `PROMPT.md` y `CONTEXTO.md`, sección 3). Última actualización: 27/11/2026, con datos hasta el 26/11.

| Problema | Detectado | Último visto | Días abierto | Estado | Nota |
|---|---|---|---|---|---|
| 410 en la portada «/» (también a Googlebot) | 15/11 | 26/11 | 12 | abierto, empeora | 26/11 (día de Madrid): 324 respuestas 410 en el día (198 el 25/11, 38 el 24/11). En la muestra de «/», 318 de 655 (49 %). Googlebot recibe 410 en 45 de 368 peticiones de la muestra (12 %). Prioridad alta. |
| Caché casi apagada | 14/11 | 26/11 | 13 | abierto | 26/11: 63,1 % en el día de Madrid, pero la subida viene de tráfico de ChromeHeadless en la franja de las 22:00 a las 23:59, no de una mejora de la configuración. Sin cambio de fondo. |
| xmlrpc.php accesible | 14/11 | 26/11 | 13 | abierto | 26/11: en la muestra, 20 respuestas 403 y 2 respuestas 200. Hay que bloquearlo del todo. |
| 404 en `/data/wp/posts/<equipo>.json` | 22/11 | 26/11 | 5 | abierto | Celtics (22/11, 24/11 y 25/11) y Bucks (26/11). Parece un patrón: la web pide un JSON por equipo que no se genera. Revisar la generación de los archivos. |

## Resueltos

| Problema | Detectado | Resuelto | Nota |
|---|---|---|---|
| Falta favicon.ico | 15/11 | 22/11 | Responde 200 en la muestra del 22 al 26. |
| 404 imagen Celtics | 17/11 | 23/11 | No aparece en la muestra del 22 ni del 23. Causa probable: la raya «–» del nombre de archivo. Revisar si reaparece. |

## Recurrentes

- 403 en un artículo legítimo sobre el draft.
- 429 en las fuentes y el logo de la propia web.
- 503, 429 y 504 entre `/wp-json` y el Worker de respaldo.
- Los PNG se llevan buena parte del ancho de banda.
- Escáneres que buscan `.env`, `.php` sueltos, `/wp-admin/` y copias de seguridad (`.zip`, `.sql`). 23/11: 1.236 de las 1.320 respuestas de las 17:00 (Madrid) fueron 4xx. 24/11: oleadas a las 09:00 y las 11:00 (Madrid), con 292 y 262 respuestas 4xx. 25/11: oleadas a las 02:00 y las 11:00 (Madrid), con 442 y 447 respuestas 4xx. 26/11: pico de 2.681 peticiones entre las 23:00 y las 23:59 (Madrid), con ChromeHeadless como navegador dominante en la muestra. Se vigila; no se ha bloqueado nada.
