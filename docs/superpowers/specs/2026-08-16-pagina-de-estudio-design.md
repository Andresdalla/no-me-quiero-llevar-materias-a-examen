# Página de estudio — diseño

Fecha: 2026-08-16 · Estado: aprobado, pendiente de plan de implementación

Una superficie visual para las dos cosas que hoy solo pasan en la terminal y se sienten
incómodas ahí: correr una sesión de tarjetas y disparar comandos. Es un HTML autocontenido
que se genera con un script y se abre con doble click. No hay servidor, no hay app, no hay
dependencias nuevas.

## Decisiones tomadas

Cada una con su alternativa descartada, para que el plan no las reabra.

- **Alcance: un script más, salida estática.** Se descartó la app web local con servidor.
  El sistema sigue siendo carpetas markdown + scripts + comandos slash.
- **Estética: fichas.** Tarjeta blanca sobre gris, sans-serif, acento índigo, chip de color
  por tipo de tarjeta. Se descartaron la dirección papel/serif y la dirección consola/oscura.
- **Layout: sidebar fijo.** Temas y comandos a la izquierda, contenido a la derecha. El
  sidebar se colapsa mientras hay una sesión activa y vuelve al terminar. Se descartaron el
  home de temas con sesión a pantalla completa y la columna única apilada.
- **Viaje de vuelta: portapapeles.** La página no escribe en el repo. Se descartaron la
  File System Access API (solo Chrome/Edge) y la descarga a `~/Downloads`.
- **PDF: simulacro en blanco y parte de la sesión.** Se descartó el mazo imprimible porque
  `/machete` ya cubre ese terreno por otra vía.

## Arquitectura

```
scripts/build_estudio.py <materia> [--abrir]
        │
        │ lee
        ├── materias/activas/<m>/cards/*.md          → los mazos
        ├── materias/activas/<m>/wiki/mapa.md        → temas y unidades
        ├── materias/activas/<m>/estado/dominio.md   → dominio por tema
        ├── materias/activas/<m>/estado/historial.md → días sin tocar
        ├── materias/activas/<m>/CLAUDE.md           → nombre y fecha de parcial
        ├── materias/activas/<m>/out/.build/sesiones/*.json → sets horneados
        └── plantillas/estudio.html                  → cáscara con CSS y JS
        │
        │ escribe
        └── materias/activas/<m>/out/estudio.html    (gitignoreado)
```

`out/` ya está en `.gitignore`, así que el HTML es artefacto puro, igual que los PDFs de
`/resumen`. Nunca se commitea.

### El script

Stdlib sola, un archivo, del mismo molde que `scripts/build_pdf.py`: docstring en castellano,
`RAIZ = Path(__file__).resolve().parent.parent`, y degradación elegante en vez de abortar.

Cuatro funciones y un `main` con `argparse`:

- `leer_mazos(dir_cards)` — parsea `cards/*.md`. El formato ya es regular:
  `## <id> · <tipo>`, `**P:**`, `**R:**`, `**Fuente:**`, `**Bloom:**`,
  `**Confundible_con:**` (opcional), `**Visto:**`.
- `leer_temas(wiki, estado, claude_md)` — cruza `mapa.md`, `dominio.md` e `historial.md`.
- `leer_sesiones(dir_build)` — levanta los sets que `/profesor` y `/simulacro` hornearon.
- `render(datos, plantilla)` — inyecta los datos en la plantilla y devuelve el HTML.

### La plantilla

`plantillas/estudio.html`, al lado del `estilo.typ` que ya existe. Contiene todo el CSS y todo
el JS. El script no lleva HTML embebido: inyecta un único bloque

```html
<script id="datos" type="application/json">{ … }</script>
```

y nada más. El diseño se retoca sin abrir Python.

### Forma de los datos inyectados

```json
{
  "materia": {
    "slug": "teoria-de-la-computacion",
    "nombre": "Teoría de la Computación",
    "parcial": "2026-12-07"
  },
  "temas": [
    {"id": "U6", "nombre": "Cardinalidad y numerabilidad",
     "dominio": 3, "ultimo": "2026-08-15", "tarjetas": 27}
  ],
  "mazos": {
    "U6": [
      {"id": "c-U6-004", "tipo": "discriminacion",
       "p": "¿Por qué `{{1, 2}} ≠ {1, 2}`…",
       "r": "El de la izquierda tiene un elemento…",
       "fuente": "revision-conjuntos p.1, p.2",
       "bloom": "analizar",
       "confundible": ["c-U6-008"]}
    ]
  },
  "sesiones": [
    {"comando": "simulacro", "modo": null, "tema": "U6",
     "generado": "2026-08-16", "minutos": 90,
     "items": [{"id": "s-01", "enunciado": "Justificá por qué…", "puntos": 10}]}
  ],
  "avisos": ["cards/U10.md · c-U10-007 sin **R:**, se salteó"]
}
```

