---
description: Procesa UN archivo de la cola ingest/ y lo vuelca al wiki de la materia
argument-hint: [archivo] [--tipo examen] [--materia <slug>]
---

# /ingest $ARGUMENTS

Procesa **un solo** archivo. Un archivo, un commit. Si querés vaciar la cola entera, usá `/vaciar-cola`.

**Si el archivo es un parcial, final o recuperatorio viejo, usá `--tipo examen`**: tiene su
propio pipeline (paso 13) y no escribe páginas de concepto. Si detectás que un archivo sin
`--tipo` es un examen (consignas numeradas, puntajes, "duración: 2 horas"), preguntá antes de
seguir.

`PY` = `.venv/bin/python` si existe, si no `python3`.

## 1. Contexto mínimo

Leé **solo** estos dos archivos de la materia:

- `materias/activas/<materia>/CLAUDE.md` → tipos activos, alias, notación, reglas propias.
- `materias/activas/<materia>/wiki/mapa.md` → qué páginas ya existen.

**No leas nada más del wiki.** Ni `index.md`, ni las páginas, ni el directorio.
Si `mapa.md` no alcanza para decidir, abrí como mucho 3 páginas concretas por su ruta.

Si hay varias materias activas y no se indicó cuál, preguntá y frená.

## 2. Elegir archivo y chequear el hash

```bash
ls -t materias/activas/<materia>/ingest/ | tail -1      # el más antiguo, si no se indicó otro
shasum -a 256 materias/activas/<materia>/ingest/<archivo>
grep -c "<hash>" materias/activas/<materia>/manifest.jsonl
```

Si el `grep` devuelve ≥1: **saltá el archivo**, avisá "ya ingerido como `<fuente_id>`" y terminá.

Definí el `fuente_id`: slug corto y estable, derivado del contenido, no del nombre del archivo
(`sipser-cap1`, `parcial-2024-1c`, `apunte-catedra-u3`). Es lo que va a aparecer en cada cita.

## 3. Extraer texto

```bash
$PY scripts/pdf_texto.py <ruta> --out .cache/<hash8>/
```

Leé **primero** `.cache/<hash8>/analisis.json`, después `texto.md`.

- Si `probable_escaneado` es `true`: frená. Avisá que necesita OCR, movelo a
  `ingest/_fallidos/` y no inventes contenido.
- Si el archivo no es PDF (`.md`, `.txt`): leelo directo, saltá al paso 6.

## 4. Documentos largos

Si `paginas > 60`: procesá **por capítulo o sección**, no entero.

```bash
$PY scripts/pdf_texto.py <ruta> --paginas 1-40 --out .cache/<hash8>-p1/
```

Un `/ingest` por tramo, cada uno con su commit. En `manifest.jsonl` va una línea por tramo,
con el mismo hash y el rango en `archivo`.

## 5. Mirar solo lo necesario

De `candidatas_visuales`, tomá las de `confianza >= 0.6`:

```bash
$PY scripts/pdf_render.py <ruta> --paginas 12,13,20 --out .cache/<hash8>/png/ --dpi 150
```

Mirá esas imágenes. **Nunca rasterices el PDF completo.** Si hay más de 15 candidatas,
quedate con las 15 de mayor confianza y anotá el resto en `wiki/log.md`.

## 6. Plan antes de escribir

Mostrá un plan de 10-15 líneas, una línea por página:

```
CREA  teoremas/lema-bombeo          U3  ← p.77-79
CREA  demostraciones/lema-bombeo    U3  ← p.78
ACTUALIZA definiciones/lenguaje-regular  U2  ← p.31 (agrega contraejemplo)
```

- Si el plan supera **20 páginas nuevas**, pedí confirmación: es señal de que el documento
  debería partirse.
- Cada página nueva usa un tipo **activo** de la materia. Si necesitás uno que no está
  activo, decilo en el plan y esperá el OK: puede ser señal de `/reperfilar`.

## 7. Escribir las páginas

Copiá la plantilla del tipo desde `plantillas/paginas/<tipo>.md` y completala. Reglas duras:

- **El cuerpo va limpio**: sin emojis y sin citas intercaladas.
- **Literal se transcribe**: definiciones, teoremas, enunciados, fórmulas, valores numéricos
  van textuales. Prohibido parafrasear.
- **Toda página cierra con `## Procedencia`**, una línea por sección: `<fuente_id> p.N`, o
  `sin cita: comentario del sistema`. La página `p.N` sale de los marcadores `<!-- p.N -->`
  de `texto.md`.
- **Contradicción con otra fuente**: la sección agrega `duda: <frase>` en su línea de
  Procedencia **y** se anota en `wiki/dudas.md`.
- Si una sección mezcla transcripción y comentario a un grano más fino del que podés
  atribuir, partila en subsecciones.
- Frontmatter completo, `actualizado` con la fecha de hoy, `id` en la forma
  `<materia>/<carpeta-plural>/<slug>`.
- Enlaces internos `[[carpeta/slug]]`; entre materias, forma completa.
- **Tope 150 líneas.** Si se pasa, partí y enlazá.
- Toda página nueva necesita al menos un enlace entrante desde otra página o desde `index.md`.

## 8. Figuras

Solo si la página las necesita para entenderse:

```bash
$PY scripts/pdf_figs.py <ruta> --pagina 12 --bbox <bbox-del-analisis> \
   --out materias/activas/<materia>/assets/<fuente_id>/p12-fig1.png
```

Referencialas con ruta relativa desde la página.

## 9. Pasada de verificación

Elegí **3 afirmaciones al azar** de secciones con fuente entre las que acabás de escribir, y
buscá cada una en `.cache/<hash8>/texto.md`:

