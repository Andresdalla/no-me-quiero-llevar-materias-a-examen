# BOOTSTRAP — no-me-quiero-llevar-materias-a-examen

> **Cómo usar este archivo**
> 1. `mkdir no-me-quiero-llevar-materias-a-examen && cd $_ && git init`
> 2. Guardá este archivo como `BOOTSTRAP.md` en la raíz.
> 3. Abrí Claude Code ahí y ejecutá: `/loop lee BOOTSTRAP.md y ejecutá la siguiente fase pendiente`
> 4. Cada iteración del loop completa **una** fase y hace **un** commit. Si algo sale mal, `git revert` de ese commit y volvés a correr.

---

## 0. MISIÓN

Construir un **template de repositorio** que implementa el patrón "LLM Wiki" de Andrej Karpathy, adaptado a cursar materias de facultad. No es una app: no hay servidor, ni frontend, ni base de datos. Es una estructura de carpetas markdown + scripts Python + comandos slash de Claude Code.

El sistema debe:
- Ingerir PDFs/apuntes/slides y compilarlos en un wiki interconectado, **por materia**.
- Mantener una capa `global/` delgada que conecta materias sin duplicar contenido.
- Generar resúmenes, machetes y PDFs con LaTeX/Mermaid/figuras extraídas.
- Interrogarte (modo profesor) y llevar registro de qué dominás y qué no.
- Ser **auditable**: todo lo que el LLM afirma tiene que rastrearse a una fuente o estar marcado como inferencia.

**Vos (el agente) construís el sistema. No construís contenido de ninguna materia.** Al terminar el bootstrap el repo está vacío de material y listo para `/nueva-materia`.

---

## 1. PROTOCOLO DE LOOP — leer primero, siempre

Este archivo se ejecuta en múltiples iteraciones. En **cada** iteración:

1. Leé `BUILD_STATE.md` (si no existe, estás en la Fase 0).
2. Identificá la primera fase con estado `PENDIENTE`.
3. Leé **solo** la sección de esa fase en este archivo. No leas las otras fases.
4. Ejecutala completa.
5. Verificá contra su **Criterio de aceptación**. Si falla, arreglá antes de commitear.
6. Actualizá `BUILD_STATE.md`: marcá la fase `OK`, anotá archivos creados y cualquier decisión no obvia en 1-2 líneas.
7. `git add -A && git commit -m "bootstrap(fase-N): <descripción>"`
8. **Terminá el turno.** No arranques la fase siguiente.

**Prohibido en cada iteración:**
- Releer archivos que ya escribiste en fases anteriores, salvo que la fase actual lo pida explícitamente.
- Leer directorios completos "para tener contexto".
- Reescribir trabajo de fases anteriores. Si detectás un error en una fase previa, anotalo en `BUILD_STATE.md` bajo `## Deuda` y seguí; se corrige en la Fase 8.

Si `BUILD_STATE.md` marca todas las fases `OK`, respondé: "Bootstrap completo. Corré `/nueva-materia <nombre>` para empezar." y terminá.

---

## 2. PRINCIPIOS NO NEGOCIABLES

Estos principios se aplican al sistema que estás construyendo y deben quedar escritos en el `CLAUDE.md` raíz. No son sugerencias: son las reglas que hacen que el sistema no se degrade.

### 2.1 Disciplina de tokens

El costo dominante es el LLM leyendo. El diseño entero está orientado a leer poco:

