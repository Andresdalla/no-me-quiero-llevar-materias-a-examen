# Base de evidencia de la capa de estudio

Por qué el sistema estudia como estudia. **No todo vale igual**: cada afirmación de acá
tiene un nivel, y el nivel determina si se implementa como mecanismo, como opción, o si no
se implementa.

Este archivo es la referencia de las fases 9-15. Antes de agregar, sacar o degradar una
función de estudio, leelo. En particular, la sección "Sobre el resumen" existe para que un
`/reperfilar` futuro no degrade `/resumen` por una lectura apurada de la literatura.

**No trates una metáfora pedagógica como si fuera un mecanismo.**

## Nivel A — evidencia fuerte

| Hallazgo | Fuente | Implicancia de diseño |
|---|---|---|
| **Práctica de recuperación**: alta utilidad, generaliza por edad, capacidad y materia | Dunlosky, Rawson, Marsh, Nathan & Willingham (2013), *Psychological Science in the Public Interest* 14(1):4-58 | Existe una vía de recuperación activa siempre disponible junto a la de lectura |
| **Práctica distribuida**: alta utilidad, misma generalización | ídem | El sistema informa cuánto hace que no tocás un tema. Informa, no obliga |
| **Recuperación a criterio, repetida en días distintos**, retiene mucho más que una sola pasada | Rawson & Dunlosky (2011, 2013); Rawson, Dunlosky & Sciartelli (2013), *Educational Psychology Review* 25:523-548 | Justifica que `/repasar` insista dentro de la sesión hasta que la recuperes bien |
| **Más de 3 sesiones de reaprendizaje deja de rendir** | Rawson & Dunlosky (2022), *Current Directions in Psychological Science* | Techo: un tema con 3 sesiones buenas se considera estable. No perseguir dominio infinito |

## Nivel B — evidencia moderada o condicionada

| Hallazgo | Fuente | Matiz obligatorio |
|---|---|---|
| **Interrogación elaborativa** ("¿por qué es cierto esto?") | Dunlosky et al. (2013), utilidad moderada | Se implementa en el perfil `anotado` de `/resumen` |
| **Autoexplicación** | ídem | Base del modo `feynman` de `/profesor` |
| **Práctica intercalada** | Brunmair & Richter (2019): g≈0.34 en tareas matemáticas, ambiguo en textos expositivos | **Solo intercalar ítems confundibles entre sí.** Intercalar temas no relacionados no aporta |
| **Dificultades deseables / generación previa** | Brown, Roediger & McDaniel, *Make It Stick* (2014) | Bien fundado conceptualmente; efectos variables según la tarea |
| **Taxonomía de Anderson & Krathwohl (2001)** | revisión de Bloom | Es un **framework de diseño, no un hallazgo empírico.** La jerarquía estricta está discutida. Se usa solo como generador de preguntas por nivel en `/profesor` |

## Sobre el resumen — leer con cuidado antes de tocar `/resumen`

Dunlosky et al. (2013) califican "summarization" como de baja utilidad. **Esa calificación se
refiere a una actividad específica y no debe extenderse más allá de ella.** Lo que el estudio
evalúa es al estudiante escribiendo resúmenes como técnica, con dos problemas: la calidad
varía enormemente según el entrenamiento previo, y frecuentemente se hace copiando sin
reelaborar.

Lo que el estudio **no** dice:

- No dice que un resumen sea mal material de referencia.
- No dice que organizar el material no sirva.
- No dice nada sobre resúmenes generados por otra fuente y usados como andamiaje.

La distinción operativa que sí se sostiene:

| Actividad | Qué es en realidad | Fuerza |
|---|---|---|
| Leer repetidamente un resumen ya hecho | Relectura | Débil |
| **Producir** un resumen reelaborando, con las fuentes cerradas | Recuperación libre + organización | Fuerte |
| Usar un resumen como estructura y trabajar sobre él | Andamiaje | Legítimo, bien establecido |

**Instrucción para el implementador:** `/resumen` es una función central del sistema.
Prohibido agregarle advertencias, banners de "esto no es estudiar", o métricas que penalicen
su uso. Lo único que corresponde es **ofrecer** perfiles adicionales que lleven hacia la
columna de arriba (`esqueleto`, `ciego`, `anotado`), como opciones, no como reproches.

## Nivel C — metáfora pedagógica, NO implementar como mecanismo

- **Modo enfocado vs. modo difuso** (Oakley) y las analogías de "grosor sináptico" o "el
  mortero que fragua": son recursos didácticos. La red neuronal por defecto en la que se
  apoyan sigue en disputa científica.
- **Qué sí conservar**: la prescripción práctica —espaciar entre días, dormir entre sesiones,
  alternar trabajo y descanso— ya justificada por práctica distribuida y consolidación
  durante el sueño, sin necesidad de la metáfora.
- **Prohibido en el repo**: afirmaciones neurobiológicas. El sistema habla de conducta y
  retención medida, no de sinapsis.

## Dos decisiones de producto

No salen de la literatura: son decisiones. No se revierten sin que el usuario lo pida.

1. **El resumen es una función de primera clase.** El usuario estudia con resúmenes y le
   funciona. No se degrada, no se advierte contra él, no se mide como "estudio pasivo".
2. **No hay scheduler.** Nada de tarjetas vencidas, colas diarias, rachas ni deuda
   acumulada. El usuario decide qué y cuándo estudia. El sistema informa y sugiere; nunca
   encola ni presiona.
