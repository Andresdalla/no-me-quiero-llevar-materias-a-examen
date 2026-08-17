---
id: ingenieria-de-software-agil-2/modelos/dora-core
tipo: modelo
tema: U1
fuentes: [ut1-calidad-devops p.25, p.26, p.27]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# DORA Core Model

Es el modelo con el que la unidad cierra: la parte medible de todo lo anterior. Su valor está
en que no mide calidad ni madurez sino un encadenamiento causal, de las capacidades del equipo
al rendimiento de entrega y de ahí a los resultados de la organización, y ese encadenamiento
es lo que se pregunta.

## Qué modela

DORA es DevOps Research and Assessment. Su objetivo, en palabras de la cátedra, es "entregar
valor a través de servicios digitales en forma continua, rápida y estable", y "DORA CORE v2 es
un modelo basado en investigación para la mejora de las organizaciones que producen software,
relaciona 'capabilities' con 'performance'". El diagrama lo enuncia como una cadena de dos
flechas: las capacidades predicen el rendimiento, y el rendimiento predice los resultados.
Está descripto como "cómo las capacidades de un equipo DevOps influyen en el rendimiento y,
finalmente, en los resultados organizacionales y el bienestar del equipo".

La dirección de las flechas es el contenido del modelo. No dice que los equipos buenos tengan
buenas métricas: dice que ciertas capacidades concretas producen mejor rendimiento de entrega,
y que ese rendimiento produce mejores resultados de negocio y mejor bienestar del equipo. Por
eso las cuatro métricas no son un objetivo en sí, son el eslabón del medio.

## Axiomas

El modelo tiene tres bloques encadenados. Las capacidades se agrupan según las tres vías del
Handbook, lo cual no es casualidad.

| Bloque | Contenido |
|---|---|
| Capabilities › Climate for learning | code maintainability · documentation quality · empowering teams to choose tools · generative culture |
| Capabilities › Fast flow | continuous delivery · database change management · deployment automation · flexible infrastructure · loosely coupled teams · streamlining change approval · version control · working in small batches |
| Capabilities › Fast feedback | continuous integration · monitoring and observability · resilience engineering · pervasive security · test automation · test data management |
| Performance › Software delivery, medido por las four key metrics | change lead time · deployment frequency · change fail percentage · failed deployment recovery time |
| Performance › Reliability, medido por SLOs | measurement coverage · measurement focus · target optimization · target compliance |
| Outcomes › Organizational performance | commercial performance · non-commercial performance |
| Outcomes › Well-being | job satisfaction · productivity · reduced burnout · reduced rework |

Que bienestar del equipo esté en la misma caja que el rendimiento comercial es una afirmación
del modelo, no un adorno: sostiene que reducir el burnout y reducir el retrabajo son resultados
del mismo sistema que produce la entrega rápida, y no un costo a pagar por ella.

## Las cuatro métricas y sus dos juegos de nombres

La lámina 25 y el diagrama de la lámina 27 nombran las mismas cuatro métricas de forma
distinta, y conviene tener los dos juegos porque un múltiple choice puede usar cualquiera.

| Lámina 25 | Core Model v2.0.0 | Qué mide |
|---|---|---|
| Lead Time for Changes | Change lead time | tiempo desde que el código se compromete hasta que corre en producción |
| Deployment Frequency | Deployment frequency | con qué frecuencia se despliega a producción |
| Change Failure Rate | Change fail percentage | qué porcentaje de cambios degrada el servicio |
| Mean Time to Recovery | Failed deployment recovery time | cuánto se tarda en recuperarse de un despliegue fallido |

Las dos primeras miden velocidad y las dos últimas estabilidad, y ese es el par que importa: el
argumento de DORA es que no hay que elegir entre ambas, porque los equipos que mejoran en las
de velocidad también mejoran en las de estabilidad. El cambio de nombre en la cuarta no es
cosmético. Mean Time to Recovery promedia recuperaciones de cualquier incidente, mientras que
failed deployment recovery time acota el alcance a los despliegues fallidos.

## Limitaciones

Las cuatro métricas miden el flujo de entrega, no el valor de lo entregado. Un equipo puede
alcanzar números de élite desplegando cambios que a nadie le sirven, y ninguna de las cuatro lo
detecta. La caja de Outcomes existe justamente para eso, pero es la que no tiene métricas
propias definidas en el modelo.

El modelo es correlacional y está construido sobre encuestas a la industria. La flecha dice
"predict", no "causa", y aplicarlo hacia atrás —adoptar las capacidades esperando el
rendimiento— asume una causalidad que el estudio no prueba. Tampoco cubre contextos donde
desplegar seguido es imposible por regulación o por el tipo de producto.

## Críticas

La crítica más frecuente es que las cuatro métricas se convierten en objetivo apenas se
publican, y ahí se degradan. Se sube la frecuencia de despliegue partiendo cambios sin valor,
se baja el tiempo de recuperación reclasificando incidentes. Medir cualquiera de las cuatro
sin mirar las otras tres es el atajo, y por eso el modelo insiste en que se leen juntas.

La segunda es que la clasificación en niveles de rendimiento se usa como ranking entre
organizaciones que no son comparables. El modelo se pensó para que un equipo se compare
consigo mismo a lo largo del tiempo.

## Relacionado

- [[modelos/tres-vias]] — las capacidades del modelo están agrupadas exactamente por sus tres vías.
- [[definiciones/devops]] — la definición de equipo cuyas capacidades el modelo mide.
- [[definiciones/deuda-tecnica]] — code maintainability, la primera capacidad listada, es su contracara.

## Procedencia

- **Qué modela** — ut1-calidad-devops p.25, p.26
- **Axiomas › Tabla** — ut1-calidad-devops p.27
- **Axiomas › Bienestar** — sin cita: comentario del sistema
- **Las cuatro métricas y sus dos juegos de nombres** — ut1-calidad-devops p.25, p.27 · incluye comentario del sistema · duda registrada en dudas.md
- **Limitaciones** — sin cita: comentario del sistema
- **Críticas** — sin cita: comentario del sistema