| Regla | Por qué |
|---|---|
| **Ruteo por `mapa.md`** — antes de tocar cualquier página, leer el `mapa.md` de la materia (≤200 líneas, una línea por página: `id · tipo · tema · 8 palabras`). Recién ahí decidir qué páginas abrir. | Sustituye leer 80 páginas por leer 4 KB. |
| **Nunca leer un directorio entero.** Usar `grep`/`glob` con patrón, nunca `Read` sobre cada archivo de una carpeta. | Un `ls` de `conceptos/` cuesta nada; leer las 40 páginas cuesta 60k tokens. |
| **Nunca abrir un PDF con `Read`.** Siempre vía `scripts/pdf_texto.py`. | Un PDF crudo en contexto es basura tokenizada. |
| **Rasterizar selectivamente.** Solo las páginas que el extractor marca como candidatas (fórmulas, diagramas, tablas). Nunca el PDF completo. | Una imagen ≈ 1.5k tokens. 300 páginas = 450k tokens. |
| **Tope de página: 150 líneas.** Si una página supera eso, se parte y se enlaza. | Páginas chicas = cargás solo lo que necesitás. |
| **Frontmatter greppable** en toda página (ver 2.3). | Permite filtrar sin abrir archivos. |
| **`.cache/` es efímero.** Se borra al terminar cada ingesta. | El repo no se infla con PNGs intermedios. |
| **No releer lo que acabás de escribir.** | Error clásico que duplica el costo de cada ingesta. |

### 2.2 Regla dual de fidelidad

Esta es la defensa contra alucinaciones horneadas.

- **Contenido literal** — definiciones, teoremas, enunciados formales, fórmulas, especificaciones, valores numéricos: **se transcriben textualmente** de la fuente, con cita `[fuente-id p.N]`. Prohibido parafrasear.
- **Contenido sintetizado** — intuiciones, explicaciones, conexiones, ejemplos propios, comparaciones: libre, pero **marcado**.

Marcadores obligatorios inline:
- `✅ [apunte-cap3 p.14]` — verificado contra fuente, literal o cita directa.
- `🧠` — inferencia/síntesis del LLM, no está así en ninguna fuente.
- `⚠️` — contradicción entre fuentes, o duda no resuelta. Debe además aparecer en `dudas.md`.

Una página sin ninguna marca `✅` es sospechosa y `/lint` la reporta.

### 2.3 Inmutabilidad y trazabilidad

- `ingest/` es una **cola**, no un depósito. Procesado → se mueve a `raw/`.
- `raw/` es **inmutable**. El agente lee, jamás escribe ni borra ahí.
- Todo archivo procesado deja una línea en `manifest.jsonl`: `{"hash":"sha256...","archivo":"...","fuente_id":"...","fecha":"...","paginas_wiki":[...],"paginas_pdf":N}`
- Antes de ingerir, se chequea el hash contra el manifiesto. Si ya está: se salta y se avisa.
- **Un commit por archivo ingerido.** El mensaje incluye el `fuente_id` y cuántas páginas tocó. Esto te da `git revert` sobre una ingesta que salió mal.

### 2.4 Namespaces

Todo ID de página es `materia/tipo/slug`. Enlaces dentro de la materia: `[[tipo/slug]]`. Entre materias: forma completa `[[seguridad-informatica/ataques/spectre]]`.

Sin esto, `conceptos/proceso` de Arquitectura y de Ing. de Software se fusionan. Es el modo de falla número uno de un wiki multi-materia.

### 2.5 Frontmatter estándar

```yaml
---
id: teoria-computacion/teoremas/bombeo-regulares
tipo: teorema
tema: U3
fuentes: [sipser-cap1 p.77, apunte-catedra p.12]
estado: completo        # esbozo | completo | verificado
dominio: 3              # 0-5, lo actualiza /profesor
actualizado: 2026-08-15
---
```

---

## 3. STACK

Fijado. No lo cambies ni propongas alternativas durante el bootstrap.

- **Python 3.11+** para todos los scripts. Única dependencia pesada: **PyMuPDF** (`pymupdf`). Además `pyyaml`. Nada más.
  - Justificación (no la re-discutas): el 97% del tiempo de una ingesta es el LLM pensando; los scripts son pegamento sobre MuPDF (C). Rust no aportaría rendimiento y encarecería la iteración del propio agente.
