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
| 8 | Autoprueba end-to-end con fixture + saldar deuda | OK |

Capa de estudio — `BOOTSTRAP-APRENDIZAJE.md`:

| Fase | Qué construye | Estado |
|---|---|---|
| 9 | `global/metodo/evidencia.md` + principios de estudio en el `CLAUDE.md` raíz | OK |
| 10 | `/cards`: tarjetas de recuperación, sin motor de agendamiento | OK |
| 11 | `/repasar`: recuperación a demanda | OK |
| 12 | Calibración, niveles de Bloom en `/profesor`, `/pre-test` | OK |
| 13 | `/plan` y `/estado` v2 (sugerencia, nunca cola) | PENDIENTE |
| 14 | `/resumen`: perfiles `esqueleto` y `anotado` + `/resumen-ciego` | PENDIENTE |
| 15 | Exámenes de práctica como fuente privilegiada + `/simulacro` | PENDIENTE |

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

- **Fase 8** — Fixture reproducible: `tests/fixtures/gen_fixture.py` genera
  `fixture-tc.pdf` (3 páginas: definición, teorema, diagrama vectorial). El generador queda
  versionado para poder regenerar el PDF si cambia el extractor.
- **Fase 8** — Autoprueba corrida de punta a punta. Los 6 chequeos del punto 2 pasan:
  frontmatter 7/7 y namespace correcto en las 2 páginas · 7 marcas `✅` con cita verificada
  por grep contra `texto.md` (3/3 en la pasada de verificación, y las páginas citadas
  coinciden: p.1, p.2, p.2) · `mapa.md` con 2 filas · archivo en `raw/` + 1 línea de
  manifiesto · `.cache/` vacío · reingesta detectada por hash.
- **Fase 8** — El fixture disparó un hallazgo real: el epígrafe de la Figura 2.3 no coincide
  con el autómata dibujado. Se marcó `⚠️` y quedó en `dudas.md`, que es exactamente el camino
  que el sistema debe seguir ante una contradicción. `/lint` lo confirmó.
- **Fase 8** — `/lint` (7 de 10 chequeos aplicables con una sola ingesta) y `/estado`
  corrieron sobre la materia de prueba y dieron salida correcta. `/resumen todo` generó el
  `.md` con las marcas preservadas (6 ✅, 1 🧠, 2 ⚠️) y el diagrama Mermaid en SVG.
- **Fase 8** — Materia de prueba borrada y entrada quitada de `global/indice.md`: el repo
  queda vacío de contenido, como pide la misión.

- **Fase 9** — `global/metodo/evidencia.md`: la sección 1 completa del addendum con los tres
  niveles, las citas completas y la subsección sobre el resumen. Se agregó al final la
  sección "Dos decisiones de producto", que aclara que no salen de la literatura: son
  decisiones y no se revierten sin pedido del usuario.
- **Fase 9** — El bloque en el `CLAUDE.md` raíz tiene 10 líneas de contenido (tope 15).
  Se le sumó una línea que el addendum pone como antipatrón pero no en el bloque: pedir la
  confianza antes de revelar. Es la que más fácil se implementa mal.
- **Fase 9** — Efecto colateral aceptado: el `CLAUDE.md` raíz pasa de 111 a 122 líneas,
  4 por encima del tope de 120 que fijó la Fase 1. El addendum ordena agregar el bloque de
  forma explícita, así que gana el addendum. Si molesta, la tabla de comandos admite
  compresión.

- **Fase 10** — `/cards` con los 4 tipos, la regla de solo-`✅`, el tope de 12 por página y
  el poblado simétrico de `Confundible_con`. Se agregó `cards/` a `materias/_plantilla/` con
  un README que deja explícito que `Visto` es historial, no agenda.
- **Fase 10** — Regla agregada: al regenerar, `/cards` conserva el `Visto` de las tarjetas
  existentes y solo agrega las nuevas. Sin esto, correr `/cards` dos veces borraría el
  historial de repaso, que es justo lo único que no se puede reconstruir.
