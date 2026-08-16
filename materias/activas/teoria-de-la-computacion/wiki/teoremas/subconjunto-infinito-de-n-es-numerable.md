---
id: teoria-de-la-computacion/teoremas/subconjunto-infinito-de-n-es-numerable
tipo: teorema
tema: U6
fuentes: [notas-conjuntos p.4]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Todo subconjunto infinito de `N` es numerable

## Enunciado

**Teorema 1.** "Todo subconjunto infinito de `N` es numerable."

## Hipótesis

- `S ⊆ N`
- `S` es infinito
- Implícita y esencial: **todo subconjunto no vacío de `N` tiene mínimo** (buen orden de
 `N`). El apunte la usa explícitamente y no la demuestra.

## Demostración

"Sea `S ⊆ N` un subconjunto infinito. Como todo subconjunto no vacío
de `N` tiene mínimo, definimos inductivamente una sucesión estrictamente creciente `(sₙ)ₙ∈N` de
elementos de S así:"

```
s₀ = mín(S)
sₙ₊₁ = mín(S \ {s₀, …, sₙ})
```

"Esto está bien definido porque S es infinito y, por lo tanto, al
remover finitamente muchos elementos aún queda un conjunto no vacío. La función `f : N → S`
dada por `f(n) = sₙ` es biyectiva: es inyectiva por construcción, y sobreyectiva porque todo
elemento de S aparece en algún paso del procedimiento. Por consiguiente, S es numerable."

## Cuándo se aplica

Es la pieza que le falta a la **Proposición 6** ("si A es contable e infinito, entonces A es
numerable"): el apunte la usa antes de probarla, diciendo "Veremos más adelante que todo
subconjunto infinito de `N` es numerable". Sin este teorema, esa proposición queda colgada.

En la práctica es lo que te habilita a **construir una inyección en vez de una biyección**.
Casi todos los ejercicios de numerabilidad se resuelven así: inyectás en `N`, mostrás que el
conjunto es infinito, y este teorema te devuelve la biyección.

## Errores típicos

- **Saltear la hipótesis de infinitud.** Sin ella, `mín(S \ {s₀, …, sₙ})` puede no existir
 porque el conjunto se vacía. Un `S` finito rompe la construcción en el paso `|S|`.
- **Dar la sobreyectividad por obvia.** Que todo elemento de `S` aparezca "en algún paso"
 usa que la sucesión es **estrictamente creciente**: si `s ∈ S`, hay a lo sumo finitos
 elementos de `S` menores que `s`, así que `s` se alcanza en tiempo finito.
- **Confundir "está bien definido" con "es sobreyectiva".** Son dos cosas distintas y el
 apunte las argumenta por separado.

## Relacionado

- [[definiciones/numerable-y-contable]] — Proposición 6, que depende de este teorema
- [[definiciones/conjunto-infinito]] — la hipótesis
- [[definiciones/comparacion-de-cardinalidades]]
- [[fuentes/notas-conjuntos]]

## Procedencia

- **Enunciado** — notas-conjuntos p.4
- **Hipótesis** — notas-conjuntos p.4 · incluye comentario del sistema
- **Demostración** — notas-conjuntos p.4
- **Cuándo se aplica** — sin cita: comentario del sistema
- **Errores típicos** — sin cita: comentario del sistema
