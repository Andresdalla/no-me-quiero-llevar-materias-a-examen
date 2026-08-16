# Teoría de la Computación (`teoria-de-la-computacion`)

- cuatrimestre: 2026-2C (5to semestre) · comisión m5a · schema_version: 1 · perfilado: **provisional**
- cursada: 4 h semanales · 15 semanas · teórico-práctica
- evaluación: **mixta** (escrito con material + oral + proyecto) · 100 puntos
- parcial: **7/12, 9.00** · 3 horas · **con material** · 60 pts
- defensas de práctico (oral): 15/9 · 29/9 · 27/10 · 7/11 · 7 pts c/u, cuentan **las 3 mejores** · 21 pts
- tarea final: entrega el último día de clases (lectura a definir) · 14 pts · actuación en clase: 5 pts
- correlativas: previas `Fundamentos de la Computación` (🧠 inferida) · posteriores `sin datos`

## Tipos activos

7 de 8; el slot libre lo decide `/reperfilar`. Reglas en `plantillas/catalogo.md`.

| Tipo | Por qué está |
|---|---|
| `definicion` | Los tres apuntes de conjuntos son pared a pared definiciones numeradas. |
| `teorema` | Numerabilidad de `Z`, `Σ*`, `P(N)`; Rice; Tesis de Church. |
| `demostracion` | El temario lista "Métodos de demostración · Demostraciones" como ítem propio. |
| `construccion` | MT universal, auto-intérpretes, emparejamiento de Cantor, funciones Haskell. |
| `reduccion` | El temario la nombra dos veces: "Reducción de problemas" (U7) y "polinomial" (U8). |
| `modelo` | "Modelos de la noción de función computable" titula el programa. |
| `comparativa` | Función vs algoritmo, P vs NP, numerable vs contable, paso corto vs largo. |

`/reperfilar` a las **8 ingestas** (van 5).

**Estructurales, fuera de los 8**: `fuente` (`fuentes/`) y `examen` (`examenes/`). No son tipos
de contenido ni están en `plantillas/catalogo.md`; se declaran acá para `/lint`.

## Evidencia de evaluación

13 consignas reales de 4 fechas (feb 2026, set/jul/may 2025), en `wiki/examenes/patron.md`.
**Sirven para los verbos, no para ponderar**: salen de un apunte sobre conjuntos, así que el
100% en U6 es sesgo de la fuente. 11 de 13 son de respuesta cerrada. Reserva ciega **vacía**.

## Vocabulario y notación de la cátedra

⚠️ **Tres apuntes, tres notaciones.** Antes de responder, mirá de qué fuente viene la consigna.

| Concepto | `revision-conjuntos` | `notas-conjuntos` (Acuña) | `numerabilidad-diag` (Copello) |
|---|---|---|---|
| función parcial | `f : A ⇸ B` | `f : A ↬ B` | `f : A ↬ B` |
| `A ∼ B` | — | existe biyección total | `A ⪯ B` y `B ⪯ A` |
| Cantor | — | `(i+j)(i+j+1)/2 + j` | `(Σ[k=0..i+j] k) + i` |
| "función" a secas | sin convención | sin convención | significa **parcial** |
| "dominio" | el conjunto de entrada | — | solo donde `f` está definida |

- `repartido` = guía · `defensa de práctico` = evaluación oral · `coordinables` = equipolentes
- `algoritmo` = pieza de código (Copello **reserva** "función" para el objeto matemático)
- `Z`, `S n` = cero y sucesor · `paso corto` = reducción · `paso largo` = evaluación

## Reglas propias

- **El parcial es con material.** No optimices para recitar: `/profesor` y `/machete`
  priorizan aplicar y construir sobre recordar.
- **Ante divergencia entre apuntes, declará qué convención usás** antes de calcular (`wiki/dudas.md`).
- **Cada función del repartido se pide en las dos formas**: `λ-notation y case` y `Pattern-Matching y guardas`.
- **La cursada no sigue el orden del temario**: empieza por U6. La numeración es del programa.
- **Ningún repartido trae soluciones**: toda resolución es `🧠` inferida y va marcada. Si
  conseguís un examen entero, **no lo abras**: va a `raw/examenes/_reservado/`.
