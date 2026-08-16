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

`N × N` parece mucho más grande que `N` —es un plano contra una recta— y sin embargo tiene el
mismo tamaño. La construcción que lo prueba es el recorrido por diagonales, y su fórmula
cerrada es de las pocas de la materia que conviene saber de memoria porque después se reutiliza
para `Nᵏ` y para `Q`.

## Objetivo

Entra un par `(i, j) ∈ N × N`; sale un natural único. Construye la biyección que prueba que
`N × N` es numerable.

"La clave para numerar pares de naturales es recorrer la grilla por
diagonales."

## Procedimiento

1. Recorré la grilla `N × N` por diagonales: "considerando primero las
 parejas `(i, j)` con `i + j = 0`, luego `i + j = 1`, luego `i + j = 2`, etc."
2. Dentro de cada diagonal, recorré en el orden
 `(s, 0), (s−1, 1), …, (0, s)` con `s = i + j`.
3. Contá cuántos pares hay **antes** de tu diagonal. "Definiendo
 `s = i + j`, la cantidad de parejas que aparecen antes de la diagonal `s` es `s(s+1)/2`."
4. Sumá la posición dentro de la diagonal, que "está determinada
 por `j`".
5. Resultado — **función de emparejamiento de Cantor**:

 ```
 π(i, j) = (i + j)(i + j + 1) / 2 + j
 ```

6. "Esta función define una biyección explícita entre `N × N` y `N`, y
 proporciona una forma cerrada de la enumeración por diagonales."

## Diagrama

La grilla que trae el apunte, recorrida por las diagonales punteadas:

```
(0,0) (1,0) (2,0) (3,0) (4,0)
 ↘ ↘ ↘ ↘
(0,1) (1,1) (2,1) (3,1) (4,1)
 ↘ ↘ ↘
(0,2) (1,2) (2,2) (3,2) (4,2)
 ↘ ↘
(0,3) (1,3) (2,3) (3,3) (4,3)
 ↘
(0,4) (1,4) (2,4) (3,4) (4,4)
```

Cada diagonal agrupa los pares con la misma suma `i + j`, y es **finita**: por eso se
termina de recorrer en finitos pasos y se pasa a la siguiente.

## Caso resuelto

Los primeros valores que da el apunte:

| `n` | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| `f(n)` | (0,0) | (1,0) | (0,1) | (2,0) | (1,1) | (0,2) | (3,0) |

Verificación de la fórmula cerrada contra la tabla, con `π(i, j)`:

- `π(0,0) = 0·1/2 + 0 = 0` ✔
- `π(1,0) = 1·2/2 + 0 = 1` ✔
- `π(0,1) = 1·2/2 + 1 = 2` ✔
- `π(2,0) = 2·3/2 + 0 = 3` ✔
- `π(1,1) = 2·3/2 + 1 = 4` ✔

Ojo: la tabla del apunte lista `f : N → N × N` (de natural a par) y la fórmula `π` va al
revés, `π : N × N → N`. Son inversas una de la otra, pero el apunte usa la misma letra `f` para
la enumeración y nunca dice explícitamente que `π = f⁻¹`.

## Por qué es biyectiva

Las dos mitades se argumentan por separado y las dos se apoyan en que cada diagonal es finita.
Que sea sobreyectiva es lo que hay que cuidar, porque es donde un recorrido mal elegido
fallaría: "toda pareja pertenece a una única diagonal determinada
por el valor de `i + j`, y cada diagonal es recorrida completamente en una cantidad finita de
pasos. Por lo tanto, toda pareja será eventualmente visitada".

La inyectividad, en cambio, sale sola del hecho de estar contando: "a cada paso del recorrido
se asigna un natural distinto, por lo que no se repiten valores".

## Antes de usar la fórmula: las dos fuentes dan fórmulas DISTINTAS

La `π` de arriba es la de Acuña. Copello-Tasistro da otra, y **no son la misma función**:
recorren cada diagonal en sentido opuesto, así que `π(1,0)` vale `1` en una y `2` en la otra.
Las dos son biyecciones válidas y ninguna está mal.

**En el parcial: fijate qué fuente usa la consigna, o declará cuál convención estás usando
antes de calcular.** El análisis completo, con la tabla de valores donde difieren, está en
[[comparativas/formulas-de-cantor]]. Anotado en `wiki/dudas.md`.

## Ejercicios del apunte

**Ejercicio 3.** "Extender la idea anterior para demostrar que `N³` es
numerable."

**Ejercicio 4.** "Demostrar que `Nᵏ` es numerable para todo `k ≥ 1`."

**Ejercicio 5.** "Probar que `Q` es numerable."

**Ejercicio 6.** "Explicar en qué difiere la demostración anterior de
la de los ejercicios 3 y 4. ¿Qué consideraciones adicionales hay que tener con los
racionales?"

La respuesta al Ejercicio 6 es la clave de todo: en `Q` **distintos pares dan el mismo
racional** (`1/2 = 2/4`), así que la enumeración por diagonales repite. Hay que quitar
repeticiones o quedarse con la fracción irreducible. Por eso `Q` sale más fácil como
**contable** y después se usa la Proposición 6 — ver [[definiciones/numerable-y-contable]].

## Relacionado

- [[definiciones/numerable-y-contable]] — qué hay que exhibir para probar numerabilidad
- [[teoremas/z-es-numerable]] — la misma idea de intercalar, más simple
- [[teoremas/palabras-finitas-son-numerables]] — el mismo recurso aplicado a `Σ*`
- [[fuentes/notas-conjuntos]]

## Procedencia

- **Objetivo** — notas-conjuntos p.5
- **Procedimiento** — notas-conjuntos p.5, p.6
- **Diagrama** — notas-conjuntos p.5 · incluye comentario del sistema
- **Caso resuelto** — notas-conjuntos p.5 · incluye comentario del sistema · duda registrada en `dudas.md`
- **Por qué es biyectiva** — notas-conjuntos p.6
- **Las dos fuentes de la materia dan fórmulas DISTINTAS** — numerabilidad-diag p.8 · notas-conjuntos p.6 · incluye comentario del sistema · duda: Las dos fuentes de la materia dan fórmulas DISTINTAS
- **Ejercicios del apunte** — notas-conjuntos p.6 · incluye comentario del sistema
