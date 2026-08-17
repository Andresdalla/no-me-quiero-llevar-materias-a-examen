---
id: ingenieria-de-software-agil-2/modelos/tres-vias
tipo: modelo
tema: U1
fuentes: [ut1-calidad-devops p.24, isa2-temario p.1]
estado: esbozo
dominio: 0
actualizado: 2026-08-16
---

# Las tres vías

Son los tres principios con los que *The DevOps Handbook* organiza todo lo demás. Importan
estructuralmente en esta materia: las cinco unidades del programa siguen su orden, así que
saber a qué vía pertenece una práctica es saber en qué parte del curso está y qué problema
viene a resolver.

## Qué modela

Modela el trabajo de un equipo DevOps como tres bucles anidados, cada uno más lento y más
amplio que el anterior. El primero mueve trabajo hacia producción, el segundo devuelve
información desde producción, y el tercero convierte esa información en cambios sobre cómo
trabaja la organización. La cátedra las nombra Flow, Feedback, y Learning and experimentation,
y el temario las traduce como los principios del flujo, del feedback, y del aprendizaje y la
experimentación continuas.

## Axiomas

Cada vía se enuncia con tres reglas en las láminas. La primera vía, Flow: "Identificar value
streams", "Entrega rápida y continua de valor" y "Equipo optimizando todo el flujo". La regla
que hace la diferencia es la tercera, porque optimizar todo el flujo y no cada etapa es lo que
impide que un área mejore su número local empeorando el total.

La segunda vía, Feedback: "Crear feedback loops en todos los niveles", "Encontrar los problemas
tempranamente" y "Evitar barreras entre equipos". El feedback solo sirve si llega antes de que
el problema se vuelva caro, y de ahí que las prácticas de esta vía se concentren en acortar el
tiempo entre que algo se rompe y que alguien se entera.

La tercera vía, Learning and experimentation: "Permitir aprender de los fallos", "Mejora
continua iterativa" y "Cultura segura para experimentar". Es la única de las tres que no se
puede automatizar: las dos primeras se apoyan en herramientas, esta se apoya en cómo reacciona
la organización cuando algo sale mal.

## Limitaciones

El modelo ordena principios, no da mecánica. Nada en las tres vías dice cómo identificar un
value stream ni cuál es un tiempo de feedback aceptable, y por eso las unidades siguientes del
programa son casi todas prácticas concretas: la vía dice hacia dónde, no cuánto ni con qué.

La tercera vía presupone algo que el modelo no puede producir por sí mismo. Una cultura segura
para experimentar depende de cómo la organización trata el error, y ninguna cantidad de
automatización la genera. Es la vía que más se cita y la que menos se implementa.

## Críticas

El orden sugiere una secuencia que en la práctica no se respeta: la mayoría de las
organizaciones adopta herramientas de la primera vía, algo de telemetría de la segunda, y
nunca llega a la tercera. Que el modelo sea acumulativo es su punto fuerte como argumento y su
punto débil como plan de adopción.

También es un modelo descriptivo construido sobre casos de empresas grandes de producto
digital. Trasladarlo a un contexto con despliegues regulados, ventanas de mantenimiento
pactadas o un solo cliente institucional exige revisar qué significa entrega continua ahí, y
el Handbook no hace ese trabajo.

## Relacionado

- [[definiciones/devops]] — la definición de equipo que estas tres vías operacionalizan.
- [[modelos/dora-core]] — las capacidades de fast flow y fast feedback son la contraparte medible.
- [[fuentes/isa2-temario]] — el mapeo de cada vía a las unidades del programa.

## Procedencia

- **Qué modela** — ut1-calidad-devops p.24 · isa2-temario p.1 · incluye comentario del sistema
- **Axiomas** — ut1-calidad-devops p.24 · incluye comentario del sistema
- **Limitaciones** — sin cita: comentario del sistema
- **Críticas** — sin cita: comentario del sistema
