---
id: teoria-de-la-computacion/definiciones/comparacion-de-cardinalidades
tipo: definicion
tema: U6
fuentes: [notas-conjuntos p.3, numerabilidad-diag p.4, numerabilidad-diag p.5]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de `⪯` y de equipolencia

Comparar tamaños de conjuntos infinitos necesita dos relaciones, no una: un "menor o igual" y
una igualdad. Ninguna de las dos se define contando, porque no se puede — las dos se definen
exhibiendo una función con cierta propiedad. Esta página es la que hace posible todo el resto
de U6.

## Enunciado

Lo primero es entender por qué hace falta maquinaria nueva. Para conjuntos finitos, si uno
está estrictamente contenido en otro es más chico, y listo; pero "este razonamiento deja de ser
válido cuando se consideran conjuntos infinitos. La razón es que una inclusión estricta ya no
implica necesariamente una diferencia de cardinalidad."

La relación "menor o igual" es la **Definición 12.** "Sean A y B conjuntos. Se dice que
`A ⪯ B` si existe una función total e inyectiva `f : A → B`." Inyectiva alcanza, y el apunte
explica por qué: "Esta relación expresa que los elementos de A pueden codificarse dentro de B
sin colisiones." Si `A` entra adentro de `B` sin pisarse, `B` no puede ser más chico.

La igualdad correspondiente pide lo mismo en las dos direcciones a la vez, o sea una biyección.
**Definición 13.** "Sean A y B conjuntos. Se dice que A y B son *equipolentes*, y se escribe
`A ∼ B`, si y sólo si existe una función biyectiva y total `f : A → B`."

Con eso ya se pueden enunciar las dos proposiciones que se usan todo el tiempo. La primera dice
que la inclusión es un caso particular de `⪯` — **Proposición 2.** "Si `A ⊆ B`, entonces
`A ⪯ B`." La segunda es la que permite reemplazar una biyección difícil por dos inyecciones
fáciles: **Proposición 3.** "`A ∼ B`, si `A ⪯ B` y `B ⪯ A`."

La Proposición 3 es el **teorema de Schröder-Bernstein**, y el apunte lo nombra en la
demostración: "si existen funciones inyectivas totales `f : A → B` y `g : B → A`, entonces por
el teorema de Schroder-Bernstein existe una biyección entre A y B". No lo demuestra, así que
en el parcial se invoca por nombre.

### Las dos fuentes DEFINEN `∼` distinto

En `⪯` no hay problema, las dos fuentes dicen lo mismo. **Definición 2.1.** "Diremos que A es
de menor o igual tamaño que B —lo cual se escribirá `A ⪯ B`— si y sólo si existe una función
total inyectiva de A en B." Es literalmente la Definición 12 de `notas-conjuntos`.

La divergencia está en `∼`, y es de las que cambian qué hay que escribir en una demostración:

| Fuente | Definición de `A ∼ B` |
|---|---|
| `notas-conjuntos` Def. 13 | existe una **biyección** total `f : A → B` |
| `numerabilidad-diag` Def. 2.2 | "`A ⪯ B` **y** `B ⪯ A`" |

No es una contradicción: las dos condiciones son equivalentes **por Schröder-Bernstein**.
Pero cambia qué hay que probar. Con la definición de Acuña, exhibir dos inyecciones no alcanza
hasta invocar Schröder-Bernstein (su Proposición 3). Con la de Copello, las dos inyecciones
**son** la definición, y lo que cuesta es sacar la biyección.

En el parcial: si te piden probar `A ∼ B`, aclará con qué definición trabajás. Anotado en
`wiki/dudas.md`.

## Notación

| Símbolo | Significa |
|---|---|
| `A ⪯ B` | existe inyección total de `A` en `B` — "`A` no es más grande que `B`" |
| `A ∼ B` | equipolentes: existe biyección total |
| `A ≺ B` | "`A ⪯ B` y `A ≁ B`" (definido recién en el Ejercicio 12) |
| `A ⊊ B` | inclusión estricta |

## Ejemplo

El ejemplo canónico es sacarle un elemento a `N` y ver que no se achica: "`N \ {0} ⊊ N`, pero
ambos conjuntos tienen el mismo tamaño, ya que la función `f(n) = n + 1` define una biyección
entre ellos." Es el ejemplo que hay que tener en la punta de la lengua, porque es el
contraejemplo a "la parte es más chica que el todo" y todo U6 se apoya en él.

La Proposición 2, en cambio, se demuestra con la función más aburrida que hay, y eso es
justamente lo que la hace fácil de recordar: "Consideremos la función identidad `i : A → B`
dada por `i(a) = a` para todo `a ∈ A`. La función está bien definida porque `A ⊆ B`, es total y
es inyectiva. Por lo tanto, `A ⪯ B`."

## Contraejemplo

Lo que falla acá no es un conjunto sino un razonamiento, y la fuente lo señala en la
**Observación 2.** "En el caso finito, si `A ⊊ B`, entonces necesariamente `A ≁ B`. En el caso
infinito, esto puede fallar: puede ocurrir que `A ⊊ B` y, sin embargo, `A ∼ B`."

O sea: `A ⊊ B` **no** es contraejemplo de `A ∼ B` cuando hay infinitos. Es exactamente el paso
que se falla en el parcial, porque la intuición finita se cuela sin que uno la note — y el
ejemplo de arriba, `N \ {0}` contra `N`, es la prueba de que se cuela mal.

## Confusiones frecuentes

- **`⊆` vs `⪯`.** Inclusión es contención literal de elementos; `⪯` solo pide poder codificar
 sin colisiones. `A ⊆ B ⇒ A ⪯ B` pero no al revés: `N ⪯ Z` sin que `N ⊆ Z` sea el argumento.
 Ver [[definiciones/conjunto]].
- **`⪯` en las dos direcciones no es "obvio" que dé biyección.** Necesita Schröder-Bernstein,
 que el apunte cita sin probar.
- **Total e inyectiva, las dos.** Sacar "total" rompe la definición: ver
 [[definiciones/funcion]].
- La Proposición 3 está enunciada con "si" pero la demostración prueba **las dos
 direcciones**. Leela como "si y sólo si".

## Relacionado

- [[definiciones/conjunto-infinito]] — la definición que usa `⪯` contra un subconjunto propio
- [[definiciones/numerable-y-contable]] — `∼ N` y `⪯ N`
- [[definiciones/funcion]] — inyectiva, sobreyectiva, total
- [[teoremas/propiedades-de-conjuntos-infinitos]] — `⪯` es reflexiva y transitiva (`?8`)
- [[fuentes/notas-conjuntos]] · [[fuentes/numerabilidad-diag]]

## Procedencia

- **Enunciado** — notas-conjuntos p.3 · incluye comentario del sistema
- **Enunciado › Las dos fuentes DEFINEN `∼` distinto** — numerabilidad-diag p.4, p.5 · incluye comentario del sistema · duda: Las dos fuentes DEFINEN `∼` distinto
- **Notación** — notas-conjuntos p.8
- **Ejemplo** — notas-conjuntos p.3 · incluye comentario del sistema
- **Contraejemplo** — notas-conjuntos p.3 · incluye comentario del sistema
- **Confusiones frecuentes** — sin cita: comentario del sistema