- **Fase 10** — Los ids `c-<tema>-<NNN>` no se reusan nunca: un id liberado que vuelve
  apuntaría al `Visto` de otra tarjeta.
- **Fase 10** — Verificado por grep en `.claude/`, `plantillas/`, `materias/_plantilla/` y
  `global/`: cero apariciones de vencimiento, racha, scheduler, Leitner, SM-2 o FSRS fuera
  de las negaciones explícitas.

- **Fase 11** — `/repasar` exige tema explícito: sin argumento lista los temas con tarjetas y
  frena. No elige por el usuario ni arranca con "el que más falta hace".
- **Fase 11** — Tope agregado al criterio de recuperación dentro de la sesión: una tarjeta
  reaparece como máximo 3 veces. Más allá de eso el problema no es la tarjeta sino que falta
  estudiar el tema, y repetirla 8 veces solo desmoraliza.
- **Fase 11** — Regla explícita de no explicar durante el repaso: el enlace a la página
  reemplaza a la explicación. Es lo que mantiene el presupuesto de tokens (1-3 archivos de
  `cards/` por sesión) y lo que hace que sea recuperación y no clase.
- **Fase 11** — `estado/historial.md` agregado a `materias/_plantilla/`.

- **Fase 12** — `/profesor` modificado (fase anterior, cambio pedido por el addendum): pide
  confianza 1-5 antes de corregir, etiqueta cada pregunta con su nivel de Bloom, escala al
  80% y ahora escribe también `calibracion.md` e `historial.md`.
- **Fase 12** — Precisión sobre el momento de la confianza en `/profesor`: va después de que
  el estudiante responde pero **antes de la corrección**. En `/repasar` va antes de revelar
  la respuesta. En ambos casos, antes de saber si acertó.
- **Fase 12** — Regla agregada: si existe `wiki/examenes/patron.md`, los verbos reales de las
  consignas fijan el techo de Bloom por encima de la tabla heurística por tipo de materia.
  Evidencia le gana a heurística; queda enganchado con la Fase 15.
- **Fase 12** — `/pre-test` no toca `dominio.md`, `errores.md` ni `calibracion.md`: solo
  anexa una línea a `historial.md`. Y no lee el wiki aunque el tema ya esté ingerido, porque
  leerlo haría preguntar lo que el wiki sabe en vez de lo que el usuario no sabe.
- **Fase 12** — `estado/calibracion.md` agregado a la plantilla con la fórmula de brecha y
  los dos umbrales.

## Deuda

- (saldada) ~~Fase 2 · camino Typst sin probar~~ → reclasificada abajo como limitación
  conocida: Typst es dependencia opcional por diseño y no se instala nada en la máquina del
  usuario sin pedirlo.
- (saldada) ~~Fase 4 · colisión de nombre `/loop`~~ → decisión tomada: se respeta el nombre
  del spec, el archivo aclara la diferencia en su primera línea. Renombrar a `/vaciar-cola`
  sigue siendo un cambio de una línea si molesta en la práctica.

## Limitaciones conocidas

- **Typst sin verificar.** No hay binario `typst` ni `pandoc` en esta máquina, así que el
  camino de compilación a PDF no se ejecutó nunca. Sí está verificado el fallback: `/resumen`
  escribe el `.md`, avisa y sale con 0. Para probarlo: `brew install typst` y volver a correr
  `scripts/build_pdf.py` sobre cualquier `.md`.
- **El conversor md→Typst es parcial.** Cubre títulos, listas, tablas, código, enlaces,
  imágenes, citas y ~50 comandos LaTeX de matemática. Un comando no reconocido pierde la
  barra y se emite como identificador: se ve, no rompe la compilación.
- **Sin OCR.** Un PDF escaneado se detecta (`probable_escaneado`) y se rechaza; no hay
  camino para procesarlo.
- (saldada) ~~Fase 5 · `quiz-log.md` faltaba en el paso 8 de `/nueva-materia`~~ → agregado.
