---
id: teoria-de-la-computacion/definiciones/conjunto
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.1, revision-conjuntos p.2]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Definición de conjunto, pertenencia e inclusión

Esta es la página de la que cuelga todo U6. Las definiciones de acá son pocas y parecen
triviales, pero el axioma de extensión y la diferencia entre `∈` y `⊆` son exactamente lo que
después se usa para comparar conjuntos infinitos, y es donde más gente se equivoca en el
parcial.

## Enunciado

El punto de partida es deliberadamente informal: "Un conjunto es una colección de elementos".
La teoría no dice qué es un elemento ni de dónde salen; lo único que se define es la relación
entre un elemento y el conjunto: "Pertenencia: x es un elemento del conjunto A", que se anota
`x ∈ A`. El caso extremo lo nombra el apunte como "Conjunto vacío", `∅ = {}`, que no tiene
ninguno.

Lo que le da contenido a la teoría es el **axioma de extensión**: "Dos conjuntos son iguales
si y sólo si tienen los mismos elementos". Es una decisión fuerte, porque implica que un
conjunto **no tiene otra identidad que sus elementos** — ni orden, ni repeticiones, ni nombre.
De ahí sale la **inclusión amplia**, `A ⊆ B ⇔ (∀x ∈ A)(x ∈ B)`, que es la versión "una
dirección sola" de esa igualdad.

Las tres propiedades que siguen son consecuencia directa y conviene tenerlas a mano, porque
la primera es la que se usa en casi toda demostración de igualdad de conjuntos: se prueba una
inclusión, después la otra.

```
A = B ⇔ A ⊆ B ∧ B ⊆ A
A ⊆ A
∅ ⊆ A
```

## Notación

La cátedra usa muy pocos símbolos acá, y la ausencia de uno importa tanto como la presencia
de los otros.

| Símbolo | Significa |
|---|---|
| `x ∈ A` | `x` pertenece a `A` |
| `∅` | conjunto vacío, igual a `{}` |
| `A ⊆ B` | inclusión amplia (permite `A = B`) |

La cátedra usa **`⊆` para la inclusión amplia** y no introduce un símbolo separado para la
inclusión estricta en este apunte. O sea que `A ⊆ B` no te dice si `A` es más chico que `B` o
si son el mismo conjunto: si necesitás la inclusión estricta, la tenés que escribir a mano
como `A ⊆ B ∧ A ≠ B`.

## Ejemplo

El caso base es `1 ∈ {1, 2, 3}`: un número pertenece a un conjunto que lo contiene. Lo
interesante empieza cuando se aplica el axioma de extensión, porque de él se sigue que ni el
orden ni la repetición importan — dos escrituras distintas nombran el mismo conjunto siempre
que tengan los mismos elementos.

```
{1, 2, 2} = {2, 1}
{{1, 2, 2}, 2} = {2, {2, 1}}
```

La segunda línea es la que vale la pena mirar dos veces: adentro pasa lo mismo que afuera,
porque `{1,2,2}` y `{2,1}` son el mismo conjunto y por lo tanto el mismo elemento. Para la
inclusión, `{1} ⊆ {2, 1}` ilustra el otro lado: todo elemento del de la izquierda está en el
de la derecha, aunque no sean iguales.

## Contraejemplo

`{{1, 2}} ≠ {1, 2}`. El de la izquierda tiene **un** elemento (que es un conjunto); el de la
derecha tiene **dos** (que son números). El axioma de extensión los separa porque no comparten
elementos, y es el mismo axioma que arriba hacía coincidir cosas que se escribían distinto:
lo único que mira es qué hay adentro.

El apunte deja abierta la pregunta `{{1, 2}} ⊆ {1, 2}?`, que es el contraste exacto del
ejemplo `{1} ⊆ {2, 1}`. La respuesta es **no**: para que valiera, el único elemento de la
izquierda —el conjunto `{1,2}`— tendría que pertenecer a `{1,2}`, y los elementos de `{1,2}`
son `1` y `2`, no `{1,2}`. Un nivel de llaves de más y la inclusión se rompe.

## Confusiones frecuentes

Las tres de abajo son la misma confusión vista desde ángulos distintos: perder de vista en
qué nivel de anidamiento estás parado.

- **`∈` vs `⊆`.** `∈` relaciona un elemento con un conjunto; `⊆` relaciona dos conjuntos.
 `1 ∈ {1,2}` pero `1 ⊆ {1,2}` no tiene sentido; `{1} ⊆ {1,2}` sí.
- Esta confusión es la que hace fallar las preguntas sobre
 [[definiciones/operaciones-con-conjuntos]] en el conjunto potencia: `∅ ∈ P(A)` **y**
 `∅ ⊆ P(A)` son las dos verdaderas, por motivos distintos.
- **Anidamiento.** `{{1,2}}` no es `{1,2}`. Contar niveles de llaves antes de responder es el
 hábito que evita los tres errores.

## Relacionado

- [[comparativas/formas-de-definir-conjuntos]] — las tres maneras de dar un conjunto
- [[definiciones/operaciones-con-conjuntos]] — unión, intersección, potencia, producto
- [[fuentes/revision-conjuntos]]

## Procedencia

- **Enunciado** — revision-conjuntos p.1, p.2 · incluye comentario del sistema
- **Notación** — sin cita: comentario del sistema
- **Ejemplo** — revision-conjuntos p.1, p.2 · incluye comentario del sistema
- **Contraejemplo** — revision-conjuntos p.1, p.2 · incluye comentario del sistema
- **Confusiones frecuentes** — sin cita: comentario del sistema
