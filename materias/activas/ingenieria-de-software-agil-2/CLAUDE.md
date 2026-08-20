# Ingeniería de Software Ágil 2 (`ingenieria-de-software-agil-2`)

- cátedra: Ingeniería de Software · cuatrimestre: 2026-2C · schema_version: 2 · perfilado: provisional
- evaluación: mixta por puntos, **sin examen final** · fechas: no se registran (decisión del usuario)
- correlativas: previas sin datos · posteriores sin datos
- `/reperfilar` a las **8 ingestas**: los tipos se eligieron sin parciales ni guías a la vista.

## Esquema de puntos

Suma 170 nominales, umbral 70. Sin final: todo se define durante el curso, así que pesa más
lo que se evalúa seguido que lo que se evalúa una vez.

| Instancia | Puntos | Qué implica para el wiki |
|---|---|---|
| Ejercicios TBL | 40 | `caso` y `practica` son el material de trabajo en clase |
| Obligatorio (2da instancia, mín. 6) | 30 | proyecto; el wiki lo respalda, no lo reemplaza |
| Proyecto DevOps | 30 | idem; la 2da instancia es una extensión individual con defensa |
| Parcial | 30 | única instancia escrita concentrada |
| Ejercicios de aplicación | 25 | 12.5 realización + 12.5 **defensas aleatorias en clase** |
| RATs | 10 | 5 individuales + 5 grupales, sobre la lectura previa |
| Investigación de tecnología + presentación | 5 | tema propio, fuera del temario |

Asistencia y evaluación de pares son obligatorias y pueden afectar los puntos de ejercicios.
Abandonar después del comienzo da 0 en la escolaridad.

## Tipos activos

| Tipo | Alias de cátedra | Por qué está |
|---|---|---|
| `practica` | — | el Handbook es un catálogo de prácticas; `Cuándo NO aplica` es lo que repreguntan las defensas |
| `definicion` | — | los RATs son múltiple choice sobre la lectura: se juegan en precisión terminológica |
| `comparativa` | — | U3 pide comparar monolitos vs. microservicios, patrones de release y cuadrantes de testing |
| `caso` | — | los ejercicios TBL y las defensas son situaciones concretas con una decisión |
| `modelo` | — | las tres vías, los cuadrantes de Agile Testing y las four keys tienen límites que hay que declarar |
| `framework` | — | Kanban entra con roles, artefactos y ceremonias en tabla |

Fuera por ahora, con motivo: `numeros` (no llega a 3 páginas propias; los valores DORA viven
dentro de `modelos/`), `mecanismo` (se solapa con `practica`), `debate` (no hay posturas
enfrentadas con fuentes distintas en el temario).

## Vocabulario y notación de la cátedra

- `las tres vías` = The Three Ways (flujo · feedback · aprendizaje y experimentación continuas)
- `RAT` = Readiness Assurance Test, múltiple choice sobre la lectura previa, individual y grupal
- `TBL` = Team-Based Learning, la modalidad de clase
- `four keys` = las cuatro métricas DORA de entrega de software
- `arquetipos arquitectónicos` = monolitos vs. microservicios (U3)

## Reglas propias

- **La cátedra mezcla dos ediciones del Handbook**: U1 y U2 citan la 1ª edición (cap. 1–4, 9–11),
  U3 a U5 la 2ª (cap. 12–21). El `fuente-id` tiene que dejar la edición explícita:
  `devops-handbook-1ed` vs. `devops-handbook-2ed`. Un capítulo 12 sin edición es una cita rota.
- El temario obliga a leer también la **introducción** de cada parte y capítulo, no solo el capítulo.
- El temario ingerido es el de **2025-1C**: puede haber cambiado. Duda abierta en `wiki/dudas.md`.
- El **RAT y el parcial más recientes se reservan sin abrir** para simulacro previo al parcial.

## Carpetas del wiki

`temas/` una página por unidad · `fuentes/` una ficha por fuente ingerida · `conceptos/`
fallback. Las carpetas de tipo (`practicas/`, `definiciones/`, `comparativas/`, `casos/`,
`modelos/`, `frameworks/`) las crea `/ingest` a demanda.
