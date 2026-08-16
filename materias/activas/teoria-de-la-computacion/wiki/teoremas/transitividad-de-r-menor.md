---
id: teoria-de-la-computacion/teoremas/transitividad-de-r-menor
tipo: teorema
tema: U6
fuentes: [revision-conjuntos p.6]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# `R<` es transitiva

El resultado es de los que se dan por obvios —que menor es transitiva no sorprende a nadie— y
sin embargo es la página más importante de esta parte del wiki, porque lo que hay que aprender
no es el enunciado sino la técnica con que se prueba.

## Enunciado

El apunte lo plantea como pregunta y responde con otra: "`R<` es transitiva ? Sí, demostración
?" Escrito de forma explícita, es la definición de transitividad instanciada sobre `R<`:

```
(∀x, y, z ∈ ℕ)((x, y) ∈ R< ∧ (y, z) ∈ R< ⇒ (x, z) ∈ R<)
```

## Hipótesis

Lo único que se supone es cómo está definida `R<`, y ahí está toda la sustancia: de las tres
definiciones posibles de [[definiciones/relacion]], acá se usa la inductiva.

- `R< ⊆ ℕ × ℕ` definida **por inducción** con las reglas :

```
(r1) n ∈ ℕ ⇒ (n, S n) ∈ R<
(r2) (n, m) ∈ R< ⇒ (n, S m) ∈ R<
```

La definición inductiva no es un detalle: es lo que habilita la demostración. Con la
definición por comprensión habría que razonar sobre la existencia de `z`, y sería otra prueba.

## Demostración

El desarrollo completo está en [[demostraciones/transitividad-de-r-menor]]. La técnica es
inducción sobre el árbol de prueba de `(y, z) ∈ R<` — no sobre `y` ni sobre `z` como números,
que es donde se cae todo el mundo.

## Cuándo se aplica

El resultado en sí es trivial; lo que se aplica es **la técnica**. Es la primera inducción
estructural **sobre un árbol de derivación** del curso —no sobre un número—, y es la misma que
reaparece en semántica operacional (U9) y en las demostraciones de equivalencia de modelos
(U4). Cuando en el parcial pidan probar una propiedad de una relación definida por reglas de
inferencia, este es el molde.

Además habilita clasificar `R<` como orden parcial estricto, que necesita transitividad:
ver [[definiciones/ordenes]].

## Errores típicos

- **Inducir sobre `x` o sobre el número, en vez de sobre la derivación.** La prueba no
 induce sobre naturales: induce sobre el árbol que justifica `(y, z) ∈ R<`. Confundir las dos
 cosas hace que el caso inductivo no cierre.
- **Elegir la relación equivocada para inducir.** El apunte induce en la **segunda**,
 `(y, z) ∈ R<`, dejando `(x, y)` fija. Si inducís sobre la primera, la hipótesis inductiva no
 te sirve.
- **Dar por hecha la transitividad al usar `R≤`.** Es la que se está probando; usarla dentro
 de su propia demostración es circular.

## Relacionado

- [[definiciones/propiedades-de-relaciones]] — la definición de transitiva que se instancia
- [[definiciones/relacion]] — `R<` y sus tres definiciones
- [[comparativas/formas-de-definir-conjuntos]] — por qué la definición inductiva es la útil acá
- [[fuentes/revision-conjuntos]]

## Procedencia

- **Enunciado** — revision-conjuntos p.6 · incluye comentario del sistema
- **Hipótesis** — revision-conjuntos p.5 · incluye comentario del sistema
- **Cuándo se aplica** — sin cita: comentario del sistema
- **Errores típicos** — sin cita: comentario del sistema
