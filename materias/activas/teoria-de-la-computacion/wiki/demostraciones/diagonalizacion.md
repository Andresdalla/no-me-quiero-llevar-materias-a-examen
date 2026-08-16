---
id: teoria-de-la-computacion/demostraciones/diagonalizacion
tipo: demostracion
tema: U6
fuentes: [notas-conjuntos p.7, notas-conjuntos p.8, notas-conjuntos p.9]
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

✅ [notas-conjuntos p.8] **Observación 3.** "La construcción anterior es un ejemplo del método
de diagonalización. La función `g` se obtiene modificando los valores de las funciones de la
lista sobre la diagonal `(fₙ(n))ₙ∈N`, asegurando que difiere de cada una de ellas."

## Pasos

1. ✅ [notas-conjuntos p.7] "Supongamos, con el fin de obtener una contradicción, que todas las
   funciones `f : N → N` son computables. Entonces podríamos enumerarlas como `f₀, f₁, f₂, …`
   donde cada `fᵢ : N → N` es una función total."

2. ✅ [notas-conjuntos p.7] "Construimos ahora una nueva función `g : N → N` definida por"

   ```
   g(n) = fₙ(n) + 1
   ```

3. ✅ [notas-conjuntos p.7] "Esta función está bien definida para todo `n ∈ N`, y es total."

4. ✅ [notas-conjuntos p.7] "Veamos que `g` no puede coincidir con ninguna función de la lista.
   Sea `k ∈ N`. Entonces: `g(k) = f_k(k) + 1 ≠ f_k(k)`."

5. ✅ [notas-conjuntos p.8] "Por lo tanto, `g ≠ f_k`. Como esto vale para todo `k`, la función
   `g` difiere de cada función `f_k` en al menos un valor (concretamente, en el punto `k`). En
   consecuencia, `g` no aparece en la enumeración."

6. ✅ [notas-conjuntos p.8] "Esto contradice la hipótesis de que la lista contenía a todas las
   funciones. Por lo tanto, el conjunto de funciones `N → N` no es numerable."

7. ✅ [notas-conjuntos p.8] "Dado que el conjunto de funciones computables es numerable, se
   concluye que existen funciones que no son computables."

## La misma técnica sobre `R`

✅ [notas-conjuntos p.8] **Ejemplo 9.3.** "Probar que `R` no es numerable."

✅ [notas-conjuntos p.9] "Solución. Basta notar que el intervalo `(0, 1)` no es numerable.
Suponiendo que sí lo fuera, se podría escribir una enumeración decimal de sus elementos y
aplicar el argumento diagonal de Cantor para construir un número en `(0, 1)` que difiere de
cada elemento de la lista en la diagonal. Esto da una contradicción."

## Dónde suele fallar el estudiante

- 🧠 **Aplicarla a un conjunto numerable y no notar que no cierra.** Es literalmente una
  consigna de examen: ✅ [notas-conjuntos p.10] *(Examen setiembre 2025)* pide diagonalizar
  sobre `Q` y "mostrar que se llega a un absurdo". La diagonal construida sobre una
  enumeración de racionales **no produce un racional**, así que no hay contradicción. Ver
  [[examenes/notas-conjuntos-ejercicios]].
- 🧠 **No verificar que el objeto diagonal pertenece al conjunto.** Es el paso que hace o
  rompe la prueba, y el único que la cátedra pregunta explícitamente ("Mencione bajo qué
  circunstancias puede aplicarse diagonalización").
- 🧠 **El `+1` no es mágico, pero tiene que cambiar el valor.** Cualquier modificación que
  garantice `g(n) ≠ fₙ(n)` sirve. Lo que no sirve es una operación que pueda dejarlo igual.
- 🧠 **Confundir "`g` no está en la lista" con "`g` no es computable".** `g` no es la función
  no computable: la contradicción es con la **suposición** de que la lista era completa.
- 🧠 **Suponer que las `fᵢ` son totales sin decirlo.** El apunte lo dice explícito; si fueran
  parciales, `fₙ(n)` podría no estar definida y `g` no quedaría bien definida.

## Relacionado

- [[teoremas/existen-funciones-no-computables]] — el enunciado
- [[teoremas/palabras-finitas-son-numerables]] — la mitad numerable del argumento
- [[definiciones/cardinales-infinitos]] — `|P(N)| > |N|` por el mismo método
- [[examenes/notas-conjuntos-ejercicios]] — dos consignas de examen sobre esta técnica
- [[fuentes/notas-conjuntos]]
