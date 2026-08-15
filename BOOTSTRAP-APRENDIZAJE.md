# BOOTSTRAP — ADDENDUM: capa de estudio

> **Requisito:** `BOOTSTRAP.md` completo (fases 0-8 en `OK`).
> **Uso:** guardá este archivo en la raíz junto a `BOOTSTRAP.md` y ejecutá
> `/loop lee BOOTSTRAP-APRENDIZAJE.md y ejecutá la siguiente fase pendiente`
> Aplica el **mismo protocolo de loop** de la sección 1 de `BOOTSTRAP.md`: una fase por iteración, un commit por fase, sin adelantarse. Agregá las fases 9-15 a `BUILD_STATE.md` como `PENDIENTE` en la primera iteración.

---

## 0. QUÉ AGREGA ESTE ADDENDUM

El sistema base compila conocimiento muy bien. Esta capa agrega las herramientas para **estudiarlo**: resúmenes en varios formatos, tarjetas de recuperación, un modo profesor con niveles, medición de calibración y explotación de exámenes de práctica.

**Dos decisiones de producto que son deliberadas y no se revierten durante la implementación:**

1. **El resumen es una función de primera clase.** El usuario estudia con resúmenes y le funciona. No se degrada, no se advierte contra ella, no se mide como "estudio pasivo". Lo que sí se hace es ofrecer perfiles adicionales que lo empujan hacia el modo productivo (ver Fase 14).
2. **No hay scheduler.** Nada de tarjetas vencidas, colas diarias, rachas ni deuda acumulada. El usuario decide qué y cuándo estudia. El sistema **informa y sugiere**; nunca encola ni presiona.

Todo lo demás en este documento respeta esas dos decisiones.

---

## 1. BASE DE EVIDENCIA — niveles, no todo vale igual

Al implementar, respetá estos niveles. **No trates una metáfora pedagógica como si fuera un mecanismo.**

### Nivel A — evidencia fuerte

| Hallazgo | Fuente | Implicancia de diseño |
|---|---|---|
| **Práctica de recuperación**: alta utilidad, generaliza por edad, capacidad y materia | Dunlosky, Rawson, Marsh, Nathan & Willingham (2013), *Psych Sci Public Interest* 14(1):4-58 | Existe una vía de recuperación activa siempre disponible junto a la de lectura |
| **Práctica distribuida**: alta utilidad, misma generalización | ídem | El sistema informa cuánto hace que no tocás un tema. Informa, no obliga |
| **Recuperación a criterio, repetida en días distintos**, retiene mucho más que una sola pasada | Rawson & Dunlosky (2011, 2013); Rawson, Dunlosky & Sciartelli (2013), *Educ Psychol Rev* 25:523-548 | Justifica que `/repasar` insista dentro de la sesión hasta que la recuperes bien |
| **Más de 3 sesiones de reaprendizaje deja de rendir** | Rawson & Dunlosky (2022), *Curr Dir Psychol Sci* | Techo: un tema con 3 sesiones buenas se considera estable. No perseguir dominio infinito |

### Nivel B — evidencia moderada o condicionada

| Hallazgo | Fuente | Matiz obligatorio |
|---|---|---|
| **Interrogación elaborativa** ("¿por qué es cierto esto?") | Dunlosky et al. (2013), utilidad moderada | Se implementa en el perfil `anotado` de `/resumen` |
| **Autoexplicación** | ídem | Base del modo `feynman` |
| **Práctica intercalada** | Brunmair & Richter (2019): g≈0.34 en tareas matemáticas, ambiguo en textos expositivos | **Solo intercalar ítems confundibles entre sí.** Intercalar temas no relacionados no aporta |
| **Dificultades deseables / generación previa** | Brown, Roediger & McDaniel, *Make It Stick* (2014) | Bien fundado conceptualmente; efectos variables por tarea |
| **Taxonomía de Anderson & Krathwohl (2001)** | revisión de Bloom | Es un **framework de diseño**, no un hallazgo. La jerarquía estricta está discutida. Usarla solo como generador de preguntas por nivel |

### Sobre el resumen — leer con cuidado antes de implementar

