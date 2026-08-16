---
description: Congela una materia terminada: genera resumen-final, la mueve a archivo/ y reapunta los puentes
argument-hint: <materia>
---

# /archivar $1

Se corre cuando la materia está aprobada. Lo que queda es lo que vas a necesitar cuando la
uses de correlativa, dentro de dos años, sin acordarte de nada.

`M` = `materias/activas/$1`. `PY` = `.venv/bin/python` si existe, si no `python3`.

## 1. Chequeos previos

```bash
ls materias/activas/$1/ingest/ | grep -v '^_' | wc -l   # tiene que dar 0
```

- Si queda material en la cola: avisá y ofrecé correr `/vaciar-cola` antes de congelar.
- Corré `/lint $1` y mostrá el resultado. Archivar con 6 páginas sin fuente congela el error
  para siempre. Preguntá si quiere arreglarlo antes.
- Preguntá la **nota final** y si la materia quedó aprobada, para registrarla en el índice.

## 2. Generar `resumen-final.md`

2-3 páginas en `$M/resumen-final.md`. No es un resumen de estudio: es lo mínimo para
retomar la materia de cero. Contenido, en este orden:

1. **Qué es la materia en 5 líneas** y para qué sirve en las correlativas.
2. **Los 10-15 resultados centrales**: enunciados literales, con su fuente en Procedencia.
3. **Los procedimientos** que hay que saber ejecutar, en una línea cada uno, con enlace.
4. **Vocabulario y notación de la cátedra**, del `CLAUDE.md` de la materia.
5. **Lo que te costó**: sacado de `estado/errores.md`. Es lo que te va a volver a costar.
6. **Puentes**: qué materias la usan o la continúan.

Compilá a PDF:
```bash
$PY scripts/build_pdf.py materias/activas/$1/resumen-final.md \
  --out materias/activas/$1/out/ --perfil guia
```

## 3. Mover

```bash
DEST=materias/archivo/<año>-<cuatri>-$1     # ej. 2026-2C-teoria-computacion
git mv materias/activas/$1 $DEST
```

El `resumen-final.md` va **fuera** de `wiki/`, en la raíz de la carpeta archivada: tiene que
ser lo primero que se vea.

## 4. Reapuntar

1. `global/indice.md`: estado `archivada`, nota final, ruta nueva.
2. **Todos los enlaces a esta materia** en puentes y en otras materias:
   ```bash
   grep -rl "\[\[$1/" global/ materias/activas/
   ```
   Reemplazá `[[$1/...]]` por `[[archivo/<año>-<cuatri>-$1/...]]`.
   Un enlace roto acá es una materia que perdiste.
3. `global/glosario.md`: las acepciones de esta materia se conservan, con la marca
   `(archivada)`.

## 5. Verificar y commitear

```bash
grep -roh "\[\[[^]]*\]\]" global/ materias/activas/ | sort -u   # ningún [[<slug-viejo>/…]]
ls materias/archivo/<año>-<cuatri>-$1/resumen-final.md
git add -A && git commit -m "archivar($1): <nota> · <N> páginas congeladas"
```

## Qué NO hace

- No borra nada. `raw/` viaja con la materia archivada.
- No toca las páginas del wiki: quedan como estaban. Archivar es congelar, no reescribir.

## Al terminar, decí exactamente

Ruta nueva, cuántas páginas se congelaron, cuántos enlaces se reapuntaron y dónde quedó el
`resumen-final.pdf`.
