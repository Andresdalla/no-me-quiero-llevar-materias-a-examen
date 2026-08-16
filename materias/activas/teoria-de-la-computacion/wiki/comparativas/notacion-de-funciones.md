---
id: teoria-de-la-computacion/comparativas/notacion-de-funciones
tipo: comparativa
tema: U6
fuentes: [revision-conjuntos p.9, notas-conjuntos p.2, numerabilidad-diag p.3, numerabilidad-diag p.4]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Las tres notaciones de función de la cátedra

Los tres apuntes de la materia escriben lo mismo de tres maneras, y en dos casos no dicen
exactamente lo mismo. La propia cátedra lo advierte —**Observación 1.** "Tener cuidado que
diferentes docentes pueden usar notaciones diferentes"— así que esto no es un descuido sino
una condición de la materia.

El parcial es con material. Lo que hay que tener resuelto de antemano no es la notación en sí
sino **de qué apunte viene la consigna que estás respondiendo**, porque de eso depende qué
significa la palabra "función" en ella. Separado de [[definiciones/funcion]] por longitud.

## Tabla

| Concepto | `revision-conjuntos` p.9 | `notas-conjuntos` p.2 |
|---|---|---|
| función parcial | `f : A ⇸ B` | `f : A ↬ B` **Definición 6** |
| función total | `f : A → B` | `f : A → B` **Definición 7** |
| inyección (inyectiva **y total**) | — | `f : A ↪ B` **Definición 9** |
| sobreyección (sobreyectiva **y total**) | — | `f : A →\| B` **Definición 10** |
| biyección (biyectiva **y total**) | — | `f : A ↔ B` **Definición 11** |

## Criterio de decisión

La diferencia importante no es el dibujo de la flecha: `notas-conjuntos` introduce los
términos **inyección / sobreyección / biyección** como "inyectiva/sobreyectiva/biyectiva **+
total**". O sea, *inyectiva* y *inyección* no son sinónimos ahí. Un enunciado que pida "una
inyección de A en B" está pidiendo una función total, y si entregás una parcial inyectiva no
respondiste la consigna.

Las dos fuentes también definen **inyectiva** de forma distinta pero equivalente:
`revision-conjuntos` p.9 usa `(∀x, y ∈ A)(x ≠ y ⇒ f(x) ≠ f(y))`;
**Definición 8** usa `f(a₁) = f(a₂) ⇒ a₁ = a₂`. Son contrarrecíprocas: no hay contradicción,
pero conviene saber demostrar con las dos, porque la segunda forma es la cómoda cuando el
argumento arranca suponiendo que dos imágenes coinciden.

## La convención de `numerabilidad-diag`: "función" **significa** función parcial

La tercera fuente hace algo más fuerte que cambiar símbolos: cambia el significado por
omisión de la palabra.

"El término función será (como hasta ahora) utilizado en el
sentido de **función parcial** (es decir, en el sentido más general de función). Por lo tanto,
cuando se quiera restringir el discurso a funciones totales se deberá hacer explícita mención a
tal condición."

Es una convención fuerte y no la comparten las tres fuentes. Si una consigna dice "sea
`f : A ↬ B` una función", **no** podés asumir que es total. Al revés, `revision-conjuntos` usa
"función" sin comprometerse. Su definición de fondo, eso sí, coincide con las otras dos:
**Definición 1.3.** "Una función (parcial) de A en B es una relación entre A y B tal que a cada
elemento de A corresponde a lo sumo uno de B."

## Notación de definida / indefinida, dominio y recorrido

Esta fuente agrega vocabulario que las otras no tienen, y que hace falta justamente porque
trabaja con parciales por omisión: si una función puede no estar definida en un punto, hace
falta poder decirlo.

"diremos que `f` está definida en `a`, lo cual se notará `f ↓ a` […]
En caso contrario, diremos que `f` no está definida en `a`, y escribiremos `f ↑ a`."

Con eso puede separar el conjunto de entrada del conjunto donde la función realmente vive:
"Llamaremos **dominio** de una función `f` al subconjunto del
conjunto de entrada de `f` determinado por aquellos elementos donde `f` está definida.
Simétricamente, llamaremos **recorrido** de `f` al subconjunto del conjunto de salida
determinado por aquellos elementos que son valores de algún elemento del dominio."

**Cuidado con "dominio".** Acá el *conjunto de entrada* es `A` y el *dominio* es solo donde
`f` está definida (para una parcial, dominio ⊊ entrada); `revision-conjuntos` p.4 llama
"dominio" al `A` entero. Dos usos distintos de la misma palabra, y en una consigna sobre
funciones parciales la diferencia decide la respuesta.

Con este vocabulario las definiciones quedan más limpias, porque cuantifican sobre el dominio
en vez de sobre la entrada: **Def. 1.5** "Una función es inyectiva si a elementos diferentes
del dominio corresponden valores diferentes." · **Def. 1.6** "Una función es sobreyectiva si su
recorrido coincide con su conjunto de salida." · **Def. 1.7** "Una función total es
biyectiva si es inyectiva y sobreyectiva."

Un sinónimo más que aparece solo acá: "Cuando existe una biyección entre dos conjuntos se dice
que éstos son **coordinables**." Es lo mismo que *equipolentes* en
[[definiciones/comparacion-de-cardinalidades]].

## Por qué importa para la computabilidad

La convención de parcial-por-omisión no es un capricho de notación. La misma fuente da la
razón: "las funciones parciales modelan programas que **pueden no terminar**, mientras que las
funciones totales modelan programas que siempre producen una salida". Esa frase es el puente
entre U6 y el problema de la terminación de U7, y explica por qué el apunte que va a hablar de
computabilidad elige que "función" signifique parcial.

## Relacionado

- [[definiciones/funcion]] — la definición y sus cuatro propiedades
- [[comparativas/relaciones-vs-funciones]] — la otra tabla de notación paralela
- [[definiciones/comparacion-de-cardinalidades]] — donde *coordinable* aparece como equipolente
- [[fuentes/revision-conjuntos]] · [[fuentes/notas-conjuntos]] · [[fuentes/numerabilidad-diag]]

## Procedencia

- **Tabla** — notas-conjuntos p.2 · revision-conjuntos p.9 · duda: Conflicto de notación entre los dos apuntes de la materia
- **Criterio de decisión** — notas-conjuntos p.2 · revision-conjuntos p.9 · incluye comentario del sistema
- **La convención de `numerabilidad-diag`** — numerabilidad-diag p.3 · incluye comentario del sistema · duda registrada en `dudas.md`
- **Notación de definida / indefinida, dominio y recorrido** — numerabilidad-diag p.3, p.4 · notas-conjuntos p.2 · incluye comentario del sistema · duda registrada en `dudas.md`
- **Por qué importa para la computabilidad** — numerabilidad-diag p.4 · incluye comentario del sistema
