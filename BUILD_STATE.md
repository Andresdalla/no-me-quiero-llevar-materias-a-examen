# BUILD_STATE

Estado del bootstrap. Una fase por iteración del loop, un commit por fase.
Fuente de verdad: `BOOTSTRAP.md`.

| Fase | Qué construye | Estado |
|---|---|---|
| 0 | Esqueleto de directorios, `.gitignore`, este archivo | OK |
| 1 | `CLAUDE.md` raíz (contrato del sistema, ≤120 líneas) | OK |
| 2 | Scripts: `pdf_texto.py`, `pdf_render.py`, `pdf_figs.py`, `build_pdf.py` | PENDIENTE |
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

## Deuda

- (vacío)
