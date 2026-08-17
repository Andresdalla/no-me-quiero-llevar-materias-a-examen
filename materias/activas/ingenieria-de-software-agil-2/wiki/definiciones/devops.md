---
id: ingenieria-de-software-agil-2/definiciones/devops
tipo: definicion
tema: U1
fuentes: [ut1-calidad-devops p.18, p.19, p.20, p.21, p.22]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# DevOps

DevOps es la respuesta que la materia da a la pregunta de cómo se sostiene la calidad en
servicios digitales que están vivos en producción. Se entiende mejor por el problema que
disuelve que por su enunciado: dos áreas con objetivos legítimos y opuestos, separadas por un
silo, que se bloquean mutuamente.

## Enunciado

La cátedra lo define por el equipo, no por las herramientas: "Un equipo DevOps es un equipo
donde todos están comprometido y son responsables de: la entrega continua de nuevas
funcionalidades, mejoras tecnológicas, innovación, de manera rápida y eficiente, sin
comprometer la calidad del software ni la estabilidad de las operaciones". Lo que hace la
definición es cerrar la escapatoria de repartir los objetivos entre dos grupos: si todos son
responsables de las dos mitades, ninguna se puede sacrificar por la otra sin que sea una
decisión del mismo equipo.

El conflicto que resuelve está enunciado como dos columnas. Del lado de Development,
"Nuevas features", "Velocidad de cambios" y "Experimentos". Del lado de IT Operations,
"Confiabilidad", "Estabilidad" y "Seguridad". La cátedra lo llama el camino del medio, con
dos silos y fricción, y lo contrapone al camino nuevo, donde la cadena Code, Build, Test,
Release, Operate la recorre un solo equipo. Ninguna de las dos columnas está equivocada, y por
eso el problema no se arregla convenciendo a un lado.

Los rasgos con los que la cátedra caracteriza a DevOps son co-responsabilidad, colaboración
interdisciplinaria y comunicación, entrega continua de valor, estabilidad, seguridad y
disponibilidad, respuesta rápida, apoyo en automatización, y experimentación y mejora
continua. La automatización aparece como apoyo y no como definición, lo cual importa: es lo
que separa esta definición de la lectura que reduce DevOps a un conjunto de herramientas.

## Notación

El ciclo se dibuja como un bucle infinito con dos lóbulos. El izquierdo agrupa Plan, Discover,
Build y Test; el derecho, Deploy, Operate y Observe; el cruce entre ambos es Continuous
Feedback, y todo el bucle está rodeado por Collaboration and Communication. Que sea un bucle y
no una línea es el punto: operar alimenta lo que se planifica.

## Ejemplo

Un equipo que despliega, recibe la alerta de su propio servicio a las tres de la mañana y
corrige el código que escribió cumple la definición, porque las dos responsabilidades caen en
las mismas personas. La retroalimentación del incidente vuelve a la planificación sin
atravesar una frontera organizativa.

## Contraejemplo

Crear un área llamada DevOps que recibe los artefactos de desarrollo y los despliega no es
DevOps: es el mismo silo con otro nombre, y hasta agrega uno. Ilustra qué parte del enunciado
se está incumpliendo, la de que todos son responsables de ambas mitades. El caso de la
lámina 19 es exactamente ese, dos silos con fricción, y es lo que la definición viene a
reemplazar.

## Confusiones frecuentes

La confusión número uno es identificar DevOps con una pila de herramientas. Se detecta con una
pregunta: si el pipeline está automatizado pero la responsabilidad por la estabilidad sigue
siendo de otro equipo, no hay DevOps por más herramientas que haya.

La segunda es tratarlo como reemplazo de ágil. La cátedra lo ubica como continuación: Scrum es
"un punto de partida" que "puede ser mal aplicado", "tiene foco en la gestión" y hay que
"profundizar en los procesos de ingeniería". DevOps agrega co-responsabilidad sobre operación
y mantenimiento a los [[modelos/principios-agiles]], no los sustituye. El desarrollo concreto
de cómo se hace está en [[modelos/tres-vias]], y la forma de medir si funcionó en
[[modelos/dora-core]].

## Relacionado

- [[modelos/tres-vias]] — los principios con los que el Handbook operacionaliza esta definición.
- [[modelos/dora-core]] — cómo se mide si el equipo efectivamente logra ambas mitades.
- [[definiciones/calidad-de-software]] — la demanda de calidad que motiva todo el planteo.
- [[modelos/principios-agiles]] — el punto de partida que DevOps extiende.

## Procedencia

- **Enunciado** — ut1-calidad-devops p.20, p.21, p.22 · incluye comentario del sistema
- **Notación** — ut1-calidad-devops p.23 · incluye comentario del sistema
- **Ejemplo** — sin cita: comentario del sistema
- **Contraejemplo** — ut1-calidad-devops p.19 · incluye comentario del sistema
- **Confusiones frecuentes › Reemplazo de ágil** — ut1-calidad-devops p.18 · incluye comentario del sistema
- **Confusiones frecuentes › Herramientas** — sin cita: comentario del sistema
