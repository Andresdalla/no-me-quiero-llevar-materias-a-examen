---
description: Vacía la cola ingest/ ejecutando /ingest archivo por archivo, un commit por archivo
argument-hint: [--materia <slug>]
---

# /loop $ARGUMENTS

Vacía la cola de una materia. **No es el `/loop` del harness** (ese agenda prompts
recurrentes): este vacía `ingest/`. Si hay ambigüedad al invocarlo, elegí el del proyecto.

## 1. Listar la cola

```bash
ls -1 materias/activas/<materia>/ingest/ | grep -v '^_' | sort
```

- Si está vacía: decí "cola vacía" y terminá.
- Mostrá la lista con su tamaño y cuántos archivos son. Si son más de 10, avisá que va a
  tomar varias iteraciones y pedí confirmación.

## 2. Orden de proceso

1. Temario y programa.
2. Parciales y finales viejos.
3. Guías de ejercicios.
4. Apuntes y libros, del más chico al más grande.

Lo chico primero: cada ingesta hace mejor la siguiente, porque `mapa.md` crece.

## 3. Bucle

Para cada archivo, en orden:

1. Ejecutá `/ingest <archivo>` completo, sus 12 pasos.
2. Verificá que el commit se hizo: `git log --oneline -1` tiene que empezar con `ingest(`.
3. **Descartá el contexto del archivo**: no arrastres `texto.md`, ni las imágenes, ni las
   páginas escritas a la iteración siguiente. La próxima arranca releyendo `mapa.md` fresco.
4. Seguí con el próximo.

## 4. Manejo de fallas

Si un archivo falla (PDF escaneado, corrupto, `pdf_texto.py` con error, o la pasada de
verificación falla en las 3 afirmaciones):

```bash
mkdir -p materias/activas/<materia>/ingest/_fallidos
mv materias/activas/<materia>/ingest/<archivo> materias/activas/<materia>/ingest/_fallidos/
```

Anotá en `wiki/log.md`: `<fecha> · <archivo> · FALLÓ: <motivo en una línea>`, commiteá esa
anotación y **seguí con el próximo archivo**. Un archivo roto no frena la cola.

## 5. Cierre

Cuando `ingest/` quede sin archivos (ignorando `_fallidos/`):

```bash
ls -1 materias/activas/<materia>/ingest/ | grep -v '^_' | wc -l   # tiene que dar 0
ls .cache/ 2>/dev/null | wc -l                                     # tiene que dar 0
git log --oneline | head -20
```

Informá en una tabla: archivo · fuente_id · páginas nuevas · resultado. Después:

- Cuántas unidades del programa cambiaron de cobertura.
- Cuántas siguen en `sin-material`.
- Qué quedó en `_fallidos/` y por qué.
- Recomendación: `/lint <materia>` si hubo más de 3 ingestas, si no `/estado <materia>`.
