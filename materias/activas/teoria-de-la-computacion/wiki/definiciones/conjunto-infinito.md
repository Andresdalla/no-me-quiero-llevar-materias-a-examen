---
id: teoria-de-la-computacion/definiciones/conjunto-infinito
tipo: definicion
tema: U6
fuentes: [notas-conjuntos p.3, notas-conjuntos p.4, numerabilidad-diag p.6]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de conjunto infinito

La definición de infinito que usa la cátedra es la que sorprende a todo el mundo la primera
vez: no habla de cantidad de elementos sino de que el conjunto se pueda meter adentro de una
parte de sí mismo. Es la única manera de definirlo sin contar, y contar es exactamente lo que
no se puede hacer acá.

## Enunciado

**Definición 14.** "Un conjunto A es *infinito* si existe un subconjunto propio `B ⊂ A` tal
que `A ⪯ B`." Dicho en palabras: "Un conjunto es infinito si puede codificarse dentro de una
parte propia de sí mismo."

Esta es la definición de **Dedekind-infinito**. Fijate lo que **no** dice: no dice "que no
es finito", ni "que tiene infinitos elementos". Define infinito sin contar, usando solo
funciones — que es justo lo que hace falta cuando contar no sirve.

**La otra fuente dice lo mismo, y agrega el caso finito.** **Definición 3.1 (Conjuntos
Infinitos y Finitos).** "Un conjunto A es infinito si y sólo si existe un subconjunto propio
`B ⊂ A` tal que `A ⪯ B`. **Un conjunto es finito cuando no es infinito.**" O sea que "finito"
es el término derivado, no al revés — al contrario de lo que sugiere la intuición.

Que las dos fuentes den la misma definición palabra por palabra la vuelve la más confiable
del wiki: es la que hay que saber de memoria. La segunda fuente además explicita la imagen
mental: "La intuición detrás de la definición precedente es que un conjunto es infinito si
puede "ser copiado" en su interior. (O sea, puede "codificarse a sí mismo".)"

Los dos casos extremos quedan como ejercicio `?13`: "Demostrar que: El conjunto vacío `∅` es
finito · `N` es infinito." El segundo está resuelto más abajo y sirve de plantilla para todos
los demás.

## Notación

- `B ⊂ A` acá es **subconjunto propio**: `B ⊆ A` y `B ≠ A`.
- El apunte usa `⊂` para propio en la Definición 14 y `⊊` para propio en la sección 3
 ("`N \ {0} ⊊ N`"). Dos símbolos para lo mismo en el mismo documento.

## Ejemplo

El caso base de todo lo que sigue es **Proposición 4.** "`N` es infinito." La demostración
ocupa tres renglones y consiste enteramente en exhibir la función correcta:

"Demostración. Sea `f : N → N` definida por `f(n) = n + 1`. Esta
función es inyectiva y su imagen es `N \ {0}`, que es un subconjunto propio de `N`. Por lo
tanto, `N` es infinito."

Esta es **la plantilla de toda la sección**: para probar que algo es infinito, exhibí una
inyección de él en una parte propia. No hay que hacer nada más — ni contar, ni razonar por
contradicción. La única creatividad está en elegir qué función usar.

## Contraejemplo

`{0, 1, 2}` no es infinito, y ver por qué falla muestra dónde muerde la definición: cualquier
subconjunto propio tiene a lo sumo 2 elementos, y no hay inyección total de un conjunto de 3
elementos en uno de 2 — se caería en una colisión por el principio del palomar. La definición
no encuentra el `B` que pide, y por lo tanto el conjunto es finito.

En el caso finito la definición coincide con la intuición precisamente por eso, y ahí es
donde la Observación 2 de [[definiciones/comparacion-de-cardinalidades]] deja de aplicar.

## Confusiones frecuentes

- **"Infinito" no es "no numerable".** Un conjunto infinito puede ser numerable (`N`, `Z`, `Q`)
 o no (`R`). Ver [[definiciones/numerable-y-contable]].
- **El subconjunto tiene que ser propio.** `A ⪯ A` vale siempre por la identidad; sin la
 exigencia de que `B` sea propio, todo conjunto sería infinito.
- La dirección de la inyección es `A ⪯ B` con `B ⊂ A`: se codifica **el todo dentro de la
 parte**, no al revés. Al revés es trivial y no dice nada.

## Ejercicios del apunte

**Ejercicio 1.** "Mostrar que `Z` es infinito usando una inyección de
`Z` en un subconjunto propio de `Z`."

**Ejercicio 2.** "Mostrar que `∀A infinito`, se cumple: `N ⪯ A`"

El Ejercicio 2 reaparece como Ejercicio 7 en la sección 9: el apunte lo repite, señal de que
importa. Dice que `N` es el infinito **más chico** — es lo que después justifica llamar `ℵ₀` al
menor cardinal infinito en [[definiciones/cardinales-infinitos]].

## Relacionado

- [[definiciones/comparacion-de-cardinalidades]] — `⪯`, la relación que usa esta definición
- [[definiciones/numerable-y-contable]] — infinito + contable = numerable
- [[teoremas/propiedades-de-conjuntos-infinitos]] — `N` es el infinito más chico, y el caso finito
- [[fuentes/notas-conjuntos]] · [[fuentes/numerabilidad-diag]]

## Procedencia

- **Enunciado** — notas-conjuntos p.3 · numerabilidad-diag p.6 · incluye comentario del sistema
- **Notación** — sin cita · duda: El apunte usa `⊂` para propio en la Definición 14 y `⊊` para propio en la sección 3
- **Ejemplo** — notas-conjuntos p.3 · incluye comentario del sistema
- **Contraejemplo** — sin cita: comentario del sistema
- **Confusiones frecuentes** — sin cita: comentario del sistema
- **Ejercicios del apunte** — notas-conjuntos p.3 · incluye comentario del sistema
