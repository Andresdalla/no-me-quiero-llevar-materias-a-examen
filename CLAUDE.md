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
  especificaciones, valores numéricos): **transcribilo textual** de la fuente.
  Prohibido parafrasear.
- **Contenido sintetizado** (intuiciones, explicaciones, conexiones, ejemplos propios,
  comparaciones): **esperado**, y declarado como tal. Una sección que es puro contenido
  literal está a medio escribir: `incluye comentario del sistema` es la marca de una página
  bien redactada, no la señal de una excepción que haya que justificar.

**El cuerpo del texto va limpio: sin emojis y sin citas intercaladas.** La atribución vive en
un bloque `## Procedencia` al final de cada página, una línea por sección o subsección:

```markdown
## Procedencia

- **Enunciado** — sipser-cap1 p.31, p.32
- **Notación › Conflicto entre apuntes** — notas-catedra p.2 · incluye comentario del sistema · duda: las dos fuentes usan flechas distintas
- **Contraejemplo** — sin cita: comentario del sistema
```

Con fuente: `<fuente-id> p.N`, varias separadas por `·`. Sin respaldo: `sin cita: comentario
del sistema`. Con ambas cosas: agregá `incluye comentario del sistema`. Con contradicción:
`duda: <frase entera>` (o `duda registrada en dudas.md`), y además entrada en `wiki/dudas.md`.

La granularidad es la del encabezado: si una sección mezcla a un grano más fino del que podés
atribuir, **partila en subsecciones**.

Una página sin ninguna línea con fuente es sospechosa: `/lint` la reporta.
`/profesor` y `/cards` solo usan secciones cuya procedencia es una fuente.

## Reglas de redacción — se escribe para leer, no para archivar

- **Ninguna cita ni fórmula queda flotando sola.** Una oración la introduce diciendo qué
  establece, o la sigue diciendo qué consecuencia tiene. La cita va textual; lo que la rodea
  es tuyo y es obligatorio.
- **Escribí en párrafos, no en fichas.** Objetivo: 40-90 palabras, dos a cuatro oraciones.
  Un párrafo de una sola oración vale solo si es un veredicto.
- **Cada sección se lee de corrido.** Si dos bloques seguidos no tienen relación explícita,
  falta una oración entre ellos o sobra uno de los dos.
- **Las listas valen cuando el contenido es una lista** (hipótesis, pasos). Cada ítem es una
  oración completa y arriba va una línea que dice qué organiza la lista.
- **Toda página abre con dos o tres oraciones antes del primer `##`**: qué es y por qué importa.
- **Prohibida la sobre-explicación.** Nada de `Es importante notar que`, `Cabe destacar`,
  `En resumen`, ni repetir el encabezado, ni resumir al final lo recién dicho, ni anunciar la
  estructura, ni hedging. **Si borrás una oración y no se pierde información, sobraba.**
- **No aplica** a `/machete`, `/cards`, `/estado`, `/plan`, `/puentes`, a las tablas de
  `comparativa` y `framework`, ni a `## Procedencia`: son tersos por diseño.

Registro, pares antes/después y contraejemplos: `global/metodo/redaccion.md`.

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
| `/vaciar-cola` | Vacía la cola: `/ingest` en bucle, un commit por archivo. |
| `/resumen <tema\|todo> [--perfil]` | Resumen por tema, con su procedencia, + PDF. |
| `/machete [tema]` | Una hoja, dos columnas, sin prosa. |
| `/profesor [tema] [modo]` | Te interroga (socratico/parcial/feynman/hueco/caso) y actualiza `estado/`. |
| `/lint [materia]` | Audita cobertura, huérfanas, links rotos, páginas sin fuente. |
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
- Tarjetas y preguntas **solo** desde secciones con fuente. Lo elaborado por el sistema
  nunca se evalúa.
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
