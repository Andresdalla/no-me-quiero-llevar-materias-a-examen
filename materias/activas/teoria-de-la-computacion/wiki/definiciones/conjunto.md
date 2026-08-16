---
id: teoria-de-la-computacion/definiciones/conjunto
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.1, revision-conjuntos p.2]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de conjunto, pertenencia e inclusión

## Enunciado

"Un conjunto es una colección de elementos"

"Pertenencia: x es un elemento del conjunto A" — `x ∈ A`

"Conjunto vacío" — `∅ = {}`

**Axioma de extensión.** "Dos conjuntos son iguales si y sólo si
tienen los mismos elementos"

**Inclusión amplia.** `A ⊆ B ⇔ (∀x ∈ A)(x ∈ B)`

Propiedades:

```
A = B ⇔ A ⊆ B ∧ B ⊆ A
A ⊆ A
∅ ⊆ A
```

## Notación

| Símbolo | Significa |
|---|---|
| `x ∈ A` | `x` pertenece a `A` |
| `∅` | conjunto vacío, igual a `{}` |
| `A ⊆ B` | inclusión amplia (permite `A = B`) |

La cátedra usa **`⊆` para la inclusión amplia** y no introduce un símbolo separado para la
inclusión estricta en este apunte.

## Ejemplo

`1 ∈ {1, 2, 3}`

Por el axioma de extensión, ni el orden ni la repetición importan:

```
{1, 2, 2} = {2, 1}
{{1, 2, 2}, 2} = {2, {2, 1}}
```

`{1} ⊆ {2, 1}`

## Contraejemplo

`{{1, 2}} ≠ {1, 2}`

Por qué: el de la izquierda tiene **un** elemento (que es un conjunto); el de la derecha
tiene **dos** (que son números). El axioma de extensión los separa porque no comparten
elementos.

El apunte deja abierta la pregunta `{{1, 2}} ⊆ {1, 2}?`

La respuesta es **no**: para que valiera, el único elemento de la izquierda —el conjunto
`{1,2}`— tendría que pertenecer a `{1,2}`, y los elementos de `{1,2}` son `1` y `2`, no
`{1,2}`.

## Confusiones frecuentes

- **`∈` vs `⊆`.** `∈` relaciona un elemento con un conjunto; `⊆` relaciona dos conjuntos.
 `1 ∈ {1,2}` pero `1 ⊆ {1,2}` no tiene sentido; `{1} ⊆ {1,2}` sí.
- Esta confusión es la que hace fallar las preguntas sobre
 [[definiciones/operaciones-con-conjuntos]] en el conjunto potencia: `∅ ∈ P(A)` **y**
 `∅ ⊆ P(A)` son las dos verdaderas, por motivos distintos.
- **Anidamiento.** `{{1,2}}` no es `{1,2}`. Contar niveles de llaves antes de responder.

## Relacionado

- [[comparativas/formas-de-definir-conjuntos]] — las tres maneras de dar un conjunto
- [[definiciones/operaciones-con-conjuntos]] — unión, intersección, potencia, producto
- [[fuentes/revision-conjuntos]]

## Procedencia

- **Enunciado** — revision-conjuntos p.1, p.2
- **Notación** — sin cita: comentario del sistema
- **Ejemplo** — revision-conjuntos p.1, p.2
- **Contraejemplo** — revision-conjuntos p.1, p.2 · incluye comentario del sistema
- **Confusiones frecuentes** — sin cita: comentario del sistema