- **Typst** para PDF (binario único, compilación en ms). Fallback: `pandoc` + LaTeX si el usuario ya lo tiene. Detectar en runtime, no exigir ambos.
- **Mermaid** vía `npx -y @mermaid-js/mermaid-cli` (sin instalación global). Pre-renderiza a SVG antes de compilar el PDF.
- Todo script debe **degradar con elegancia**: si falta Typst, `/resumen` igual escribe el `.md` y avisa que no pudo generar el PDF. Nunca fallar entero por una herramienta opcional.

---

## 4. FASES

### FASE 0 — Esqueleto y estado

Crear:
- `BUILD_STATE.md` con la tabla de las 9 fases (0-8), todas `PENDIENTE` salvo la 0 que queda `OK`, más secciones `## Decisiones` y `## Deuda`.
- Árbol de directorios vacío (con `.gitkeep` donde haga falta):

```
.claude/commands/
scripts/
plantillas/paginas/
materias/activas/
materias/archivo/
materias/_plantilla/{ingest,raw,wiki/{temas,conceptos,fuentes},estado,assets,out}
global/puentes/
global/metodo/
tests/fixtures/
```

- `.gitignore`:
```
# Material de cátedra: nunca se commitea (copyright + peso)
materias/*/*/ingest/*
materias/*/*/raw/*
materias/*/*/assets/*
materias/*/*/out/*
.cache/
__pycache__/
.venv/
!**/.gitkeep
```

**Criterio de aceptación:** `git status` limpio tras el commit; `find . -type d | wc -l` ≥ 20.

---

### FASE 1 — `CLAUDE.md` raíz

El contrato del sistema. Debe ser **denso y corto: máximo 120 líneas.** Se carga en cada sesión; cada línea de más es un impuesto permanente.

Contenido, en este orden:
1. Qué es el repo (3 líneas).
2. Arquitectura federada: contenido vive en `materias/activas/<m>/`; `global/` **solo enlaza, nunca guarda contenido**.
3. Las reglas de la sección 2 de este documento, condensadas. Prioridad a 2.1 (tokens) y 2.2 (fidelidad).
4. Tabla de comandos disponibles, una línea cada uno.
5. Protocolo de commits.
6. Qué **no** hacer: no inventar contenido de materias, no modificar `raw/`, no fusionar páginas de materias distintas, no crear páginas sin fuente.

Escribilo en español, en imperativo, sin ejemplos largos. Los ejemplos van en las plantillas.

**Criterio de aceptación:** ≤120 líneas; incluye las tres marcas `✅ 🧠 ⚠️` y la regla de namespaces.

---

### FASE 2 — Scripts

Cuatro scripts. Todos con `--help`, salida JSON a stdout cuando corresponda, y errores legibles a stderr.

**`scripts/pdf_texto.py`**
```
uso: pdf_texto.py <pdf> [--out DIR] [--paginas 1-20]
```
- Extrae texto preservando estructura (usa `page.get_text("dict")` para detectar tamaños de fuente → inferir jerarquía de títulos).
- Escribe `<out>/texto.md` con marcadores `<!-- p.N -->` al inicio de cada página. **Estos marcadores son la base de toda la citación posterior; sin ellos el sistema no puede citar páginas.**
- Escribe `<out>/analisis.json`:
```json
{
  "paginas": 42,
  "titulo_detectado": "...",
  "candidatas_visuales": [
    {"pagina": 12, "razon": "diagrama", "confianza": 0.8, "bbox": [x0,y0,x1,y1]},
    {"pagina": 13, "razon": "tabla|formula|imagen_embebida", ...}
  ],
  "densidad_texto": 0.72,
  "probable_escaneado": false
}
```
- Heurísticas para `candidatas_visuales`: imágenes embebidas (`page.get_images`), densidad de vectores (`page.get_drawings()` > umbral → diagrama), bloques con muchos símbolos no-ASCII (fórmula), grillas de líneas (tabla).
- Si `probable_escaneado` es true (densidad de texto ≈ 0), avisar que hace falta OCR y no fingir extracción.

