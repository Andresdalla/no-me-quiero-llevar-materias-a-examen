---
id: teoria-de-la-computacion/construcciones/emparejamiento-de-cantor
tipo: construccion
tema: U6
fuentes: [notas-conjuntos p.5, notas-conjuntos p.6, numerabilidad-diag p.7, numerabilidad-diag p.8]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Construcción del emparejamiento de Cantor (`N × N` es numerable)

## Objetivo

Entra un par `(i, j) ∈ N × N`; sale un natural único. Construye la biyección que prueba que
`N × N` es numerable.

✅ [notas-conjuntos p.5] "La clave para numerar pares de naturales es recorrer la grilla por
diagonales."

## Procedimiento

1. ✅ [notas-conjuntos p.5] Recorré la grilla `N × N` por diagonales: "considerando primero las
   parejas `(i, j)` con `i + j = 0`, luego `i + j = 1`, luego `i + j = 2`, etc."
2. Dentro de cada diagonal, ✅ [notas-conjuntos p.6] recorré en el orden
   `(s, 0), (s−1, 1), …, (0, s)` con `s = i + j`.
3. Contá cuántos pares hay **antes** de tu diagonal. ✅ [notas-conjuntos p.6] "Definiendo
   `s = i + j`, la cantidad de parejas que aparecen antes de la diagonal `s` es `s(s+1)/2`."
4. Sumá la posición dentro de la diagonal, que ✅ [notas-conjuntos p.6] "está determinada
   por `j`".
5. ✅ [notas-conjuntos p.6] Resultado — **función de emparejamiento de Cantor**:

   ```
   π(i, j) = (i + j)(i + j + 1) / 2  +  j
   ```

6. ✅ [notas-conjuntos p.6] "Esta función define una biyección explícita entre `N × N` y `N`, y
   proporciona una forma cerrada de la enumeración por diagonales."

## Diagrama

✅ [notas-conjuntos p.5] La grilla que trae el apunte, recorrida por las diagonales punteadas:

```
(0,0)   (1,0)   (2,0)   (3,0)   (4,0)
   ↘       ↘       ↘       ↘
(0,1)   (1,1)   (2,1)   (3,1)   (4,1)
   ↘       ↘       ↘
(0,2)   (1,2)   (2,2)   (3,2)   (4,2)
   ↘       ↘
(0,3)   (1,3)   (2,3)   (3,3)   (4,3)
   ↘
(0,4)   (1,4)   (2,4)   (3,4)   (4,4)
```

🧠 Cada diagonal agrupa los pares con la misma suma `i + j`, y es **finita**: por eso se
termina de recorrer en finitos pasos y se pasa a la siguiente.

## Caso resuelto

✅ [notas-conjuntos p.5] Los primeros valores que da el apunte:

| `n` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| `f(n)` | (0,0) | (1,0) | (0,1) | (2,0) | (1,1) | (0,2) | (3,0) |

🧠 Verificación de la fórmula cerrada contra la tabla, con `π(i, j)`:

- `π(0,0) = 0·1/2 + 0 = 0` ✔
- `π(1,0) = 1·2/2 + 0 = 1` ✔
- `π(0,1) = 1·2/2 + 1 = 2` ✔
- `π(2,0) = 2·3/2 + 0 = 3` ✔
- `π(1,1) = 2·3/2 + 1 = 4` ✔

⚠️ Ojo: la tabla del apunte lista `f : N → N × N` (de natural a par) y la fórmula `π` va al
revés, `π : N × N → N`. Son inversas una de la otra, pero el apunte usa la misma letra `f` para
la enumeración y nunca dice explícitamente que `π = f⁻¹`.

## Por qué es biyectiva

✅ [notas-conjuntos p.6] Sobreyectiva: "toda pareja pertenece a una única diagonal determinada
por el valor de `i + j`, y cada diagonal es recorrida completamente en una cantidad finita de
pasos. Por lo tanto, toda pareja será eventualmente visitada".

✅ [notas-conjuntos p.6] Inyectiva: "a cada paso del recorrido se asigna un natural distinto,
por lo que no se repiten valores".

## ⚠️ Las dos fuentes de la materia dan fórmulas DISTINTAS

Este es el conflicto más concreto del wiki. Las dos son biyecciones válidas de `N × N` en `N`,
pero **no son la misma función**: recorren cada diagonal en sentido opuesto.

✅ [numerabilidad-diag p.8] Copello-Tasistro: "quedando `f` expresada mediante la siguiente
expresión:"

```
f(i, j) = ( Σ[k=0..i+j] k ) + i
```

✅ [notas-conjuntos p.6] Acuña: `π(i, j) = (i + j)(i + j + 1) / 2 + j`

🧠 Como `Σ[k=0..s] k = s(s+1)/2`, la parte izquierda es idéntica. La diferencia es el
sumando final: **`+ i` contra `+ j`**.

| `(i, j)` | Copello `+i` | Acuña `+j` |
|---|---|---|
| `(0,0)` | 0 | 0 |
| `(1,0)` | **2** | **1** |
| `(0,1)` | **1** | **2** |
| `(1,1)` | 4 | 4 |
| `(2,0)` | **5** | **3** |

✅ [numerabilidad-diag p.8] La tabla de Copello lo confirma: fila `0` vale `0 1 3`, fila `1`
vale `2 4`, fila `2` vale `5`. O sea `f(1,0) = 2`, mientras que la enumeración de Acuña da
`f(1) = (1, 0)`, o sea `π(1,0) = 1`.

🧠 Ninguna está mal. Copello ordena cada diagonal empezando por `(0, s)` y bajando por `i`;
Acuña empieza por `(s, 0)` y sube por `j`. **En el parcial: fijate qué fuente usa la consigna,
o declará cuál convención estás usando antes de calcular.** Anotado en `wiki/dudas.md`.

## Ejercicios del apunte

✅ [notas-conjuntos p.6] **Ejercicio 3.** "Extender la idea anterior para demostrar que `N³` es
numerable."

✅ [notas-conjuntos p.6] **Ejercicio 4.** "Demostrar que `Nᵏ` es numerable para todo `k ≥ 1`."

✅ [notas-conjuntos p.6] **Ejercicio 5.** "Probar que `Q` es numerable."

✅ [notas-conjuntos p.6] **Ejercicio 6.** "Explicar en qué difiere la demostración anterior de
la de los ejercicios 3 y 4. ¿Qué consideraciones adicionales hay que tener con los
racionales?"

🧠 La respuesta al Ejercicio 6 es la clave de todo: en `Q` **distintos pares dan el mismo
racional** (`1/2 = 2/4`), así que la enumeración por diagonales repite. Hay que quitar
repeticiones o quedarse con la fracción irreducible. Por eso `Q` sale más fácil como
**contable** y después se usa la Proposición 6 — ver [[definiciones/numerable-y-contable]].

## Relacionado

- [[definiciones/numerable-y-contable]] — qué hay que exhibir para probar numerabilidad
- [[teoremas/z-es-numerable]] — la misma idea de intercalar, más simple
- [[teoremas/palabras-finitas-son-numerables]] — el mismo recurso aplicado a `Σ*`
- [[fuentes/notas-conjuntos]]
