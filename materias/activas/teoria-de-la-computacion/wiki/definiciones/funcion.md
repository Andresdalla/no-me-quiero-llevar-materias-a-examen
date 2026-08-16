---
id: teoria-de-la-computacion/definiciones/funcion
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.9, revision-conjuntos p.10]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de función y sus propiedades

## Enunciado

✅ [revision-conjuntos p.9] "Funciones · Caso especial de relaciones · Donde cada elemento del
dominio está relacionado con **a lo sumo un** elemento del codominio"

**Parciales vs totales.** ✅ [revision-conjuntos p.9] "Si están o no definidas para todos los
elementos en el dominio" — `Total f : A → B` · `Parcial f : A ⇸ B`

**Inyectiva.** ✅ [revision-conjuntos p.9] `(∀x, y ∈ A)(x ≠ y ⇒ f(x) ≠ f(y))`

**Sobreyectiva.** ✅ [revision-conjuntos p.9] `(∀y ∈ B)(∃x ∈ A)(f(x) = y)`

**Biyectiva.** ✅ [revision-conjuntos p.10] "Si es inyectiva y sobreyectiva"

## Notación

| Símbolo | Significa |
|---|---|
| `f : A → B` | función **total** |
| `f : A ⇸ B` | función **parcial** (flecha con barra) |
| `f(x) = y` | equivale a `(x, y) ∈ f` |

🧠 El "a lo sumo uno" del enunciado es lo que deja lugar a las parciales: si fuera "exactamente
uno", toda función sería total por definición.

## Ejemplo

✅ [revision-conjuntos p.9] Inyectiva: `f : ℕ → ℕ, f(x) = x + 1`

✅ [revision-conjuntos p.9] Sobreyectiva: `f : ℕ → ℕ, f(x) = x`

✅ [revision-conjuntos p.10] Propiedades de las biyectivas: "La función inversa existe y es
total" · "Si la función es además total, entonces es sobreyectiva también"

✅ [revision-conjuntos p.9] Propiedad de las inyectivas: "Existe la función inversa si y sólo
si es inyectiva"

✅ [revision-conjuntos p.10] Operaciones: "Al ser casos especiales de relaciones heredan todas
las operaciones de relaciones". "La unión no es cerrada, esto es, a veces el resultado deja de
ser función". "La inversa sólo es cerrada cuando la función es inyectiva."

## Contraejemplo

🧠 `f : ℕ → ℕ, f(x) = x + 1` **no es sobreyectiva**: ningún `x` da `f(x) = 0`. Sirve de
contraejemplo justo del ejemplo de al lado, que sí lo es.

🧠 La unión de dos funciones que no es función: `f = {(1, 2)}` y `g = {(1, 3)}` son funciones,
pero `f ∪ g = {(1, 2), (1, 3)}` relaciona el `1` con dos elementos. Es el caso al que apunta
"la unión no es cerrada".

## Confusiones frecuentes

- **Inyectiva vs sobreyectiva.** Inyectiva mira el **dominio** (no repetir salidas);
  sobreyectiva mira el **codominio** (cubrirlo entero). Se confunden porque las dos empiezan
  con un `∀`, pero uno cuantifica sobre `A` y el otro sobre `B`.
- **Total vs sobreyectiva.** Total es "definida para todo `x` del dominio"; sobreyectiva es
  "alcanza todo `y` del codominio". Son lados opuestos. 🧠 El apunte las conecta solo en el
  caso biyectivo.
- **Función es un caso de relación.** Todo lo de [[definiciones/operaciones-con-relaciones]]
  vale, pero la notación cambia: ver [[comparativas/relaciones-vs-funciones]].
- 🧠 Inyectiva y sobreyectiva son exactamente lo que se necesita para **comparar tamaños de
  conjuntos**, que es a lo que va U6.

## Relacionado

- [[comparativas/relaciones-vs-funciones]] — la tabla de notación paralela
- [[definiciones/relacion]] · [[definiciones/operaciones-con-relaciones]]
- [[fuentes/revision-conjuntos]]