Dunlosky et al. (2013) califican "summarization" como de baja utilidad. **Esa calificación se refiere a una actividad específica y no debe extenderse más allá de ella.** Lo que el estudio evalúa es al estudiante escribiendo resúmenes como técnica, con dos problemas: la calidad varía enormemente según el entrenamiento previo, y frecuentemente se hace copiando sin reelaborar.

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

**Instrucción para el implementador:** `/resumen` es una función central del sistema. Prohibido agregarle advertencias, banners de "esto no es estudiar", o métricas que penalicen su uso. Lo único que corresponde es **ofrecer** perfiles adicionales que lleven hacia la columna de arriba (`esqueleto`, `ciego`, `anotado`), como opciones, no como reproches.

### Nivel C — metáfora pedagógica, NO implementar como mecanismo

- **Modo enfocado vs. modo difuso** (Oakley) y las analogías de "grosor sináptico" o "el mortero que fragua": son recursos didácticos. La red neuronal por defecto en la que se apoyan sigue en disputa científica.
- **Qué sí conservar**: la prescripción práctica —espaciar entre días, dormir entre sesiones, alternar trabajo y descanso— ya justificada por práctica distribuida y consolidación durante el sueño, sin la metáfora.
- **Prohibido** en el repo: afirmaciones neurobiológicas. El sistema habla de conducta y retención medida, no de sinapsis.

---

## 2. FASES

### FASE 9 — `global/metodo/evidencia.md` y reglas derivadas

Crear `global/metodo/evidencia.md` con **la sección 1 completa de este archivo**, incluida la subsección sobre el resumen (es la que evita que un futuro reperfilado lo degrade por error) y las citas completas.

Agregar al `CLAUDE.md` raíz un bloque de **≤15 líneas** (no más: es impuesto por sesión):

```
## Principios de estudio
- Dos vías igual de válidas: leer/reelaborar (resúmenes) y recuperar (tarjetas, profesor).
- /resumen es función central. Nunca advertir contra su uso ni penalizarlo.
- Tarjetas y preguntas SOLO desde contenido ✅. El material 🧠 nunca se evalúa.
- Sin scheduler: no hay colas, vencimientos, rachas ni deuda. El usuario elige qué y cuándo.
- El sistema informa ("hace 9 días que no tocás X") y sugiere. Nunca presiona.
- Intercalar solo ítems confundibles entre sí, nunca temas no relacionados.
- Nunca afirmar mecanismos neurobiológicos. Solo conducta y retención medida.
- Detalle y citas: global/metodo/evidencia.md
```

**Criterio de aceptación:** `evidencia.md` incluye la tabla de tres niveles, la subsección sobre el resumen con su instrucción explícita al implementador, y marca a Oakley como nivel C. El bloque en `CLAUDE.md` raíz no supera 15 líneas.

---

### FASE 10 — Tarjetas (sin motor de agendamiento)

Las tarjetas son un **recurso del que tirás cuando querés**, no una cola que te empuja. No hay `scheduler.jsonl`, no hay cajas, no hay fechas de vencimiento.

**Contenido — `materias/activas/<m>/cards/<tema>.md`:**

```markdown
---
tema: U3
generado: 2026-08-15
fuente_paginas: [teoremas/bombeo-regulares, definiciones/lenguaje-regular]
---

## c-U3-001 · concepto
**P:** Enunciá el lema de bombeo para lenguajes regulares.
**R:** Si L es regular, existe p≥1 tal que toda w∈L con |w|≥p se escribe w=xyz con
(1) |y|>0, (2) |xy|≤p, (3) ∀i≥0: xy^i z ∈ L.
**Fuente:** ✅ [sipser-cap1 p.78]
**Bloom:** recordar
**Confundible_con:** [c-U3-004]
**Visto:** 2026-08-15:ok, 2026-08-12:fallo
```

El campo `Visto` es **historial, no agenda**. Sirve para que `/repasar` priorice dentro de una sesión que vos iniciaste y para que `/estado` te informe. Nunca genera una obligación ni una fecha futura.

**Cuatro tipos de tarjeta, y ninguno más:**

