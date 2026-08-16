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

Una relación no es un objeto nuevo: es un conjunto, y todo lo de
[[definiciones/conjunto]] le sigue valiendo. Lo único que se agrega es la exigencia de que sus
elementos sean pares, y de ahí sale todo lo demás — propiedades, órdenes y, más adelante,
funciones.

## Enunciado

La definición es deliberadamente amplia: "Relación: Cualquier subconjunto de un producto
cartesiano". No pide ninguna condición sobre qué pares están y cuáles no, así que cualquier
colección de pares sirve, incluso el conjunto vacío.

```
R ⊆ A × B
```

Los dos conjuntos que arman el producto tienen nombre: "A es el dominio y B el codominio". El
caso que más se usa en la materia es aquel en el que coinciden, porque es el único donde tiene
sentido preguntar si un elemento se relaciona consigo mismo: "Cuando el dominio y codominio
son iguales (`R ⊆ A × A`) se llama relación binaria en A". Todas las propiedades de
[[definiciones/propiedades-de-relaciones]] se definen sobre este caso.

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

El apunte usa una sola relación de ejemplo en toda la unidad, "Ejemplo de Relación en ℕ
Binaria: Menor", y la define de las tres maneras de
[[comparativas/formas-de-definir-conjuntos]]. Vale la pena verlas juntas porque es el caso
donde se ve para qué sirve cada método.

Por extensión queda incompleta, y eso es justamente lo que muestra que el método no alcanza
para conjuntos infinitos:

```
R< ⊆ ℕ × ℕ
R< = {(0, 1), (0, 2) . . . (1, 2) . . . }
```

Por comprensión ya queda cerrada, apoyándose en `ℕ` y en la suma:
`R< = {(x, y) : x, y ∈ ℕ ∧ (∃z ∈ ℕ)(z > 0 ∧ x + z = y)}`.

Por inducción no hace falta nada previo, solo los constructores, y aparecen las dos reglas que
después se usan en la demostración de transitividad:

```
(r1) n ∈ ℕ ⇒ (n, S n) ∈ R<
(r2) (n, m) ∈ R< ⇒ (n, S m) ∈ R<
```

Con esas reglas cada elemento de `R<` se justifica construyéndolo, y ese árbol de construcción
es sobre lo que después se induce. Prueba de que `1 < 3`: por la regla base `(r1)`,
`(S Z, S (S Z)) ∈ R<`; luego aplicando la regla inductiva `(r2)`, `(S Z, S (S (S Z))) ∈ R<`.

## Contraejemplo

`{1, 2, 3}` no es una relación sobre `ℕ`: sus elementos son números, no pares. Una relación
es un conjunto **de pares**, y la definición no admite excepciones.

`{(1, 2), 3}` tampoco, y es el caso más engañoso porque parece que "casi" cumple: para ser
subconjunto de `ℕ × ℕ` **todos** sus elementos tienen que ser pares, y `3` no lo es. Alcanza
con un elemento fuera de lugar para que el conjunto entero deje de ser una relación.

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
