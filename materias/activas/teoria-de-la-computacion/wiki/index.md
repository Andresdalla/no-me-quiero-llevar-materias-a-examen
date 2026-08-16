# Índice

<!-- Puerta de entrada humana. Una sección por unidad, enlaces a las páginas.
     Para rutear el LLM se usa mapa.md, no este archivo. -->

## Transversal

- [[fuentes/tc-temario]] — ficha del temario oficial: alcance, vigencia y límites

## U1 · Modelos de la noción de función computable

## U2 · Modelos imperativos

## U3 · Modelos funcionales

## U4 · La equivalencia de los modelos

## U5 · Auto-intérpretes y programas como datos

## U6 · Cardinalidad y numerabilidad

**Conjuntos**

- [[definiciones/conjunto]] — pertenencia, vacío, axioma de extensión, inclusión
- [[comparativas/formas-de-definir-conjuntos]] — extensión, comprensión, inducción
- [[definiciones/operaciones-con-conjuntos]] — `∪`, `∩`, `P(A)`, producto cartesiano

**Relaciones**

- [[definiciones/relacion]] — subconjunto de un producto cartesiano; `R<`
- [[definiciones/propiedades-de-relaciones]] — reflexiva, simétrica, transitiva y compañía
- [[definiciones/ordenes]] — parciales y totales, laxos y estrictos
- [[definiciones/operaciones-con-relaciones]] — inversa y composición
- [[teoremas/transitividad-de-r-menor]] → [[demostraciones/transitividad-de-r-menor]]

**Funciones**

- [[definiciones/funcion]] — parcial/total, inyectiva, sobreyectiva, biyectiva
- [[comparativas/relaciones-vs-funciones]] — notación paralela y la trampa de `∘`

**Cardinalidad y numerabilidad**

- [[definiciones/comparacion-de-cardinalidades]] — `⪯` y equipolencia `∼`
- [[definiciones/conjunto-infinito]] — infinito = se codifica en una parte propia
- [[definiciones/numerable-y-contable]] — las dos definiciones que se confunden
- [[teoremas/subconjunto-infinito-de-n-es-numerable]] — el teorema que las une
- [[teoremas/z-es-numerable]] · [[construcciones/emparejamiento-de-cantor]] — los ejemplos
- [[definiciones/cardinales-infinitos]] — `ℵ₀`, `ℵ₁`, hipótesis del continuo (extra)

**El argumento central de la materia**

- [[comparativas/funcion-vs-algoritmo]] — el vocabulario: empezá por acá
- [[teoremas/palabras-finitas-son-numerables]] — los programas son numerables
- [[demostraciones/diagonalizacion]] — las funciones `N → N` no lo son
- [[teoremas/p-de-n-no-es-numerable]] — la misma técnica sobre `P(N)` y `N → Bool`
- [[teoremas/existen-funciones-no-computables]] — la conclusión
- [[teoremas/propiedades-de-conjuntos-infinitos]] — `N` es el infinito más chico

**Exámenes**

- [[examenes/patron]] — cómo pregunta la cátedra
- [[examenes/notas-conjuntos-ejercicios]] · [[examenes/mayo-2025-multiple-opcion]]

**Fuentes**

- [[fuentes/notas-conjuntos]] — notas de Acuña 2026, la fuente más confiable
- [[fuentes/numerabilidad-diag]] — Copello-Tasistro 2022, y en qué diverge de las notas
- [[fuentes/revision-conjuntos]] — ficha del apunte de láminas, con sus tres erratas

## U7 · Indecidibilidad

## U8 · Clases de complejidad algorítmica

## U9 · Fundamentos de lenguajes de programación

## U10 · Programación funcional

- [[comparativas/lambda-case-vs-pattern-matching]] — las dos formas de definir que pide la cátedra
- [[construcciones/funciones-sobre-bool]] — `data Bool`, `not`, operadores booleanos
- [[construcciones/funciones-sobre-enteros]] — recursión y funciones de orden superior
- [[construcciones/funciones-sobre-listas]] — `length`, `map`, `filter`, `zip`, plegados
- [[construcciones/funciones-sobre-arboles]] — `data Arb`, `cantNodos`, recursión con dos ramas
- [[fuentes/repaso-haskell]] — ficha del repartido