| Tipo | Qué pregunta | De qué páginas sale |
|---|---|---|
| `concepto` | definición o enunciado, recuperación literal | `definicion`, `teorema`, `numeros` |
| `aplicacion` | usar el concepto en un caso concreto | `construccion`, `reduccion`, `ejercicio-tipo`, `caso` |
| `discriminacion` | distinguir dos cosas parecidas ("¿por qué esto NO es X sino Y?") | `comparativa` y todo par marcado `Confundible_con` |
| `cloze` | huecos en un enunciado formal o procedimiento | `teorema`, `protocolo`, `mecanismo` |

**Comando `/cards <tema> [--tipos a,b] [--max N]`:**
1. Rutear por `mapa.md`; cargar solo las páginas del tema.
2. **Generar exclusivamente desde contenido marcado `✅`.** Nunca desde `🧠`. Si una página no tiene contenido verificado, saltarla y reportarlo.
3. Máximo **12 tarjetas por página fuente**. Si el tema da para más, es señal de partirlo — avisar.
4. Poblar `Confundible_con` cruzando tarjetas del mismo tema y de temas hermanos. **Este campo es lo que habilita el intercalado útil**; sin él, intercalar es ruido.
5. Escribir/actualizar `cards/<tema>.md`. Commit propio.

**Reglas de calidad — rechazar tarjetas malas:**
- Nada de preguntas sí/no ni adivinables por eliminación.
- Nada de preguntas cuya respuesta esté en el enunciado.
- Una tarjeta = un ítem recuperable. Respuesta con más de ~4 elementos → partirla.
- Sin cita `✅` no se crea la tarjeta.

**Criterio de aceptación:** `/cards` documentado con los 4 tipos, la regla de solo-`✅`, el tope de 12 y el poblado de `Confundible_con`. **No existe ningún archivo de agenda ni campo de fecha futura en todo el sistema.**

---

### FASE 11 — `/repasar`: recuperación a demanda

Comando que **vos iniciás**, sobre el tema que **vos elegís**. Nunca se abre solo, nunca reclama.

**`/repasar <tema> [--n 15] [--tipos a,b] [--desde-errores]`**

1. Cargar `cards/<tema>.md`. **Nunca cargar páginas del wiki durante el repaso** — las tarjetas se bastan; el link a la página solo aparece si fallás.
2. Selección dentro de la sesión, en este orden de prioridad:
   - tarjetas con `fallo` en su último `Visto`,
   - tarjetas nunca vistas,
   - tarjetas con `origen: examen` (Fase 15),
   - el resto, las menos recientes primero.
3. **Ordenar con intercalado por confundibilidad**: alternar tarjetas ligadas por `Confundible_con`. Fuera de esos grupos, no intercalar.
4. Por cada tarjeta: pregunta → tu respuesta → **confianza 1-5 antes de revelar** (Fase 12) → respuesta → autocalificás `ok` / `parcial` / `fallo`.
   - Ante `fallo` o `parcial`: mostrar el link a la página del wiki y **volver a preguntarla más tarde en la misma sesión**. Esto es lo único que queda del criterio de recuperación, y opera dentro de la sesión, no entre días.
   - No explicar de nuevo durante el repaso. El repaso es recuperación, no clase.
5. Al cerrar: actualizar el campo `Visto` de las tarjetas tocadas, anexar a `estado/historial.md` y actualizar `estado/dominio.md` y `estado/calibracion.md`. Un commit por sesión.

**Presupuesto de tokens:** una sesión de 15 tarjetas cuesta leer 1-3 archivos de `cards/`. Si abre páginas del wiki fuera de un fallo, está mal implementada.

**Criterio de aceptación:** `/repasar` requiere que el usuario indique tema; no existe ningún modo que arranque solo ni que hable de "vencidas". La repetición dentro de la sesión ante fallo está implementada.

---

### FASE 12 — Calibración, niveles de Bloom y pre-test

**12.1 Calibración.** Es la función más valiosa de esta capa: mide la distancia entre lo que creés que sabés y lo que sabés. Funciona igual de bien para quien estudia con resúmenes — de hecho es justo la que detecta cuándo un resumen te dejó una sensación de dominio que no se corresponde.

- En `/repasar` y `/profesor`, pedir confianza **1-5 antes de revelar la respuesta**.
- `estado/calibracion.md` registra por tema: confianza media, acierto real, brecha.
- Alertas:
  - **Sobreconfianza** (confianza ≥4, acierto <60%): el riesgo real de parcial.
  - **Subconfianza** (confianza ≤2, acierto >80%): sabés más de lo que creés; dejá de reestudiar eso.
