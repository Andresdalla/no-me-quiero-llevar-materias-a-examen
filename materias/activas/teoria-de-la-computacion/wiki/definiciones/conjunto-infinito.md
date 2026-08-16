---
id: teoria-de-la-computacion/definiciones/conjunto-infinito
tipo: definicion
tema: U6
fuentes: [notas-conjuntos p.3, notas-conjuntos p.4]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de conjunto infinito

## Enunciado

✅ [notas-conjuntos p.3] **Definición 14.** "Un conjunto A es *infinito* si existe un
subconjunto propio `B ⊂ A` tal que `A ⪯ B`."

✅ [notas-conjuntos p.3] Idea intuitiva: "Un conjunto es infinito si puede codificarse dentro
de una parte propia de sí mismo."

🧠 Esta es la definición de **Dedekind-infinito**. Fijate lo que **no** dice: no dice "que no
es finito", ni "que tiene infinitos elementos". Define infinito sin contar, usando solo
funciones — que es justo lo que hace falta cuando contar no sirve.

## Notación

- `B ⊂ A` acá es **subconjunto propio**: `B ⊆ A` y `B ≠ A`.
- ⚠️ El apunte usa `⊂` para propio en la Definición 14 y `⊊` para propio en la sección 3
  ("`N \ {0} ⊊ N`"). Dos símbolos para lo mismo en el mismo documento.

## Ejemplo

✅ [notas-conjuntos p.3] **Proposición 4.** "`N` es infinito."

✅ [notas-conjuntos p.3] "Demostración. Sea `f : N → N` definida por `f(n) = n + 1`. Esta
función es inyectiva y su imagen es `N \ {0}`, que es un subconjunto propio de `N`. Por lo
tanto, `N` es infinito."

🧠 Esta es **la plantilla de toda la sección**: para probar que algo es infinito, exhibí una
inyección de él en una parte propia. No hay que hacer nada más.

## Contraejemplo

🧠 `{0, 1, 2}` no es infinito: cualquier subconjunto propio tiene a lo sumo 2 elementos, y no
hay inyección total de un conjunto de 3 elementos en uno de 2 — se caería en una colisión por
el principio del palomar.

🧠 En el caso finito la definición coincide con la intuición precisamente por eso, y ahí es
donde la Observación 2 de [[definiciones/comparacion-de-cardinalidades]] deja de aplicar.

## Confusiones frecuentes

- **"Infinito" no es "no numerable".** Un conjunto infinito puede ser numerable (`N`, `Z`, `Q`)
  o no (`R`). Ver [[definiciones/numerable-y-contable]].
- **El subconjunto tiene que ser propio.** `A ⪯ A` vale siempre por la identidad; sin la
  exigencia de que `B` sea propio, todo conjunto sería infinito.
- 🧠 La dirección de la inyección es `A ⪯ B` con `B ⊂ A`: se codifica **el todo dentro de la
  parte**, no al revés. Al revés es trivial y no dice nada.

## Ejercicios del apunte

✅ [notas-conjuntos p.3] **Ejercicio 1.** "Mostrar que `Z` es infinito usando una inyección de
`Z` en un subconjunto propio de `Z`."

✅ [notas-conjuntos p.3] **Ejercicio 2.** "Mostrar que `∀A infinito`, se cumple: `N ⪯ A`"

🧠 El Ejercicio 2 reaparece como Ejercicio 7 en la sección 9: el apunte lo repite, señal de que
importa. Dice que `N` es el infinito **más chico** — es lo que después justifica llamar `ℵ₀` al
menor cardinal infinito en [[definiciones/cardinales-infinitos]].

## Relacionado

- [[definiciones/comparacion-de-cardinalidades]] — `⪯`, la relación que usa esta definición
- [[definiciones/numerable-y-contable]] — infinito + contable = numerable
- [[fuentes/notas-conjuntos]]
