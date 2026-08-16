---
id: teoria-de-la-computacion/teoremas/palabras-finitas-son-numerables
tipo: teorema
tema: U6
fuentes: [notas-conjuntos p.6, notas-conjuntos p.7, numerabilidad-diag p.8]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# `Σ*` es numerable, y por lo tanto los programas también

## Enunciado

✅ [notas-conjuntos p.6] **Teorema 3.** "Si `Σ` es un alfabeto finito, entonces el conjunto
`Σ*` de todas las palabras finitas sobre `Σ` es numerable."

✅ [notas-conjuntos p.7] **Proposición 7.** "El conjunto de los programas válidos en un
lenguaje de programación fijo es numerable."

## Hipótesis

- `Σ` es un alfabeto **finito** ✅ [notas-conjuntos p.6]
- Las palabras son **finitas** ✅ [notas-conjuntos p.6]
- Para la Proposición 7: ✅ [notas-conjuntos p.7] "todo programa válido es una palabra finita
  sobre un alfabeto finito (Los 128 símbolos de ASCII por ejemplo)"

## Demostración

**Primera vía — por longitud.** ✅ [notas-conjuntos p.6] "Para cada `n ∈ N`, sea `Σⁿ` el
conjunto de palabras de longitud exactamente `n`. Como `Σ` es finito, también lo es `Σⁿ` (de
hecho, `|Σⁿ| = mⁿ`)." Y `Σ* = ⋃ₙ₌₀^∞ Σⁿ`.

✅ [notas-conjuntos p.7] "Se puede entonces enumerar `Σ*` recorriendo primero todas las
palabras de longitud 0, luego las de longitud 1, luego las de longitud 2, y así sucesivamente.
Dentro de cada `Σⁿ`, se fija un orden lexicográfico. Este procedimiento produce una enumeración
sin repeticiones de todas las palabras finitas, por lo que `Σ*` es numerable."

**Segunda vía — codificación explícita.** ✅ [notas-conjuntos p.7] "Asignamos a cada símbolo
`aᵢ` un número `i ∈ {1, …, m}`. Dada una palabra `w = a_{i₁}a_{i₂}⋯a_{i_k}`, la interpretamos
como el número natural"

```
φ(w) = i₁(m+1)^(k−1) + i₂(m+1)^(k−2) + ⋯ + i_k
```

✅ [notas-conjuntos p.7] "Como no se utiliza el dígito 0, distintas palabras producen números
distintos. Por lo tanto, `φ` es inyectiva y se concluye que `Σ* ⪯ N`."

🧠 Los exponentes están transcriptos contra la página rasterizada: el texto plano los pierde.

**Conclusión para programas.** ✅ [notas-conjuntos p.7] "Dado que todo programa puede
representarse como una palabra finita sobre un alfabeto finito, el conjunto de todos los
programas es un subconjunto de `Σ*`. Por lo tanto, es numerable."

## La segunda fuente da la misma prueba, sin fórmula

✅ [numerabilidad-diag p.8] **Ejemplo 3.2 (Palabras).** "Dado un alfabeto finito `Σ`, el
conjunto de las palabras sobre este alfabeto lo denominaremos mediante `Σ*`. Podemos ver que
`Σ* ⪯ N` construyendo una inyección `f : Σ* ↪ N`. Como el alfabeto es finito lo podemos ver
como una enumeración de `n` símbolos `Σ = {a₁, …, aₙ}`, y asignar a cada carácter un dígito
distinto de cero en una base `n + 1`. Podemos entonces ver a cada palabra como un natural
codificado en un sistema en base `n+1`. **Excluimos el dígito 0 para garantizar la
inyectividad**, dado que si lo hubiéramos incluido tendríamos problemas con los ceros a la
izquierda no significativos en palabras."

🧠 Es exactamente la `φ(w)` de arriba, explicada sin escribir la fórmula: "base `n+1` sin el
dígito 0". Las dos fuentes coinciden, y la segunda **dice el porqué** del `+1` que la primera
solo enuncia. Si te cuesta recordar la fórmula, recordá la frase.

✅ [numerabilidad-diag p.8] Y la conclusión sobre programas, encadenada: "el conjunto formado
por los programas válidos en cierto lenguaje `Prog` esta incluido en `Σ*` y por lo tanto
`Prog ⪯ Σ*`. […] Tenemos así que `Prog ⪯ Σ* ⪯ N`, con lo cual podemos concluir que
`Prog ⪯ N`."

🧠 Notá que esta fuente concluye `Prog ⪯ N` (**contable**), no directamente "numerable". Es más
cuidadosa: para numerable hace falta además que `Prog` sea infinito. Ver
[[definiciones/numerable-y-contable]].

## Cuándo se aplica

🧠 Es **la mitad del argumento central de la materia**. La otra mitad es que las funciones
`N → N` no son numerables. Juntas dan
[[teoremas/existen-funciones-no-computables]].

🧠 La base `m+1` con dígitos en `{1, …, m}` es un truco reutilizable: evitar el `0` impide que
`aa` y `a` colisionen (como pasaría con ceros a la izquierda en base `m`).

## Errores típicos

- 🧠 **Olvidar que el alfabeto tiene que ser finito.** Con `Σ` infinito el teorema es falso en
  general, y toda la conclusión sobre programas se cae.
- 🧠 **Confundir "palabras finitas" con "cantidad finita de palabras".** `Σ*` es **infinito**;
  lo finito es cada palabra. Es la confusión que hace que el resultado parezca trivial.
- 🧠 **Enumerar por orden lexicográfico puro**, sin agrupar por longitud primero. Con el
  lexicográfico solo nunca llegás a las palabras que empiezan con la segunda letra: `a`, `aa`,
  `aaa`, … no termina. **Primero longitud, después lexicográfico.**
- 🧠 **Creer que la Proposición 7 depende del lenguaje.** No: cualquier lenguaje cuyo código
  fuente sea texto finito sobre un alfabeto finito cae bajo el mismo argumento.

## Relacionado

- [[teoremas/existen-funciones-no-computables]] — la otra mitad del argumento
- [[definiciones/numerable-y-contable]] · [[definiciones/comparacion-de-cardinalidades]]
- [[construcciones/emparejamiento-de-cantor]] — la misma estrategia de recorrido por bloques
- [[comparativas/funcion-vs-algoritmo]] — por qué contar programas responde una pregunta sobre funciones
- [[fuentes/notas-conjuntos]] · [[fuentes/numerabilidad-diag]]
