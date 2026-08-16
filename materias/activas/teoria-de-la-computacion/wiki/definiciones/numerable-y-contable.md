---
id: teoria-de-la-computacion/definiciones/numerable-y-contable
tipo: definicion
tema: U6
fuentes: [notas-conjuntos p.4]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de numerable y de contable

## Enunciado

✅ [notas-conjuntos p.4] **Definición 15.** "Un conjunto A es *numerable* si `A ∼ N` (existe
una biyección `f : N → A`)."

✅ [notas-conjuntos p.4] **Definición 16.** "Un conjunto A es *contable* si `A ⪯ N`."

✅ [notas-conjuntos p.4] Interpretación: "Un conjunto numerable puede listarse **sin
repeticiones**: `a₀, a₁, a₂, …`. Un conjunto contable puede enumerarse **permitiendo
repeticiones**."

✅ [notas-conjuntos p.4] **Proposición 5.** "Todo conjunto numerable es contable."

✅ [notas-conjuntos p.4] **Proposición 6.** "Si A es contable e infinito, entonces A es
numerable."

## Notación

| Término | Condición | Intuición |
|---|---|---|
| numerable | `A ∼ N` (biyección) | se lista sin repetir |
| contable | `A ⪯ N` (inyección total) | se lista, quizás repitiendo |

⚠️ **Esta pareja de términos no es universal.** En mucha bibliografía "contable" (*countable*)
significa lo que acá se llama numerable, y se usa "numerable" para *countably infinite*. En
esta materia **valen las Definiciones 15 y 16 de la cátedra**, y son las que se evalúan.

## Ejemplo

🧠 Todo conjunto **finito** es contable (inyectalo en `{0, …, n-1} ⊆ N`) pero **no** numerable:
no hay biyección entre un conjunto finito y `N`.

✅ [notas-conjuntos p.4] Demostración de la Proposición 5: "Si A es numerable, existe una
biyección `f : N → A`. Su inversa `f⁻¹ : A → N` existe y es inyectiva; por lo tanto, `A ⪯ N`."

🧠 Las Proposiciones 5 y 6 juntas dan la equivalencia útil:
**contable + infinito ⟺ numerable**. Ese es el resultado que se usa en la práctica, porque
casi siempre es más fácil construir una inyección que una biyección.

## Contraejemplo

🧠 `{a, b, c}` es contable pero **no** numerable: es finito. Es el contraejemplo que separa las
dos definiciones y el que hace que la Proposición 6 necesite la hipótesis "e infinito".

🧠 `R` no es ninguna de las dos: ver [[teoremas/existen-funciones-no-computables]] y el
argumento de [[demostraciones/diagonalizacion]].

## Confusiones frecuentes

- **Numerable ⇒ contable, nunca al revés.** El recíproco necesita la hipótesis de infinitud.
  Es exactamente la trampa de la Proposición 6.
- **"Numerable" no quiere decir "chico".** `N × N`, `Z` y `Q` son numerables aunque
  "parezcan" más grandes que `N`. Ver [[construcciones/emparejamiento-de-cantor]] y
  [[teoremas/z-es-numerable]].
- 🧠 **La dirección de la biyección da igual.** `A ∼ N` y `N ∼ A` son lo mismo: si hay biyección
  hay inversa. El apunte escribe `f : N → A` pero en las demostraciones usa las dos.
- **Contable con repeticiones no es lo mismo que sobreyectiva desde `N`.** Ojo con la consigna
  de examen de febrero 2026 sobre funciones sobreyectivas: ver
  [[examenes/notas-conjuntos-ejercicios]].

## Relacionado

- [[definiciones/comparacion-de-cardinalidades]] — `∼` y `⪯`
- [[definiciones/conjunto-infinito]] — la hipótesis que necesita la Proposición 6
- [[teoremas/subconjunto-infinito-de-n-es-numerable]] — el teorema que cierra la Proposición 6
- [[fuentes/notas-conjuntos]]
