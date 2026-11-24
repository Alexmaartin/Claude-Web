# Problemas abiertos · undraftedzone.com

Lo mantiene el agente de Analítica cada día (ver `PROMPT.md` y `CONTEXTO.md`, sección 3). Última actualización: 24/11/2026, con datos hasta el 23/11 (día de Madrid).

| Problema | Detectado | Último visto | Días abierto | Estado | Nota |
|---|---|---|---|---|---|
| 410 en la portada «/» (también a Googlebot) | 15/11 | 23/11 | 9 | abierto | 23/11: 22 de 239 peticiones de Googlebot en la muestra (9 %) recibieron 410. En «/», la muestra tiene 20 410, 135 403 y 80 200. Sigue sin resolverse. |
| Caché casi apagada | 14/11 | 23/11 | 10 | abierto | 23/11: 7,2 % (22/11: 24,8 %; media de 7 días UTC: 16,2 %). Los días 19 a 21 llegaron al 18–32 %, así que no es constante. |
| xmlrpc.php accesible | 14/11 | 23/11 | 10 | abierto | 23/11: 7 de 9 respuestas en la muestra son 403, pero 2 son 200. Hay que bloquearlo del todo. |

## Resueltos

| Problema | Detectado | Resuelto | Nota |
|---|---|---|---|
| 404 imagen Celtics | 17/11 | 23/11 | No aparece en la muestra del 22 ni del 23. Causa probable: la raya «–» del nombre de archivo. Revisar si reaparece. |
| Falta favicon.ico | 15/11 | 22/11 | Responde 200 en la muestra del 22 y del 23. |

## Recurrentes

- 403 en un artículo legítimo sobre el draft.
- 429 en las fuentes y el logo de la propia web.
- 503, 429 y 504 entre `/wp-json` y el Worker de respaldo.
- Los PNG se llevan buena parte del ancho de banda.
- Escáneres que buscan `.env`, copias de seguridad (`.zip`, `.sql`) y similares. 23/11: 1.236 de las 1.320 respuestas de la hora de las 17:00 (Madrid) fueron 4xx, casi todas 403 a rutas de copia de seguridad.
