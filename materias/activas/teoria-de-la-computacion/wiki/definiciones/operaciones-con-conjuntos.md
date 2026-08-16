---
id: teoria-de-la-computacion/definiciones/operaciones-con-conjuntos
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.3, revision-conjuntos p.4]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de las operaciones con conjuntos

## Enunciado

**Tamaño o cardinalidad.** "Número de elementos de un conjunto" —
`|{1, 4}| = 2`

**Unión.** `A ∪ B = {x : x ∈ A ∨ x ∈ B}`

**Intersección.** `A ∩ B = {x : x ∈ A ∧ xB}`

**Eso está mal en el apunte.** La transcripción es literal —verificada contra la página
rasterizada, no es pérdida de extracción— pero le falta el `∈`. Debe leerse
`A ∩ B = {x : x ∈ A ∧ x ∈ B}`. Anotado en `wiki/dudas.md`.

**Potencia o partes.** `P(A) = 2^A = {B : B ⊆ A}`

**Par o tupla ordenada.** "Elemento formado por una pareja de
elementos" — `(1, 2)`. "Importa el orden y la aridad".

**Producto cartesiano.** `A × B = {(x, y) : x ∈ A ∧ y ∈ B}`

## Notación

| Símbolo | Operación |
|---|---|
| `\|A\|` | cardinalidad |
| `A ∪ B` · `A ∩ B` | unión · intersección |
| `P(A)` o `2^A` | conjunto potencia (dos notaciones para lo mismo) |
| `(x, y)` | par ordenado — paréntesis, no llaves |
| `A × B` | producto cartesiano |

## Ejemplo

```
{1, 2} ∪ {3, 1} = {1, 2, 3}
{1, 2} ∩ {3, 1} = {1}
P({1, 2}) = {∅, {1}, {2}, {1, 2}}
```

`{1, 2} × {#, !} = {(1, #), (1, !), (2, #), (2, !)}`

Propiedades del conjunto potencia: `∅ ⊆ P(A)`, `∅ ∈ P(A)`,
`A ∈ P(A)`.

El apunte deja dos preguntas abiertas: `|P(A)| = ?` "Asumiendo A
finito, y por ende |A| definido", y `A ⊆ P(A)?`

Respuestas: `|P(A)| = 2^|A|` —de ahí viene la notación `2^A`—. Y `A ⊆ P(A)` es **falso** en
general: exigiría que cada elemento de `A` fuera además un subconjunto de `A`.

## Contraejemplo

El par ordenado no es un conjunto:

```
(1, 2) ≠ (2, 1)
(1, 2) ≠ (1, 2, 2)
```

Contrastá con [[definiciones/conjunto]]: ahí `{1, 2, 2} = {2, 1}`. En los pares **el orden y
la repetición sí importan**; en los conjuntos no. Es la diferencia que hace que el producto
cartesiano tenga sentido.

## Confusiones frecuentes

- **`∅ ∈ P(A)` vs `∅ ⊆ P(A)`.** Las dos son verdaderas y el apunte las lista juntas a
 propósito. La primera porque `∅ ⊆ A`; la segunda porque el vacío está incluido en cualquier
 conjunto. Ver [[definiciones/conjunto]].
- **`P(A)` crece exponencial, no lineal.** `|A| = 3` da `|P(A)| = 8`. Es el germen del
 argumento de cardinalidad de U6.
- **`(x, y)` vs `{x, y}`.** Paréntesis = ordenado; llaves = conjunto.

## Relacionado

- [[definiciones/conjunto]] — pertenencia, inclusión, axioma de extensión
- [[definiciones/relacion]] — una relación es un subconjunto de un producto cartesiano
- [[fuentes/revision-conjuntos]]

## Procedencia

- **Enunciado** — revision-conjuntos p.3, p.4 · duda registrada en `dudas.md`
- **Ejemplo** — revision-conjuntos p.3, p.4 · incluye comentario del sistema
- **Contraejemplo** — revision-conjuntos p.4 · incluye comentario del sistema
- **Confusiones frecuentes** — sin cita: comentario del sistema
