---
id: teoria-de-la-computacion/definiciones/comparacion-de-cardinalidades
tipo: definicion
tema: U6
fuentes: [notas-conjuntos p.3]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de `⪯` y de equipolencia

## Enunciado

**Por qué hace falta.** ✅ [notas-conjuntos p.3] "este razonamiento deja de ser válido cuando
se consideran conjuntos infinitos. La razón es que una inclusión estricta ya no implica
necesariamente una diferencia de cardinalidad."

✅ [notas-conjuntos p.3] **Definición 12.** "Sean A y B conjuntos. Se dice que `A ⪯ B` si
existe una función total e inyectiva `f : A → B`."

✅ [notas-conjuntos p.3] "Esta relación expresa que los elementos de A pueden codificarse
dentro de B sin colisiones."

✅ [notas-conjuntos p.3] **Definición 13.** "Sean A y B conjuntos. Se dice que A y B son
*equipolentes*, y se escribe `A ∼ B`, si y sólo si existe una función biyectiva y total
`f : A → B`."

✅ [notas-conjuntos p.3] **Proposición 2.** "Si `A ⊆ B`, entonces `A ⪯ B`."

✅ [notas-conjuntos p.3] **Proposición 3.** "`A ∼ B`, si `A ⪯ B` y `B ⪯ A`."

🧠 La Proposición 3 es el **teorema de Schröder-Bernstein**, y el apunte lo nombra en la
demostración: "si existen funciones inyectivas totales `f : A → B` y `g : B → A`, entonces por
el teorema de Schroder-Bernstein existe una biyección entre A y B".

## Notación

| Símbolo | Significa |
|---|---|
| `A ⪯ B` | existe inyección total de `A` en `B` — "`A` no es más grande que `B`" |
| `A ∼ B` | equipolentes: existe biyección total |
| `A ≺ B` | ✅ [notas-conjuntos p.8] "`A ⪯ B` y `A ≁ B`" (definido recién en el Ejercicio 12) |
| `A ⊊ B` | inclusión estricta |

## Ejemplo

✅ [notas-conjuntos p.3] "`N \ {0} ⊊ N`, pero ambos conjuntos tienen el mismo tamaño, ya que la
función `f(n) = n + 1` define una biyección entre ellos."

✅ [notas-conjuntos p.3] Demostración de la Proposición 2: "Consideremos la función identidad
`i : A → B` dada por `i(a) = a` para todo `a ∈ A`. La función está bien definida porque
`A ⊆ B`, es total y es inyectiva. Por lo tanto, `A ⪯ B`."

🧠 Este es el ejemplo que hay que tener en la punta de la lengua: es el contraejemplo a "la
parte es más chica que el todo", y todo U6 se apoya en él.

## Contraejemplo

✅ [notas-conjuntos p.3] **Observación 2.** "En el caso finito, si `A ⊊ B`, entonces
necesariamente `A ≁ B`. En el caso infinito, esto puede fallar: puede ocurrir que `A ⊊ B` y,
sin embargo, `A ∼ B`."

🧠 O sea: `A ⊊ B` **no** es contraejemplo de `A ∼ B` cuando hay infinitos. Es exactamente el
paso que se falla en el parcial.

## Confusiones frecuentes

- **`⊆` vs `⪯`.** Inclusión es contención literal de elementos; `⪯` solo pide poder codificar
  sin colisiones. `A ⊆ B ⇒ A ⪯ B` pero no al revés: `N ⪯ Z` sin que `N ⊆ Z` sea el argumento.
  Ver [[definiciones/conjunto]].
- **`⪯` en las dos direcciones no es "obvio" que dé biyección.** Necesita Schröder-Bernstein,
  que el apunte cita sin probar.
- **Total e inyectiva, las dos.** Sacar "total" rompe la definición: ver
  [[definiciones/funcion]].
- 🧠 La Proposición 3 está enunciada con "si" pero la demostración prueba **las dos
  direcciones**. Leela como "si y sólo si".

## Relacionado

- [[definiciones/conjunto-infinito]] — la definición que usa `⪯` contra un subconjunto propio
- [[definiciones/numerable-y-contable]] — `∼ N` y `⪯ N`
- [[definiciones/funcion]] — inyectiva, sobreyectiva, total
- [[fuentes/notas-conjuntos]]
