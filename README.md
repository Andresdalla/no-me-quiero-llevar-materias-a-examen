# no me quiero llevar materias a examen

Un wiki de estudio que se construye solo a partir de tus PDFs, y después te toma examen.

Es el patrón **LLM Wiki** de Andrej Karpathy adaptado a cursar la facultad: tirás apuntes,
slides y parciales viejos en una carpeta, y el sistema los compila en páginas markdown
interconectadas, con cada afirmación rastreable a la página del PDF de donde salió. Después
genera resúmenes, machetes y simulacros de parcial, y lleva registro de qué dominás.

No es una app. No hay servidor, ni frontend, ni base de datos: son carpetas markdown, cuatro
scripts de Python y once comandos de Claude Code.

## ⚠️ Antes que nada

**El wiki puede contener errores.** Lo escribe un modelo de lenguaje leyendo tus PDFs.
Por eso todo lleva marca:

| Marca | Qué significa | ¿Podés estudiarlo? |
|---|---|---|
| `✅ [fuente p.14]` | Transcripción literal de la fuente, con página | Sí |
| `🧠` | Inferencia del modelo. **No está en ninguna fuente** | Solo para entender, nunca para citar |
| `⚠️` | Dos fuentes se contradicen, o hay una duda sin resolver | No, resolvelo primero |

`🧠` y `⚠️` **no son contenido verificado**. Si vas a escribir algo en un parcial, que sea `✅`.

**Corré `/lint` antes de cada parcial.** Reporta páginas sin ninguna cita, unidades del
programa sin material y contradicciones sin resolver. Es la diferencia entre un wiki que te
salva y uno que te hace estudiar mal con confianza.

## Instalación

Necesitás **Python 3.11+** y **PyMuPDF**:

```bash
uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python pymupdf pyyaml
# o, sin uv:
python3 -m venv .venv && .venv/bin/pip install pymupdf pyyaml
```

Opcionales, cada uno degrada con elegancia si falta:

| Herramienta | Para qué | Si falta |
|---|---|---|
| **Typst** (`brew install typst`) | compilar los PDFs | se prueba pandoc; si tampoco está, queda el `.md` |
| **pandoc + LaTeX** | motor alternativo de PDF | idem |
| **Node/npx** | renderizar diagramas Mermaid | el diagrama queda como bloque de código |

Nada se instala globalmente: Mermaid se ejecuta con `npx -y @mermaid-js/mermaid-cli`.

## Flujo

```
1. /nueva-materia teoria-computacion    # datos de cursada + temario → perfila los tipos
2. copiá los PDFs a materias/activas/teoria-computacion/ingest/
3. /loop                                 # vacía la cola, un commit por archivo
4. /resumen U3 --perfil guia-parcial     # resumen + PDF
5. /profesor U3 parcial                  # simulacro y registro de dominio
```

Entre el 3 y el 4, cuando quieras: `/estado` te dice qué hacer hoy.

## Comandos

| Comando | Qué hace |
|---|---|
| `/nueva-materia <slug>` | Crea la materia, la perfila con parciales viejos y genera el programa |
| `/ingest [archivo]` | Procesa **un** archivo de la cola y lo vuelca al wiki |
| `/loop` | Vacía `ingest/` entero, un commit por archivo |
| `/resumen <tema\|todo> [--perfil]` | Resumen `breve`, `completo` o `guia-parcial`, + PDF |
| `/machete [tema]` | Una hoja, dos columnas, sin prosa |
| `/profesor [tema] [modo]` | Te interroga: `socratico`, `parcial`, `feynman`, `hueco`, `caso` |
| `/lint [materia]` | Auditoría: páginas sin cita, huérfanas, enlaces rotos, unidades sin material |
| `/estado [materia]` | Tablero + **una** recomendación accionable |
| `/puentes` | Conexiones entre materias, leyendo solo los mapas |
| `/reperfilar <materia>` | Audita el esquema de tipos contra el wiki real |
| `/archivar <materia>` | Congela la materia y genera el resumen para la correlativa |

## Cómo está organizado

```
CLAUDE.md              contrato del sistema (se carga en cada sesión)
scripts/               4 scripts: extraer texto, rasterizar, recortar figuras, compilar PDF
plantillas/            catálogo de 15 tipos de página + una plantilla por tipo
materias/activas/<m>/  ingest/ (cola) · raw/ (inmutable) · wiki/ · estado/ · assets/ · out/
materias/archivo/      materias aprobadas, congeladas
global/                índice, glosario de términos colisionados, puentes. Solo enlaces.
```

Dos reglas de diseño que conviene conocer:

- **El wiki se audita contra `programa.md`**, no contra sí mismo. Cada unidad del temario
  tiene su estado de cobertura: por eso el sistema sabe lo que le falta.
- **Nada se lee entero.** Antes de tocar una página, el modelo lee `mapa.md` (una línea por
  página) y decide qué abrir. Es lo que hace que ingerir un libro de 300 páginas sea viable.

## Qué NO hace

- No hace OCR: si el PDF es un escaneo sin texto, avisa y lo deja en `_fallidos/`.
- No commitea tu material de cátedra: `ingest/`, `raw/`, `assets/` y `out/` están
  en `.gitignore` (copyright y peso). El wiki sí se versiona.
- No estudia por vos.
