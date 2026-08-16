---
description: Sesión de recuperación con las tarjetas de un tema que vos elegís
argument-hint: <tema> [--n 15] [--tipos concepto,cloze] [--desde-errores] [--materia <slug>]
---

# /repasar $ARGUMENTS

Recuperación a demanda. **Lo iniciás vos, sobre el tema que elegís vos.**

Si no se indicó tema: listá los temas que tienen tarjetas y **frená**. No elijas por el
usuario, no arranques con "el que más falta hace". El sistema no decide qué estudiás.

**Nunca uses lenguaje de caducidad ni de deuda**: acá nada se vence, nada se acumula y
nadie lleva la cuenta de los días que pasaron.

## 1. Cargar solo las tarjetas

```bash
ls materias/activas/<materia>/cards/
```

Cargá `cards/<tema>.md`. **No abras ninguna página del wiki.** Las tarjetas se bastan solas:
el enlace a la página aparece únicamente cuando fallás una.

Una sesión de 15 tarjetas cuesta leer 1-3 archivos de `cards/`. Si estás abriendo páginas del
wiki fuera de un fallo, la sesión está mal armada.

## 2. Elegir las tarjetas de esta sesión

`--n` tarjetas (default 15), en este orden de prioridad:

1. Las que tienen `fallo` en su último `Visto`.
2. Las que nunca se vieron (`Visto` vacío).
3. Las marcadas `origen: examen`.
4. El resto: las menos recientes primero.

`--desde-errores` restringe la sesión al grupo 1. `--tipos` filtra por tipo de tarjeta.

Esto es prioridad **dentro de una sesión que vos pediste**, no una cola que se acumula sola.

## 3. Ordenar: intercalado solo entre confundibles

Alterná las tarjetas ligadas por `Confundible_con`: si `c-U3-001` y `c-U3-004` se confunden,
que no queden juntas ni lejísimos — que aparezcan intercaladas con otras del mismo grupo.

**Fuera de esos grupos, no intercales.** Mezclar temas no relacionados no aporta nada: el
efecto del intercalado depende de que los ítems compitan entre sí
(`global/metodo/evidencia.md`, nivel B).

## 4. La sesión, tarjeta por tarjeta

Para cada una, en este orden exacto:

1. Mostrá **solo la pregunta**.
2. El usuario responde.
3. **Pedí la confianza 1-5 ANTES de revelar la respuesta.** Después de ver la respuesta no
   mide nada: ya sabe si acertó.
4. Mostrá la respuesta con su cita.
5. El usuario se autocalifica: `ok` · `parcial` · `fallo`.

Ante `parcial` o `fallo`:

- Mostrá el enlace a la página del wiki de donde salió la tarjeta.
- **Volvé a preguntarla más tarde en la misma sesión**, después de al menos 3 tarjetas.
  Si vuelve a fallar, otra vez. Máximo 3 reapariciones por tarjeta: más allá de eso el
  problema no es la tarjeta, es que falta estudiar el tema.
- **No expliques.** El repaso es recuperación, no clase. Si querés la explicación,
  está en la página que te acabo de enlazar.

No adelantes la respuesta, no des pistas antes de la calificación, no seas complaciente:
una respuesta a medias es `parcial` y se dice qué faltó.

## 5. Al cerrar la sesión

1. **`cards/<tema>.md`** — anexá al `Visto` de cada tarjeta tocada: `<fecha>:ok|parcial|fallo`.
   El más reciente primero. Nunca escribas una fecha futura.
2. **`estado/historial.md`** — una línea:
   `| 2026-08-15 | U3 | repaso | 15 tarjetas · 9 ok / 4 parcial / 2 fallo |`
3. **`estado/dominio.md`** — actualizá el nivel del tema. Sube como máximo 1 punto por
   sesión; baja lo que haga falta.
4. **`estado/calibracion.md`** — confianza media declarada vs. acierto real del tema.
5. Commit: `repaso(<materia>): <tema> · <ok>/<total>`.

## Al terminar, decí exactamente

Resultado (ok/parcial/fallo), las 2-3 tarjetas que más te costaron con su enlace, y la brecha
de calibración si la hubo. **Sin sugerir cuándo volver.** Si querés saber qué hace rato que
no tocás, eso lo dice `/estado`.
