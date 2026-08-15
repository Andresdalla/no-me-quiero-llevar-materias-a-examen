---
description: Procesa UN archivo de la cola ingest/ y lo vuelca al wiki de la materia
argument-hint: [archivo] [--materia <slug>]
---

# /ingest $ARGUMENTS

Procesa **un solo** archivo. Un archivo, un commit. Si querés vaciar la cola entera, usá `/loop`.

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

- **Literal se transcribe**: definiciones, teoremas, enunciados, fórmulas, valores numéricos
  van textuales, con `✅ [<fuente_id> p.N]`. La página `p.N` sale de los marcadores
  `<!-- p.N -->` de `texto.md`. Prohibido parafrasear.
- **Síntesis se marca `🧠`**: intuiciones, conexiones, ejemplos propios.
- **Contradicción con otra fuente → `⚠️`** en la página **y** entrada en `wiki/dudas.md`.
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

Elegí **3 afirmaciones marcadas `✅` al azar** entre las que acabás de escribir y buscá cada
una en `.cache/<hash8>/texto.md`:

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

## Al terminar, decí exactamente

`<fuente_id>`: N páginas nuevas, M actualizadas, verificación N/3, unidades que cambiaron de
cobertura, y qué quedó en `dudas.md`. Nada más.
