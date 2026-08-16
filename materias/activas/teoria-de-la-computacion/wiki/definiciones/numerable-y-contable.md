---
id: teoria-de-la-computacion/definiciones/numerable-y-contable
tipo: definicion
tema: U6
fuentes: [notas-conjuntos p.4, numerabilidad-diag p.7]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de numerable y de contable

Dos términos que suenan a sinónimos y no lo son, y cuya diferencia es exactamente la que hay
entre una biyección y una inyección. La distinción parece burocrática hasta que se ve que
juntas dan una equivalencia muy práctica: para probar que algo es numerable casi nunca se
construye una biyección, se construye una inyección y se invoca la infinitud.

## Enunciado

La pareja se define con las dos relaciones de
[[definiciones/comparacion-de-cardinalidades]], una con cada una. **Definición 15.** "Un
conjunto A es *numerable* si `A ∼ N` (existe una biyección `f : N → A`)." **Definición 16.**
"Un conjunto A es *contable* si `A ⪯ N`."

La lectura operativa es en términos de listas: "Un conjunto numerable puede listarse **sin
repeticiones**: `a₀, a₁, a₂, …`. Un conjunto contable puede enumerarse **permitiendo
repeticiones**." Permitir repeticiones es más fácil, así que contable es la condición más
débil, y eso es lo que enuncia la **Proposición 5.** "Todo conjunto numerable es contable."

La vuelta no vale en general, pero casi: **Proposición 6.** "Si A es contable e infinito,
entonces A es numerable." Esa hipótesis de infinitud es toda la diferencia, y el contraejemplo
de más abajo muestra por qué no se puede sacar.

**Las dos fuentes coinciden acá.** **Definición 3.2.** "A es contable si y sólo si `A ⪯ N`."
**Definición 3.3.** "A es numerable si y sólo si `A ∼ N`." Idénticas a las Definiciones 16 y
15 de `notas-conjuntos`. Es de lo poco que no diverge entre apuntes: podés confiar en estas
dos.

La caracterización por listas (`?15`) es la que conviene tener en la cabeza para razonar
rápido en el parcial, porque convierte las tres relaciones en tres preguntas sobre listas:

- "A es numerable ssi existe una lista (infinita) que contiene a todos los elementos de A,
 **sin repeticiones**."
- "A es contable ssi existe una lista (infinita) que contiene a todos los elementos de A, **con
 posibles repeticiones**."
- "`N ⪯ A` ssi existe una lista (infinita) formada por elementos de A, sin repeticiones."

Un detalle de vocabulario antes de seguir: el ejercicio `?14` dice "Demostrar que si un
conjunto es contable entonces o bien es finito o bien es **enumerable**". La palabra
"enumerable" aparece una sola vez en todo el repartido y nunca se define: casi seguro es un
desliz por "numerable". Anotado en `wiki/dudas.md`.

## Notación

| Término | Condición | Intuición |
|---|---|---|
| numerable | `A ∼ N` (biyección) | se lista sin repetir |
| contable | `A ⪯ N` (inyección total) | se lista, quizás repitiendo |

**Esta pareja de términos no es universal.** En mucha bibliografía "contable" (*countable*)
significa lo que acá se llama numerable, y se usa "numerable" para *countably infinite*. En
esta materia **valen las Definiciones 15 y 16 de la cátedra**, y son las que se evalúan.

## Ejemplo

El caso que separa limpiamente los dos términos es el finito: todo conjunto **finito** es
contable (inyectalo en `{0, …, n-1} ⊆ N`) pero **no** numerable, porque no hay biyección entre
un conjunto finito y `N`. Ahí se ve que contable es estrictamente más débil.

La Proposición 5 se demuestra en dos renglones, y el truco es simplemente dar vuelta la
biyección: "Si A es numerable, existe una biyección `f : N → A`. Su inversa `f⁻¹ : A → N`
existe y es inyectiva; por lo tanto, `A ⪯ N`."

Las Proposiciones 5 y 6 juntas dan la equivalencia útil: **contable + infinito ⟺ numerable**.
Ese es el resultado que se usa en la práctica, porque casi siempre es más fácil construir una
inyección que una biyección. En los hechos, cada vez que en U6 se prueba que algo es numerable
—`Z`, `Σ*`, `N × N`— se está usando esta equivalencia.

## Contraejemplo

`{a, b, c}` es contable pero **no** numerable, y el motivo es que es finito. Es el
contraejemplo que separa las dos definiciones y el que hace que la Proposición 6 necesite la
hipótesis "e infinito": sin ella la proposición sería directamente falsa, y este conjunto de
tres elementos alcanza para refutarla.

Del otro extremo, `R` no es ninguna de las dos cosas: no hay ni siquiera una inyección de `R`
en `N`. Ver [[teoremas/existen-funciones-no-computables]] y el argumento de
[[demostraciones/diagonalizacion]].

## Confusiones frecuentes

- **Numerable ⇒ contable, nunca al revés.** El recíproco necesita la hipótesis de infinitud.
 Es exactamente la trampa de la Proposición 6.
- **"Numerable" no quiere decir "chico".** `N × N`, `Z` y `Q` son numerables aunque
 "parezcan" más grandes que `N`. Ver [[construcciones/emparejamiento-de-cantor]] y
 [[teoremas/z-es-numerable]].
- **La dirección de la biyección da igual.** `A ∼ N` y `N ∼ A` son lo mismo: si hay biyección
 hay inversa. El apunte escribe `f : N → A` pero en las demostraciones usa las dos.
- **Contable con repeticiones no es lo mismo que sobreyectiva desde `N`.** Ojo con la consigna
 de examen de febrero 2026 sobre funciones sobreyectivas: ver
 [[examenes/notas-conjuntos-ejercicios]].

## Relacionado

- [[definiciones/comparacion-de-cardinalidades]] — `∼` y `⪯`
- [[definiciones/conjunto-infinito]] — la hipótesis que necesita la Proposición 6
- [[teoremas/subconjunto-infinito-de-n-es-numerable]] — el teorema que cierra la Proposición 6
- [[fuentes/notas-conjuntos]]

## Procedencia

- **Enunciado** — notas-conjuntos p.4 · numerabilidad-diag p.7 · duda registrada en `dudas.md`
- **Notación** — sin cita: comentario del sistema
- **Ejemplo** — notas-conjuntos p.4 · incluye comentario del sistema
- **Contraejemplo** — sin cita: comentario del sistema
- **Confusiones frecuentes** — sin cita: comentario del sistema
