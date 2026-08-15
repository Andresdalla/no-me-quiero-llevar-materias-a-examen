---
description: Propone un reparto de temas hasta una fecha. Es un documento, no una agenda con obligaciones.
argument-hint: <materia> [--hasta AAAA-MM-DD] [--horas-dia 2]
---

# /plan $ARGUMENTS

Una **propuesta de reparto**. No es un motor: nada se marca cumplido ni incumplido, nada
acumula deuda, nada te reclama. Si no lo seguís no pasa absolutamente nada.

Volver a correr `/plan` **regenera desde cero** con el estado actual. No hay plan anterior que
respetar ni arrastre de lo que no se hizo.

Sin `--hasta`, usá la fecha del próximo parcial del `CLAUDE.md` de la materia.

## 1. De dónde lee

Solo archivos índice y de estado. **Ninguna página de contenido.**

```bash
M=materias/activas/<materia>
grep "^## U\|cobertura:" $M/wiki/programa.md
cat $M/estado/dominio.md $M/estado/calibracion.md
cat $M/wiki/examenes/patron.md 2>/dev/null      # si existe
grep -h "^\*\*Visto:\*\*" $M/cards/*.md 2>/dev/null | tail -50
```

## 2. Calcular lo que hay

- **Días disponibles**: de hoy a `--hasta`, inclusive.
- **Bloques por día**: `--horas-dia` (default 2), un tema por bloque de ~1 hora.
- **Temas a cubrir**: las unidades del programa que entran en esa evaluación.

## 3. Si no alcanza, decilo

**Antes de escribir el plan**, compará temas contra bloques disponibles.

Si no entran, **no comprimas ni inventes viabilidad**. Decí exactamente esto:

```
No alcanza. 8 unidades · 3 días · 2 bloques por día = 6 bloques para 8 temas.

Entran (por prioridad):    U3, U5, U1, U7, U2, U6
Quedan afuera:             U4, U8

U4 vale 15% según patron.md y tenés dominio 1 — es el que más duele dejar.
Opciones: sumar bloques por día, correr la fecha, o aceptar el recorte.
```

Un calendario que finge que entra todo es peor que no tener plan: te hace llegar al parcial
creyendo que estabas cubierto.

## 4. Prioridad

En este orden:

1. **Sobreconfianza detectada** en `calibracion.md` (confianza ≥4, acierto <60%). Es el
   riesgo más caro: vas a entrar tranquilo a un tema que no está.
2. **Unidades con `cobertura: sin-material`** que entran en la evaluación. Sin material no hay
   nada que estudiar: ese bloque es `/loop`, no `/repasar`.
3. **Puntaje en riesgo**, si hay `patron.md`: `(% que vale la unidad) × (1 − dominio/5)`.
   Un tema que vale 30% con dominio 2 (riesgo 18) va antes que uno que vale 5% con dominio 1
   (riesgo 4). El porcentaje sale de la tabla "Puntaje por unidad" de `patron.md`, promediado
   sobre todos los exámenes procesados.
4. **Tiempo sin tocar el tema**, según el `Visto` de sus tarjetas y `historial.md`.

Distribuí **sin acumular**: los temas de mayor prioridad primero y repartidos, no todos el
último día.

## 5. Escribir `estado/plan.md`

```markdown
# Plan hasta 2026-09-20 (parcial 1)

Generado 2026-08-15. Es una propuesta: si no la seguís no pasa nada.
Volvé a correr `/plan` cuando quieras y se regenera con el estado de ese momento.

## Lunes 18/8
- **U3 · Reducciones** — sobreconfianza (conf 4.2 / acierto 41%)
  - `/repasar reducciones --desde-errores`   ← recuperación
  - `/resumen reducciones --perfil ciego`    ← reelaboración
- **U5 · Autómatas de pila** — sin tocar hace 14 días
  - `/repasar autómatas-pila`   o   `/resumen autómatas-pila --perfil anotado`
```

**Cada día ofrece las dos vías y vos elegís**: recuperar (`/repasar`, `/profesor`) o
leer y reelaborar (`/resumen` con cualquiera de sus perfiles). Ninguna es la correcta;
las dos cuentan igual.

Cerrá el archivo con los temas que quedaron afuera, si los hay, y por qué.

## 6. Qué NO hace

- No marca días como cumplidos ni incumplidos.
- No arrastra lo que no hiciste al día siguiente.
- No cuenta días seguidos ni interrumpidos.
- No te avisa nada: `plan.md` es un archivo que abrís cuando querés.

## 7. Qué actualiza

- Escribe `estado/plan.md`, pisando el anterior.
- Commit: `plan(<materia>): hasta <fecha> · <N> temas en <M> bloques`.
- No toca `dominio.md`, `calibracion.md` ni las tarjetas.

## Al terminar, decí exactamente

Cuántos temas entraron en cuántos bloques, cuáles quedaron afuera y por qué, y el tema con
el que conviene empezar. Sin insistir en que lo sigas.
