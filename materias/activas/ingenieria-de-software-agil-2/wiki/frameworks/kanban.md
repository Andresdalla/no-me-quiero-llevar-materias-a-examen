---
id: ingenieria-de-software-agil-2/frameworks/kanban
tipo: framework
tema: U1
fuentes: [ut1-kanban p.12, p.13, p.14, p.15, p.16, p.18, p.19, p.20, p.21, p.39]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Kanban

La cátedra lo presenta con una advertencia en el título de lámina: Kanban es "mucho más que un
tablero". Lo que define al marco no es la herramienta sino seis prácticas fundamentales y una
forma de adopción que no pide reorganizar nada antes de empezar, y eso último es lo que lo
hace encajar con DevOps.

## Roles

Kanban no define roles propios, y esa ausencia es deliberada. La regla de adopción dice
"Respeta roles y responsabilidades actuales", junto con "Empieza con lo que haces ahora" y
"Hazlo en forma incremental y evolutivo". La consecuencia práctica es que la adopción no
requiere una reorganización previa: se aplica sobre la estructura existente y los cambios de
responsabilidad aparecen después, como resultado de lo que el tablero deja ver.

| Responsabilidad | Quién la asume |
|---|---|
| Definir y mantener el flujo y sus etapas | el equipo, sobre su cadena de valor real |
| Acordar y hacer explícitas las políticas de movimiento | el equipo en conjunto |
| Respetar el límite de WIP y desbloquear antes de empezar algo nuevo | cada integrante |
| Revisar indicadores y proponer experimentos de mejora | el equipo, con datos del tablero |

Esa tabla es una lectura del sistema, no una lista de la fuente: la fuente lo que dice es que
los roles previos se conservan.

## Artefactos

El tablero es el artefacto central, organizado en columnas que representan las etapas del
flujo, con etiquetas para agregar información visual. El ejemplo de la cátedra usa etiquetas de
funcionalidad, prioridad y estado en proceso. Cada columna en curso lleva su límite de WIP
escrito en el encabezado, de modo que la restricción es parte del artefacto y no una regla
aparte.

El flujo de ejemplo tiene seis etapas, cada una con su definición: backlog, "fase inicial donde
se recopilan y priorizan las tareas"; análisis, "evaluación y planificación detallada de los
requisitos"; develop, "fase de codificación donde se escribe el código del software"; testing,
"fase de prueba para identificar y corregir errores"; release, "lanzamiento del producto a los
usuarios finales"; y released, "estado post-lanzamiento donde se monitorea el rendimiento". A
las etapas se les suman estados intermedios cuando hace falta visualizar una espera, por
ejemplo testing completado o user story ready.

Las políticas explícitas son el tercer artefacto y el más olvidado. Son las reglas de
movimiento entre columnas, escritas: el ejemplo de la cátedra es que una tarjeta pasa a done en
testing "porque ha cumplido todas las pruebas", y en entornos más complejos se explicita qué
tipos de prueba, en general o por funcionalidad.

## Ceremonias

Las seis prácticas fundamentales son la estructura del marco, en el orden en que la cátedra
las numera.

| Práctica | Propósito | Frecuencia |
|---|---|---|
| 1. Focalizar y visualizar el flujo | "Establece un flujo claro y visual del trabajo basado en la cadena de valor" | al empezar, y se ajusta al aprender |
| 2. Hacer las políticas explícitas | fijar por escrito las reglas de movimiento entre columnas | al empezar, se revisa al cambiar el proceso |
| 3. Limitar el WIP | "Restringe el trabajo en proceso – eficiencia. Reduce el 'batch size'" | permanente, revisable por evidencia |
| 4. Ciclos de retroalimentación | "Implementa ciclos regulares de retroalimentación" | continua, en varios niveles a la vez |
| 5. Gestionar y medir el flujo | "Para evaluar y optimizar el flujo de trabajo y la entrega de valor" | continua, con indicadores |
| 6. Mejora continua y experimentación (kaizen) | ajustar el sistema con evidencia | continua |

Los ciclos de retroalimentación de la práctica 4 se implementan con cuatro mecanismos
concretos: niveles de feedback, que involucran "a todos los interesados en el proceso";
reuniones diarias, "reuniones breves para sincronizar el trabajo y abordar los impedimentos";
revisión del flujo de trabajo, "evaluación de procesos para mayor eficiencia"; y
retrospectivas, "reflexiones sobre el trabajo pasado para identificar mejoras". El criterio que
los une está enunciado como "flujo constante de retroalimentación en toda la cadena de valor.
Permite una detección y recuperación rápida. Así se crea calidad en forma continua".

La práctica 5 persigue objetivos explícitos: "maximizar valor entregado y calidad", "mejorar
tiempos de entrega", "incrementar predictibilidad" y "facilitar la mejora continua", todo bajo
mejora continua basada en evidencia. Los indicadores con que se hace están en
[[definiciones/indicadores-de-flujo]]. La práctica 6, kaizen, se implementa mediante
experimentación y aprendizaje incremental, un enfoque colaborativo y basado en datos, evolución
del sistema según las necesidades del equipo y del negocio, empoderamiento del equipo, y
optimización del flujo reduciendo desperdicios.

## Por qué acompaña a DevOps

La cátedra cierra con cuatro razones. Kanban "hace explícito y visible el flujo de valor",
representándolo en un tablero que integra todas las áreas involucradas y fomentando
responsabilidad compartida. Optimiza el flujo, porque permite detectar cuellos de botella y
usa el WIP para evitar sobrecarga. Facilita la entrega continua, ya que "no depende de ciclos
predefinidos" y "se adapta mejor a los principios de CI/CD". Y fomenta la retroalimentación
entre Ops y Dev, no solo en una dirección sino entre todas las etapas del proceso.

## Críticas

La adopción incremental es su mayor virtud y su mayor riesgo. Empezar con lo que se hace ahora
y respetar los roles actuales permite arrancar sin permiso de nadie, pero también permite
quedarse ahí: un tablero que refleja el proceso disfuncional existente, sin límites de WIP ni
políticas escritas, no cambia nada y da la sensación de que sí. La propia cátedra ataca esto de
frente con el título "mucho más que un tablero".

La segunda crítica es la contracara de no tener estructura. La comparación de la cátedra lo
dice sin rodeos: Kanban es "menos estructurado, pero requiere más compromiso, colaboración y
autogestión en el equipo". Un equipo sin esa autogestión obtiene de Scrum una disciplina que
Kanban da por supuesta. Ver [[comparativas/scrum-vs-kanban]].

## Relacionado

- [[practicas/limitar-el-wip]] — la práctica 3, desarrollada aparte.
- [[definiciones/indicadores-de-flujo]] — con qué se mide la práctica 5.
- [[comparativas/scrum-vs-kanban]] — cuándo conviene cada uno.
- [[modelos/tps-toyota]] — de dónde salen las tarjetas y el enfoque pull.

## Procedencia

- **Roles › Regla de adopción** — ut1-kanban p.12
- **Roles › Tabla** — sin cita: comentario del sistema
- **Artefactos › Tablero y políticas** — ut1-kanban p.15, p.16, p.37
- **Artefactos › Etapas del flujo** — ut1-kanban p.13, p.14
- **Ceremonias › Las seis prácticas** — ut1-kanban p.12
- **Ceremonias › Mecanismos de retroalimentación** — ut1-kanban p.18, p.19
- **Ceremonias › Objetivos de gestión y kaizen** — ut1-kanban p.20, p.21
- **Por qué acompaña a DevOps** — ut1-kanban p.39
- **Críticas** — ut1-kanban p.5, p.38 · incluye comentario del sistema