**`scripts/pdf_render.py`**
```
uso: pdf_render.py <pdf> --paginas 12,13,20 --out DIR [--dpi 150]
```
- Rasteriza **solo** las páginas pedidas. Nunca todas por defecto — si no se pasa `--paginas`, error.

**`scripts/pdf_figs.py`**
```
uso: pdf_figs.py <pdf> --pagina 12 --bbox x0,y0,x1,y1 --out assets/fuente/p12-fig1.png
```
- Recorta a 300 dpi. También modo `--auto` que extrae las imágenes embebidas de una página.

**`scripts/build_pdf.py`**
```
uso: build_pdf.py <archivo.md> [--out out/] [--perfil resumen|machete|guia]
```
- Pipeline: leer md → extraer bloques ```mermaid``` → renderizar a SVG con `npx mmdc` → sustituir por `![](ruta.svg)` → compilar.
- Motor: Typst si está en PATH, si no pandoc+LaTeX, si no dejar el `.md` y avisar.
- Perfiles cambian márgenes/tamaño de fuente/columnas: `machete` es dos columnas, 9pt, márgenes mínimos.
- Preámbulo en `plantillas/estilo.typ`.

**Criterio de aceptación:** los 4 scripts corren con `--help` sin excepción. `python scripts/pdf_texto.py --help` retorna 0.

---

### FASE 3 — Catálogo de tipos de página

Este es el corazón de la calidad del wiki. Crear `plantillas/catalogo.md` con **15 tipos primitivos**. Para cada uno: nombre, cuándo usarlo, campos obligatorios, **regla de verificación** (qué debe chequear `/lint`), y ejemplo mínimo de 5-8 líneas.

Los 15 tipos:

| Tipo | Campos obligatorios |
|---|---|
| `definicion` | enunciado literal ✅ · notación · ejemplo · contraejemplo · confusiones frecuentes |
| `teorema` | enunciado literal ✅ · hipótesis explícitas · demostración (o `estado: sin-demo`) · cuándo se aplica · errores típicos de aplicación |
| `demostracion` | qué prueba · técnica (inducción/contradicción/diagonalización/construcción) · pasos · dónde suele fallar el estudiante |
| `construccion` | objetivo · procedimiento paso a paso · diagrama Mermaid · caso de prueba resuelto |
| `reduccion` | de A a B · qué implica · esquema del argumento · diagrama |
| `mecanismo` | qué problema resuelve · cómo funciona por dentro · diagrama · costo/latencia |
| `protocolo` | actores · secuencia (Mermaid `sequenceDiagram`) · garantías · supuestos · modos de falla |
| `comparativa` | tabla obligatoria (nunca prosa) · criterio de decisión · cuándo elegir cada uno |
| `ataque` | precondiciones · mecanismo · impacto · mitigación · detección |
| `modelo` | qué modela · axiomas/reglas · limitaciones · críticas |
| `practica` | qué es · cuándo aplica · **cuándo NO aplica** · antipatrón asociado |
| `framework` | roles · artefactos · ceremonias/fases (tabla) · críticas |
| `caso` | situación · decisión · justificación · qué cambiaría si... |
| `debate` | postura A ✅ · postura B ✅ · dónde está el desacuerdo real · tu posición 🧠 |
| `numeros` | valores a memorizar · orden de magnitud · fuente ✅ |

Además, en `plantillas/paginas/` un archivo `.md` por tipo, listo para copiar, con frontmatter completo y secciones vacías.

Reglas del catálogo (escribirlas en el archivo):
- Máximo **8 tipos activos por materia**.
- Se pueden **renombrar** tipos al vocabulario de la materia (`construccion` → `maquinas`), manteniendo la regla de verificación del tipo base. Registrar el alias en el `CLAUDE.md` de la materia.
- Se puede **proponer un tipo nuevo** solo si: ningún primitivo encaja, se esperan ≥3 instancias, y se escribe su regla de verificación.
- Todo tipo hereda las marcas de fidelidad (2.2). Ninguno se las salta.