Los ítems de `sesiones` no llevan respuesta: son texto libre que se corrige después en la
terminal contra la rúbrica de la cátedra.

## Flujo de datos

El ciclo tiene dos direcciones, y solo una de ellas necesita a Claude.

**Terminal → página.** `/profesor <tema> <modo> --a-la-pagina` y
`/simulacro <tema> --a-la-pagina` generan el set de preguntas desde secciones con fuente, lo
dejan como JSON en `out/.build/sesiones/` y rehornean el HTML.

**Página → terminal.** Al terminar cualquier sesión, un botón copia un bloque al portapapeles.
Lo pegás en Claude Code y el comando lo aplica.

`/repasar` no necesita la ida: las tarjetas ya están en `cards/` desde que se horneó el HTML.
Abrís y estudiás.

### Formato del portapapeles

Bloque cercado, primera línea el comando. Para `/repasar`, una línea por tarjeta:

```
/repasar --registrar U6 2026-08-16
c-U6-002 conf:5 fallo
c-U6-007 conf:3 parcial
c-U6-004 conf:4 ok
```

La calificación es la escala de tres que ya usa `/repasar`: `ok` · `parcial` · `fallo`.
La página no puede inventar una escala propia porque el `Visto` de `cards/*.md` se escribe
con esos tres valores.

Para `/profesor` y `/simulacro`, cada ítem abre con `## ` y su respuesta libre va debajo. El
prefijo delimita los ítems sin que el texto escrito pueda colisionar:

```
/simulacro --registrar U6 2026-08-16 87min
## s-01 conf:4
Por el axioma de extensión, un conjunto no tiene más identidad que sus
elementos, así que ni el orden ni la repetición cambian nada.
## s-02 conf:2
No me salió.
```

`conf` es la confianza declarada **antes** de revelar, en la escala 1-5 que ya usa el sistema.

### Superficie de comandos

Dos flags sobre comandos que ya existen, y un comando nuevo.

| Invocación | Qué hace |
|---|---|
| `/estudio <materia>` | Rehornea `out/estudio.html` y lo abre. Nuevo. |
| `/profesor <tema> <modo> --a-la-pagina` | Hornea el set en `out/.build/sesiones/` y rehornea el HTML, en vez de preguntar en la terminal. Solo `hueco`, `parcial` y `caso`. |
| `/simulacro <tema> --a-la-pagina` | Ídem, con minutos y puntaje del parcial. |
| `/repasar --registrar` | Aplica el bloque pegado desde la página. |
| `/profesor --registrar` | Ídem, corrigiendo las respuestas libres. |
| `/simulacro --registrar` | Ídem, contra la rúbrica de la cátedra. |

### Qué escribe cada `--registrar`

| Comando | Archivos que anexa o actualiza |
|---|---|
| `/repasar --registrar` | `cards/<tema>.md` (campo `Visto`), `estado/historial.md`, `estado/dominio.md`, `estado/calibracion.md` |
| `/profesor --registrar` | `estado/quiz-log.md`, `estado/historial.md`, `estado/calibracion.md`, `estado/dominio.md`, `estado/errores.md` |
| `/simulacro --registrar` | `estado/simulacros.md`, `estado/historial.md`, `estado/calibracion.md` |

El parseo del pegado lo hace el comando markdown, no un script: es Claude leyendo el bloque y
editando los `.md`, como todo el resto del sistema.

## Modos soportados

- **`/repasar`** — completo en la página. Las respuestas ya están escritas en `cards/`.
- **`/simulacro`** — completo en la página. Un examen es por naturaleza un lote de preguntas
  fijo, un cronómetro y una corrección posterior; encaja mejor que las tarjetas incluso.
- **`/profesor`** — solo `hueco`, `parcial` y `caso`, que son sets de preguntas fijos.

`socratico` y `feynman` **se quedan en la terminal**. Su valor es repreguntar según lo que
contestás, y un HTML horneado no puede branchear. Ponerlos en la página los convertiría en un
cuestionario disfrazado.

## Pantallas

**Sidebar fijo** (186 px): materia arriba con días al parcial, lista de temas con su cantidad
de tarjetas, y abajo la lista de comandos. Click en un comando copia el slash command ya
armado con la materia y el tema puestos — no ejecuta nada, no puede.

