# BUILD_STATE

Estado del bootstrap. Una fase por iteración del loop, un commit por fase.
Fuente de verdad: `BOOTSTRAP.md`.

| Fase | Qué construye | Estado |
|---|---|---|
| 0 | Esqueleto de directorios, `.gitignore`, este archivo | OK |
| 1 | `CLAUDE.md` raíz (contrato del sistema, ≤120 líneas) | OK |
| 2 | Scripts: `pdf_texto.py`, `pdf_render.py`, `pdf_figs.py`, `build_pdf.py` | OK |
| 3 | Catálogo de 15 tipos de página + plantillas | OK |
| 4 | Comandos núcleo: `/nueva-materia`, `/ingest`, `/loop` | OK |
| 5 | Comandos de salida: `/resumen`, `/machete`, `/profesor` | OK |
| 6 | Comandos de mantenimiento: `/lint`, `/estado`, `/puentes`, `/reperfilar`, `/archivar` | OK |
| 7 | Capa `global/`, `materias/_plantilla/` completa, `README.md` | OK |
| 8 | Autoprueba end-to-end con fixture + saldar deuda | PENDIENTE |

## Decisiones

- **Fase 0** — El `.gitignore` del spec usa `materias/*/*/<dir>/*`, que cubre
  `materias/activas/<slug>/…` pero **no** `materias/_plantilla/<dir>/…` (un nivel menos).
  Se agregaron 4 líneas explícitas para `_plantilla` en vez de cambiar el patrón original.
- **Fase 0** — Rama `main`. `.gitkeep` en las 16 carpetas del árbol para que el esqueleto
  viaje en el repo.

- **Fase 1** — `CLAUDE.md` raíz: 111 líneas. Documenta los 11 comandos de las fases 4-6
  antes de que existan; las fases siguientes deben respetar esos nombres y firmas.
- **Fase 1** — Regla de precedencia agregada (no estaba en el spec): ante conflicto, el
  `CLAUDE.md` de la materia gana sobre el raíz. Sin esto los alias de tipos no funcionan.

- **Fase 2** — Entorno: el `python3` del sistema es 3.9 sin PyMuPDF. Se creó `.venv`
  con `uv` (Python 3.12 + pymupdf 1.28 + pyyaml). Los scripts se corren con
  `.venv/bin/python scripts/<x>.py`. `--help` funciona igual con cualquier Python 3.9+
  porque el import de PyMuPDF es diferido.
- **Fase 2** — `pdf_texto.py` redirige el stdout de PyMuPDF a stderr: la librería imprime
  avisos que rompían el JSON de salida.
- **Fase 2** — Diagramas: se cuentan *segmentos* de path (`items`), no paths, con umbral
  ≥3 paths y ≥12 segmentos. Contar paths dejaba pasar diagramas chicos (3 círculos +
  flechas = 9 paths pero 18 segmentos).
- **Fase 2** — Typst no lee markdown: `build_pdf.py` incluye un conversor md→Typst
  (~120 líneas) con traducción de los ~50 comandos LaTeX de matemática más comunes.
  Todo lo no reconocido pierde la barra y se emite como identificador.
- **Fase 2** — Mermaid verificado: `npx -y @mermaid-js/mermaid-cli` renderizó un
  `flowchart` a SVG (12 KB) sin instalación global. Primera corrida ~1 min por la descarga.
- **Fase 2** — Verificado a mano: extracción de texto con marcadores `<!-- p.N -->`,
  detección de diagrama (confianza 0.8), recorte por bbox a 300 dpi, `--paginas`
  obligatorio en render, y degradación sin motor de PDF (exit 0 + aviso).

- **Fase 3** — `plantillas/catalogo.md` (457 líneas): 15 tipos, cada uno con cuándo usarlo,
  campos obligatorios, regla de verificación para `/lint` y ejemplo de 5-8 líneas.
- **Fase 3** — Agregado al spec: tabla tipo→carpeta en plural (`definicion` →
  `definiciones/`) y una tabla "elegir tipo" por lo que presenta la fuente. Sin la primera,
  cada ingesta inventa su propio plural y los ids dejan de ser predecibles.
- **Fase 3** — Las 15 plantillas de `plantillas/paginas/` se generaron desde una tabla
  única, así que frontmatter y orden de secciones son idénticos entre tipos. Cada sección
  vacía lleva un comentario HTML con la regla que le toca.
