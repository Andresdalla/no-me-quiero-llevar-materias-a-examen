---
id: teoria-de-la-computacion/definiciones/funcion
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.9, revision-conjuntos p.10, notas-conjuntos p.2]
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

### Las dos fuentes no usan la misma notación

⚠️ **Conflicto de notación entre los dos apuntes de la materia.** La propia cátedra lo
advierte: ✅ [notas-conjuntos p.2] **Observación 1.** "Tener cuidado que diferentes docentes
pueden usar notaciones diferentes".

| Concepto | `revision-conjuntos` p.9 | `notas-conjuntos` p.2 |
|---|---|---|
| función parcial | `f : A ⇸ B` | `f : A ↬ B` ✅ **Definición 6** |
| función total | `f : A → B` | `f : A → B` ✅ **Definición 7** |
| inyección (inyectiva **y total**) | — | `f : A ↪ B` ✅ **Definición 9** |
| sobreyección (sobreyectiva **y total**) | — | `f : A →\| B` ✅ **Definición 10** |
| biyección (biyectiva **y total**) | — | `f : A ↔ B` ✅ **Definición 11** |

🧠 La diferencia importante no es el dibujo de la flecha: `notas-conjuntos` introduce los
términos **inyección / sobreyección / biyección** como "inyectiva/sobreyectiva/biyectiva **+
total**". O sea, *inyectiva* y *inyección* no son sinónimos ahí. En el parcial con material,
tené a mano de qué apunte viene la notación que estés usando.

⚠️ Las dos fuentes definen **inyectiva** de forma distinta pero equivalente:
`revision-conjuntos` p.9 usa `(∀x, y ∈ A)(x ≠ y ⇒ f(x) ≠ f(y))`; ✅ [notas-conjuntos p.2]
**Definición 8** usa `f(a₁) = f(a₂) ⇒ a₁ = a₂`. Son contrarrecíprocas: no hay contradicción,
pero conviene saber demostrar con las dos.

🧠 ✅ [notas-conjuntos p.2] La lectura computacional que agrega esta fuente: "las funciones
parciales modelan programas que **pueden no terminar**, mientras que las funciones totales
modelan programas que siempre producen una salida". Esa frase es el puente entre U6 y el
problema de la terminación de U7.

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
- [[definiciones/comparacion-de-cardinalidades]] — para qué se usan inyectiva y biyectiva en U6
- [[fuentes/revision-conjuntos]] · [[fuentes/notas-conjuntos]]