- `/estado` muestra la brecha por tema, no solo el dominio.

**12.2 Niveles de Bloom en `/profesor`.** Etiquetar cada pregunta con `recordar | comprender | aplicar | analizar | evaluar | crear`. El modo profesor **escala**: no pasa al nivel siguiente hasta ≥80% en el actual.
- Teoría de la computación: hasta `crear` (construir una MT, diseñar una reducción nueva).
- Seguridad: hasta `evaluar` (justificar una mitigación frente a alternativas).
- Materias de proceso: hasta `evaluar` sobre casos, que es lo que efectivamente toman.

Documentar en `evidencia.md` que esto es un framework de generación de preguntas, no un hallazgo empírico.

**12.3 `/pre-test <tema>`.** Antes de estudiar un tema, 5 preguntas que todavía no sabés responder. Vas a fallar casi todo, y ese es el punto: el intento fallido prepara el terreno para lo que estudies después (efecto de generación).
- Se genera desde `programa.md`, no desde el wiki: el tema puede no estar ingerido aún.
- **Avisar explícitamente que fallar es lo esperado**, o la experiencia desmoraliza.
- No cuenta para `dominio.md`.

**Criterio de aceptación:** la confianza se pide **antes** de revelar en ambos comandos. `calibracion.md` distingue sobre y subconfianza. `/pre-test` avisa que fallar es lo esperado.

---

### FASE 13 — `/plan` y `/estado` v2 (sugerencia, nunca cola)

**`/plan <materia> [--hasta AAAA-MM-DD]`** — produce una **propuesta de reparto**, no una agenda con obligaciones.

1. Leer `programa.md`, `dominio.md`, `calibracion.md`, `patron.md` (Fase 15) y los `Visto` de las tarjetas.
2. Distribuir los temas a lo largo de los días disponibles, sin acumular. Si el tiempo no alcanza, **decirlo explícitamente** en vez de fingir viabilidad: informar qué entra y qué no, y proponer priorización.
3. Priorizar por: (a) sobreconfianza detectada, (b) unidades sin cobertura, (c) puntaje en riesgo según exámenes (Fase 15), (d) tiempo sin tocar el tema.
4. Escribir `estado/plan.md` con días y el comando sugerido para cada uno.
5. **El plan es un documento, no un motor.** Si no lo seguís no pasa nada: nada se marca vencido, nada acumula deuda. Volver a correr `/plan` regenera desde cero con el estado actual.
6. Cada día propuesto ofrece **las dos vías**, y el usuario elige: `/resumen <tema> --perfil X` o `/repasar <tema>`.

**`/estado` v2** — agregar al tablero:
```
Tarjetas:      142 · 38 nunca vistas · 17 con último intento fallido
Calibración:   brecha +1.4 (sobreconfianza) · peor tema: Reducciones (conf 4.2 / acierto 41%)
Sin tocar:     Reducciones hace 9 días · Autómatas de pila hace 14 días
→ Sugerencia: /repasar reducciones --desde-errores   o   /resumen reducciones --perfil ciego
```

La línea "Sin tocar" es **información**, no reproche. Sin signos de alarma, sin rachas rotas, sin conteo de días perdidos.

**Criterio de aceptación:** `/plan` se niega a inventar un plan imposible y lo dice. `/estado` informa tiempo sin tocar cada tema sin lenguaje de deuda ni penalización. Ninguna salida del sistema usa las palabras "vencido", "atrasado" o "racha".

---

### FASE 14 — `/resumen` de primera clase: cinco perfiles

`/resumen` y `/machete` quedan **exactamente como estaban** en la Fase 5 del bootstrap base, sin advertencias ni penalizaciones. Esta fase solo **agrega perfiles**.

**`/resumen <tema|todo> --perfil <p>`**

