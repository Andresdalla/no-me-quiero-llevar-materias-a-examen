---
id: ingenieria-de-software-agil-2/modelos/principios-agiles
tipo: modelo
tema: U1
fuentes: [ut1-calidad-devops p.6]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Principios ágiles

Son el punto de partida declarado de la materia: lo que la cátedra da por sabido y sobre lo
que construye. Vale tenerlos textuales porque varios de ellos son la justificación directa de
prácticas de DevOps que aparecen después, y porque son material típico de un múltiple choice
sobre lectura previa.

## Qué modela

Modela cómo debería trabajar un equipo de desarrollo, expresado como doce principios y no como
un proceso. Esa forma importa: un principio no dice qué hacer el lunes, dice contra qué
criterio evaluar lo que se decidió hacer. La cátedra los ubica dentro de un encuadre de tres
frentes que la ingeniería de software moderna tiene que atender a la vez, negocio, tecnología
y equipo, y los doce principios son la respuesta del frente equipo.

## Axiomas

Los doce, en el orden en que los presenta la cátedra.

- Satisfacción del cliente mediante entrega temprana y continua de software valioso.
- Aceptar cambios, incluso tarde en desarrollo.
- Entrega frecuente de software funcionando.
- Colaboración entre personas del negocio y desarrolladores.
- Construir proyectos en base a equipos motivados, darles apoyo y confianza.
- La mejor forma de comunicación es cara a cara.
- Software funcionando como medida principal de progreso.
- Ritmo de desarrollo sostenible en el tiempo.
- Atención continua a la excelencia técnica y al buen diseño.
- Simplicidad, el arte de maximizar cantidad de trabajo no hecho.
- Equipos autoorganizados.
- En intervalos regulares, el equipo reflexiona y hace ajustes.

Cuatro de ellos se leen distinto una vez que se llega a DevOps. El primero y el tercero exigen
entregar seguido, que es lo que las prácticas de entrega continua vuelven posible sin romper
nada. El noveno, excelencia técnica y buen diseño, es el que la cátedra dice que Scrum deja
sin desarrollar. El duodécimo, reflexionar y ajustar en intervalos regulares, es la tercera de
[[modelos/tres-vias]] enunciada veinte años antes.

## Limitaciones

Los principios no dicen cómo cumplirlos, y varios entran en tensión entre sí sin que el modelo
diga cómo resolverla. Entregar frecuentemente y mantener excelencia técnica compiten por el
mismo tiempo, y decidir ese balance en cada caso es exactamente el trabajo que el modelo deja
fuera.

Ninguno de los doce menciona operación, mantenimiento ni el software una vez que está
corriendo. El progreso se mide con software funcionando, pero funcionando en la demo, no en
producción a las tres de la mañana. Ese hueco es el que la materia va a llenar.

## Críticas

El sexto principio, la comunicación cara a cara, envejeció peor que el resto: la cátedra
describe equipos globales, distribuidos e híbridos, con lo cual el principio o se reinterpreta
como sincronía y alto ancho de banda, o directamente no aplica.

La crítica más de fondo la hace la propia cátedra sobre el marco que popularizó estos
principios. Scrum es "un punto de partida", "puede ser mal aplicado", "tiene foco en la
gestión" y hay que "profundizar en los procesos de ingeniería". El diagnóstico es que los doce
principios se adoptaron como ceremonias de gestión sin las prácticas de ingeniería que los
harían ciertos, y [[definiciones/devops]] es el intento de corregir eso.

## Relacionado

- [[definiciones/devops]] — lo que la materia agrega sobre estos principios.
- [[modelos/tres-vias]] — el duodécimo principio reaparece ahí como tercera vía.
- [[definiciones/calidad-de-software]] — la excelencia técnica del noveno principio, ya instrumentada.

## Procedencia

- **Qué modela** — ut1-calidad-devops p.2, p.6 · incluye comentario del sistema
- **Axiomas › Los doce** — ut1-calidad-devops p.6
- **Axiomas › Lectura desde DevOps** — sin cita: comentario del sistema
- **Limitaciones** — sin cita: comentario del sistema
- **Críticas › Cara a cara** — ut1-calidad-devops p.5 · incluye comentario del sistema
- **Críticas › Scrum** — ut1-calidad-devops p.18 · incluye comentario del sistema
