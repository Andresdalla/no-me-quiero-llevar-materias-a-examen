---
description: Examen completo en condiciones reales, corregido con la rúbrica de la cátedra
argument-hint: <materia> [--reservado] [--unidades U3,U5]
---

# /simulacro $ARGUMENTS

Un examen entero, de una sentada, sin ayuda. Distinto de `/profesor parcial`: ahí te
interrogan y podés preguntar; acá rendís.

Es la medición más cercana a la condición real, y por eso pesa más que cualquier repaso.

## 1. Elegir el examen

**Con `--reservado`** (cuando quieras una medición limpia, típicamente la última):

```bash
ls materias/activas/<materia>/raw/examenes/_reservado/
```

- Si hay un examen ahí: **este es el bueno.** Nunca lo viste, ni vos ni el wiki.
- Extraé su texto ahora con `pdf_texto.py` a `.cache/`, tomalo, y al terminar movelo a
  `raw/examenes/` y procesalo con `/ingest --tipo examen` para que alimente `patron.md`.
- Si la reserva está vacía: **decilo y no lo disimules.** "No hay examen reservado: el
  simulacro va a estar armado con consignas que ya viste, así que el puntaje va a salir más
  alto de lo real."

**Sin `--reservado`**: armá el examen desde `wiki/examenes/patron.md`, imitando distribución
de puntaje, cantidad de ejercicios y verbos reales. Si no hay `patron.md`, avisá que es
genérico y usá la modalidad del `CLAUDE.md` de la materia.

## 2. Condiciones

Antes de empezar, anunciá: cantidad de ejercicios, puntaje de cada uno, tiempo total (el real
de la cátedra) y hora de inicio.

Durante el simulacro:

- **Entregá todas las consignas juntas**, como en un parcial. No de a una.
- **No respondas preguntas, no des pistas, no corrijas sobre la marcha.** Si el usuario
  pregunta algo, contestá "en el parcial tampoco te lo van a responder" y seguí.
- No interrumpas para avisar el tiempo salvo que lo pida.

## 3. Corrección

Al recibir las respuestas, corregí **con la rúbrica de la cátedra**:

| Ejercicio | Puntaje | Obtenido | Qué se esperaba | Qué faltó |
|---|---|---|---|---|

- Nota en la **escala de la cátedra** (la del `CLAUDE.md` de la materia), no en porcentaje
  genérico. Si el parcial se aprueba con 60/100, decí si aprobabas.
- **Sin complacencia.** Una demostración con el paso clave sin justificar no es "casi
  correcta": es incompleta, y en el parcial se corrige así.
- Cada ejercicio fallado lleva el enlace a la página del wiki que lo cubría, o la marca
  `HUECO` si el wiki no lo cubría.

## 4. Cruce con calibración

Lo más útil del simulacro. Para cada ejercicio pedí la confianza 1-5 **antes de corregir**, y
después mostrá:

```
Dónde te sentías seguro y fallaste:
  Ej. 3 (25 pts) · confianza 5 · obtuviste 8/25 → [[teoremas/rice]]
  Es el ejercicio que más caro te sale en el parcial real.
```

Esa combinación —alta confianza, bajo puntaje, mucho valor— es exactamente lo que hace que
alguien reprueba un parcial que creía tener.

## 5. Qué actualiza

1. **`estado/simulacros.md`**:
   ```
   ## 2026-09-15 · parcial-2025-2 (reservado) · 62/100
   - por unidad: U3 20/25 · U5 12/30 · U7 30/45
   - sobreconfianza en: U5 (conf 4.5 / 40%)
   ```
2. **`estado/dominio.md`** — con **más peso que un repaso**: un simulacro puede mover el
   dominio de un tema hasta 2 puntos, para arriba o para abajo. Es la medición más honesta
   que tiene el sistema.
3. **`estado/calibracion.md`** — la brecha medida en condiciones reales pisa a la de repasos.
4. **`estado/historial.md`** y `estado/errores.md` con lo recurrente.
5. Si usaste `--reservado`: movelo a `raw/examenes/` y marcalo `"reservado": false, "usado":
   "<fecha>"` en `manifest.jsonl`. **La reserva queda vacía**: avisalo, porque el próximo
   simulacro ya no va a ser ciego.
6. Commit: `simulacro(<materia>): <fuente_id> · <nota>`.

## Al terminar, decí exactamente

Nota en la escala de la cátedra y si aprobabas, el desglose por unidad, el ejercicio donde la
brecha de calibración fue mayor, y qué unidades tienen `HUECO` en el wiki. Sin sugerir cuándo
repetirlo.
