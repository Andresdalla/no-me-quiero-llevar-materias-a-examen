---
id: teoria-de-la-computacion/definiciones/relacion
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.4, revision-conjuntos p.5]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de relación

## Enunciado

"Relación: Cualquier subconjunto de un producto cartesiano"

```
R ⊆ A × B
```

"A es el dominio y B el codominio"

"Cuando el dominio y codominio son iguales (`R ⊆ A × A`) se llama
relación binaria en A"

## Notación

| Símbolo | Significa |
|---|---|
| `R ⊆ A × B` | `R` es una relación de `A` en `B` |
| `(x, y) ∈ R` | `x` está relacionado con `y` |
| `R<` | la relación "menor" sobre `ℕ`, ejemplo recurrente del apunte |
| `Z`, `S n` | cero y sucesor: los constructores de `ℕ` de la cátedra |

Ojo con `Z`: en este apunte **no** son los enteros, es el constructor del **cero**. `S (S Z)`
es el 2.

## Ejemplo

"Ejemplo de Relación en ℕ Binaria: Menor"

```
R< ⊆ ℕ × ℕ
R< = {(0, 1), (0, 2) . . . (1, 2) . . . }
```

Por comprensión:
`R< = {(x, y) : x, y ∈ ℕ ∧ (∃z ∈ ℕ)(z > 0 ∧ x + z = y)}`

Por inducción:

```
(r1) n ∈ ℕ ⇒ (n, S n) ∈ R<
(r2) (n, m) ∈ R< ⇒ (n, S m) ∈ R<
```

Prueba de que `1 < 3`: por la regla base `(r1)`,
`(S Z, S (S Z)) ∈ R<`; luego aplicando la regla inductiva `(r2)`,
`(S Z, S (S (S Z))) ∈ R<`.

## Contraejemplo

`{1, 2, 3}` no es una relación sobre `ℕ`: sus elementos son números, no pares. Una relación
es un conjunto **de pares**.

`{(1, 2), 3}` tampoco: para ser subconjunto de `ℕ × ℕ` **todos** sus elementos tienen que
ser pares, y `3` no lo es.

## Confusiones frecuentes

- **Relación vs función.** Toda función es una relación, no al revés. La restricción está en
 [[definiciones/funcion]] y la notación paralela en [[comparativas/relaciones-vs-funciones]].
- **Codominio vs imagen.** El apunte define codominio (`B` entero) y no habla de imagen. No
 los mezcles: el codominio se declara, la imagen se calcula.
- **`(r2)` no dice "sumar 1 al primero".** Deja `n` fijo y avanza el segundo componente. Por
 eso `R<` no es reflexiva — ver [[definiciones/propiedades-de-relaciones]].

## Relacionado

- [[definiciones/operaciones-con-conjuntos]] — el producto cartesiano del que es subconjunto
- [[comparativas/formas-de-definir-conjuntos]] — los tres métodos, aplicados a `R<`
- [[definiciones/propiedades-de-relaciones]] · [[definiciones/operaciones-con-relaciones]]
- [[teoremas/transitividad-de-r-menor]]
- [[fuentes/revision-conjuntos]]

## Procedencia

- **Enunciado** — revision-conjuntos p.4
- **Notación** — sin cita: comentario del sistema
- **Ejemplo** — revision-conjuntos p.5
- **Contraejemplo** — sin cita: comentario del sistema
