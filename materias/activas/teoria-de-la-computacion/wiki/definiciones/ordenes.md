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

Los órdenes no son propiedades nuevas: son **combinaciones con nombre** de las cinco de
[[definiciones/propiedades-de-relaciones]]. Hay dos ejes independientes —laxo contra estricto,
parcial contra total— y de cruzarlos salen las cuatro categorías. Esta página también contiene
una contradicción real de la fuente que conviene tener presente antes del parcial.

## Enunciado

Los **órdenes laxos** son los que admiten que un elemento se relacione consigo mismo: "Una
relacion es un **orden parcial laxo** si es: reflexiva · antisimétrica · transitiva." Se vuelve
total cuando además no queda ningún par sin comparar — "Es un **orden total laxo** si además
cumple: `(∀x, y ∈ A)((x, y) ∈ R ∨ (y, x) ∈ R)`".

Los **órdenes estrictos** cambian las dos primeras propiedades por una sola: "Una relacion es
un **orden parcial estricto** si es: asimétrica · transitiva." La asimetría prohíbe de entrada
que un elemento se relacione consigo mismo, así que reflexividad y antisimetría dejan de tener
sentido acá. La condición de totalidad que agrega el apunte es literalmente la misma: "Es un
**orden total estricto laxo** si además cumple:
`(∀x, y ∈ A)((x, y) ∈ R ∨ (y, x) ∈ R)`".

Que sea la misma condición es el problema, y se desarrolla en el contraejemplo. Antes de eso,
un detalle menor: "orden total estricto **laxo**" está transcripto literal y se contradice a
sí mismo, porque o es estricto o es laxo. Es un error de tipeo de la fuente. Anotado en
`wiki/dudas.md`.

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

El apunte da un solo ejemplo positivo y es constructivo: "`R≤ = R< ∪ {(x, x) : x ∈ A}` es un
orden total". Fijate en la construcción más que en el resultado: al unirle la diagonal a `R<`
la volvés reflexiva sin romper la transitividad, y el precio es perder la asimetría. Es la
receta estándar para pasar de estricto a laxo, y funciona para cualquier orden estricto, no
solo para `R<`.

## Contraejemplo

Del lado negativo el apunte afirma dos cosas sobre la misma relación: "`R<` no es un orden
total porque no es reflexiva." y "`R<` no es un orden total estricto." La primera es esperable
—`R<` es estricta, no laxa—, pero la segunda es la que abre el problema.

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
