# Cómo se escribe en este repo

Las páginas del wiki y los resúmenes se leen. No son fichas ni volcados: se estudia con
ellos. Este archivo fija el registro y da los contraejemplos.

**El texto que no se puede leer de corrido no se estudia**, se hojea. Una página que es una
pila de etiquetas y citas sueltas obliga al lector a reconstruir él las conexiones — que es
justo el trabajo que la página tenía que haber hecho.

Lo lee `/ingest` antes de escribir una página y `/resumen` antes de armar un resumen.

## El registro

Un apunte bien escrito por alguien que entendió el tema y te lo está contando. Voseo, directo,
sin ceremonia. Podés decir "acá se cae todo el mundo" o "parece burocrático y no lo es".

No es un paper formal: no hay que impostar objetividad ni escribir en pasiva. Tampoco es un
chat: no hay saludos, ni "¡buena pregunta!", ni cierres cordiales.

## Las cinco reglas

1. **Ninguna cita ni fórmula queda flotando sola.** Una oración la introduce diciendo qué
   establece, o la sigue diciendo qué consecuencia tiene. La cita se transcribe textual — eso
   no cambia — pero lo que la rodea es tuyo y es obligatorio.
2. **Párrafo objetivo: 40-90 palabras, dos a cuatro oraciones.** Un párrafo de una sola
   oración vale solo cuando es un veredicto: `Prohibido parafrasear.`
3. **Cada sección se lee de corrido.** Si dos bloques seguidos no tienen relación explícita,
   o falta una oración entre ellos o sobra uno de los dos.
4. **Las listas siguen valiendo cuando el contenido es una lista** — las hipótesis de un
   teorema, los pasos de un procedimiento. Pero cada ítem es una oración completa, y arriba
   va una línea que dice qué organiza la lista y qué hay que mirar al recorrerla.
5. **Toda página abre con dos o tres oraciones antes del primer `##`**, que dicen qué es esto
   y por qué importa en la materia. El modelo está en
   `teoria-de-la-computacion/wiki/comparativas/formas-de-definir-conjuntos.md`.

## Antipatrones — la sobre-explicación es el otro modo de escribir mal

Alargar no es explicar. Estas son las formas de inflar un texto sin agregarle nada, y están
prohibidas:

- **Muletillas de relleno**: `Es importante notar que`, `Cabe destacar`, `Vale la pena
  mencionar`, `Como podemos ver`, `En resumen`, `En otras palabras` cuando no hay otras
  palabras.
- **Repetir el encabezado en la primera oración.** Si la sección se llama `Contraejemplo`, no
  empieza con "Un contraejemplo de esto es".
- **Cerrar resumiendo lo que se acaba de decir.** El lector lo acaba de leer.
- **Anunciar la estructura**: `Primero veremos X, después Y`. Los encabezados ya lo dicen.
- **Hedging**: `podría decirse`, `en cierto sentido`, `de alguna manera`, `básicamente`.
- **Explicar lo que el nivel de la materia da por sabido.** En teoría de la computación no se
  explica qué es un conjunto.
- **Paralelismos decorativos** y tríos de adjetivos que no distinguen nada.

**Test de borrado:** si borrás una oración y no se pierde información, la oración sobraba.
Aplicalo a cada oración que agregues.

## Pares antes / después

Todos salen de páginas reales de este repo. La cita literal es idéntica en las dos columnas:
lo único que cambia es lo que la rodea.

### 1. Etiqueta + fórmula, sin nada alrededor

`definiciones/funcion.md`

> **Antes**
> ```
> **Inyectiva.** `(∀x, y ∈ A)(x ≠ y ⇒ f(x) ≠ f(y))`
>
> **Sobreyectiva.** `(∀y ∈ B)(∃x ∈ A)(f(x) = y)`
>
> **Biyectiva.** "Si es inyectiva y sobreyectiva"
> ```

> **Después**
> Las tres propiedades que siguen miran cómo se reparte el codominio. Es inyectiva cuando
> `(∀x, y ∈ A)(x ≠ y ⇒ f(x) ≠ f(y))`, o sea cuando no colapsa dos entradas distintas en la
> misma salida. Es sobreyectiva cuando `(∀y ∈ B)(∃x ∈ A)(f(x) = y)`: no sobra nada del
> codominio. Biyectiva es la conjunción de las dos, "si es inyectiva y sobreyectiva", y es la
> que habilita que exista la inversa.

Fijate que la fórmula no se tocó. Lo que se agregó es qué mira cada una y qué habilita la
tercera.

### 2. Citas apiladas sin sujeto

`definiciones/funcion.md`, sección `## Ejemplo`

> **Antes**
> Operaciones: "Al ser casos especiales de relaciones heredan todas las operaciones de
> relaciones". "La unión no es cerrada, esto es, a veces el resultado deja de ser función".
> "La inversa sólo es cerrada cuando la función es inyectiva."

> **Después**
> Como "al ser casos especiales de relaciones heredan todas las operaciones de relaciones",
> todo lo de [[definiciones/operaciones-con-relaciones]] se puede aplicar acá. Lo que no se
> hereda es la clausura: "la unión no es cerrada, esto es, a veces el resultado deja de ser
> función", porque unir dos funciones puede relacionar una entrada con dos salidas. "La
> inversa sólo es cerrada cuando la función es inyectiva", que es exactamente la condición que
> evita el mismo problema al dar vuelta los pares.

