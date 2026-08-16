---
id: teoria-de-la-computacion/comparativas/lambda-case-vs-pattern-matching
tipo: comparativa
tema: U10
fuentes: [repaso-haskell p.1-3]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# λ-notation y case vs Pattern-Matching y guardas

Las dos formas de escribir la misma función en Haskell. En otra materia sería una cuestión de
gusto; acá es una consigna literal y repetida, y la pide para **cada** función del repartido:

"Para cada una de las funciones de este repartido se les pedirá
definirlas utilizando:
- λ − notation y case.
- Pattern-Matching y guardas."

No son dos estilos entre los que elegís: la cátedra pide **las dos para la misma función**.
Lo que hay que tener automatizado, entonces, no es cuál conviene sino cómo se traduce una en
la otra sin pensar.

## Tabla

| Criterio | λ-notation y case | Pattern-Matching y guardas |
|---|---|---|
| Forma de la definición | **una** ecuación: `f = λx -> ...` | **varias** ecuaciones, una por patrón |
| Dónde se analizan los casos | dentro, en un `case ... of {...}` | afuera, en la cabeza de cada ecuación |
| Argumentos | anónimos, atados por el `λ` | nombrados en cada patrón |
| Nombre de la función | aparece 1 vez (+1 en la firma) | aparece 1 vez por caso |
| Relación con el cálculo λ | directa: es una λ-abstracción | azúcar sintáctico sobre la anterior |
| Separador de casos | `;` dentro de las llaves | salto de línea |

## Criterio de decisión

Lo que decide es **de dónde viene el análisis de casos**: si el `data` te da constructores
(`True`/`False`, `[]`/`(:)`, `Hoja`/`Nodo`), hay un caso por constructor y las dos formas
tienen exactamente la misma cantidad de ramas. Traducir es mecánico:

- cada rama `patrón -> cuerpo` del `case` ⇄ una ecuación `f patrón = cuerpo`.

## Cuándo elegir cada uno

- Usá **λ + case** cuando tengas que conectar con el cálculo λ (U3) o cuando la función
 sea el argumento de otra (no necesita nombre).
- Usá **pattern-matching** cuando haya muchos constructores: se lee por casos y no se te
 pierde ninguno.
- En el parcial y en las defensas, **asumí que te piden las dos** salvo que diga otra cosa:
 es la consigna literal del repartido.

## Los cuatro ejemplos resueltos por la cátedra

Son las únicas cuatro funciones con respuesta oficial. Todo lo demás son consignas.

Bool:

```haskell
not :: Bool -> Bool
not = λb -> case b of {True -> False; False -> True}

not :: Bool -> Bool
not True = False
not False = True
```

Integer:

```haskell
sumi :: Integer -> Integer
sumi = λn -> case n of { 0 -> 0; x -> x+(sumi (x-1))}

sumi :: Integer -> Integer
sumi 0 = 0
sumi x = x+(sumi (x-1))
```

Listas:

```haskell
length :: [a] -> Integer
length = λl -> case l of { [] -> 0; x:xs -> 1+(length xs)}

length :: [a] -> Integer
length [] = 0
length (x:xs) = 1+(length xs)
```

Árboles:

```haskell
cantNodos :: Arb a -> Integer
cantNodos = λa -> case a of {
 Hoja x -> 0; Nodo i x d -> 1+(cantNodos i)+(cantNodos d) }

cantNodos :: Arb a -> Integer
cantNodos (Hoja x) = 0
cantNodos (Nodo i x d) = 1+(cantNodos i)+(cantNodos d)
```

Mirá el patrón: en las cuatro, el `case` tiene una rama por constructor del `data`, y el
pattern-matching tiene una ecuación por rama. En `length` y `cantNodos` el patrón del `case`
va sin paréntesis (`x:xs`) y en la ecuación va con ellos (`(x:xs)`).

## Relacionado

- [[fuentes/repaso-haskell]] — la ficha de la fuente
- [[construcciones/funciones-sobre-bool]] · [[construcciones/funciones-sobre-enteros]]
- [[construcciones/funciones-sobre-listas]] · [[construcciones/funciones-sobre-arboles]]

## Procedencia

- **Tabla** — sin cita: comentario del sistema
- **Criterio de decisión** — sin cita: comentario del sistema
- **Cuándo elegir cada uno** — sin cita: comentario del sistema
- **Los cuatro ejemplos resueltos por la cátedra** — repaso-haskell p.1, p.2, p.2-3 · incluye comentario del sistema
