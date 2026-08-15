# BUILD_STATE

Estado del bootstrap. Una fase por iteración del loop, un commit por fase.
Fuente de verdad: `BOOTSTRAP.md`.

| Fase | Qué construye | Estado |
|---|---|---|
| 0 | Esqueleto de directorios, `.gitignore`, este archivo | OK |
| 1 | `CLAUDE.md` raíz (contrato del sistema, ≤120 líneas) | OK |
| 2 | Scripts: `pdf_texto.py`, `pdf_render.py`, `pdf_figs.py`, `build_pdf.py` | OK |
| 3 | Catálogo de 15 tipos de página + plantillas | PENDIENTE |
| 4 | Comandos núcleo: `/nueva-materia`, `/ingest`, `/loop` | PENDIENTE |
| 5 | Comandos de salida: `/resumen`, `/machete`, `/profesor` | PENDIENTE |
| 6 | Comandos de mantenimiento: `/lint`, `/estado`, `/puentes`, `/reperfilar`, `/archivar` | PENDIENTE |
| 7 | Capa `global/`, `materias/_plantilla/` completa, `README.md` | PENDIENTE |
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

## Deuda

- **Fase 2** — El camino Typst no está probado: no hay binario `typst` en esta máquina.
  El fallback (dejar el `.md` + avisar) sí quedó verificado. Revisar en Fase 8.
