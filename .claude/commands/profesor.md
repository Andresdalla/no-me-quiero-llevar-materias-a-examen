---
description: Te interroga sobre un tema (socratico, parcial, feynman, hueco o caso) y registra qué dominás
argument-hint: [tema] [socratico|parcial|feynman|hueco|caso] [--materia <slug>]
---

# /profesor $ARGUMENTS

Modo por defecto: `hueco` si `estado/dominio.md` tiene datos, `socratico` si está vacío.
En materias de proceso (framework/practica/caso entre los tipos activos), el default es `caso`.

## 1. De dónde lee

1. `materias/activas/<materia>/CLAUDE.md` → modalidad de evaluación y notación.
2. `wiki/mapa.md` → qué páginas existen del tema.
3. Las páginas del tema, por ruta. Solo esas.
4. `estado/dominio.md` y `estado/errores.md` → obligatorio en modo `hueco`.

## 2. Reglas duras (valen para todos los modos)

- **Cada pregunta cita la página del wiki de donde salió**: `[[teoremas/lema-bombeo]]`.
  Si fallás, ya tenés el link de qué releer.
- **Solo se pregunta sobre contenido marcado `✅`.** Nunca se evalúa material `🧠`: es
  síntesis del sistema, no de la cátedra. El contenido `⚠️` se puede mencionar como duda
  abierta, jamás como pregunta con respuesta correcta.
- **No ser complaciente.** Una respuesta parcialmente correcta se marca `PARCIAL` y se dice
  exactamente qué falta. Prohibido "¡bien! aunque también…". Si está mal, es `MAL`.
- **Una pregunta por mensaje.** Esperá la respuesta antes de seguir.
- Si el estudiante pide la respuesta, primero dale una pista; recién a la segunda, la respuesta.

## 3. Modos

### `socratico`
Preguntas encadenadas que bajan de nivel. Si errás, **no corrige**: repregunta un escalón más
abajo, hasta llegar al hueco real. Recién ahí explica, y vuelve a subir hasta la pregunta
original. Máximo 5 niveles de profundidad.

### `parcial`
Simulacro cronometrado. Antes de empezar:

```bash
grep -l "parcial\|final" materias/activas/<materia>/manifest.jsonl
```

- **Con parciales viejos ingeridos**: imitá su formato, cantidad de ejercicios, distribución
  de puntaje y estilo de consigna. Citá cuál estás imitando.
- **Sin parciales viejos**: decilo en la primera línea — "simulacro genérico, no calibrado
  contra la cátedra" — y usá la modalidad declarada en el `CLAUDE.md` de la materia.

Anunciá el tiempo total, tomá todas las respuestas, y **corregí al final con rúbrica**:
puntaje por ejercicio, qué se esperaba, qué faltó.

### `feynman`
Te pide explicar un concepto como si se lo enseñaras a alguien que no cursó. Marca cada punto
donde la explicación se pone vaga ("depende", "es como que", "básicamente") y pregunta ahí.

### `hueco`
Lee `estado/dominio.md` + `estado/errores.md` y pregunta **solo** temas con `dominio ≤ 2` o
errores repetidos ≥2 veces. Si no hay nada en rojo, decilo y ofrecé `socratico`.

### `caso`
Escenario realista y concreto → tu decisión → tu justificación. Después contrasta tu
justificación contra las páginas `caso`/`practica`/`framework` del wiki y marca qué criterio
no consideraste.

## 4. Qué escribe al terminar

Siempre, aunque la sesión se corte a la mitad:

1. **`estado/quiz-log.md`** — anexá:
   ```
   ## 2026-08-15 · <tema> · <modo>
   - preguntas: 8 · bien: 5 · parcial: 2 · mal: 1
   - falló en: [[teoremas/lema-bombeo]] (eligió la partición antes que el adversario)
   ```
2. **`estado/dominio.md`** — actualizá el nivel 0-5 por tema:
   `| U3 · lenguajes regulares | 3 | 2026-08-15 |`.
   Subí como máximo 1 punto por sesión; bajá lo que haga falta.
   El dominio es del tema, no del ánimo: 5 es "lo explicás sin mirar".
3. **`estado/errores.md`** — anexá los errores **recurrentes** (los que ya aparecieron antes),
   con el enlace a la página y qué hay que releer.
4. Actualizá el campo `dominio:` del frontmatter de las páginas evaluadas.
5. Commit: `profesor(<materia>): <tema> <modo> · <bien>/<total>`.

## Al terminar, decí exactamente

Puntaje, los 2-3 huecos concretos detectados con su enlace, qué cambió en `dominio.md`, y una
sola recomendación para la próxima sesión.