Tres citas sueltas pasan a ser un argumento: heredan las operaciones, pero no la clausura, y
la razón es siempre la misma.

### 3. El ejemplo que es solo una fórmula

`definiciones/funcion.md`, sección `## Ejemplo`

> **Antes**
> ```
> Inyectiva: `f : ℕ → ℕ, f(x) = x + 1`
> ```

> **Después**
> `f : ℕ → ℕ, f(x) = x + 1` es inyectiva: sumarle uno a dos números distintos da dos
> resultados distintos, así que nunca colapsa dos entradas. Conviene retenerla porque la misma
> función es el contraejemplo de sobreyectiva de más abajo — ningún `x` da `f(x) = 0`.

Un ejemplo sin una oración que diga qué ilustra es un ejemplo que hay que descifrar.

### 4. Pasos que son cita encadenada

`demostraciones/diagonalizacion.md`, sección `## Pasos`

> **Antes**
> ```
> 1. "Supongamos, con el fin de obtener una contradicción, que todas las funciones
>    `f : N → N` son computables. …"
> 2. "Construimos ahora una nueva función `g : N → N` definida por"
> 3. "Esta función está bien definida para todo `n ∈ N`, y es total."
> ```

> **Después**
> La demostración arma una función que no puede estar en la lista, y para eso primero supone
> que la lista existe. Los pasos 1 a 3 montan el escenario; el trabajo real es el paso 4.
> ```
> 1. "Supongamos, con el fin de obtener una contradicción, que todas las funciones
>    `f : N → N` son computables. …"
> 2. "Construimos ahora una nueva función `g : N → N` definida por"
> 3. "Esta función está bien definida para todo `n ∈ N`, y es total."
> ```

La lista numerada se queda —los pasos de una demostración **son** una lista— pero ahora arriba
dice qué mirar mientras se la recorre. Regla 4 en acción.

### 5. Definiciones consecutivas sin conectivo

`out/resumen-todo-completo.md`

> **Antes**
> ```
> **Definición 12.** "Sean A y B conjuntos. Se dice que `A ⪯ B` si existe una función
> total e inyectiva `f : A → B`."
>
> **Definición 13.** "Se dice que A y B son *equipolentes*, y se escribe `A ∼ B`, si y
> sólo si existe una función biyectiva y total `f : A → B`."
> ```

> **Después**
> Comparar tamaños de conjuntos infinitos necesita dos relaciones, no una. La primera es
> "menor o igual": **Definición 12**, "sean A y B conjuntos. Se dice que `A ⪯ B` si existe una
> función total e inyectiva `f : A → B`" — inyectiva alcanza porque codificar A dentro de B sin
> colisiones ya prueba que B no es más chico. La segunda es la igualdad que le corresponde:
> **Definición 13**, "se dice que A y B son *equipolentes*, y se escribe `A ∼ B`, si y sólo si
> existe una función biyectiva y total `f : A → B`".

Dos definiciones seguidas sin una palabra entre ellas obligan al lector a adivinar que son un
preorden y su equivalencia. Decirlo cuesta una oración.

### 6. El par positivo — esto ya está bien, imitalo

`out/resumen-todo-completo.md`, sección sobre inducción estructural

> **Dónde falla todo el mundo**: inducir sobre el número en vez de sobre la derivación. La
> hipótesis inductiva habla del **árbol de prueba**, no de `z` como natural. Si escribís
> "supongamos que vale para z, veamos para z+1" estás haciendo otra demostración.
>
> El resultado es trivial; **lo que se aprende es la técnica**. Es la primera inducción
> estructural sobre un árbol de derivación del curso, y es la misma que reaparece en semántica
> operacional (U9) y en equivalencia de modelos (U4).

Dice el error concreto, por qué es un error, y dónde vuelve a aparecer la técnica. Nada
sobra y nada es relleno.

## Dónde NO aplica

El registro es para las páginas del wiki, los resúmenes y `resumen-final.md`. Estas salidas
son deliberadamente tersas y **no** se tocan:

- **`/machete`** — dos columnas a 9pt, tope de 9000 caracteres. "Prosa explicativa" está en la
  columna *No entra* por diseño.
- **`/cards`** — respuesta de hasta cuatro elementos. Una tarjeta con un párrafo no se recupera.
- **`/estado`**, **`/plan`** — salida de ancho fijo, una línea por dato.
- **`/puentes`** — máximo 15 líneas, solo enlaces y una línea de por qué.
- **Las tablas** de `comparativa`, `framework` y `numeros`. Una tabla es una tabla. La prosa va
  antes o después, nunca adentro de una celda.
- **`## Procedencia`** — una línea por sección, formato fijo.

## Contra el tope de 150 líneas

El registro alarga las páginas. El tope de 150 líneas por página del contrato **no se
flexibiliza**: si una página se pasa, se parte y se enlaza. Una página de 200 líneas no se
estudia mejor que dos de 100 bien separadas.
