---
id: teoria-de-la-computacion/definiciones/cardinales-infinitos
tipo: definicion
tema: U6
fuentes: [notas-conjuntos p.9, notas-conjuntos p.10]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de los cardinales infinitos `ℵ₀` y `ℵ₁`

La sección está titulada "**(Extra pero muy recomendado)**
Cardinalidad infinita y la hipótesis del continuo". Es material marcado como extra por la
cátedra: no des por hecho que entra al parcial.

## Enunciado

Hasta acá "numerable" y "no numerable" alcanzaban para todo. Los cardinales le ponen nombre a
los tamaños y permiten preguntarse si hay algo **entre** los dos, que es donde la cosa se
vuelve interesante.

El piso de los infinitos es el de los naturales: "El menor cardinal infinito se denota por
`ℵ₀` (alef cero) y corresponde al tamaño del conjunto de los números naturales." Y es
exactamente la noción que ya venías usando con otro nombre, porque "Un conjunto tiene cardinal
`ℵ₀` si y sólo si es numerable. En particular, `|N| = |Z| = |Q| = ℵ₀`."

El siguiente escalón se define por su posición, no por un conjunto concreto: "El símbolo `ℵ₁`
se utiliza para denotar el menor cardinal estrictamente mayor que `ℵ₀`." Retené que hasta acá
`ℵ₁` es una definición vacía de contenido: sabemos dónde está, no qué es.

Por otro lado sí hay un tamaño mayor conocido y con nombre: "El argumento de diagonalización
muestra que `|P(N)| > |N|`." A eso se le suma que "`|P(N)| = |R|`, por lo que el conjunto de
los números reales tiene una cardinalidad estrictamente mayor que la de los naturales. Este
cardinal se denomina **el cardinal del continuo**."

Tenemos entonces dos cosas definidas por caminos distintos —el escalón siguiente y el tamaño
de los reales— y la pregunta obvia es si coinciden. Eso es lo que dice la **hipótesis del
continuo**, que "afirma que no existen cardinales intermedios entre `ℵ₀` y `|R|`, es decir,
`|R| = ℵ₁`. Equivalentemente, todo subconjunto infinito de `R` es o bien numerable o bien tiene
la misma cardinalidad que `R`."

Y la respuesta es que no hay respuesta: "la hipótesis del continuo **no puede demostrarse ni
refutarse** a partir de los axiomas usuales de la teoría de conjuntos (axiomas de
Zermelo-Fraenkel con el axioma de elección)", porque "existen modelos de la teoría donde la
hipótesis del continuo es verdadera; existen modelos donde es falsa." No es que no se sepa
todavía: se demostró que los axiomas no alcanzan para decidirlo.

## Notación

| Símbolo | Significa |
|---|---|
| `ℵ₀` | menor cardinal infinito; el de `N` |
| `ℵ₁` | menor cardinal estrictamente mayor que `ℵ₀` |
| `\|P(N)\|` = `\|R\|` | el cardinal del continuo |

`ℵ₁` y "el cardinal del continuo" **no son lo mismo por definición**. Que coincidan es
exactamente lo que afirma la hipótesis del continuo, y es indecidible. Escribir `|R| = ℵ₁` como
si fuera un hecho es el error que esta sección existe para evitar.

## Ejemplo

Los tres ejemplos de conjuntos numerables que da la fuente son "`N`, `Z` o `Q`", todos con
cardinal `ℵ₀`. Que `Q` esté en la lista es lo llamativo: los racionales parecen muchos más que
los naturales y sin embargo tienen el mismo cardinal.

## Contraejemplo

Del otro lado quedan los no numerables: "`R`, o `N ⟶ N`". Son los que no se pueden poner en
biyección con `N` por más que se intente, y en los dos casos la prueba es la misma técnica.

`N ⟶ N` (el conjunto de funciones de `N` en `N`) es el que aparece en
[[demostraciones/diagonalizacion]]: no es numerable, y esa es toda la fuerza del argumento —
como los programas sí son numerables, tiene que haber funciones que ningún programa calcula.

## Confusiones frecuentes

- **`ℵ₁` vs continuo.** Ver arriba: es la confusión central de la sección.
- **"Más grande" para infinitos no es contención.** `Q ⊋ N` y sin embargo `|Q| = |N| = ℵ₀`. Ver
 [[definiciones/comparacion-de-cardinalidades]].
- **Nada de esto hace falta para el resultado de computabilidad.**
 "basta con observar que `ℵ₀ < |P(N)|`". Si en el parcial invocás la hipótesis del continuo
 para probar que existen funciones no computables, estás usando un martillo que además es
 indecidible. Ver [[teoremas/existen-funciones-no-computables]].

## Relacionado

- [[demostraciones/diagonalizacion]] — de dónde sale `|P(N)| > |N|`
- [[definiciones/numerable-y-contable]] — cardinal `ℵ₀` ⟺ numerable
- [[definiciones/comparacion-de-cardinalidades]]
- [[fuentes/notas-conjuntos]]

## Procedencia

- **Enunciado** — notas-conjuntos p.9, p.10
- **Notación** — sin cita: comentario del sistema
- **Ejemplo** — notas-conjuntos p.9
- **Contraejemplo** — notas-conjuntos p.9 · incluye comentario del sistema
- **Confusiones frecuentes** — notas-conjuntos p.10 · incluye comentario del sistema
