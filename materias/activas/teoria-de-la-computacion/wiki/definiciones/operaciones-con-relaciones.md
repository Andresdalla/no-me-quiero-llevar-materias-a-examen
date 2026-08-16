---
id: teoria-de-la-computacion/definiciones/operaciones-con-relaciones
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.8]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de las operaciones con relaciones

Como una relación es un conjunto de pares, se la puede manipular con operaciones propias. Las
dos que importan son dar vuelta los pares y encadenar dos relaciones. La segunda es la que
después reaparece disfrazada en la composición de funciones, con la notación invertida, y ese
es el error más caro de toda la unidad.

## Enunciado

La **relación inversa** es simplemente dar vuelta todos los pares:
`R⁻¹ = {(x, y) : (y, x) ∈ R}`. Siempre existe, sin condiciones, porque no se le pide nada a
`R`: un conjunto de pares dado vuelta sigue siendo un conjunto de pares.

La **composición** sí exige que los conjuntos encastren, y por eso el apunte la enuncia
declarando los tres: "Sean `R ⊆ A × B` y `S ⊆ B × C`:". El `B` tiene que ser el mismo de los
dos lados, y es lo que permite usar el `y` intermedio como puente entre `x` y `z`.

```
R ∘ S = {(x, z) : (x, y) ∈ R ∧ (y, z) ∈ S}
```

## Notación

| Símbolo | Operación |
|---|---|
| `R⁻¹` | relación inversa |
| `R ∘ S` | composición: **primero `R`, después `S`** |

**Ojo con el orden.** Para relaciones la cátedra escribe `R ∘ S` aplicando `R` primero.
Para funciones invierte la notación: la tabla pone `R ∘ S` del lado de relaciones y `s ∘ r`
del lado de funciones. No es un descuido del apunte sino la convención habitual en cada
contexto, pero significa que el mismo símbolo `∘` se lee al revés según de qué estés hablando.
Ver [[comparativas/relaciones-vs-funciones]].

## Ejemplo

El apunte plantea tres ejercicios y **no los resuelve**: `R⁻¹< = ?`, `R< ∘ R< = ?`,
`R< ∘ R< ∘ R< = ?`. Sirven para ver que componer una relación consigo misma la va endureciendo.

Resoluciones inferidas, no oficiales:

- `R⁻¹<` es `R>`: los pares dados vuelta, o sea la relación "mayor".
- `R< ∘ R<` es "hay al menos dos pasos de menor entre `x` y `z`", es decir `x + 2 ≤ z`.
- `R< ∘ R< ∘ R<` es `x + 3 ≤ z`.

El patrón es que cada composición extra pide un paso más de distancia. Y como `x + 2 ≤ z`
implica `x < z`, resulta que `R< ∘ R< ⊆ R<`, que es exactamente lo que dice
[[teoremas/transitividad-de-r-menor]]: componer no te saca de la relación.

## Contraejemplo

La composición **no es conmutativa**, y el motivo es más fuerte que "da distinto": con
`R ⊆ A × B` y `S ⊆ B × C`, `S ∘ R` puede ni siquiera estar definida, porque el codominio de
`S` no tiene por qué coincidir con el dominio de `R`. Antes de preguntarse si el resultado
cambia hay que preguntarse si la expresión existe.

La inversa, que para relaciones siempre existe, **no siempre devuelve una función**: ver
[[definiciones/funcion]], donde el apunte aclara que "La inversa sólo es cerrada cuando la
función es inyectiva". Es el precio de que una función sea un caso particular de relación —
hereda la operación, pero no la garantía de quedarse adentro del caso particular.

## Confusiones frecuentes

- **`R⁻¹` no es "uno sobre R"** ni requiere que `R` sea invertible como función. Para
 relaciones siempre existe: es dar vuelta todos los pares.
- **El orden de la composición** es el error más caro, porque cambia según hables de
 relaciones o de funciones. Ver [[comparativas/relaciones-vs-funciones]].
- **Componer no preserva propiedades.** Que `R` sea reflexiva no dice nada de `R ∘ S`. Ver
 [[definiciones/propiedades-de-relaciones]].

## Relacionado

- [[definiciones/relacion]] — qué es una relación
- [[definiciones/funcion]] — las funciones heredan estas operaciones
- [[comparativas/relaciones-vs-funciones]] — la notación paralela y su trampa
- [[fuentes/revision-conjuntos]]

## Procedencia

- **Enunciado** — revision-conjuntos p.8
- **Notación** — revision-conjuntos p.9 · duda registrada en `dudas.md`
- **Ejemplo** — revision-conjuntos p.8 · incluye comentario del sistema
- **Contraejemplo** — sin cita: comentario del sistema
