---
id: teoria-de-la-computacion/teoremas/existen-funciones-no-computables
tipo: teorema
tema: U6
fuentes: [notas-conjuntos p.7, notas-conjuntos p.8]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Existen funciones no computables

Este es el resultado al que apunta toda la unidad, y llama la atención lo poco que hace falta
para llegar: no aparece ninguna máquina, ningún lenguaje ni ninguna noción técnica de cómputo.
Es un argumento de conteo puro, y esa es exactamente su fuerza.

## Enunciado

**Teorema 4.** "Existen funciones `f : N → N` que no son computables por ningún programa." La
afirmación es existencial: dice que hay, no dice cuál.

La motivación del apunte anticipa la estrategia entera en una oración: "si el conjunto de los
programas es numerable y el conjunto de las funciones no lo es, entonces necesariamente existen
funciones que no pueden ser calculadas por ningún programa." Todo lo demás es justificar las
dos premisas.

## Hipótesis

Las tres se encadenan: las dos primeras se prueban aparte, y la tercera es la que las junta.
La que más se olvida es la segunda, sin la cual el conteo no cierra.

- El conjunto de programas es numerable — ver
 [[teoremas/palabras-finitas-son-numerables]].
- "A cada programa se le asocia, **a lo sumo**, una función
 `f : N → N` que dicho programa computa."
- De ahí sale el paso clave: el conjunto de funciones **computables** es numerable, porque
 se inyecta en el de programas.

## Demostración

El argumento completo, con la construcción de la función que se escapa de la lista, está en
[[demostraciones/diagonalizacion]]: es una diagonalización dentro de una demostración por
contradicción. Lo que queda una vez probado que las funciones `N → N` no son numerables es la
resta: "Dado que el conjunto de funciones computables es numerable, se concluye que existen
funciones que no son computables."

## Cuándo se aplica

Es el primer resultado de **imposibilidad** del curso, y el patrón se repite después en el
problema de la terminación y en el teorema de Rice (U7). El molde es siempre el mismo: contar
cuántos programas hay, contar cuántos objetos hay que computar, y mostrar que no alcanzan.

Conviene retener hasta dónde llega la conclusión, porque es más amplia de lo que parece:
"Este argumento no depende del lenguaje de programación utilizado. La conclusión es
completamente general y expresa una limitación matemática intrínseca del cómputo: siempre
existirán funciones que no pueden ser calculadas por ningún algoritmo."

Y hacia el otro lado, tampoco necesita maquinaria pesada. Alcanza con la desigualdad más
básica entre cardinales: "basta con observar que `ℵ₀ < |P(N)|`. Esta desigualdad es suficiente
para demostrar que existen funciones no computables. La hipótesis del continuo no es necesaria
para este argumento". Invocar la hipótesis del continuo acá —que además es indecidible— sería
usar un martillo de más.

## Errores típicos

- **Creer que el teorema exhibe una función no computable concreta.** No lo hace: es un
 argumento de conteo, puramente **existencial**. Sabés que hay, no cuál es. Las funciones no
 computables concretas (terminación) vienen después, en U7.
- **Pensar que es una limitación de un lenguaje o de una máquina.** No depende del lenguaje:
 eso es lo que el apunte subraya dos veces.
- **Confundir "no computable" con "difícil de computar".** No es una cuestión de costo — eso
 es U8 (P y NP). Acá directamente no existe programa.
- **Saltear el "a lo sumo una función" por programa.** Es lo que permite inyectar funciones
 computables en programas. Si un programa computara muchas funciones, el conteo no cerraría.

## Relacionado

- [[demostraciones/diagonalizacion]] — el argumento
- [[teoremas/palabras-finitas-son-numerables]] — que los programas son numerables
- [[definiciones/cardinales-infinitos]] — `ℵ₀ < |P(N)|`
- [[definiciones/numerable-y-contable]]
- [[fuentes/notas-conjuntos]]

## Procedencia

- **Enunciado** — notas-conjuntos p.7, p.1 · incluye comentario del sistema
- **Hipótesis** — notas-conjuntos p.7 · incluye comentario del sistema
- **Demostración** — notas-conjuntos p.8
- **Cuándo se aplica** — notas-conjuntos p.8, p.10 · incluye comentario del sistema
- **Errores típicos** — sin cita: comentario del sistema
