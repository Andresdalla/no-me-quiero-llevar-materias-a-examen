---
id: teoria-de-la-computacion/definiciones/funcion
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.9, revision-conjuntos p.10]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Definición de función y sus propiedades

Una función no es un objeto nuevo sino una relación con una restricción encima, y por eso
hereda todo lo de [[definiciones/operaciones-con-relaciones]]. Las cuatro propiedades que se
definen acá —total, inyectiva, sobreyectiva, biyectiva— son exactamente las que después se
usan para comparar tamaños de conjuntos infinitos, que es a lo que va toda U6.

Las tres fuentes de la materia notan esto de tres maneras distintas y en un caso hasta con
distinto significado: eso está en [[comparativas/notacion-de-funciones]] y conviene mirarlo
antes del parcial.

## Enunciado

La definición se apoya en la de relación y le agrega una sola condición: "Funciones · Caso
especial de relaciones · Donde cada elemento del dominio está relacionado con **a lo sumo un**
elemento del codominio". El "a lo sumo uno" es lo que deja lugar a las parciales: si dijera
"exactamente uno", toda función sería total por definición y no habría nada más que decir.

De ahí sale la primera distinción, que mira el **dominio**: si están o no definidas en todos
sus puntos. El apunte lo enuncia como "Si están o no definidas para todos los elementos en el
dominio", y le da un símbolo a cada caso — `Total f : A → B` · `Parcial f : A ⇸ B`.

Las otras tres propiedades miran cómo se reparte el **codominio**. Es inyectiva cuando
`(∀x, y ∈ A)(x ≠ y ⇒ f(x) ≠ f(y))`, o sea cuando no colapsa dos entradas distintas en la misma
salida. Es sobreyectiva cuando `(∀y ∈ B)(∃x ∈ A)(f(x) = y)`: no sobra nada del codominio.
Biyectiva es la conjunción de las dos, "Si es inyectiva y sobreyectiva", y es la que habilita
que exista la inversa — el punto de contacto con
[[definiciones/comparacion-de-cardinalidades]].

## Notación

| Símbolo | Significa |
|---|---|
| `f : A → B` | función **total** |
| `f : A ⇸ B` | función **parcial** (flecha con barra) |
| `f(x) = y` | equivale a `(x, y) ∈ f` |

La última fila es la que recuerda de dónde viene todo esto: escribir `f(x) = y` es una
comodidad para no escribir el par, pero la función sigue siendo un conjunto de pares.

La cátedra no usa una sola notación para esto. Las divergencias entre los tres apuntes, y la
convención de `numerabilidad-diag` donde la palabra "función" significa función **parcial**,
están en [[comparativas/notacion-de-funciones]].

## Ejemplo

Los dos ejemplos que da el apunte sobre `ℕ` son el par mínimo para separar las dos
propiedades. `f : ℕ → ℕ, f(x) = x + 1` es inyectiva: sumarle uno a dos números distintos da
dos resultados distintos, así que nunca colapsa dos entradas. `f : ℕ → ℕ, f(x) = x` es
sobreyectiva, porque todo `y` es imagen de sí mismo.

Sobre las biyectivas el apunte enuncia dos propiedades encadenadas: "La función inversa existe
y es total", y "Si la función es además total, entonces es sobreyectiva también". La primera
es la que importa para U6, porque es lo que permite dar vuelta una biyección y usarla en la
otra dirección. Para el caso más débil vale la versión con condición: "Existe la función
inversa si y sólo si es inyectiva" — la sobreyectividad no hace falta para invertir, solo la
inyectividad.

Como "Al ser casos especiales de relaciones heredan todas las operaciones de relaciones", todo
lo de [[definiciones/operaciones-con-relaciones]] se puede aplicar acá. Lo que no se hereda es
la clausura: "La unión no es cerrada, esto es, a veces el resultado deja de ser función",
porque unir dos funciones puede relacionar una entrada con dos salidas. La otra operación
heredada tiene su propia condición: "La inversa sólo es cerrada cuando la función es
inyectiva." Es exactamente lo que evita el mismo problema al dar vuelta los pares.

## Contraejemplo

`f : ℕ → ℕ, f(x) = x + 1` **no es sobreyectiva**: ningún `x` da `f(x) = 0`. Sirve de
contraejemplo justo del ejemplo de al lado, que sí lo es, y muestra que las dos propiedades
son independientes — la misma función cumple una y falla la otra.

El caso de la unión que deja de ser función se ve con dos funciones de un solo par:
`f = {(1, 2)}` y `g = {(1, 3)}` son funciones, pero `f ∪ g = {(1, 2), (1, 3)}` relaciona el `1`
con dos elementos y por lo tanto viola el "a lo sumo uno" del enunciado. Es el caso al que
apunta "la unión no es cerrada".

## Confusiones frecuentes

Las dos primeras son la misma confusión: no tener presente sobre qué conjunto cuantifica cada
propiedad.

- **Inyectiva vs sobreyectiva.** Inyectiva mira el **dominio** (no repetir salidas);
 sobreyectiva mira el **codominio** (cubrirlo entero). Se confunden porque las dos empiezan
 con un `∀`, pero uno cuantifica sobre `A` y el otro sobre `B`.
- **Total vs sobreyectiva.** Total es "definida para todo `x` del dominio"; sobreyectiva es
 "alcanza todo `y` del codominio". Son lados opuestos. El apunte las conecta solo en el
 caso biyectivo.
- **Función es un caso de relación.** Todo lo de [[definiciones/operaciones-con-relaciones]]
 vale, pero la notación cambia: ver [[comparativas/relaciones-vs-funciones]].
- Inyectiva y sobreyectiva son exactamente lo que se necesita para **comparar tamaños de
 conjuntos**, que es a lo que va U6.

## Relacionado

- [[comparativas/notacion-de-funciones]] — las tres notaciones de la cátedra y sus conflictos
- [[comparativas/relaciones-vs-funciones]] — la tabla de notación paralela
- [[definiciones/relacion]] · [[definiciones/operaciones-con-relaciones]]
- [[definiciones/comparacion-de-cardinalidades]] — para qué se usan inyectiva y biyectiva en U6
- [[fuentes/revision-conjuntos]]

## Procedencia

- **Enunciado** — revision-conjuntos p.9, p.10 · incluye comentario del sistema
- **Notación** — sin cita: comentario del sistema
- **Ejemplo** — revision-conjuntos p.9, p.10 · incluye comentario del sistema
- **Contraejemplo** — sin cita: comentario del sistema
- **Confusiones frecuentes** — sin cita: comentario del sistema
