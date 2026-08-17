---
id: ingenieria-de-software-agil-2/definiciones/indicadores-de-flujo
tipo: definicion
tema: U1
fuentes: [ut1-kanban p.26, p.27, p.28, p.29, p.30, p.31, p.33, p.36]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Indicadores de flujo

Son las cuatro medidas con las que Kanban gestiona el flujo: WIP, cycle time, lead time y
throughput. Importan porque son la parte cuantitativa de la unidad y porque la relación entre
tres de ellas es una igualdad, no una intuición, lo cual las vuelve el material más
examinable de U1.

## Enunciado

Los cuatro se definen por dónde empiezan y dónde terminan sobre el tablero, y esa geometría es
la definición. El lead time abarca todo el recorrido, desde que el ítem entra al backlog hasta
que queda released. El cycle time abarca desde que el trabajo efectivamente empieza, o sea
desde la primera columna en curso, hasta released. El WIP es la cantidad de ítems que en un
momento dado están en las columnas en curso, sin contar backlog ni released.

De ahí sale la lectura que la cátedra remarca: "Lead Time – Cycle Time mide el tiempo que las
tareas están en espera antes de comenzar". La diferencia entre ambos no es un residuo
estadístico sino una cantidad con significado: es la cola. Si el lead time es largo y el cycle
time es corto, el problema no es la ejecución sino que las tarjetas esperan.

El throughput se define aparte, sobre un período en vez de sobre un ítem: "cantidad de tareas o
ítems fueron totalmente finalizados en un período de tiempo específico", escrito como
`Count(Items, t)`. La cátedra lo ubica por analogía: "así como en SCRUM se usa Velocity en
Kanban se usa Throughput". Medido por etapa, "puede ayudar a identificar cuellos de botella o
áreas donde el flujo se ralentiza".

## Notación

La ley de Little enuncia la relación entre tres de los cuatro:

```
Lead Time = WIP / Throughput
```

con "WIP (Work in Progress) = cantidad de elementos en el Doing en un momento dado" y
"Throughput = cantidad de elementos entregados al cliente en un periodo dado". De la igualdad
la cátedra deriva la única palanca disponible: "si quiero reducir el Lead Time debo reducir el
WIP o aumentar el Throughput". Es la justificación formal de [[practicas/limitar-el-wip]], y
también la razón por la que las tres medidas no se pueden mejorar de a una sin mirar las otras.

## Ejemplo

La interpretación de los valores está enunciada en la fuente. Un WIP "muy alto" indica "cuellos
de botella, sobrecarga, falta de foco", y uno bajo que "se podrían tomar más tareas o hay
inactividad por alguna causa". Un ciclo corto "suele ser positivo, flujo rápido y eficiente",
y uno largo apunta a "problemas de capacidad del equipo, complejidad tareas,
priorización/dependencias". Sobre el lead time, "un tiempo de entrega corto indica un servicio
más rápido y mayor satisfacción del cliente".

El ejemplo trabajado de la cátedra es un histograma de throughput diario cuya moda es 3 tareas,
con media 3.43 y mediana 3, y del que concluye que "tomaría entre 3 y 4 para planificar". Los
días de 9, 10 y 12 tareas los marca como picos a investigar, porque "capaz que hay algo que se
puede replicar", y los de 1 tarea como días a revisar. La moraleja del ejemplo es que se
planifica con el valor típico y se investigan los extremos, no al revés.

## Contraejemplo

El caso que muestra qué parte de la definición importa es el histograma de lead time: "80% de
las tareas se completan en 6 días o menos", y "las tareas que llevan 9-10 días son menos del
10%, por lo que se puede considerar valores atípicos". Un promedio de lead time sobre esos
mismos datos quedaría empujado por los outliers y prometería un plazo que el equipo cumple casi
siempre por adelantado y a veces por mucho. El indicador se define sobre la distribución, no
sobre la media, y comprometerse con un percentil es lo que la vuelve una expectativa honesta.

## Confusiones frecuentes

La confusión número uno es intercambiar lead time y cycle time. El truco para no fallar es
recordar de quién es cada reloj: el lead time es el del cliente, que empieza a contar cuando
pide; el cycle time es el del equipo, que empieza cuando toma la tarjeta. Como el primero
contiene al segundo, el lead time nunca puede ser menor.

La segunda es tratar el throughput como productividad individual. Se mide sobre el sistema y en
un período, y subirlo partiendo tarjetas en pedazos más chicos no entrega más valor: sube el
número sin mover nada. La tercera es leer un indicador solo. El objetivo declarado del flujo
óptimo pide "Lead Time y Cycle Time relativamente estables y predecibles" y "Throughput sin
grandes variaciones": lo que se busca es predictibilidad, no un récord. Se conecta con
[[modelos/dora-core]], donde el mismo razonamiento aparece aplicado a la entrega en producción.

## Relacionado

- [[practicas/limitar-el-wip]] — la práctica que la ley de Little justifica.
- [[frameworks/kanban]] — la práctica 5, gestionar y medir el flujo.
- [[modelos/dora-core]] — change lead time es el mismo indicador llevado al despliegue.

## Procedencia

- **Enunciado › Geometría sobre el tablero** — ut1-kanban p.26 · incluye comentario del sistema
- **Enunciado › Lead time menos cycle time** — ut1-kanban p.27, p.28 · incluye comentario del sistema
- **Enunciado › Throughput** — ut1-kanban p.29, p.30
- **Notación** — ut1-kanban p.30 · incluye comentario del sistema
- **Ejemplo › Interpretación de valores** — ut1-kanban p.28
- **Ejemplo › Histograma de throughput** — ut1-kanban p.33 · incluye comentario del sistema
- **Contraejemplo** — ut1-kanban p.36 · incluye comentario del sistema
- **Confusiones frecuentes › Flujo óptimo** — ut1-kanban p.31
- **Confusiones frecuentes › Resto** — sin cita: comentario del sistema
