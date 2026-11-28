# Problemas abiertos · undraftedzone.com

Lo mantiene el agente de Analítica cada día (ver `PROMPT.md` y `CONTEXTO.md`, sección 3). Última actualización: 28/11/2026, con datos hasta el 27/11.

| Problema | Detectado | Último visto | Días abierto | Estado | Nota |
|---|---|---|---|---|---|
| 410 en la portada «/» (también a Googlebot) | 15/11 | 27/11 | 12 | abierto, mejora en volumen | 27/11 (día de Madrid): 190 respuestas 410 en el día (324 el 26/11). En la muestra de «/», 185 de 712 (26 %). Googlebot recibe 410 en 27 de 352 peticiones de la muestra (8 %). Sigue siendo prioridad. |
| Caché casi apagada | 14/11 | 27/11 | 13 | abierto | 27/11: 71,4 % en el día de Madrid, pero el dato viene del tráfico de ChromeHeadless. El día UTC de referencia no lo confirma como mejora. Sin cambio de fondo. |
| xmlrpc.php accesible | 14/11 | 27/11 | 13 | abierto | 27/11: en la muestra, 7 respuestas 403 y 2 respuestas 200. Hay que bloquearlo del todo. |
| 404 en `/data/wp/posts/<equipo>.json` | 22/11 | 27/11 | 5 | abierto, sin confirmar | Celtics (22, 24 y 25/11) y Bucks (26/11). El 27/11 no aparece en la muestra; sigue en vigilancia. |

## Resueltos

| Problema | Detectado | Resuelto | Nota |
|---|---|---|---|
| Falta favicon.ico | 15/11 | 22/11 | Responde 200 en la muestra del 22 al 27. |
| 404 imagen Celtics | 17/11 | 23/11 | No aparece en la muestra del 22 ni del 23. Causa probable: la raya «–» del nombre de archivo. Revisar si reaparece. |

## Recurrentes

- 403 en un artículo legítimo sobre el draft.
- 429 en las fuentes y el logo de la propia web.
- 503, 429 y 504 entre `/wp-json` y el Worker de respaldo.
- Los PNG se llevan buena parte del ancho de banda.
- Escáneres que buscan `.env`, `.php` sueltos, `/wp-admin/` y copias de seguridad (`.zip`, `.sql`, `.bak`). 23/11: 1.236 de las 1.320 respuestas de las 17:00 (Madrid) fueron 4xx. 24/11: oleadas a las 09:00 y las 11:00 (Madrid). 25/11: oleadas a las 02:00 y las 11:00 (Madrid). 26/11: pico de 2.681 peticiones a las 23:00 (Madrid). 27/11: 15.071 peticiones en el día de Madrid, con pico de 5.422 a las 21:00, ChromeHeadless como navegador dominante y el 85 % de la muestra desde España. Pendiente de confirmar en los logs del origen antes de decidir un bloqueo.
