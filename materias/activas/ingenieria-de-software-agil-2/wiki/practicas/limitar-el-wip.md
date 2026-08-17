---
id: ingenieria-de-software-agil-2/practicas/limitar-el-wip
tipo: practica
tema: U1
fuentes: [ut1-kanban p.12, p.17, p.30]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Limitar el WIP

Es la tercera práctica fundamental de Kanban y la única que impone una restricción real sobre
lo que el equipo puede hacer. Las otras cinco hacen visible el trabajo o lo miden; esta obliga
a dejar de empezar cosas, y por eso es la que más resistencia genera y la que más cambia el
comportamiento.

## Qué es

La cátedra la enuncia como "Restringe el trabajo en proceso – eficiencia. Reduce el 'batch
size'", y la resume en una consigna: "Stop starting, start finishing". En la práctica es un
número escrito en el encabezado de cada columna en curso del tablero, que fija cuántas tarjetas
puede haber ahí a la vez. Si la columna está llena, no entra nada nuevo hasta que salga algo, y
la persona que iba a empezar una tarea tiene que ir a ayudar a terminar una que ya está.

Su justificación cuantitativa es la ley de Little, que la unidad enuncia como
`Lead Time = WIP / Throughput`. La consecuencia que la cátedra extrae explícitamente es que
"si quiero reducir el Lead Time debo reducir el WIP o aumentar el Throughput". De las dos
palancas, bajar el WIP es la que está bajo control inmediato del equipo: aumentar el throughput
depende de capacidad, herramientas o habilidad, y lleva tiempo. Ver
[[definiciones/indicadores-de-flujo]].

## Cuándo aplica

Aplica cuando el problema del equipo es que empieza más de lo que termina, y se detecta antes
de medir nada: muchas tarjetas en columnas intermedias, tareas que llevan semanas sin moverse,
gente que responde "estoy en cinco cosas". La cátedra asocia el WIP alto a "cuellos de botella,
sobrecarga, falta de foco", que son exactamente los síntomas que el límite ataca.

También aplica como instrumento de diagnóstico, y este es el uso menos obvio. Poner un límite
bajo hace que el sistema se trabe rápido y en un lugar preciso, y ese lugar es el cuello de
botella real. Un tablero sin límites nunca se traba, así que nunca señala nada.

## Cuándo NO aplica

No aplica tal cual cuando el trabajo del equipo es mayoritariamente reactivo y no
planificable. En un equipo de guardia, la llegada de incidentes no respeta ningún límite, y
poner uno estricto sobre una columna que se llena sola solo produce una regla que todos violan.
Ahí el instrumento es una calle aparte en el tablero con su propia política, no un límite
uniforme.

Tampoco aplica antes de la primera práctica. Limitar el WIP de un flujo que nadie mapeó pone un
número sobre etapas que no representan cómo trabaja el equipo, y el resultado es que el límite
se ajusta hasta volverse inofensivo. El orden de las seis prácticas de [[frameworks/kanban]] no
es decorativo: primero se visualiza el flujo real, después se lo restringe.

El caso restante es el de un equipo con un solo integrante por especialidad y dependencias
externas fuertes. El límite no puede resolver lo que está bloqueado afuera, y confundir
bloqueo externo con exceso de WIP lleva a bajar el límite hasta que nadie puede trabajar.

## Antipatrón

El antipatrón concreto es el **límite negociado a la suba**: cada vez que el tablero se traba,
el equipo aumenta el número en vez de terminar lo que está trabado. Después de tres o cuatro
rondas el límite queda por encima de la cantidad de trabajo que nunca se supera, con lo cual la
columna nunca se llena y la práctica dejó de existir aunque el número siga escrito.

La forma degradada hermana es el WIP declarado y no respetado: el límite dice cuatro, hay ocho
tarjetas, y nadie lo menciona. Se detecta con una sola pregunta en la revisión de flujo, y es
la razón por la que la práctica 2, políticas explícitas, tiene que incluir qué se hace cuando
el límite se alcanza.

## Relacionado

- [[frameworks/kanban]] — la práctica 3 dentro del marco completo.
- [[definiciones/indicadores-de-flujo]] — la ley de Little, que la justifica.
- [[modelos/tps-toyota]] — el WIP es el inventario que Toyota no podía financiar.

## Procedencia

- **Qué es** — ut1-kanban p.12, p.17, p.30
- **Cuándo aplica** — ut1-kanban p.28 · incluye comentario del sistema
- **Cuándo NO aplica** — sin cita: comentario del sistema
- **Antipatrón** — sin cita: comentario del sistema
