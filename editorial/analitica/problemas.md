# Problemas abiertos · undraftedzone.com

Lo mantiene el agente de Analítica cada día (ver `CONTEXTO.md`, sección 3). Última actualización: 18/11/2026.

| Problema | Detectado | Último visto | Días abierto | Estado | Nota |
|---|---|---|---|---|---|
| 410 en la portada «/» (también a Googlebot) | 15/11 | 17/11 | 3 | abierto | 49 (15/11), 62 (16/11), 33 a Googlebot (17/11). La auditoría del 18/11 vio 200 en 5 de 5 peticiones: confirmar en el informe del 19/11 |
| Caché casi apagada | 14/11 | 17/11 | 4 | abierto | 11 % → 9,8 % → 2,4 % → 2,1 % |
| xmlrpc.php accesible | 14/11 | 17/11 | 4 | abierto | 21 peticiones el 17/11. El 18/11 ya respondía 403 |
| 404 imagen Celtics | 17/11 | 17/11 | 1 | abierto | Causa probable: la raya «–» del nombre de archivo |
| Falta favicon.ico | 15/11 | 17/11 | 3 | abierto | El 18/11 ya respondía 200 |

## Recurrentes

- 403 en un artículo legítimo sobre el draft.
- 429 en las fuentes y el logo de la propia web.
- 503, 429 y 504 entre `/wp-json` y el Worker de respaldo.
- Los PNG se llevan buena parte del ancho de banda.
- Escáneres que buscan `.env` y similares (16/11, uno desde Francia).
