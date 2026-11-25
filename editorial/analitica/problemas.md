# Problemas abiertos · undraftedzone.com

Lo mantiene el agente de Analítica cada día (ver `PROMPT.md` y `CONTEXTO.md`, sección 3). Última actualización: 25/11/2026, con datos hasta el 24/11.

| Problema | Detectado | Último visto | Días abierto | Estado | Nota |
|---|---|---|---|---|---|
| 410 en la portada «/» (también a Googlebot) | 15/11 | 24/11 | 10 | abierto | 24/11 (día de Madrid): 36 respuestas 410 en «/» sobre 405 de la muestra (9 %). Googlebot recibe 410 en 37 de 339 peticiones de la muestra (11 %). Sigue sin resolverse. |
| Caché casi apagada | 14/11 | 24/11 | 11 | abierto | 24/11: 10,4 % en el día de Madrid y 6,7 % en el día UTC (23/11: 7,2 %; media de 7 días UTC: 18,3 %). Los días 19 a 21 llegaron al 18–32 %, así que no es constante. |
| xmlrpc.php accesible | 14/11 | 24/11 | 11 | abierto | 24/11: en la muestra, 4 respuestas 403 y 2 respuestas 200. Hay que bloquearlo del todo. |
| 404 en `/data/wp/posts/boston-celtics.json` | 22/11 | 24/11 | 3 | abierto | Una sola petición 404 en la muestra del 22 y otra en la del 24. Revisar si la ficha de los Celtics pide un archivo que no se genera. |

## Resueltos

| Problema | Detectado | Resuelto | Nota |
|---|---|---|---|
| Falta favicon.ico | 15/11 | 22/11 | Responde 200 en la muestra del 22, del 23 y del 24. |
| 404 imagen Celtics | 17/11 | 23/11 | No aparece en la muestra del 22 ni del 23. Causa probable: la raya «–» del nombre de archivo. Revisar si reaparece. |

## Recurrentes

- 403 en un artículo legítimo sobre el draft.
- 429 en las fuentes y el logo de la propia web.
- 503, 429 y 504 entre `/wp-json` y el Worker de respaldo.
- Los PNG se llevan buena parte del ancho de banda.
- Escáneres que buscan `.env`, copias de seguridad (`.zip`, `.sql`) y similares. 23/11: 1.236 de las 1.320 respuestas de la hora de las 17:00 (Madrid) fueron 4xx. 24/11: oleadas a las 09:00 y las 11:00 (Madrid), con 292 y 262 respuestas 4xx.