**Criterio de aceptación:** 15 tipos documentados + 15 plantillas en `plantillas/paginas/`. Cada tipo tiene regla de verificación explícita.

---

### FASE 4 — Comandos: núcleo (`nueva-materia`, `ingest`, `loop`)

Los comandos son archivos markdown en `.claude/commands/`. Cada uno describe un procedimiento paso a paso. **Deben ser específicos y verificables, no aspiracionales.**

**`/nueva-materia <slug>`**
1. Crear `materias/activas/<slug>/` desde `_plantilla`.
2. Pedir al usuario: nombre completo, cuatrimestre, fecha de parciales/final, modalidad de evaluación (escrito / oral / múltiple choice / proyecto).
3. Pedirle que ponga en `ingest/` el **temario oficial** y, si los tiene, **parciales viejos y guías de ejercicios**.
4. Procesar esos archivos primero (son la evidencia de perfilado).
5. **Perfilar**: seleccionar del catálogo hasta 8 tipos. Prioridad de evidencia:
   - Parciales viejos ★★★★★ (dicen qué forma tiene la evaluación)
   - Guías de ejercicios ★★★★
   - Índice de bibliografía ★★★
   - Temario ★★★
   - Si **no hay parciales**: marcar `perfilado: provisional` en el CLAUDE.md de la materia y programar `/reperfilar` a las 8 ingestas en vez de 20.
6. Generar `wiki/programa.md` con **una entrada por unidad del temario**, cada una con `cobertura: sin-material | parcial | cubierto`. Esta es la espina dorsal: el wiki se audita contra el programa, no contra sí mismo.
7. Generar `CLAUDE.md` de la materia: tipos activos + alias + reglas propias + vocabulario/notación de la cátedra + fechas.
8. Inicializar `wiki/index.md`, `wiki/mapa.md`, `wiki/log.md`, `wiki/dudas.md`, `estado/dominio.md`, `estado/errores.md`, `estado/repaso.md`, `manifest.jsonl`.
9. Registrar la materia en `global/indice.md`.

**`/ingest [archivo]`** — procesa **un** archivo:
1. Leer `CLAUDE.md` de la materia + `wiki/mapa.md`. **Nada más.**
2. Elegir archivo (el indicado, o el más antiguo de `ingest/`). Calcular SHA-256; si está en `manifest.jsonl`, saltar y avisar.
3. `pdf_texto.py` → `.cache/<hash>/`. Leer `analisis.json` primero, después `texto.md`.
4. Si el documento es largo (>60 páginas), procesar **por capítulo/sección**, no entero.
5. Rasterizar solo `candidatas_visuales` con confianza ≥0.6 y mirarlas.
6. **Plan antes de escribir**: listar en 10-15 líneas qué páginas se crean y cuáles se actualizan. Mostrarlo. Si supera 20 páginas nuevas, pedir confirmación (señal de que el documento debería partirse).
7. Escribir/actualizar páginas según el catálogo y la regla dual (2.2).
8. Extraer figuras necesarias a `assets/<fuente-id>/`.
9. **Pasada de verificación**: elegir 3 afirmaciones marcadas `✅` al azar y contrastarlas contra `texto.md`. Si alguna no coincide, corregirla y anotarlo en el log.
10. Actualizar `mapa.md`, `index.md`, `log.md`, y la `cobertura` de las unidades tocadas en `programa.md`.
11. Mover `ingest/x.pdf` → `raw/x.pdf`. Anexar línea a `manifest.jsonl`. Borrar `.cache/<hash>/`.
12. Commit: `ingest(<materia>): <fuente-id> · N páginas`.

**`/loop`** — vacía la cola: ejecuta `/ingest` en bucle hasta que `ingest/` esté vacío, un commit por archivo. Entre archivos **no** acumula contexto: cada iteración arranca leyendo `mapa.md` fresco. Si un archivo falla, lo mueve a `ingest/_fallidos/`, lo registra y sigue con el siguiente.

**Criterio de aceptación:** los 3 comandos existen y describen pasos numerados y verificables, sin frases vagas del tipo "analizá el documento cuidadosamente".

