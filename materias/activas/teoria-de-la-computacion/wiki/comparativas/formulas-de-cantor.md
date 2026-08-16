---
id: teoria-de-la-computacion/comparativas/formulas-de-cantor
tipo: comparativa
tema: U6
fuentes: [notas-conjuntos p.6, numerabilidad-diag p.8]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Las dos fórmulas de Cantor de la materia

Este es el conflicto más concreto del wiki: los dos apuntes dan fórmulas cerradas distintas
para el emparejamiento de Cantor, y las dos son correctas. No es un error de ninguna fuente
sino una diferencia de convención, pero da **números distintos para el mismo par**, así que en
un ejercicio con cuentas hay que decidir cuál se usa antes de empezar.

Separado de [[construcciones/emparejamiento-de-cantor]], donde está la construcción.

## Tabla

Copello-Tasistro presenta la suya así: "quedando `f` expresada mediante la siguiente
expresión:"

```
f(i, j) = ( Σ[k=0..i+j] k ) + i
```

Acuña da la forma cerrada: `π(i, j) = (i + j)(i + j + 1) / 2 + j`

Como `Σ[k=0..s] k = s(s+1)/2`, la parte izquierda es **idéntica** — las dos cuentan igual
cuántos pares hay antes de la diagonal. La diferencia está solo en el sumando final, que es el
que ubica la posición dentro de la diagonal: **`+ i` contra `+ j`**.

| `(i, j)` | Copello `+i` | Acuña `+j` |
|---|---|---|
| `(0,0)` | 0 | 0 |
| `(1,0)` | **2** | **1** |
| `(0,1)` | **1** | **2** |
| `(1,1)` | 4 | 4 |
| `(2,0)` | **5** | **3** |

Coinciden exactamente sobre la diagonal (`i = j`) y en el origen, y difieren en todo lo demás.

## Criterio de decisión

Lo que cambia es **en qué sentido se recorre cada diagonal**. Copello ordena cada una empezando
por `(0, s)` y bajando por `i`; Acuña empieza por `(s, 0)` y sube por `j`. Como las dos
recorren la diagonal entera antes de pasar a la siguiente, las dos son biyecciones: lo único
que cambia es el orden interno, y por lo tanto los índices que le tocan a cada par.

La propia tabla de valores de Copello lo confirma: fila `0` vale `0 1 3`, fila `1`
vale `2 4`, fila `2` vale `5`. O sea `f(1,0) = 2`, mientras que la enumeración de Acuña da
`f(1) = (1, 0)`, o sea `π(1,0) = 1`.

## Cuándo elegir cada uno

- Si la consigna cita una fuente o usa su notación, usá **esa** fórmula y no la otra.
- Si la consigna no lo aclara, **declará cuál convención usás antes de calcular**. Es la regla
 propia de la materia para todas las divergencias entre apuntes, y acá es donde más se nota.
- Para argumentos cualitativos —probar que `N × N` es numerable— da igual cuál uses: las dos
 son biyecciones y eso es todo lo que hace falta.

## Relacionado

- [[construcciones/emparejamiento-de-cantor]] — la construcción y el recorrido por diagonales
- [[definiciones/numerable-y-contable]] — para qué sirve exhibir una biyección
- [[fuentes/notas-conjuntos]] · [[fuentes/numerabilidad-diag]]

## Procedencia

- **Tabla** — numerabilidad-diag p.8 · notas-conjuntos p.6 · incluye comentario del sistema · duda: Las dos fuentes de la materia dan fórmulas DISTINTAS
- **Criterio de decisión** — numerabilidad-diag p.8 · incluye comentario del sistema
- **Cuándo elegir cada uno** — sin cita: comentario del sistema