```bash
grep -n "<fragmento textual>" .cache/<hash8>/texto.md
```

- Si no aparece, o aparece en otra página: corregí la cita o el texto.
- Anotá el resultado en `wiki/log.md`: `verificación: 3/3 OK` o el detalle de lo corregido.

## 10. Actualizar los índices

- `wiki/mapa.md`: una línea por página nueva, formato
  `<carpeta>/<slug> · <tipo> · <U#> · <descripción de 8 palabras>`. Ordenado por unidad.
- `wiki/index.md`: enlace a las páginas nuevas bajo su unidad.
- `wiki/log.md`: `<fecha> · <fuente_id> · <N> páginas nuevas, <M> actualizadas · verificación N/3`.
- `wiki/programa.md`: subí la `cobertura` de las unidades tocadas y agregá el `fuente_id` a
  su lista de `fuentes`. `parcial` si quedó material sin cubrir, `cubierto` si no.

## 11. Cerrar la ingesta

```bash
mv materias/activas/<materia>/ingest/<archivo> materias/activas/<materia>/raw/<archivo>
echo '{"hash":"<sha256>","archivo":"<archivo>","fuente_id":"<id>","fecha":"<hoy>","paginas_wiki":["<id1>","<id2>"],"paginas_pdf":<N>}' \
  >> materias/activas/<materia>/manifest.jsonl
rm -rf .cache/<hash8>/
```

`raw/` es inmutable: movés el archivo ahí y no lo tocás nunca más.

## 12. Commit

```bash
git add -A && git commit -m "ingest(<materia>): <fuente_id> · <N> páginas"
```

## 13. Pipeline `--tipo examen`

Reemplaza los pasos 6-11. Un enunciado de parcial **no es una definición**: no escribe ni
toca ninguna página de concepto.

### 13.1 ¿Va a la reserva ciega?

```bash
ls materias/activas/<materia>/raw/examenes/ 2>/dev/null | wc -l
ls materias/activas/<materia>/raw/examenes/_reservado/ 2>/dev/null | wc -l
```

**El examen más reciente de la materia se reserva sin abrir.** Si el que estás por procesar
es más nuevo que todos los de `raw/examenes/`, y la reserva está vacía:

```bash
mkdir -p materias/activas/<materia>/raw/examenes/_reservado
mv <archivo> materias/activas/<materia>/raw/examenes/_reservado/
```

**No lo extraigas, no lo leas, no lo transcribas.** Anotalo en `manifest.jsonl` con
`"reservado": true` y terminá. Sin reserva ciega, el simulacro previo al parcial no mide
nada: ya viste todo. Si el usuario insiste en procesarlo, avisá qué pierde y pedí confirmación
explícita.

Si ya hay uno reservado y el nuevo es más reciente, ofrecé rotar: el reservado pasa a
procesarse y el nuevo ocupa su lugar.

### 13.2 Transcribir consignas

Una entrada por consigna en `wiki/examenes/<fuente_id>.md`:

```markdown
## e2024p1-q3
**Consigna:** [transcripción literal]
**Fuente:** parcial-2024-1 p.2
**Unidad:** U3          **Puntaje:** 20/100
**Tipo:** demostrar     **Verbo:** "probar que ... no es regular"
**Bloom:** aplicar
**Resolución:** inferida    # oficial | catedra | inferida
**Cubierto_por:** [teoremas/bombeo-regulares]
**Estado_wiki:** cubierto   # cubierto | parcial | HUECO
```

- La consigna se transcribe **literal**, palabra por palabra. Es lo único que dice cómo
  escriben las preguntas.
- `Resolución: oficial` solo si el PDF trae la solución de la cátedra. Si la resolvés vos,
  es `inferida`. **Nunca presentes una resolución inferida como verificada**:
  estudiar una solución equivocada es peor que no tener ninguna.
- `Estado_wiki` sale de contrastar contra `mapa.md`: `HUECO` si el wiki no tiene con qué
  responderla. Cada `HUECO` genera una entrada en `wiki/dudas.md`.

### 13.3 Regenerar `wiki/examenes/patron.md`

Con **todos** los exámenes procesados (nunca el reservado):

```markdown
# Patrón de evaluación · 3 exámenes

## Puntaje por unidad
| Unidad | 2023-1 | 2024-1 | 2024-2 | Promedio |
|---|---|---|---|---|
| U3 | 20 | 30 | 25 | 25% |

## Verbos recurrentes
| Verbo | Veces | Nivel |
|---|---|---|
| "probar que… no es regular" | 3/3 | aplicar |
| "construir un autómata que…" | 2/3 | crear |

## Constantes, ausencias y novedades
- **Siempre**: U3 (3/3), bombeo (3/3)
- **Nunca**, aunque está en el programa: U7
- **Nuevo en el último**: reducciones entre problemas

## Huecos
| Consigna | Unidad | Por qué no se puede responder |
|---|---|---|
| e2024p1-q5 | U6 | sin material ingerido de la unidad |
```

Los verbos son lo que fija a qué nivel de Bloom hay que llegar en cada unidad: **evidencia,
no heurística**.

### 13.4 Cerrar

```bash
mkdir -p materias/activas/<materia>/raw/examenes
mv <archivo> materias/activas/<materia>/raw/examenes/
```

Manifiesto con `"tipo": "examen"`. Commit: `ingest(<materia>): <fuente_id> · examen · N consignas`.

## Al terminar, decí exactamente

`<fuente_id>`: N páginas nuevas, M actualizadas, verificación N/3, unidades que cambiaron de
cobertura, y qué quedó en `dudas.md`. Nada más.

Con `--tipo examen`: N consignas transcriptas, cuántas quedaron `HUECO`, qué cambió en
`patron.md`, y si el archivo fue a la reserva ciega.
