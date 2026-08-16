---
id: teoria-de-la-computacion/demostraciones/diagonalizacion
tipo: demostracion
tema: U6
fuentes: [notas-conjuntos p.7, notas-conjuntos p.8, notas-conjuntos p.9, numerabilidad-diag p.9]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Demostración por diagonalización

## Qué prueba

[[teoremas/existen-funciones-no-computables]] — y, de paso, que el conjunto de funciones
`N → N` no es numerable.

## Técnica

**Diagonalización**, dentro de una demostración por contradicción.

**Observación 3.** "La construcción anterior es un ejemplo del método
de diagonalización. La función `g` se obtiene modificando los valores de las funciones de la
lista sobre la diagonal `(fₙ(n))ₙ∈N`, asegurando que difiere de cada una de ellas."

## Pasos

1. "Supongamos, con el fin de obtener una contradicción, que todas las
 funciones `f : N → N` son computables. Entonces podríamos enumerarlas como `f₀, f₁, f₂, …`
 donde cada `fᵢ : N → N` es una función total."

2. "Construimos ahora una nueva función `g : N → N` definida por"

 ```
 g(n) = fₙ(n) + 1
 ```

3. "Esta función está bien definida para todo `n ∈ N`, y es total."

4. "Veamos que `g` no puede coincidir con ninguna función de la lista.
 Sea `k ∈ N`. Entonces: `g(k) = f_k(k) + 1 ≠ f_k(k)`."

5. "Por lo tanto, `g ≠ f_k`. Como esto vale para todo `k`, la función
 `g` difiere de cada función `f_k` en al menos un valor (concretamente, en el punto `k`). En
 consecuencia, `g` no aparece en la enumeración."

6. "Esto contradice la hipótesis de que la lista contenía a todas las
 funciones. Por lo tanto, el conjunto de funciones `N → N` no es numerable."

7. "Dado que el conjunto de funciones computables es numerable, se
 concluye que existen funciones que no son computables."

## La otra fuente diagonaliza sobre `P(N)`, no sobre funciones

"Usaremos una técnica usada en estos casos, llamada **método de
diagonalización**, para demostrar que un conjunto no es numerable."

El objeto construido no es una función sino un conjunto:
`D = {j : not(T(j, j))}`, con `T` la tabla booleana de pertenencias. Desarrollo completo en
[[teoremas/p-de-n-no-es-numerable]].

**Son la misma técnica con distinto disfraz**, y conviene verlo: por
"`P(N) ∼ N → Bool`", diagonalizar sobre subconjuntos de `N` *es*
diagonalizar sobre funciones `N → Bool`. La versión de `notas-conjuntos` lo hace sobre
`N → N` y suma 1; ésta lo hace sobre `N → Bool` y niega. El esqueleto —construir algo que
difiera de cada elemento de la lista en la posición diagonal— es idéntico.

## La misma técnica sobre `R`

**Ejemplo 9.3.** "Probar que `R` no es numerable."

"Solución. Basta notar que el intervalo `(0, 1)` no es numerable.
Suponiendo que sí lo fuera, se podría escribir una enumeración decimal de sus elementos y
aplicar el argumento diagonal de Cantor para construir un número en `(0, 1)` que difiere de
cada elemento de la lista en la diagonal. Esto da una contradicción."

## Dónde suele fallar el estudiante

- **Aplicarla a un conjunto numerable y no notar que no cierra.** Es literalmente una
 consigna de examen: *(Examen setiembre 2025)* pide diagonalizar
 sobre `Q` y "mostrar que se llega a un absurdo". La diagonal construida sobre una
 enumeración de racionales **no produce un racional**, así que no hay contradicción. Ver
 [[examenes/notas-conjuntos-ejercicios]].
- **No verificar que el objeto diagonal pertenece al conjunto.** Es el paso que hace o
 rompe la prueba, y el único que la cátedra pregunta explícitamente ("Mencione bajo qué
 circunstancias puede aplicarse diagonalización").
- **El `+1` no es mágico, pero tiene que cambiar el valor.** Cualquier modificación que
 garantice `g(n) ≠ fₙ(n)` sirve. Lo que no sirve es una operación que pueda dejarlo igual.
- **Confundir "`g` no está en la lista" con "`g` no es computable".** `g` no es la función
 no computable: la contradicción es con la **suposición** de que la lista era completa.
- **Suponer que las `fᵢ` son totales sin decirlo.** El apunte lo dice explícito; si fueran
 parciales, `fₙ(n)` podría no estar definida y `g` no quedaría bien definida.

## Relacionado

- [[teoremas/existen-funciones-no-computables]] — el enunciado
- [[teoremas/palabras-finitas-son-numerables]] — la mitad numerable del argumento
- [[definiciones/cardinales-infinitos]] — `|P(N)| > |N|` por el mismo método
- [[teoremas/p-de-n-no-es-numerable]] — la variante sobre `P(N)`
- [[examenes/notas-conjuntos-ejercicios]] — dos consignas de examen sobre esta técnica
- [[fuentes/notas-conjuntos]] · [[fuentes/numerabilidad-diag]]

## Procedencia

- **Técnica** — notas-conjuntos p.8
- **Pasos** — notas-conjuntos p.7, p.8
- **La otra fuente diagonaliza sobre `P(N)`, no sobre funciones** — numerabilidad-diag p.9 · incluye comentario del sistema
- **La misma técnica sobre `R`** — notas-conjuntos p.8, p.9
- **Dónde suele fallar el estudiante** — notas-conjuntos p.10 · incluye comentario del sistema
