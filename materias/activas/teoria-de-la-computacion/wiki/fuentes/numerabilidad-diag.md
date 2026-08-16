---
id: teoria-de-la-computacion/fuentes/numerabilidad-diag
tipo: fuente
tema: U6
fuentes: [numerabilidad-diag p.1-10]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Ficha · Numerabilidad y diagonalización (repartido)

## Qué es

"Numerabilidad y diagonalización", **E. Copello · Á. Tasistro**,
**Marzo de 2022**. 10 páginas, 3 secciones, 20 ejercicios numerados `?1`-`?20`.

Es un **repartido teórico con ejercicios intercalados**, no láminas ni notas de clase.
Declara su objetivo desde la primera página y lo cumple: "El propósito final del
presente estudio es demostrar que el concepto matemático clásico de función es mucho más
general que el de algoritmo."

## Qué cubre

| Sec. | Contenido | Páginas del wiki |
|---|---|---|
| — | Función vs algoritmo: la decisión de vocabulario | [[comparativas/funcion-vs-algoritmo]] |
| 1 | Producto cartesiano, relaciones, funciones | [[definiciones/funcion]] (actualizada) · [[definiciones/relacion]] |
| 2 | Tamaños: `⪯`, equipolencia, ejercicios `?5`-`?12` | [[definiciones/comparacion-de-cardinalidades]] (actualizada) |
| 3.1 | Conjuntos infinitos y finitos, Teorema 3.1 | [[definiciones/conjunto-infinito]] · [[teoremas/propiedades-de-conjuntos-infinitos]] |
| 3.2 | Contables y numerables, `N × N`, `Σ*` | [[definiciones/numerable-y-contable]] · [[construcciones/emparejamiento-de-cantor]] · [[teoremas/palabras-finitas-son-numerables]] |
| 3.3 | No numerables: `P(N)` por diagonalización | [[teoremas/p-de-n-no-es-numerable]] · [[demostraciones/diagonalizacion]] |
| final | El argumento vía `S : algoritmos → funciones` | [[comparativas/funcion-vs-algoritmo]] |

## Cuán confiable es

**Alta**, y es la fuente más cuidadosa de las tres en las distinciones finas: separa
entrada/dominio, parcial/total, contable/numerable, y concluye `Prog ⪯ N` en vez de saltar a
"numerable".

**Pero diverge de `notas-conjuntos` en tres puntos concretos**, todos verificados y anotados en
`wiki/dudas.md`:

| Punto | `numerabilidad-diag` | `notas-conjuntos` |
|---|---|---|
| Definición de `∼` | `A ⪯ B` y `B ⪯ A` | existe biyección total |
| Emparejamiento de Cantor | `f(i,j) = (Σ[k=0..i+j] k) + i` | `π(i,j) = (i+j)(i+j+1)/2 + j` |
| "función" a secas | significa **parcial** | sin convención explícita |

La segunda divergencia da **funciones distintas**: `f(1,0) = 2` acá y `π(1,0) = 1` allá.
Ver [[construcciones/emparejamiento-de-cantor]].

El ejercicio `?14` usa la palabra "**enumerable**", que no aparece definida en
ningún lado. Casi seguro es "numerable".

## Deja 20 ejercicios sin resolver

`?1` a `?20`, ninguno con solución. Toda resolución en este wiki es inferida.

Dos de ellos valen la pena aparte: `?7` ("condición necesaria y suficiente para `A ⪯ B` es
que exista una función sobreyectiva de `B` en `A`") es **la consigna de examen de febrero
2026**, y `?19.3` (`N → Nₖ` no numerable) es el **Ejercicio 14 de `notas-conjuntos`**. Lo que
aparece en dos fuentes se pregunta.

## Nota de procesamiento

Se rasterizaron las páginas **8 y 9**: la fórmula con sumatoria y las dos tablas (la
numeración por diagonales y la tabla booleana `T`) son ilegibles en el texto plano. La
divergencia con `notas-conjuntos` en el emparejamiento de Cantor se confirmó contra esas
imágenes antes de afirmarla.

## Relacionado

- [[fuentes/notas-conjuntos]] — cubre el mismo tema; leelas juntas y atento a las divergencias
- [[fuentes/revision-conjuntos]] · [[fuentes/tc-temario]]

## Procedencia

- **Qué es** — numerabilidad-diag p.1 · incluye comentario del sistema
- **Cuán confiable es** — p.7 · duda: La segunda divergencia da funciones distintas
- **Deja 20 ejercicios sin resolver** — sin cita: comentario del sistema
- **Nota de procesamiento** — sin cita: comentario del sistema
