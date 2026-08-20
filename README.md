# no me quiero llevar materias a examen

Es el patrón **LLM Wiki** de Andrej Karpathy adaptado a cursar la facultad: tirás apuntes,
slides y parciales viejos en una carpeta, y el sistema los compila en páginas markdown
interconectadas, con cada afirmación rastreable a la página del PDF de donde salió. Después
genera resúmenes, machetes, tarjetas y simulacros, y lleva registro de qué dominás y de
cuánto te estás creyendo que sabés.

## Antes que nada

**El wiki puede contener errores.** Lo escribe un modelo de lenguaje leyendo tus PDFs. Por eso
cada página cierra con un bloque **`## Procedencia`** que dice, sección por sección, de dónde
salió lo que leíste:

```markdown
## Procedencia

- **Enunciado** — sipser-cap1 p.31, p.32
- **Notación › Conflicto entre apuntes** — notas-catedra p.2 · incluye comentario del sistema · duda: las dos fuentes usan flechas distintas
- **Contraejemplo** — sin cita: comentario del sistema
```

| Lo que dice la procedencia | ¿Podés estudiarlo? |
|---|---|
| `<fuente> p.N` | Sí: es transcripción literal de esa página |
| `incluye comentario del sistema` | El contenido de la fuente sí; el comentario, para entender |
| `sin cita: comentario del sistema` | **No está en ninguna fuente.** Nunca lo cites en un parcial |
| `duda: …` | No: hay una contradicción sin resolver. Está en `dudas.md` |

El cuerpo del texto va limpio, sin emojis ni citas intercaladas. Las tarjetas y las preguntas
del modo profesor salen **solo** de secciones con fuente: nunca vas a terminar memorizando
una inferencia del sistema.

Las páginas se escriben en prosa, no en fichas: cada definición o fórmula va embebida en una
oración que dice qué hace y por qué está ahí. El registro, con pares antes/después de páginas
reales: `global/metodo/redaccion.md`.

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
1. /nueva-materia teoria-computacion   # datos de cursada + temario → perfila los tipos
2. copiá los PDFs a materias/activas/teoria-computacion/ingest/
3. /vaciar-cola                        # compila el wiki, un commit por archivo
4. /resumen U3 --perfil completo       # estudiás
   /cards U3  →  /repasar U3           # o recuperás