| Perfil | Qué produce | Cuándo sirve |
|---|---|---|
| `breve` | 1-2 páginas, lo esencial | Repaso rápido, ya existía |
| `completo` | Cobertura total con diagramas y fórmulas | Estudio principal, ya existía |
| `guia-parcial` | Ordenado por probabilidad de que lo tomen, según `patron.md` | Semana previa, ya existía |
| **`esqueleto`** | La estructura completa —títulos, subtítulos, nombres de teoremas, encabezados de tabla— **con el contenido vacío**, para que lo completes vos. Al terminar podés pedir la corrección contra el wiki | Convierte el resumen en generación activa manteniendo la estructura que te sirve |
| **`anotado`** | El resumen completo, con preguntas al margen tipo "¿por qué vale esto?", "¿qué pasa si sacamos esta hipótesis?" | Interrogación elaborativa (nivel B) sin cambiar tu forma de estudiar |

**`/resumen-ciego <tema>`** — comando aparte:
1. El sistema te pide que escribas el resumen del tema **con el wiki cerrado**, en `out/ciego-<tema>.md`.
2. Cuando terminás, lo compara contra las páginas del wiki y devuelve tres listas: **qué te faltó**, **qué pusiste mal** (con la cita `✅` correcta al lado), y **qué agregaste que no está en ninguna fuente** (esto último es lo más informativo: suele ser donde mezclaste materias o inventaste).
3. Los temas donde faltó mucho se reflejan en `dominio.md`.

Es la versión productiva de lo que ya hacés, y produce un artefacto que te queda. No reemplaza a `/resumen`: lo complementa.

Todos los perfiles preservan las marcas `✅ 🧠 ⚠️` en la salida y pasan por `build_pdf.py`.

**Criterio de aceptación:** `/resumen` no emite ninguna advertencia sobre su propia eficacia. Los 5 perfiles existen. `/resumen-ciego` devuelve las tres listas, incluida la de contenido sin respaldo en fuentes.

---

### FASE 15 — Exámenes de práctica como fuente privilegiada

**El usuario tiene exámenes de práctica en todas sus materias.** Es la mejor evidencia del sistema: la única que dice **qué te van a preguntar y cómo**.

**15.1 Tipo de fuente propio.** `/ingest` acepta `--tipo examen` y aplica un pipeline distinto:
- Se guarda en `raw/examenes/` y **nunca alimenta páginas de concepto**. Un enunciado de parcial no es una definición.
- Genera `wiki/examenes/<id>.md` con una entrada por consigna:

```markdown
## e2024p1-q3
**Consigna:** [transcripción literal] ✅ [parcial-2024-1 p.2]
**Unidad:** U3          **Puntaje:** 20/100
**Tipo:** demostrar     **Verbo:** "probar que ... no es regular"
**Bloom:** aplicar
**Resolución:** inferida    # oficial | catedra | inferida
**Cubierto_por:** [teoremas/bombeo-regulares, ejercicios/no-regularidad]
**Estado_wiki:** cubierto   # cubierto | parcial | HUECO
```

- La consigna se transcribe **literal**. Si no hay solución oficial, la resolución va marcada `inferida` + `🧠`. Nunca presentar una resolución inferida como verificada.

**15.2 `wiki/examenes/patron.md` — el archivo más valioso de la materia.** Se regenera con cada examen ingerido:
- Distribución de puntaje por unidad a lo largo de todos los exámenes.
- Verbos de consigna recurrentes con su frecuencia — define a qué nivel de Bloom hay que llegar en cada unidad, con evidencia.
- Temas que aparecen siempre, temas que nunca aparecieron aunque estén en el programa, temas nuevos del último examen.
- **Huecos**: consignas que el wiki no puede responder. Cada una genera entrada en `dudas.md`.

**15.3 Reserva ciega — regla no negociable.** De N exámenes aportados, el sistema **reserva el más reciente** en `raw/examenes/_reservado/`: no se transcribe, no genera tarjetas, no alimenta `patron.md` ni el perfilado. Uso único: `/simulacro --reservado`, unos días antes del parcial real. Sin esto, el simulacro no mide nada porque ya viste todo. `/lint` alerta si la reserva está vacía habiendo 2+ exámenes.

**15.4 Efectos en comandos existentes:**

