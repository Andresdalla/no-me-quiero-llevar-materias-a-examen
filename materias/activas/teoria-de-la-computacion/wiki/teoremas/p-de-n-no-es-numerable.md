---
id: teoria-de-la-computacion/teoremas/p-de-n-no-es-numerable
tipo: teorema
tema: U6
fuentes: [numerabilidad-diag p.8, numerabilidad-diag p.9]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# `P(N)` no es numerable

## Enunciado

"Vamos a demostrar que el conjunto partes o potencia de `N`
(`P(N)` o `2^N`) no es numerable."

Corolario que el apunte deja anotado: "Observar que, como se puede
ver en la tabla anterior, `P(N) ∼ N → Bool`."

## Hipótesis

- `P(N) = {A : A ⊆ N}`
- Ninguna otra: es un resultado cerrado.

## Demostración

Por diagonalización, ver [[demostraciones/diagonalizacion]]. En resumen:

"Esta técnica se basa en suponer por absurdo `P(N)` es numerable,
entonces existe una biyección `f : N ↔ P(N)`. Luego usamos esta biyección para fabricar una
tabla booleana, llamada `T`, donde en la columna `j` representamos el conjunto de naturales
`f(j)`, colocando en la fila `i` el booleano `True` si `i ∈ f(j)` y `False` si `i ∉ f(j)`."

"A partir de esta tabla construimos un conjunto de naturales que
difiere de cada conjunto `f(j)` en la diagonal (posición `(j, j)` de la tabla):"

```
D = {j : not(T(j, j))}
```

"Con lo cual construimos un conjunto `D` de naturales tal que
`∀j, D ≠ f(j)` ya que por definición de `D` se cumple que `j ∈ D ⇔ j ∉ f(j)`. Concluyendo así
que `f` no es sobreyectiva, por tanto tampoco biyectiva, pero esto es absurdo ya que supusimos
`f` era biyectiva."

## Cuándo se aplica

Es la **versión conjuntista** del argumento de
[[teoremas/existen-funciones-no-computables]], que en `notas-conjuntos` se hace sobre
funciones `N → N`. Las dos fuentes de la materia prueban lo mismo por caminos distintos:

| | `numerabilidad-diag` | `notas-conjuntos` |
|---|---|---|
| Diagonaliza sobre | subconjuntos de `N` (`P(N)`) | funciones `N → N` |
| Objeto construido | el conjunto `D = {j : not(T(j,j))}` | la función `g(n) = fₙ(n) + 1` |
| Difiere de cada uno en | la pertenencia de `j` | el valor en `n` |

Saber las dos paga: la múltiple opción de mayo 2025 pregunta por `N → Bool`, que es
exactamente `P(N)` vía este corolario. Ver [[examenes/mayo-2025-multiple-opcion]].

Los corolarios que el apunte deja como ejercicio `?19`: "Demostrar
que `N ↬ N` no es numerable" · "Demostrar que `N → N` no es numerable" · "Sea `Nₖ` el conjunto
de los primeros `k` naturales. ¿Para qué valores de `k` es `N → Nₖ` no numerable? Demostrar" ·
"Concluir que el intervalo `(0, 1)` de reales no es numerable" · "Concluir que el conjunto `R`
de los números reales no es numerable".

Ese tercer ítem es **el mismo ejercicio** que el Ejercicio 14 de `notas-conjuntos`. Aparece
en las dos fuentes: señal fuerte de que se pregunta.

## Errores típicos

- **Confundir filas con columnas.** Acá las **columnas** son los conjuntos `f(j)` y las
 **filas** los naturales `i`. La diagonal `(j, j)` pregunta "¿está `j` en el `j`-ésimo
 conjunto?". Invertirlo no rompe la prueba pero sí las cuentas de un ejercicio concreto.
- **Concluir "`f` no es inyectiva".** La contradicción es con la **sobreyectividad**: `D` es
 un elemento de `P(N)` que no está en la imagen.
- **Olvidar que `D` es un subconjunto de `N` legítimo.** Es el paso que hace válida la
 contradicción, y el que falla al intentar copiar el argumento sobre `Q`.

## Relacionado

- [[demostraciones/diagonalizacion]] — la técnica, con las dos variantes
- [[teoremas/existen-funciones-no-computables]] — la conclusión sobre computabilidad
- [[definiciones/cardinales-infinitos]] — `|P(N)| > |N|`
- [[definiciones/operaciones-con-conjuntos]] — qué es `P(A)`
- [[fuentes/numerabilidad-diag]]

## Procedencia

- **Enunciado** — numerabilidad-diag p.8, p.9
- **Hipótesis** — numerabilidad-diag p.8
- **Demostración** — numerabilidad-diag p.9
- **Cuándo se aplica** — numerabilidad-diag p.9 · incluye comentario del sistema
- **Errores típicos** — sin cita: comentario del sistema