5. /profesor U3 parcial                # te toma examen y mide qué dominás
```

Cuando no sepas qué hacer, `/estado` te dice cómo venís y sugiere una cosa.

## Dos vías, y ninguna es la correcta

El sistema no te empuja a estudiar de una manera:

- **Leer y reelaborar** — `/resumen` en cinco perfiles, `/machete`. Si estudiás con
  resúmenes y te funciona, seguí: es una función central y no vas a encontrar una sola
  advertencia en contra.
- **Recuperar** — `/cards` + `/repasar`, `/profesor`, `/simulacro`.

Las dos cuentan igual. Lo que sí hace el sistema es **medir la brecha entre lo que creés que
sabés y lo que sabés**: te pide la confianza antes de cada respuesta, y te avisa cuando un
tema te dejó una sensación de dominio que no se corresponde. Esa es la función que más
parciales salva.

**No hay agenda.** Nada se vence, nada se acumula, no hay colas diarias ni conteo de días.
Vos elegís qué y cuándo; el sistema informa ("hace 9 días que no tocás reducciones") y
sugiere. Por qué está diseñado así, con las citas: `global/metodo/evidencia.md`.

## Exámenes viejos: la mejor fuente que tenés

Un parcial viejo es lo único que dice **qué te van a preguntar y cómo**. Se ingiere aparte:

```bash
/ingest parcial-2024-1.pdf --tipo examen
```

- No escribe páginas de concepto: un enunciado de parcial no es una definición.
- Genera `wiki/examenes/patron.md`: cuánto vale cada unidad, qué verbos usan las consignas,
  qué entra siempre, qué nunca entró y qué consignas tu wiki **no puede responder**.
- Con eso, `/plan` prioriza por puntaje en riesgo y `/profesor parcial` imita el formato real.
- **El examen más reciente se reserva sin abrirlo**, para que el simulacro previo al parcial
  mida algo. `/lint` te avisa si te quedaste sin reserva.

## Comandos

**Construir el wiki**

| Comando | Qué hace |
|---|---|
| `/nueva-materia <slug>` | Crea la materia, la perfila con los parciales viejos y genera el programa |
| `/ingest [archivo] [--tipo examen]` | Procesa **un** archivo de la cola y lo vuelca al wiki |
| `/vaciar-cola` | Vacía `ingest/` entero, un commit por archivo |

**Estudiar**

| Comando | Qué hace |
|---|---|
| `/resumen <tema> [--perfil]` | `breve`, `completo`, `guia-parcial`, `esqueleto` (para completar vos) o `anotado` (con preguntas al margen) |
| `/resumen-ciego <tema>` | Lo escribís de memoria y te dice qué faltó, qué está mal y qué te inventaste |
| `/machete [tema]` | Una hoja, dos columnas, sin prosa |
| `/cards <tema>` | Tarjetas de recuperación, solo desde secciones con fuente |
| `/repasar <tema>` | Sesión de recuperación con esas tarjetas, cuando vos quieras |
| `/pre-test <tema>` | Cinco preguntas **antes** de estudiar. Vas a fallar: ese es el punto |

**Medir**

| Comando | Qué hace |
|---|---|
| `/profesor [tema] [modo]` | Te interroga: `socratico`, `parcial`, `feynman`, `hueco`, `caso` |
| `/simulacro <materia> [--reservado]` | Examen completo, tiempo real, corregido en la escala de la cátedra |
| `/estado [materia]` | Tablero: cobertura, dominio, calibración, qué hace rato que no tocás |
| `/plan <materia> --hasta <fecha>` | Propone un reparto. Si no alcanza el tiempo, te lo dice |

**Mantener**

| Comando | Qué hace |
|---|---|
| `/lint [materia]` | Auditoría: páginas sin cita, huérfanas, enlaces rotos, consignas sin cubrir |
| `/puentes` | Conexiones entre materias, leyendo solo los mapas |
| `/reperfilar <materia>` | Audita el esquema de tipos contra el wiki real |
| `/archivar <materia>` | Congela la materia y genera el resumen para la correlativa |

## Cómo está organizado

```
CLAUDE.md              contrato del sistema (se carga en cada sesión)
scripts/               4 scripts: extraer texto, rasterizar, recortar figuras, compilar PDF
plantillas/            catálogo de 15 tipos de página + una plantilla por tipo
materias/activas/<m>/
  ingest/              cola de entrada
  raw/                 inmutable · raw/examenes/_reservado/ es el examen ciego
  wiki/                las páginas · mapa.md para rutear · programa.md como espina dorsal
  cards/               tarjetas por tema
  estado/              dominio, calibración, errores, historial, simulacros, plan
  out/                 resúmenes, machetes y PDFs generados
materias/archivo/      materias aprobadas, congeladas
global/                índice, glosario, puentes y método. Solo enlaces, nunca contenido.
```

Tres reglas de diseño que conviene conocer:

- **El wiki se audita contra `programa.md`**, no contra sí mismo. Cada unidad del temario
  tiene su estado de cobertura: por eso el sistema sabe lo que le falta.
- **Nada se lee entero.** Antes de tocar una página, el modelo lee `mapa.md` (una línea por
  página) y decide qué abrir. Es lo que hace que ingerir un libro de 300 páginas sea viable.
- **Un commit por archivo ingerido.** Si una ingesta sale mal, `git revert` de ese commit.

## Qué NO hace

- No hace OCR: si el PDF es un escaneo sin texto, avisa y lo deja en `_fallidos/`.
- No commitea tu material de cátedra: `ingest/`, `raw/`, `assets/` y `out/` están
  en `.gitignore` (copyright y peso). El wiki y las tarjetas sí se versionan.
- No te reclama nada: no hay notificaciones, ni rachas, ni nada que se venza.
- No estudia por vos.
