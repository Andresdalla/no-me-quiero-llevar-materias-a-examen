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

⚠️ ✅ [notas-conjuntos p.9] La sección está titulada "**(Extra pero muy recomendado)**
Cardinalidad infinita y la hipótesis del continuo". Es material marcado como extra por la
cátedra: no des por hecho que entra al parcial.

## Enunciado

✅ [notas-conjuntos p.9] "El menor cardinal infinito se denota por `ℵ₀` (alef cero) y
corresponde al tamaño del conjunto de los números naturales."

✅ [notas-conjuntos p.9] "Un conjunto tiene cardinal `ℵ₀` si y sólo si es numerable. En
particular, `|N| = |Z| = |Q| = ℵ₀`."

✅ [notas-conjuntos p.9] "El símbolo `ℵ₁` se utiliza para denotar el menor cardinal
estrictamente mayor que `ℵ₀`."

✅ [notas-conjuntos p.9] "El argumento de diagonalización muestra que `|P(N)| > |N|`." Y
"`|P(N)| = |R|`, por lo que el conjunto de los números reales tiene una cardinalidad
estrictamente mayor que la de los naturales. Este cardinal se denomina **el cardinal del
continuo**."

**Hipótesis del continuo.** ✅ [notas-conjuntos p.10] "afirma que no existen cardinales
intermedios entre `ℵ₀` y `|R|`, es decir, `|R| = ℵ₁`. Equivalentemente, todo subconjunto
infinito de `R` es o bien numerable o bien tiene la misma cardinalidad que `R`."

✅ [notas-conjuntos p.10] "la hipótesis del continuo **no puede demostrarse ni refutarse** a
partir de los axiomas usuales de la teoría de conjuntos (axiomas de Zermelo-Fraenkel con el
axioma de elección)": "existen modelos de la teoría donde la hipótesis del continuo es
verdadera; existen modelos donde es falsa."

## Notación

| Símbolo | Significa |
|---|---|
| `ℵ₀` | menor cardinal infinito; el de `N` |
| `ℵ₁` | menor cardinal estrictamente mayor que `ℵ₀` |
| `\|P(N)\|` = `\|R\|` | el cardinal del continuo |

⚠️ `ℵ₁` y "el cardinal del continuo" **no son lo mismo por definición**. Que coincidan es
exactamente lo que afirma la hipótesis del continuo, y es indecidible. Escribir `|R| = ℵ₁` como
si fuera un hecho es el error que esta sección existe para evitar.

## Ejemplo

✅ [notas-conjuntos p.9] Numerables: "`N`, `Z` o `Q`" — todos con cardinal `ℵ₀`.

## Contraejemplo

✅ [notas-conjuntos p.9] No numerables: "`R`, o `N ⟶ N`".

🧠 `N ⟶ N` (el conjunto de funciones de `N` en `N`) es el que aparece en
[[demostraciones/diagonalizacion]]: no es numerable, y esa es toda la fuerza del argumento.

## Confusiones frecuentes

- **`ℵ₁` vs continuo.** Ver arriba: es la confusión central de la sección.
- **"Más grande" para infinitos no es contención.** `Q ⊋ N` y sin embargo `|Q| = |N| = ℵ₀`. Ver
  [[definiciones/comparacion-de-cardinalidades]].
- 🧠 **Nada de esto hace falta para el resultado de computabilidad.** ✅ [notas-conjuntos p.10]
  "basta con observar que `ℵ₀ < |P(N)|`". Si en el parcial invocás la hipótesis del continuo
  para probar que existen funciones no computables, estás usando un martillo que además es
  indecidible. Ver [[teoremas/existen-funciones-no-computables]].

## Relacionado

- [[demostraciones/diagonalizacion]] — de dónde sale `|P(N)| > |N|`
- [[definiciones/numerable-y-contable]] — cardinal `ℵ₀` ⟺ numerable
- [[definiciones/comparacion-de-cardinalidades]]
- [[fuentes/notas-conjuntos]]