---

### FASE 5 — Comandos: salida (`resumen`, `machete`, `profesor`)

**`/resumen <tema|todo> [--perfil breve|completo|guia-parcial]`**
- Rutea por `mapa.md`, carga solo las páginas del tema.
- `breve`: 1-2 páginas, solo lo esencial. `completo`: cobertura total con diagramas. `guia-parcial`: ordenado por probabilidad de que lo tomen, según los parciales viejos ingeridos.
- Preserva las marcas ✅/🧠/⚠️ en el resumen. Un resumen sin trazabilidad no sirve para estudiar.
- Escribe `out/resumen-<tema>-<perfil>.md` y llama a `build_pdf.py`.
- `--tema todo` con más de ~40 páginas: generar por unidad y concatenar, no de una.

**`/machete [tema]`**
- 1-2 páginas, dos columnas, sin prosa: fórmulas, enunciados, tablas, procedimientos, diagramas mínimos. Lo que entra en una hoja.

**`/profesor [tema] [modo]`** — modos:
- `socratico`: preguntas encadenadas; si errás no corrige, repregunta más abajo hasta encontrar el hueco real.
- `parcial`: simulacro cronometrado. **Si hay parciales viejos ingeridos, imita su formato, distribución de puntaje y estilo de consigna.** Si no, avisa que es genérico. Corrige con rúbrica.
- `feynman`: te pide explicar; marca dónde tu explicación se pone vaga.
- `hueco`: lee `estado/dominio.md` + `estado/errores.md` y pregunta **solo** lo que venís fallando.
- `caso`: escenario realista → tu decisión → justificación. Default para materias de proceso.

Reglas duras del modo profesor:
- **Cada pregunta cita la página del wiki de donde salió.** Si fallás, tenés el link a qué releer.
- **No ser complaciente.** Una respuesta parcialmente correcta se marca parcialmente correcta y se dice qué falta. Nada de "¡bien! aunque también...".
- Al terminar: escribir en `estado/quiz-log.md`, actualizar `estado/dominio.md` (0-5 por tema) y anexar errores recurrentes a `estado/errores.md`.
- Solo pregunta sobre contenido `✅`. Nunca evalúa sobre material marcado `🧠`.

**Criterio de aceptación:** los 3 comandos especifican de dónde leen, qué escriben y qué archivos de estado actualizan.

---

### FASE 6 — Comandos: mantenimiento (`lint`, `estado`, `puentes`, `reperfilar`, `archivar`)

**`/lint [materia]`** — auditoría. Reporta, no corrige sin confirmación:
- Unidades del programa con `cobertura: sin-material`.
- Páginas huérfanas (sin enlaces entrantes).
- Enlaces rotos y conceptos mencionados sin página propia.
- Páginas sin ninguna marca `✅` (riesgo de alucinación).
- Contradicciones entre páginas (`⚠️` sin entrada en `dudas.md`).
- Páginas >150 líneas (candidatas a partir).
- Tipos activos con 0 instancias tras 10 ingestas (tipo muerto).
- Páginas cuyo `actualizado` es anterior a la última ingesta que tocó sus fuentes.

**`/estado [materia]`** — tablero compacto: cobertura del programa, dominio promedio, temas en rojo, unidades sin material, días al parcial, última ingesta, y **una** recomendación accionable (`→ Hoy: /profesor series hueco`).

**`/puentes [--materias a,b,c]`** — lee **solo** los `mapa.md` de las materias activas (nunca las páginas). Propone conexiones antes de escribir. Clasifica: `⚡ fuerte`, `○ media`, `⚠️ tensión` (materias que se contradicen — lo más valioso para finales orales). Escribe páginas puente de ≤15 líneas en `global/puentes/`, que **solo enlazan**. Si una página puente crece más de eso, ese contenido pertenece a una materia: moverlo.