**Panel derecho**: la tarjeta o el ítem de examen, centrado, en tarjeta blanca con sombra
suave. Chip de color por tipo (`concepto`, `cloze`, `discriminacion`, `aplicacion`), contador
`4 de 27`, y la fuente al pie.

**Durante una sesión activa el sidebar se colapsa** y vuelve al terminar. Pedir la confianza
antes de revelar solo funciona si la respuesta y el próximo botón no están en el campo visual.

**Orden del sidebar**: por dominio bajo y días sin tocar. Sin vencimientos, sin rachas, sin
deuda acumulada. El sistema informa y sugiere; nunca reclama.

## PDF

`window.print()` más una hoja `@media print` en la plantilla. Cero dependencias, no toca
`scripts/build_pdf.py`.

Dos salidas. El botón fija `data-print` en `<html>` y el CSS muestra solo el bloque
correspondiente; también fija `document.title` para que el nombre de archivo que propone el
navegador salga bien:

| Salida | `data-print` | Título / nombre sugerido | Contenido |
|---|---|---|---|
| Simulacro en blanco | `simulacro` | `simulacro-U6-2026-08-16` | Enunciados numerados con renglones para escribir a mano, encabezado con minutos y condiciones, pie con paginado |
| Parte de la sesión | `parte` | `sesion-U6-2026-08-16` | Tabla de tarjeta, confianza declarada, resultado y brecha; abajo el diagnóstico de sobreconfianza y qué releer |

La hoja de impresión apaga sombras, fondo gris, sidebar y todo control interactivo.

## Bordes y degradación

Del mismo espíritu que `build_pdf.py`: nunca falla entero por una pieza opcional.

- Tema sin `cards/` → aparece gris en el sidebar con acción "Generar". No rompe el build.
- Tarjeta malformada → se saltea, su id entra en `avisos` y el HTML lo muestra arriba.
- `estado/dominio.md` sin filas, que es el caso hoy → se muestra `—`, nunca `0`. Un 0
  significa "no lo viste", que es una afirmación distinta y falsa.
- Fecha de parcial que no se puede parsear de `- parcial:` en el `CLAUDE.md` de la materia →
  el encabezado omite la cuenta regresiva en lugar de inventar un número.
- Pegado que no se entiende en un `--registrar` → el comando reporta qué línea falló y **no
  escribe nada**. Todo o nada, para no dejar `estado/` a medias entre archivos.
- `--abrir` usa `webbrowser.open`; si falla, imprime la ruta del archivo.

## Lo que deliberadamente no hace

- **No inventa contenido.** Solo lee `cards/`, que ya sale de secciones con fuente.
- **El navegador no escribe en el repo.** Su única salida es el portapapeles.
- **No hay scheduler.** Sin colas, vencimientos, rachas ni deuda.
- **No ejecuta comandos.** El launcher copia texto; ejecutar requiere un servidor, que está
  fuera de alcance por decisión.

## Tests

`tests/test_build_estudio.py` con `unittest` de stdlib (`python -m unittest`), sobre un
fixture chico en `tests/fixtures/cards-ejemplo.md`. No se agrega framework: hoy no hay
ninguno instalado.

Cubre:

1. Parseo de una tarjeta completa, con y sin `**Confundible_con:**`.
2. Una tarjeta malformada se saltea, entra en `avisos` y el resto del mazo sobrevive.
3. `dominio` sin filas produce `—`, no `0`.
4. Fecha de parcial impresentable produce un HTML sin cuenta regresiva, no una excepción.
5. **El HTML generado no tiene referencias externas** — sin `src="http`, `href="http`,
   `@import` ni `//cdn`. Es lo que garantiza que abra offline y sin servidor.

## Documentación a actualizar

- `CLAUDE.md` raíz: la frase *"son carpetas markdown + 4 scripts Python + comandos slash"*
  pasa a 5, y la tabla de comandos suma `/estudio`.
- `.claude/commands/repasar.md`, `profesor.md`, `simulacro.md`: el flag `--registrar`, y
  `--a-la-pagina` en los dos últimos.
- `.claude/commands/estudio.md`: nuevo. Rehornea el HTML de la materia y lo abre.
- `materias/_plantilla/`: que una materia nueva nazca con `out/.build/sesiones/`.

## Commits

Todo esto es cambio de sistema, no ingesta. Va en commits propios y nunca mezclado con
`ingest(...)`. No cambia el esquema del wiki, así que no toca `schema_version`.

## Fuera de alcance

- Tablero de estado visual (dominio, calibración, errores como gráficos). No se pidió.
- Mazo de tarjetas imprimible: `/machete` ya lo cubre.
- `socratico` y `feynman` en la página.
- Escritura al repo desde el navegador, y cualquier forma de servidor local.
