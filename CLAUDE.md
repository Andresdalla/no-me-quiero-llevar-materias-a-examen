# CLAUDE.md — contrato del sistema

Wiki de estudio multi-materia: PDFs y apuntes entran por `ingest/`, salen como páginas
markdown interconectadas, resúmenes, machetes y simulacros de parcial.
No es una app: son carpetas markdown + 4 scripts Python + comandos slash.
Este archivo se carga en cada sesión. Respetalo literalmente.

## Arquitectura federada

- El contenido vive **solo** en `materias/activas/<materia>/wiki/`.
- `global/` **enlaza, nunca guarda contenido**. Página puente: ≤15 líneas, solo links.
  Si una puente crece más, ese contenido pertenece a una materia: movelo.
- Cada materia tiene su propio `CLAUDE.md` (tipos activos, alias, notación de cátedra,
  fechas). Ante conflicto, el de la materia gana sobre este.
- `materias/_plantilla/` es el molde de `/nueva-materia`. `materias/archivo/` son materias
  cerradas: leelas, no las edites.

## Disciplina de tokens — leer poco es el diseño

- **Ruteá por `mapa.md`.** Antes de abrir cualquier página, leé el `mapa.md` de la materia
  (≤200 líneas, una por página: `id · tipo · tema · 8 palabras`). Recién ahí decidí qué abrir.
- **Nunca leas un directorio entero.** Usá `grep`/`glob` con patrón. Jamás `Read` en bucle
  sobre los archivos de una carpeta.
- **Nunca abras un PDF con `Read`.** Siempre vía `scripts/pdf_texto.py`.
- **Rasterizá selectivamente.** Solo páginas marcadas en `candidatas_visuales` con
  confianza ≥0.6. Nunca el PDF completo.
- **Tope de página: 150 líneas.** Si se pasa, partila y enlazá.
- **Frontmatter greppable en toda página** (ver abajo). Permite filtrar sin abrir archivos.
- **`.cache/` es efímero.** Borralo al terminar cada ingesta.
- **No releas lo que acabás de escribir.**

## Regla dual de fidelidad — defensa contra alucinaciones

- **Contenido literal** (definiciones, teoremas, enunciados formales, fórmulas,
  especificaciones, valores numéricos): **transcribilo textual** de la fuente, con cita
  `[fuente-id p.N]`. Prohibido parafrasear.
- **Contenido sintetizado** (intuiciones, explicaciones, conexiones, ejemplos propios,
  comparaciones): libre, pero **marcado**.

Marcadores inline obligatorios:

| Marca | Significa |
|---|---|
| `✅ [apunte-cap3 p.14]` | Verificado contra la fuente: literal o cita directa. |
| `🧠` | Inferencia o síntesis tuya. No está así en ninguna fuente. |
| `⚠️` | Contradicción entre fuentes o duda sin resolver. Va también a `wiki/dudas.md`. |

Una página sin ninguna marca `✅` es sospechosa: `/lint` la reporta.
`/profesor` solo evalúa sobre contenido `✅`, nunca sobre `🧠`.

## Namespaces

Todo ID de página es `materia/tipo/slug`.
Enlace dentro de la materia: `[[tipo/slug]]`. Entre materias: forma completa,
`[[seguridad-informatica/ataques/spectre]]`.
Sin esto, `conceptos/proceso` de dos materias se fusionan: es el modo de falla número uno
de un wiki multi-materia.

## Frontmatter estándar

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

## Inmutabilidad y trazabilidad

- `ingest/` es una **cola**, no un depósito: procesado → se mueve a `raw/`.
- `raw/` es **inmutable**. Leé; jamás escribas ni borres ahí.
- Todo archivo procesado anexa una línea a `manifest.jsonl`:
  `{"hash":"sha256…","archivo":"…","fuente_id":"…","fecha":"…","paginas_wiki":[…],"paginas_pdf":N}`
- Antes de ingerir, chequeá el hash contra el manifiesto. Si ya está: saltalo y avisá.

## Comandos

| Comando | Qué hace |
|---|---|
| `/nueva-materia <slug>` | Crea la materia desde `_plantilla`, perfila tipos y genera `programa.md`. |
| `/ingest [archivo]` | Procesa **un** archivo de `ingest/` y lo vuelca al wiki. |
| `/loop` | Vacía la cola: `/ingest` en bucle, un commit por archivo. |
| `/resumen <tema\|todo> [--perfil]` | Resumen por tema, preservando marcas, + PDF. |
| `/machete [tema]` | Una hoja, dos columnas, sin prosa. |
| `/profesor [tema] [modo]` | Te interroga (socratico/parcial/feynman/hueco/caso) y actualiza `estado/`. |
| `/lint [materia]` | Audita cobertura, huérfanas, links rotos, páginas sin `✅`. |
| `/estado [materia]` | Tablero + una recomendación accionable. |
| `/puentes` | Conexiones entre materias leyendo **solo** los `mapa.md`. |
| `/reperfilar <materia>` | Audita el esquema de tipos contra el wiki real. |
| `/archivar <materia>` | Congela la materia y la mueve a `materias/archivo/`. |

## Commits

- **Un commit por archivo ingerido**: `ingest(<materia>): <fuente-id> · N páginas`.
  Así `git revert` deshace una ingesta que salió mal.
- Migraciones de esquema: commit aislado, `schema_version` +1 en el CLAUDE.md de la materia.
- Nunca mezcles ingesta con cambios de sistema en un mismo commit.

## Principios de estudio

- Dos vías igual de válidas: leer/reelaborar (resúmenes) y recuperar (tarjetas, profesor).
- `/resumen` es función central. Nunca advertir contra su uso ni penalizarlo.
- Tarjetas y preguntas **solo** desde contenido `✅`. El material `🧠` nunca se evalúa.
- Sin scheduler: no hay colas, vencimientos, rachas ni deuda. El usuario elige qué y cuándo.
- El sistema informa ("hace 9 días que no tocás X") y sugiere. Nunca presiona.
- Intercalar solo ítems confundibles entre sí, nunca temas no relacionados.
- Pedir la confianza **antes** de revelar la respuesta, nunca después.
- Nunca afirmar mecanismos neurobiológicos. Solo conducta y retención medida.
- Detalle y citas: `global/metodo/evidencia.md`.

## Prohibido

- **Inventar contenido de materias.** Sin fuente no hay página.
- **Escribir o borrar en `raw/`.**
- **Fusionar páginas de materias distintas.** Cada materia tiene su namespace.
- **Poner contenido en `global/`.** Solo enlaces.
- **Parafrasear un enunciado formal.** Se transcribe o no se pone.
- **Leer el wiki entero "para tener contexto".** Ruteá por `mapa.md`.
