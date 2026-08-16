---
id: teoria-de-la-computacion/definiciones/operaciones-con-conjuntos
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.3, revision-conjuntos p.4]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de las operaciones con conjuntos

De las seis operaciones de esta página, cuatro son las esperables y dos son las que después
hacen todo el trabajo de U6: el **conjunto potencia**, que crece exponencialmente y es el
germen del argumento de cardinalidad, y el **producto cartesiano**, del que las relaciones son
subconjuntos.

## Enunciado

Las tres primeras son las de siempre. El **tamaño o cardinalidad** es el "Número de elementos
de un conjunto", que se anota `|{1, 4}| = 2` y que más adelante habrá que redefinir cuando el
conjunto sea infinito. La **unión** es `A ∪ B = {x : x ∈ A ∨ x ∈ B}` y la **intersección**,
`A ∩ B = {x : x ∈ A ∧ xB}`.

**Eso está mal en el apunte.** La transcripción es literal —verificada contra la página
rasterizada, no es pérdida de extracción— pero le falta el `∈`. Debe leerse
`A ∩ B = {x : x ∈ A ∧ x ∈ B}`. Anotado en `wiki/dudas.md`.

La **potencia o partes** junta todos los subconjuntos en un conjunto nuevo:
`P(A) = 2^A = {B : B ⊆ A}`. Fijate que sus elementos son conjuntos, no elementos de `A`, y de
ahí sale la mitad de las confusiones de más abajo.

Las dos últimas construyen el terreno de las relaciones. Un **par o tupla ordenada** es un
"Elemento formado por una pareja de elementos" como `(1, 2)`, y a diferencia de un conjunto
"Importa el orden y la aridad". El **producto cartesiano** los junta a todos:
`A × B = {(x, y) : x ∈ A ∧ y ∈ B}`. Una relación va a ser cualquier subconjunto de esto — ver
[[definiciones/relacion]].

## Notación

| Símbolo | Operación |
|---|---|
| `\|A\|` | cardinalidad |
| `A ∪ B` · `A ∩ B` | unión · intersección |
| `P(A)` o `2^A` | conjunto potencia (dos notaciones para lo mismo) |
| `(x, y)` | par ordenado — paréntesis, no llaves |
| `A × B` | producto cartesiano |

## Ejemplo

Los tres primeros casos son directos, y el tercero es el que conviene mirar: con dos elementos
la potencia ya tiene cuatro.

```
{1, 2} ∪ {3, 1} = {1, 2, 3}
{1, 2} ∩ {3, 1} = {1}
P({1, 2}) = {∅, {1}, {2}, {1, 2}}
```

El producto cartesiano multiplica de la misma manera:
`{1, 2} × {#, !} = {(1, #), (1, !), (2, #), (2, !)}`, dos por dos igual a cuatro pares.

El apunte lista tres propiedades del conjunto potencia —`∅ ⊆ P(A)`, `∅ ∈ P(A)`, `A ∈ P(A)`— y
las tres son verdaderas por razones distintas, que es justo lo que las hace confusas.

Después deja dos preguntas abiertas: `|P(A)| = ?` "Asumiendo A finito, y por ende |A|
definido", y `A ⊆ P(A)?`. La primera es la que después importa en U6.

Respuestas: `|P(A)| = 2^|A|` —de ahí viene la notación `2^A`—, o sea que la potencia crece
exponencialmente en el tamaño del conjunto. Y `A ⊆ P(A)` es **falso** en general: exigiría que
cada elemento de `A` fuera además un subconjunto de `A`, y en `A = {1, 2}` el elemento `1` no
es un subconjunto de nada.

## Contraejemplo

El par ordenado no es un conjunto, y las dos desigualdades de abajo muestran las dos maneras
en que se separan:

```
(1, 2) ≠ (2, 1)
(1, 2) ≠ (1, 2, 2)
```

Contrastá con [[definiciones/conjunto]]: ahí `{1, 2, 2} = {2, 1}`, o sea que esas mismas dos
desigualdades serían igualdades. En los pares **el orden y la repetición sí importan**; en los
conjuntos no. Es exactamente la diferencia que hace que el producto cartesiano tenga sentido:
si los pares fueran conjuntos, `(1, 2)` y `(2, 1)` serían el mismo elemento y no se podría
distinguir "`x` está relacionado con `y`" de "`y` está relacionado con `x`".

## Confusiones frecuentes

- **`∅ ∈ P(A)` vs `∅ ⊆ P(A)`.** Las dos son verdaderas y el apunte las lista juntas a
 propósito. La primera porque `∅ ⊆ A`; la segunda porque el vacío está incluido en cualquier
 conjunto. Ver [[definiciones/conjunto]].
- **`P(A)` crece exponencial, no lineal.** `|A| = 3` da `|P(A)| = 8`. Es el germen del
 argumento de cardinalidad de U6.
- **`(x, y)` vs `{x, y}`.** Paréntesis = ordenado; llaves = conjunto.

## Relacionado

- [[definiciones/conjunto]] — pertenencia, inclusión, axioma de extensión
- [[definiciones/relacion]] — una relación es un subconjunto de un producto cartesiano
- [[fuentes/revision-conjuntos]]

## Procedencia

- **Enunciado** — revision-conjuntos p.3, p.4 · duda registrada en `dudas.md`
- **Ejemplo** — revision-conjuntos p.3, p.4 · incluye comentario del sistema
- **Contraejemplo** — revision-conjuntos p.4 · incluye comentario del sistema
- **Confusiones frecuentes** — sin cita: comentario del sistema
