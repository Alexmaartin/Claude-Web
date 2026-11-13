# Agentes de UndraftedZone

Cada agente tiene una sesión fija, y el trabajo rutinario se pide escribiendo en esa sesión, sin abrir sesiones nuevas en el entorno Radar. Escríbele directamente para hablar con él. No se crean sesiones nuevas para su trabajo habitual.

| Agente | Sesión | Qué hace | Instrucciones |
|---|---|---|---|
| Radar | `session_01TFZkNFvbzXxyeGsDGD1aTd` | Detecta noticias en las fuentes permitidas | `editorial/radar/PROMPT.md` |
| Redacción | `session_01TFZkNGRXnT659fv9DSdz95` | Escribe los borradores de la guía o de la noticia del día | `editorial/redaccion/PROMPT.md` |
| Verificador | `session_01TFZkNER2DME5VBXnEYTMiF` | Contrasta y corrige los borradores pendientes, sin aprobar ni publicar | `editorial/verificador/PROMPT.md` |
| Métricas | `session_01TFZkNFALx5r5zgtaUH3Hbr` | Actualiza las métricas web del panel cada día a las 06:13 (Madrid), rutina `trig_019HenoJ2nggVmG1LBH7mD1F` | `editorial/radar/PROMPT.md`, sección «Métricas web» |
| Publicador | `session_01TFZkNEWHUaXbVQ3HittCWD` | Sube a WordPress los borradores aprobados, siempre como borrador, y concilia el estado con el panel | `editorial/wordpress/PROMPT.md` |
| Auditor SEO | `session_01TFZkNFPrZMqC4wzx7KDy7W` | Revisa el SEO de la web y deja incidencias priorizadas | `editorial/seo/PROMPT.md` |
| Aprendizaje | `session_01TFZkNHYQJtyo4n4uf4Eptq` | Aprende de lo que se aprueba y se corrige, sin cambiar reglas duras | `editorial/APRENDIZAJE.md` |
| JalandBot (orquestador) | `session_01TFZkNHTz9Lscwonw8q2JdY` | Recibe las tareas de Alejandro, las reparte entre los agentes y supervisa el resultado. No aprueba ni publica | `editorial/ORQUESTADOR.md` |
| Diseño y UX | `session_01TFZkNF8c2DbEsAqKVnbCA8` | Busca mejoras de diseño, uso y funcionalidad del panel y del sistema; propone, no cambia | `editorial/ux/PROMPT.md` |

Reglas comunes: ningún agente publica en WordPress por su cuenta ni aprueba borradores. Solo el Publicador escribe en WordPress, y siempre como borrador salvo el clic de publicación que das tú en el panel. Solo Alejandro aprueba y publica, desde el panel. Ninguna credencial va al chat.