- **Fase 3** — Sección `## Relacionado` obligatoria en los 15 tipos: es lo que evita que
  `/lint` reporte huérfanas por diseño.

- **Fase 4** — `/nueva-materia` (10 pasos), `/ingest` (12 pasos), `/loop` (5 pasos). Todos
  con comandos shell concretos; cero frases del tipo "analizá en profundidad" (verificado
  por grep).
- **Fase 4** — Los comandos usan `PY = .venv/bin/python si existe, si no python3`, para no
  depender de qué Python tenga activo el usuario.
- **Fase 4** — `fuente_id` se deriva del contenido, no del nombre del archivo: es lo que
  aparece en cada cita y tiene que sobrevivir a que renombren el PDF.
- **Fase 4** — Documentos >60 páginas: un `/ingest` por tramo, una línea de manifiesto por
  tramo con el mismo hash. Así el reingreso por hash sigue funcionando.

- **Fase 5** — Los tres comandos declaran explícitamente de dónde leen (siempre vía
  `mapa.md`), qué escriben en `out/` y qué archivos de `estado/` tocan. `/resumen` y
  `/machete` no tocan `estado/`: el dominio solo lo mueve `/profesor`.
- **Fase 5** — Regla agregada: al machete no entra nada marcado `🧠`. En un parcial no
  querés copiarte de una inferencia del sistema.
- **Fase 5** — `/machete` tiene tope duro medible (~9000 caracteres = 2 páginas A4 a 9pt en
  dos columnas) y una prioridad de tipos para recortar. Sin tope, "machete" degrada a resumen.
- **Fase 5** — `/profesor` sube el dominio como máximo 1 punto por sesión y lo baja sin
  límite: evita que una sesión afortunada marque un tema como sabido.

- **Fase 6** — Los 10 chequeos de `/lint` vienen con el comando shell que los ejecuta, no
  con una descripción. El más importante (páginas sin `✅`) es un `grep -rL`.
- **Fase 6** — `/puentes` declara la regla de lectura en su segunda sección, con el motivo
  económico, y deja una única excepción acotada: para confirmar una tensión puede abrir
  como máximo una página por materia.
- **Fase 6** — `/estado` es de solo lectura, no commitea, y da **una** recomendación con
  prioridad explícita de 5 niveles (parcial cerca + sin material gana a todo).
- **Fase 6** — `/reperfilar` mide el costo de migración con `grep | wc -l` (archivos y
  enlaces), no lo estima. Y exige commit aislado para que `git revert` funcione.
- **Fase 6** — `/archivar` corre `/lint` antes de congelar: archivar con páginas sin fuente
  hornea el error para siempre.

- **Fase 7** — `materias/_plantilla/` completa: 11 archivos base con encabezado y comentario
  de uso + `manifest.jsonl` vacío. Verificado copiándola: quedan todos los archivos que
  espera el paso 8 de `/nueva-materia`.
- **Fase 7** — Ambigüedad del spec resuelta: la Fase 0 fija las carpetas `wiki/{temas,
  conceptos,fuentes}` pero el catálogo (Fase 3) nombra las carpetas por tipo en plural.
  Quedan las dos cosas: `temas/` (una página por unidad), `fuentes/` (una ficha por fuente
  ingerida), `conceptos/` (fallback), y las carpetas por tipo se crean a demanda. Documentado
  en el `CLAUDE.md` de la plantilla.
- **Fase 7** — `global/glosario.md` sembrado con 18 filas sobre los 8 términos conocidos que
  colisionan. Las filas sin página son recordatorios, no errores.
- **Fase 7** — `estado/quiz-log.md` agregado a la plantilla (resuelve la mitad de la deuda
  de la Fase 5).

## Deuda

- **Fase 2** — El camino Typst no está probado: no hay binario `typst` en esta máquina.
  El fallback (dejar el `.md` + avisar) sí quedó verificado. Revisar en Fase 8.
- **Fase 4** — `.claude/commands/loop.md` colisiona de nombre con el skill `/loop` del
  harness (el que agenda prompts). El spec fija ese nombre, así que quedó como está y el
  archivo aclara la diferencia en la primera línea. Si molesta en la práctica, renombrar a
  `/vaciar-cola` es un cambio de una línea.
- **Fase 5** — `estado/quiz-log.md` ya está en `materias/_plantilla/`, pero falta sumarlo al
  `ls` del paso 8 de `.claude/commands/nueva-materia.md`.
