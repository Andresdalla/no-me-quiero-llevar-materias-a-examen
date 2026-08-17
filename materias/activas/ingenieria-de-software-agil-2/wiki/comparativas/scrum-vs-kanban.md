---
id: ingenieria-de-software-agil-2/comparativas/scrum-vs-kanban
tipo: comparativa
tema: U1
fuentes: [ut1-kanban p.3, p.38]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Scrum vs. Kanban

La cátedra dedica una lámina entera a esta comparación y la usa para justificar por qué la
materia trabaja con Kanban. El argumento no es que Scrum esté mal, sino que su cadencia fija
choca con la entrega continua que DevOps necesita.

## Tabla

| | Scrum | Kanban |
|---|---|---|
| Estructura | definida con roles, artefactos y eventos | sistema flexible, se adapta a lo que ya manejas |
| Cadencia | sprints regulares de duración fija | flujo continuo gestionado por WIP |
| Entregas | al final de cada sprint | continua |
| Reuniones | daily, sprint planning, sprint review, retro | daily standup opcional, flow review, revisión de bloqueos |
| Adaptabilidad | cambios en el próximo sprint | cambios en cualquier momento |
| Uso típico | entornos donde se puede hacer un plan-driven por sprint con el valor de entregas incrementales; los cambios de requisitos en su gran mayoría pueden esperar al próximo sprint | entornos con más incertidumbre, flujo de trabajo continuo y prioridades dinámicas; entornos de DevOps; menos estructurado, pero requiere más compromiso, colaboración y autogestión en el equipo |

## Criterio de decisión

El criterio real es uno solo: si los cambios de requisitos pueden esperar al próximo sprint. Si
pueden, la cadencia fija de Scrum es una ventaja, porque protege al equipo de la interrupción y
da un punto de sincronización previsible con el negocio. Si no pueden, esa misma cadencia se
vuelve el problema, y el flujo continuo de Kanban es lo que corresponde.

El segundo criterio es de capacidad del equipo, y la fuente lo dice sin adornos: Kanban es
menos estructurado pero exige más compromiso, colaboración y autogestión. Scrum aporta
disciplina desde afuera mediante sus eventos; Kanban espera que el equipo la ponga. Elegir
Kanban con un equipo que no la tiene no da flexibilidad, da un tablero sin política.

## Cuándo elegir cada uno

- **Scrum**: elegilo cuando el trabajo se puede planificar por período, el valor se entrega en
  incrementos discretos y la mayoría de los cambios tolera esperar al próximo sprint.
- **Kanban**: elegilo cuando hay incertidumbre alta, prioridades que cambian dentro del
  período, o trabajo que llega de forma continua, y en particular cuando hay operación en
  producción, que es el caso de DevOps.

## Por qué Kanban acompaña mejor a DevOps

La lámina 3 lo plantea sobre el ciclo completo del producto. El trabajo se divide en discovery,
"building the right thing", con las etapas de definir el problema correcto y definir la
solución, y delivery, "building the thing right", con desarrollar y entregar con calidad y
después seguir validando en operación. El bucle Dev-Ops vive entero en la mitad de delivery y
no se detiene, así que el trabajo de operar no encaja en un sprint. La razón de fondo está en
la fila de entregas de la tabla: DevOps necesita entrega continua, y Scrum entrega al final de
cada sprint.

## Relacionado

- [[frameworks/kanban]] — el marco completo, con sus seis prácticas.
- [[definiciones/devops]] — la co-responsabilidad que exige el flujo continuo.
- [[modelos/principios-agiles]] — la crítica de la cátedra a Scrum como punto de partida.

## Procedencia

- **Tabla** — ut1-kanban p.38
- **Criterio de decisión** — ut1-kanban p.38 · incluye comentario del sistema
- **Cuándo elegir cada uno** — ut1-kanban p.38 · incluye comentario del sistema
- **Por qué Kanban acompaña mejor a DevOps** — ut1-kanban p.3, p.38 · incluye comentario del sistema
