---
id: teoria-de-la-computacion/comparativas/funcion-vs-algoritmo
tipo: comparativa
tema: U6
fuentes: [numerabilidad-diag p.1, numerabilidad-diag p.9, numerabilidad-diag p.10]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Función (matemática) vs algoritmo

🧠 Esta página no es sobre un resultado: es sobre **una decisión de vocabulario de la cátedra**
que, si no la tenés clara, hace que el teorema central de la materia suene a trabalenguas.

## El problema

✅ [numerabilidad-diag p.1] "La palabra función es usada en el contexto de la Programación con
el significado de "pieza" o "componente" de código como, por ejemplo, cuando uno habla de
función Haskell, C, etc. Ahora bien, en la Matemática clásica también se utiliza ese término,
pero con un significado radicalmente distinto."

✅ [numerabilidad-diag p.1] "Nuestra solución para despejar esa ambigüedad será **reservar el
término función para su uso matemático clásico**. En cuanto a las piezas de código ejecutable
automáticamente que en general producen un cierto dato como resultado cuando son provistas con
cierto dato de entrada, las llamaremos **(codificaciones de) algoritmos**."

## Tabla

| Criterio | Función (matemática) | Algoritmo |
|---|---|---|
| Qué es | un **conjunto** de pares ordenados | una pieza de código ejecutable |
| Definida en | [[definiciones/funcion]], como relación | por su texto fuente |
| Cuántos hay | no numerables (`N ↬ N`) | numerables |
| Por qué esa cantidad | [[teoremas/p-de-n-no-es-numerable]] | [[teoremas/palabras-finitas-son-numerables]] |
| Relación entre ellos | cada algoritmo computa **una y una sola** función | cada función **puede o no** tener algoritmo |

## Criterio de decisión

✅ [numerabilidad-diag p.1] "Cada algoritmo puede ser interpretado como (implementación o
método de cómputo de) una función. Recíprocamente, **cada función puede verse como un problema
de programación**, a saber, el problema de diseñar o escribir un algoritmo que sirva como
método de cómputo de la función en cuestión."

🧠 Ese "recíprocamente" es la bisagra de la materia: convierte una pregunta sobre tamaños de
conjuntos en una pregunta sobre qué se puede programar.

## El argumento final, en la versión de esta fuente

✅ [numerabilidad-diag p.10] "Llamemos ahora `S` a la correspondencia entre algoritmos y
funciones en `N ↬ N` computadas por ellos. Esa correspondencia `S` es una función total,
puesto que todo algoritmo computa una (y una sola) función."

✅ [numerabilidad-diag p.10] "Ahora bien, si toda función en `N ↬ N` fuese computable por un
algoritmo, `S` sería sobreyectiva. Y la solución de uno de los ejercicios precedentes nos daría
entonces el resultado de que el conjunto `N ↬ N` sería de tamaño menor o igual que el de los
algoritmos. Pero éste es a su vez numerable. Luego, se concluiría que `N ↬ N ⪯ N`. Pero ya
tenemos (en virtud de otro ejercicio) que `N ⪯ N ↬ N` y, por lo tanto, tendríamos
`N ∼ N ↬ N`, lo cual es imposible, como ya ha quedado demostrado."

🧠 El "ejercicio precedente" es el `?7`: ✅ [numerabilidad-diag p.5] "Demostrar que una
condición necesaria y suficiente para `A ⪯ B` es que exista una función sobreyectiva de `B` en
`A`". **Ese mismo enunciado es la consigna de examen de febrero 2026** — ver
[[examenes/notas-conjuntos-ejercicios]]. Aparece como ejercicio en una fuente y como pregunta
de examen en la otra: estudialo.

✅ [numerabilidad-diag p.10] "La formalización de este argumento exige hacer precisa la
intuición de función computable a la que hemos hecho referencia, lo cual es materia de otro
repartido."

## Cuándo elegir cada uno

- 🧠 Decí **función** cuando hables del objeto matemático: un conjunto de pares, que existe
  tenga o no quien lo compute.
- 🧠 Decí **algoritmo** (no "función") cuando hables de código. En esta materia "función
  Haskell" es un algoritmo, no una función.
- 🧠 Ojo con `notas-conjuntos`, que usa "programa" donde esta fuente dice "algoritmo", y no
  hace la distinción terminológica explícita. Son intercambiables en la práctica, pero si la
  consigna del parcial usa una de las dos palabras, contestá con esa.

## Relacionado

- [[definiciones/funcion]] — la definición matemática, y la convención "función = parcial"
- [[teoremas/existen-funciones-no-computables]] — el mismo resultado por la vía de `notas-conjuntos`
- [[teoremas/palabras-finitas-son-numerables]] · [[teoremas/p-de-n-no-es-numerable]]
- [[fuentes/numerabilidad-diag]]
