---
id: teoria-de-la-computacion/definiciones/propiedades-de-relaciones
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.6, revision-conjuntos p.7]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de las propiedades de una relación

Estas cinco propiedades son el vocabulario con el que después se nombran los órdenes y las
equivalencias: casi todo lo que se pregunta sobre una relación concreta es cuáles de las cinco
cumple. Todas se definen sobre `R ⊆ A × A`, es decir relaciones **binarias**, donde entrada y
salida son el mismo conjunto — sin eso, preguntar si `(x, x) ∈ R` no tendría sentido.

## Enunciado

Las cinco se enuncian con cuantificadores y sin prosa, y conviene leerlas en este orden porque
cada una restringe un poco más que la anterior.

| Propiedad | Enunciado |
|---|---|
| Reflexiva | `(∀x ∈ A)((x, x) ∈ R)` |
| Simétrica | `(∀x, y ∈ A)((x, y) ∈ R ⇒ (y, x) ∈ R)` |
| Antisimétrica | `(∀x, y ∈ A)((x, y) ∈ R ∧ (y, x) ∈ R ⇒ x = y)` |
| Asimétrica | `(∀x, y ∈ A)((x, y) ∈ R ⇒ (y, x) ∉ R)` |
| Transitiva | `(∀x, y, z ∈ A)((x, y) ∈ R ∧ (y, z) ∈ R ⇒ (x, z) ∈ R)` |

La única de las seis que se define combinando otras es la relación **de equivalencia**: "Si R
es reflexiva, simétrica y transitiva." Es la combinación que aparece cada vez que se quiere
partir un conjunto en clases, y por eso tiene nombre propio.

El apunte escribe "Antisimétcia" y "Asimétcia" en los títulos. Es un error de tipeo de la
fuente; las fórmulas están bien.

## Notación

Dos detalles de notación que cambian cómo se lee la tabla de arriba y cómo conviene contestar.

- `∉` es la negación de `∈`. En la extracción de texto aparece como `/∈`.
- La cátedra enuncia todo con cuantificadores explícitos, nunca en prosa. En el parcial
 conviene responder en el mismo formato: es el único que garantiza que no se te escape un
 cuantificador al traducir.

## Ejemplo

El apunte trabaja siempre con las mismas dos relaciones sobre los naturales, y el contraste
entre ellas es el que hay que retener. De `R<` afirma que "`R<` es transitiva ? Sí" — el
desarrollo está en [[teoremas/transitividad-de-r-menor]].

`R≤` sí es reflexiva, simétrica no, antisimétrica sí y transitiva sí: es el orden parcial
laxo del que habla [[definiciones/ordenes]]. O sea que pasar de `<` a `≤` cambia exactamente
una respuesta, la de reflexividad, y eso es lo que separa un orden estricto de uno laxo.

## Contraejemplo

`R<` funciona como contraejemplo de casi todas, y por eso el apunte la usa de banco de pruebas.
Las dos que resuelve son las que fallan por un caso concreto:

- "`R<` es reflexiva ? No, dado que `(0, 0) ∉ R<`"
- "`R<` es simétrica ? No, dado que `(0, 1) ∈ R<` pero `(1, 0) ∉ R<`"

De ahí se sigue lo que el apunte concluye: "`R<` es de equivalencia ? No, por no ser reflexiva
ni simétrica." Basta que falle una de las tres condiciones, y acá fallan dos.

Quedan **dos preguntas sin responder** en el apunte: "`R<` es antisimétrica ?" y "`R<` es
asimétrica ?" Las dos son **sí**, pero por razones de distinta naturaleza y ahí está lo
interesante. Asimétrica se verifica de frente: si `x < y` entonces nunca `y < x`.
Antisimétrica, en cambio, se cumple sin que haya nada que verificar, porque la premisa
`(x,y) ∈ R< ∧ (y,x) ∈ R<` no se cumple nunca y la implicación queda **verdadera por
vacuidad**. Ese razonamiento por vacuidad es el que más se falla: la respuesta correcta se
siente como una trampa hasta que se ve que una implicación con antecedente falso es verdadera.

## Confusiones frecuentes

- **Antisimétrica vs asimétrica.** No son lo mismo y el apunte las pone seguidas a propósito.
 Asimétrica prohíbe `(y,x)` siempre; antisimétrica la permite **solo si `x = y`**. Toda
 relación asimétrica es antisimétrica, no al revés: `R≤` es antisimétrica pero no asimétrica.
- **"No es simétrica" ≠ "es antisimétrica".** Son propiedades independientes, no opuestas.
 Una relación puede no cumplir ninguna de las dos.
- **Vacuidad.** Una propiedad universal sobre una premisa que nunca se cumple es verdadera.
 Ver [[definiciones/relacion]] para por qué `(x,y)` y `(y,x)` nunca coexisten en `R<`.

## Relacionado

- [[definiciones/relacion]] — qué es una relación binaria
- [[definiciones/ordenes]] — las combinaciones de estas propiedades que tienen nombre
- [[teoremas/transitividad-de-r-menor]] · [[demostraciones/transitividad-de-r-menor]]
- [[fuentes/revision-conjuntos]]

## Procedencia

- **Enunciado** — revision-conjuntos p.6, p.7 · incluye comentario del sistema
- **Notación** — sin cita: comentario del sistema
- **Ejemplo** — revision-conjuntos p.6 · incluye comentario del sistema
- **Contraejemplo** — revision-conjuntos p.6, p.7 · incluye comentario del sistema
