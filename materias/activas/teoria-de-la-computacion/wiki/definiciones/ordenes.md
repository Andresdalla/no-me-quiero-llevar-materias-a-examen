---
id: teoria-de-la-computacion/definiciones/ordenes
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.7, revision-conjuntos p.8]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de órdenes parciales y totales, laxos y estrictos

## Enunciado

**Órdenes laxos.** "Una relacion es un **orden parcial laxo** si
es: reflexiva · antisimétrica · transitiva."

"Es un **orden total laxo** si además cumple:
`(∀x, y ∈ A)((x, y) ∈ R ∨ (y, x) ∈ R)`"

**Órdenes estrictos.** "Una relacion es un **orden parcial
estricto** si es: asimétrica · transitiva."

"Es un **orden total estricto laxo** si además cumple:
`(∀x, y ∈ A)((x, y) ∈ R ∨ (y, x) ∈ R)`"

"orden total estricto **laxo**" está transcripto literal y se contradice a sí mismo: o es
estricto o es laxo. Es un error de tipeo de la fuente. Anotado en `wiki/dudas.md`.

## Notación

| Combinación | Propiedades exigidas |
|---|---|
| orden parcial laxo | reflexiva + antisimétrica + transitiva |
| orden total laxo | las tres anteriores + totalidad |
| orden parcial estricto | asimétrica + transitiva |
| orden total estricto | las dos anteriores + totalidad |

La diferencia laxo/estricto es **una sola**: el laxo pide reflexiva + antisimétrica, el
estricto pide asimétrica. Todo lo demás se repite.

## Ejemplo

"`R≤ = R< ∪ {(x, x) : x ∈ A}` es un orden total"

Fijate en la construcción: al unirle la diagonal a `R<` la volvés reflexiva sin romper la
transitividad. Es la receta estándar para pasar de estricto a laxo.

## Contraejemplo

"`R<` no es un orden total porque no es reflexiva."

"`R<` no es un orden total estricto."

Acá hay un problema real de la fuente: la condición de totalidad que da el apunte,
`(∀x, y ∈ A)((x, y) ∈ R ∨ (y, x) ∈ R)`, **evaluada en `x = y`** exige `(x, x) ∈ R`. Es decir,
exige reflexividad. Con esa definición **ningún orden estricto puede ser total jamás**, y la
categoría "orden total estricto" queda vacía. La versión habitual usa tricotomía
(`x < y ∨ y < x ∨ x = y`). Preguntalo: no lo resuelvo por mi cuenta. Anotado en
`wiki/dudas.md`.

## Confusiones frecuentes

- **Total no es "cualquier par está relacionado en algún sentido" a secas**: hay que chequear
 también `x = y`, que es justo donde se rompe para los órdenes estrictos.
- **`R<` es un orden parcial estricto** (asimétrica + transitiva) aunque no sea total. Parcial
 no significa "incompleto por error", significa que no se exige comparar todo par.
- La diferencia asimétrica/antisimétrica está en
 [[definiciones/propiedades-de-relaciones]] y es la que separa las dos familias.

## Relacionado

- [[definiciones/propiedades-de-relaciones]] — las cinco propiedades que se combinan acá
- [[definiciones/relacion]] · [[definiciones/operaciones-con-relaciones]]
- [[fuentes/revision-conjuntos]]

## Procedencia

- **Enunciado** — revision-conjuntos p.7, p.8 · duda registrada en `dudas.md`
- **Notación** — sin cita: comentario del sistema
- **Ejemplo** — revision-conjuntos p.8 · incluye comentario del sistema
- **Contraejemplo** — revision-conjuntos p.8 · duda registrada en `dudas.md`
