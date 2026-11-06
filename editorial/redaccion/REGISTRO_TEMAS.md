# Registro de temas: no repetir y no dos días seguidos

Este archivo define cómo el sistema evita repetir temas y evita dos artículos seguidos sobre la misma franquicia o jugador. Mandan sobre la rotación cuando chocan.

## Qué es el registro

La colección `temas_usados` del panel guarda una entrada por cada artículo que existe en WordPress, lo haya escrito el sistema o tú. Cada entrada tiene:
- `id`: el id de WordPress.
- `titulo`, `slug`, `url`, `fecha` (la de publicación o la de borrador).
- `franquicia`: la de la rotación de `ROTACION.md`, o `ninguna` si es evergreen de temática general.
- `jugadores`: lista de jugadores principales del artículo, en minúsculas y con apellido.
- `tema_clave`: el suceso o tema en pocas palabras (por ejemplo, «lesión de Morant en el isquiotibial»).
- `tipo`: `actualidad`, `guia`, `analisis`, `reportaje` o `evergreen`.

## Cómo se mantiene

1. **Cada día, antes de seleccionar**, la pasada lee las entradas de WordPress de los últimos 365 días (publicadas y borradores, con la API) y actualiza el registro. Así cuenta también lo que subes tú a mano.
2. **Cada vez que el publicador sube un borrador**, añade su entrada al registro.
3. Un tema se considera **ya usado** si coincide con un `tema_clave` existente, o si comparte slug raíz o jugador principal con un artículo de los últimos 30 días y el mismo tipo.

## Reglas de selección

- **No repetir tema.** Un tema ya usado no vuelve a salir. Si una actualización es realmente nueva (por ejemplo, la baja termina y hay un regreso), se escribe como artículo nuevo que enlaza al anterior.
- **No dos días seguidos con la misma franquicia.** Si ayer salió algo de una franquicia, hoy no sale nada de esa franquicia, aunque sea un evergreen o una noticia bomba. Se pasa a la siguiente franquicia del turno y la que tocaba se queda para el día siguiente.
- **No dos días seguidos con el mismo jugador.** Si ayer era sobre un jugador, hoy no se escribe de él, aunque sea de otra franquicia.
- **La noticia bomba tiene que cumplir las dos reglas.** Si una noticia bomba choca con ayer, no se redacta ese día: se deja la alerta `tecnica` y se propone la siguiente.
- **El evergreen no tiene franquicia**, así que solo cuenta para el tema y para los jugadores que cite.

## Qué hace el sistema si hay conflicto

- Antes de redactar, se revisa la regla. Si el artículo elegido infringe una regla, no se redacta: se elige el siguiente candidato válido y se anota en la alerta del día por qué se descartó el anterior.
- Antes de subir a WordPress, el publicador vuelve a comprobar las dos reglas contra el registro. Si una falla, no sube nada y deja una alerta `tecnica`.
