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

## Enunciado

✅ [notas-conjuntos p.5] **Teorema 2.** "`Z` es numerable."

## Hipótesis

- Ninguna: es un resultado cerrado sobre `Z`.
- 🧠 Lo que hay que exhibir, por la Definición 15, es una **biyección total `f : N → Z`**.

## Demostración

✅ [notas-conjuntos p.5] "Consideremos la enumeración `0, −1, 1, −2, 2, −3, 3, …` y definamos
`f : N → Z` por"

```
        ⎧  n/2        si n es par,
f(n) =  ⎨
        ⎩  −(n+1)/2   si n es impar.
```

✅ [notas-conjuntos p.5] "Es inmediato verificar que `f` es biyectiva."

🧠 Transcripción de la llave y las fracciones contra la página rasterizada: el texto plano las
aplana y se pierde qué está sobre qué.

🧠 Cómo se lee: los pares van a los no negativos (`0↦0, 2↦1, 4↦2`) y los impares a los
negativos (`1↦−1, 3↦−2, 5↦−3`). Intercalar es la única idea de la prueba.

## Cuándo se aplica

🧠 Es el primer ejemplo no trivial de numerabilidad y el molde de la técnica de
**intercalado**: cuando querés numerar la unión de dos copias de `N`, mandá una a los pares y
la otra a los impares. La misma idea reaparece en el Ejemplo 9.2 del apunte ("la unión de dos
conjuntos numerables es numerable") y en el Ejercicio 10.

🧠 Sirve de contraejemplo a la intuición de tamaño: `N ⊊ Z` y sin embargo `N ∼ Z`. Ver
[[definiciones/comparacion-de-cardinalidades]].

## Errores típicos

- 🧠 **Escribir `f(n) = ±n/2` sin separar pares de impares.** Sin la partición, `f` no está
  bien definida sobre los enteros y se rompe la inyectividad.
- 🧠 **Equivocar el desfasaje.** Es `−(n+1)/2`, no `−n/2`: con `−n/2` el `1` iría a `−0.5`, que
  no es entero. El `+1` es lo que hace que los impares caigan justo.
- 🧠 **Aceptar "es inmediato verificar" sin verificarlo.** El apunte lo dice; en un parcial con
  material te pueden pedir la verificación. Chequeá inyectividad y sobreyectividad por
  separado.

## Relacionado

- [[definiciones/numerable-y-contable]] — la definición que se instancia
- [[construcciones/emparejamiento-de-cantor]] — el mismo objetivo con una técnica más potente
- [[definiciones/comparacion-de-cardinalidades]]
- [[fuentes/notas-conjuntos]]
