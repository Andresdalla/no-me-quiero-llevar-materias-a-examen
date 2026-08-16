# Teoría de la Computación (`teoria-de-la-computacion`)

- cuatrimestre: 2026-2C (5to semestre) · comisión m5a · schema_version: 1 · perfilado: **provisional**
- cursada: 4 h semanales · 15 semanas · teórico-práctica
- evaluación: **mixta** (escrito con material + oral + proyecto) · 100 puntos
- parcial: **7/12, 9.00** · 3 horas · **con material** · 60 pts
- defensas de práctico (oral): 15/9 · 29/9 · 27/10 · 7/11 · 7 pts c/u, cuentan **las 3 mejores** · 21 pts
- tarea final: entrega el último día de clases (lectura a definir) · 14 pts
- actuación en clase: 5 pts
- correlativas: previas `Fundamentos de la Computación` (🧠 inferida, sin confirmar) · posteriores `sin datos`

## Tipos activos

Máximo 8. Hay **7**: el slot libre lo decide `/reperfilar` cuando exista evidencia real de
evaluación. Cada uno hereda su regla de verificación de `plantillas/catalogo.md`.

| Tipo | Alias de cátedra | Por qué está |
|---|---|---|
| `definicion` | — | El apunte de conjuntos es pared a pared: relación, función parcial/total, inyección, sobreyección, biyección, numerabilidad. |
| `teorema` | — | Temario: "demostrar que ciertos conjuntos no son numerables", Tesis de Church, teorema de Rice. |
| `demostracion` | — | Temario lista "Métodos de demostración: compilación e interpretación · Demostraciones" como ítem propio. |
| `construccion` | — | MT universal, auto-intérpretes, intérpretes embebidos, eliminación de recursión, cada función del repartido. |
| `reduccion` | — | Temario la nombra dos veces: "Reducción de problemas" (U7) y "Reducción polinomial" (U8). |
| `modelo` | — | "Modelos de la noción de función computable" titula el programa: MT, lenguaje con asignación e iteración, λ puro, λ extendido. |
| `comparativa` | — | Equivalencia imperativo/funcional, P vs NP, numerable vs no numerable, sintaxis abstracta vs concreta, paso corto vs paso largo. |

`/reperfilar` programado a las **8 ingestas** (no 20): sin parciales viejos el perfilado no
tiene evidencia de evaluación.

## Vocabulario y notación de la cátedra

- `repartido` = guía de ejercicios · `defensa de práctico` = evaluación oral del práctico
- `λ-notation y case` = definición por expresión lambda con análisis de casos
- `Pattern-Matching y guardas` = definición por ecuaciones con patrones
- Declaración de tipos: la cátedra **migró** de la forma de Fundamentos
  `data Bool where {False :: Bool; True :: Bool}` a `data Bool = False | True`.
  Usá la segunda; mencioná la primera solo al conectar con Fundamentos.
- `paso corto` = reducción (semántica operacional) · `paso largo` = evaluación

## Reglas propias

- **El parcial es con material.** No optimices para recitar: las páginas y los machetes se
  juzgan por si te dejan *construir* y *demostrar* en el momento, no por ser memorizables.
  `/profesor` y `/machete` priorizan aplicar y crear sobre recordar.
- **Cada función del repartido se pide en las dos formas** (λ+case y pattern-matching). Una
  página `construccion` muestra **ambas**, no una.
- **La cursada no sigue el orden del temario.** Empieza por U6 (cardinalidad). La numeración
  de `programa.md` es del programa, no del calendario.
- **Los repartidos no traen soluciones oficiales.** Toda resolución es `🧠` inferida y va
  marcada como tal. Nunca la presentes como verificada.
- **No hay exámenes viejos ingeridos**, así que la reserva ciega está vacía. Si conseguís uno,
  no lo abras: va directo a `raw/examenes/_reservado/` para el simulacro previo al 7/12.

## Carpetas del wiki

- `temas/` — una página por unidad del programa: qué entra, cobertura, enlaces.
- `fuentes/` — una ficha por fuente ingerida: qué es, qué cubre, cuán confiable es.
- `conceptos/` — fallback: páginas de tipos que no tienen carpeta propia declarada.
- El resto (`definiciones/`, `teoremas/`, …) las crea `/ingest` a demanda, con el nombre
  plural que fija `plantillas/catalogo.md`.
