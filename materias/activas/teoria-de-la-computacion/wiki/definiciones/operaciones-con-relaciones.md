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

## Enunciado

**Relación inversa.** ✅ [revision-conjuntos p.8] `R⁻¹ = {(x, y) : (y, x) ∈ R}`

**Composición.** ✅ [revision-conjuntos p.8] "Sean `R ⊆ A × B` y `S ⊆ B × C`:"

```
R ∘ S = {(x, z) : (x, y) ∈ R ∧ (y, z) ∈ S}
```

## Notación

| Símbolo | Operación |
|---|---|
| `R⁻¹` | relación inversa |
| `R ∘ S` | composición: **primero `R`, después `S`** |

⚠️ **Ojo con el orden.** Para relaciones la cátedra escribe `R ∘ S` aplicando `R` primero.
Para funciones invierte la notación: ✅ [revision-conjuntos p.9] la tabla pone `R ∘ S` del lado
de relaciones y `s ∘ r` del lado de funciones. Ver
[[comparativas/relaciones-vs-funciones]].

## Ejemplo

✅ [revision-conjuntos p.8] El apunte plantea tres ejercicios y **no los resuelve**:
`R⁻¹< = ?`, `R< ∘ R< = ?`, `R< ∘ R< ∘ R< = ?`

🧠 Resoluciones inferidas, no oficiales:

- `R⁻¹<` es `R>`: los pares dados vuelta, o sea la relación "mayor".
- `R< ∘ R<` es "hay al menos dos pasos de menor entre `x` y `z`", es decir `x + 2 ≤ z`.
- `R< ∘ R< ∘ R<` es `x + 3 ≤ z`.

🧠 Que `R< ∘ R< ⊆ R<` es exactamente lo que dice
[[teoremas/transitividad-de-r-menor]]: componer no te saca de la relación.

## Contraejemplo

🧠 La composición **no es conmutativa**: con `R ⊆ A × B` y `S ⊆ B × C`, `S ∘ R` puede ni
siquiera estar definida, porque el codominio de `S` no tiene por qué coincidir con el dominio
de `R`.

🧠 La inversa **no siempre devuelve una función**: ver [[definiciones/funcion]], donde el
apunte aclara que "La inversa sólo es cerrada cuando la función es inyectiva".

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
