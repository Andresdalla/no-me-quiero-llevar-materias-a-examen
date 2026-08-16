---
id: teoria-de-la-computacion/teoremas/z-es-numerable
tipo: teorema
tema: U6
fuentes: [notas-conjuntos p.5]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# `Z` es numerable

`Z` tiene "el doble" de elementos que `N` y sin embargo se numera igual. Es el primer resultado
donde la intuición de tamaño falla de manera visible, y la técnica que lo resuelve —intercalar
dos copias— reaparece varias veces después.

## Enunciado

**Teorema 2.** "`Z` es numerable." Por la Definición 15, eso significa que existe una biyección
con `N`, y probarlo consiste enteramente en exhibirla.

## Hipótesis

No hay ninguna condición que verificar; toda la dificultad está en construir la función
correcta.

- Ninguna: es un resultado cerrado sobre `Z`.
- Lo que hay que exhibir, por la Definición 15, es una **biyección total `f : N → Z`**.

## Demostración

La idea entera está en la enumeración que el apunte propone antes de escribir la fórmula, y
conviene leerla primero: "Consideremos la enumeración `0, −1, 1, −2, 2, −3, 3, …` y definamos
`f : N → Z` por"

```
 ⎧ n/2 si n es par,
f(n) = ⎨
 ⎩ −(n+1)/2 si n es impar.
```

El apunte cierra con "Es inmediato verificar que `f` es biyectiva.", y no lo verifica.

Cómo se lee la fórmula: los pares van a los no negativos (`0↦0, 2↦1, 4↦2`) y los impares a los
negativos (`1↦−1, 3↦−2, 5↦−3`). Intercalar es la única idea de la prueba; el resto es
aritmética para que los índices caigan justo. La transcripción de la llave y las fracciones
está verificada contra la página rasterizada, porque el texto plano las aplana y se pierde qué
está sobre qué.

## Cuándo se aplica

Es el primer ejemplo no trivial de numerabilidad y el molde de la técnica de
**intercalado**: cuando querés numerar la unión de dos copias de `N`, mandá una a los pares y
la otra a los impares. La misma idea reaparece en el Ejemplo 9.2 del apunte ("la unión de dos
conjuntos numerables es numerable") y en el Ejercicio 10, así que conviene tenerla automatizada.

Además sirve de contraejemplo a la intuición de tamaño, y en eso hace pareja con el `N \ {0}`
de [[definiciones/comparacion-de-cardinalidades]]: `N ⊊ Z` y sin embargo `N ∼ Z`.

## Errores típicos

- **Escribir `f(n) = ±n/2` sin separar pares de impares.** Sin la partición, `f` no está
 bien definida sobre los enteros y se rompe la inyectividad.
- **Equivocar el desfasaje.** Es `−(n+1)/2`, no `−n/2`: con `−n/2` el `1` iría a `−0.5`, que
 no es entero. El `+1` es lo que hace que los impares caigan justo.
- **Aceptar "es inmediato verificar" sin verificarlo.** El apunte lo dice; en un parcial con
 material te pueden pedir la verificación. Chequeá inyectividad y sobreyectividad por
 separado.

## Relacionado

- [[definiciones/numerable-y-contable]] — la definición que se instancia
- [[construcciones/emparejamiento-de-cantor]] — el mismo objetivo con una técnica más potente
- [[definiciones/comparacion-de-cardinalidades]]
- [[fuentes/notas-conjuntos]]

## Procedencia

- **Enunciado** — notas-conjuntos p.5
- **Hipótesis** — sin cita: comentario del sistema
- **Demostración** — notas-conjuntos p.5 · incluye comentario del sistema
- **Cuándo se aplica** — sin cita: comentario del sistema
- **Errores típicos** — sin cita: comentario del sistema