| Comando | Cambio |
|---|---|
| `/nueva-materia` | Los exámenes son evidencia ★★★★★ de perfilado. Con ≥2 ingeridos, el perfilado deja de ser `provisional` |
| `/cards` | Genera tarjetas `aplicacion` desde consignas reales, marcadas `origen: examen`. Prioridad alta en la selección de `/repasar` |
| `/resumen --perfil guia-parcial` | Ordena por puntaje histórico real de cada unidad |
| `/profesor parcial` | Formato, distribución de puntaje y verbos reales. Nota en la escala de la cátedra |
| `/plan` | Prioriza por **puntaje en riesgo** = (% que vale la unidad) × (1 − dominio/5). Un tema que vale 30% con dominio 2 va antes que uno que vale 5% con dominio 1 |
| `/estado` | Cobertura ponderada por examen, además de por programa |
| `/lint` | Consignas con `Estado_wiki: HUECO` como prioridad máxima. Son agujeros comprobados, no hipotéticos |

**15.5 `/simulacro <materia> [--reservado]`** — distinto de `/profesor parcial`:
- Examen completo, tiempo real, sin ayuda ni interrupciones.
- Corrección al final con rúbrica y puntaje de la cátedra.
- Desglose por unidad cruzado con `calibracion.md`: dónde te sentías seguro y fallaste.
- Escribe en `estado/simulacros.md` y actualiza `dominio.md` con más peso que un repaso (es la medición más cercana a la condición real).
- `--reservado` consume el examen ciego y lo marca usado.

**Criterio de aceptación:** los exámenes no escriben páginas de concepto; `patron.md` incluye distribución de puntaje y huecos; la reserva ciega se respeta y `/lint` la vigila; `/plan` prioriza por puntaje en riesgo.

---

### AUTOPRUEBA FINAL (al cerrar la Fase 15)

Con el fixture de la Fase 8:
1. `/nueva-materia test-estudio` → ingerir fixture → `/cards U1`.
2. Verificar: tarjetas con cita `✅`, ninguna desde `🧠`, al menos un `Confundible_con` poblado, **ningún archivo con fechas futuras o estado de agenda**.
3. `/repasar U1` con respuestas mixtas: confirmar que una tarjeta fallada **reaparece en la misma sesión** y que se pidió confianza antes de revelar.
4. `/resumen U1 --perfil esqueleto`: confirmar que sale la estructura con contenido vacío y **sin ninguna advertencia sobre la utilidad del resumen**.
5. `/resumen-ciego U1`: confirmar que devuelve las tres listas.
6. `/plan test-estudio --hasta` con fecha a 3 días: confirmar que **avisa que no alcanza** en vez de inventar un plan.
7. `grep -ri "vencid\|atrasad\|racha" .claude/ plantillas/` debe volver vacío.
8. Borrar la materia de prueba. Commit final.

---

## 3. ANTIPATRONES DE ESTA CAPA

- ❌ Advertir al usuario contra `/resumen`, penalizar su uso, o medir una relación "resúmenes vs repasos". Decisión de producto: el resumen es central.
- ❌ Implementar cualquier forma de agendamiento: SM-2, FSRS, cajas de Leitner, fechas de vencimiento, colas diarias, rachas, notificaciones o deuda acumulada.
- ❌ Que un comando arranque solo o reclame atención. Todo se inicia por pedido explícito.
- ❌ Generar tarjetas o preguntas desde contenido `🧠`. Memorizarías alucinaciones: es el peor modo de falla posible.
- ❌ Intercalar temas no relacionados "porque el intercalado es bueno". El efecto depende de que los ítems sean confundibles.
- ❌ Pedir la confianza después de revelar la respuesta. No mide nada.
- ❌ Cargar páginas del wiki durante `/repasar` fuera de un fallo.
- ❌ Afirmar mecanismos neurobiológicos (modos del cerebro, sinapsis, mortero que fragua). Nivel C.
- ❌ Que `/plan` genere un calendario viable cuando no lo es.
- ❌ Volcar enunciados de examen a páginas de concepto, o presentar una resolución inferida como oficial.
- ❌ Consumir todos los exámenes. Sin reserva ciega no hay medición limpia antes del parcial.
- ❌ Optimizar solo contra los exámenes viejos. El patrón informa prioridad; el programa define cobertura.
- ❌ Ser complaciente al corregir. Una respuesta parcial se marca parcial y se dice qué falta.
