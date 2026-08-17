---
id: ingenieria-de-software-agil-2/modelos/tps-toyota
tipo: modelo
tema: U1
fuentes: [ut1-kanban p.9, p.10]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Toyota Production System

Es de donde viene Kanban, y la cátedra lo cuenta porque explica por qué las prácticas son las
que son. Casi todo lo que después aparece en el tablero y en las métricas se entiende como
traducción de una decisión industrial de los años cincuenta, tomada bajo una restricción de
capital muy concreta.

## Qué modela

Modela la producción como un flujo tirado por la demanda en vez de empujado por la capacidad.
El problema que resuelve está planteado como contraste: "Ford & General Motors Línea de
fabricación fluida = fabricación de piezas para tener siempre disponible JUST IN CASE", contra
"Toyota no podia afrontar eso" por el costo de mantener inventario. La cátedra lista ese costo
como almacenamiento, seguro, deterioro y obsolescencia, y capital parado.

La solución vino de una analogía que la cátedra cuenta literalmente: "El Ing. Taiicho Ohno va
al supermercado". La góndola se repone cuando el cliente se lleva algo, no antes, y esa señal
de reposición es exactamente lo que hace una tarjeta Kanban entre dos estaciones. El inventario
deja de ser un colchón contra la incertidumbre y pasa a ser un síntoma de que alguien produjo
más rápido de lo que el siguiente consume.

## Axiomas

El TPS es "una filosofía" sostenida por tres pilares que la cátedra enuncia así.

- **Just in time**: "Lo necesario, cuando es necesario y en la cantidad necesaria", con
  "Enfoque PULL no PUSH". Las tarjetas Kanban "viajan entre estaciones para activar la
  producción Just-In-Time sin generar excesos".
- **Jidoka**: "Énfasis en la calidad. Automatización con un toque humano". Se enuncia como
  "Diseñamos equipos para detectar anomalías y detenerse automáticamente cuando ocurren.
  Equipamos a nuestros operadores con medios para detener el flujo de producción siempre que
  noten algo sospechoso". Los mecanismos asociados son andon y swarming, y la regla de fondo
  es que todo el equipo colabora cuando la línea se detiene.
- **Kaizen**: "Mejora continua. Los empleados están empoderados para identificar y solucionar
  problemas, optimizando procesos y reduciendo desperdicios".

Jidoka es el pilar que más se pierde al traducir a software y el que más rinde. Autorizar a
cualquiera a detener la línea invierte la prioridad por defecto: frenar sale más barato que
seguir produciendo sobre un defecto, y esa es la misma lógica que después justifica que un
build roto bloquee la integración.

## Limitaciones

Es un modelo de manufactura, y la analogía tiene un límite claro. Una pieza física es idéntica
a la anterior y su tiempo de producción es predecible, mientras que dos tareas de software con
el mismo tamaño aparente pueden diferir en un orden de magnitud. Todo lo que en Toyota es
variabilidad controlable, en software es variabilidad inherente, y por eso los indicadores de
flujo se leen como distribuciones y no como promedios.

Tampoco traslada bien la noción de inventario. En una línea, el trabajo en proceso ocupa
espacio y se ve; en software es invisible, y hay que decidir explícitamente contarlo. Esa es
justamente la razón de ser de [[practicas/limitar-el-wip]].

## Críticas

El relato de origen se cuenta como si el sistema fuera puro ingenio y no una respuesta a una
restricción de capital. Toyota adoptó pull porque no podía financiar inventario, no porque
hubiera descubierto una verdad universal, y en contextos donde el inventario es barato el
argumento pierde fuerza.

La otra crítica es la de siempre con lean: sin la parte de jidoka y kaizen, el just in time
solo aprieta el sistema hasta que cualquier variación se convierte en un paro. Adoptar el
tablero y los límites sin autorizar a nadie a detener la línea reproduce la presión sin el
mecanismo que la hace sostenible.

## Relacionado

- [[frameworks/kanban]] — la traducción a software de estos tres pilares.
- [[practicas/limitar-el-wip]] — el equivalente de no acumular inventario.
- [[definiciones/devops]] — kaizen reaparece como la tercera vía del Handbook.

## Procedencia

- **Qué modela** — ut1-kanban p.9 · incluye comentario del sistema
- **Axiomas › Pilares** — ut1-kanban p.10
- **Axiomas › Jidoka en software** — sin cita: comentario del sistema
- **Limitaciones** — sin cita: comentario del sistema
- **Críticas** — sin cita: comentario del sistema