**`/reperfilar <materia>`** — audita el esquema contra el wiki real: tipos infrautilizados, patrones repetidos que merecen tipo propio, desalineación con la evidencia de evaluación. Propone cambios con su costo de migración explícito (cuántos archivos y enlaces). Toda migración: `schema_version` +1 en el CLAUDE.md de la materia y **commit aislado**, revertible.

**`/archivar <materia>`** — congela: genera `resumen-final.md` (2-3 páginas, lo que vas a necesitar como correlativa), mueve a `materias/archivo/<año>-<c>-<slug>/`, actualiza `global/indice.md` y reapunta los puentes.

**Criterio de aceptación:** los 5 comandos existen; `/puentes` documenta explícitamente que no lee páginas de contenido.

---

### FASE 7 — Capa global, plantilla de materia y README

1. `global/indice.md`: registro de materias (activa/archivada, cuatrimestre, correlativas, estado).
2. `global/glosario.md`: términos que colisionan entre materias, con desambiguación. **Sembrar con los casos conocidos**: `proceso`, `estado`, `modelo`, `protocolo`, `máquina`, `arquitectura`, `política`, `capa`.
3. `global/metodo/`: `como-estudio.md` (preferencias transversales), `errores-transversales.md`.
4. Completar `materias/_plantilla/` con todos los archivos base vacíos pero con frontmatter y encabezados correctos.
5. `README.md`: qué es, instalación (Python + PyMuPDF, Typst opcional, npx para Mermaid), flujo de 5 pasos (`/nueva-materia` → tirar PDFs en `ingest/` → `/loop` → `/resumen` → `/profesor`), tabla de comandos, y **advertencia explícita**: el wiki puede contener errores; `⚠️` y `🧠` no son contenido verificado; usar `/lint` antes de cada parcial.

**Criterio de aceptación:** `materias/_plantilla` se puede copiar y produce una materia funcional sin editar nada a mano.

---

### FASE 8 — Autoprueba y saldar deuda

1. Generar con PyMuPDF un PDF de prueba de 3 páginas en `tests/fixtures/fixture-tc.pdf`: una definición, un teorema con enunciado, y un diagrama vectorial simple (para que dispare `candidatas_visuales`).
2. Correr el pipeline real: `/nueva-materia test-fixture` → ingerir el fixture → verificar que:
   - Se crearon páginas con frontmatter válido.
   - Hay al menos una marca `✅` con cita de página correcta.
   - `mapa.md` se actualizó.
   - El archivo se movió a `raw/` y quedó en `manifest.jsonl`.
   - `.cache/` está vacío.
   - Reingerir el mismo archivo lo saltea por hash.
3. Correr `/lint test-fixture` y `/estado test-fixture`.
4. Correr `/resumen todo` y verificar que genera `.md` (y PDF si Typst está disponible).
5. Borrar `materias/activas/test-fixture/` y su entrada en `global/indice.md`.
6. Resolver todo lo anotado en `## Deuda` de `BUILD_STATE.md`.
7. Commit final: `bootstrap(fase-8): autoprueba OK`.

**Criterio de aceptación:** los 6 chequeos del punto 2 pasan. Si alguno falla, arreglar el componente correspondiente antes de cerrar.

---

## 5. ANTIPATRONES — no hagas esto

- ❌ Escribir comandos con instrucciones vagas ("analizá en profundidad", "considerá el contexto"). Todo paso debe ser verificable.
- ❌ Crear un `CLAUDE.md` raíz de 400 líneas. Es impuesto permanente sobre cada sesión.
- ❌ Meter una capa de abstracción "por si acaso" (plugins, config genérica, sistema de hooks). El repo tiene ~600 líneas de Python. Mantenelo así.
- ❌ Poner contenido real en `global/`. Solo enlaces.
- ❌ Que `/ingest` lea el wiki completo "para tener contexto". Rutea por `mapa.md`.
- ❌ Generar contenido de materias durante el bootstrap. El repo termina vacío.
- ❌ Rasterizar un PDF entero.
- ❌ Adelantarte de fase.
