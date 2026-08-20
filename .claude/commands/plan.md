---
description: Lista ordenada de por dónde seguir en una materia, con el porqué de cada tema. No es una agenda.
argument-hint: <materia> [--tope N]
---

# /plan $ARGUMENTS

Una **lista ordenada de por dónde seguir**, con el motivo de cada tema al lado. No es un
motor ni un calendario: no hay días, no hay bloques, no hay fechas, nada se marca cumplido ni
incumplido, nada acumula deuda, nada te reclama. Si no seguís el orden no pasa absolutamente
nada.

Volver a correr `/plan` **regenera desde cero** con el estado actual. No hay plan anterior que
respetar ni arrastre de lo que no se hizo.

Con `--tope N`, cortá la lista en N temas. Sin `--tope`, entran todos los que tengan algo que
justifique estar.

## 1. De dónde lee

Solo archivos índice y de estado. **Ninguna página de contenido, ninguna fecha.**

```bash
M=materias/activas/<materia>
head -2 $M/wiki/programa.md | grep "^modo:"
grep "^## \|cobertura:" $M/wiki/programa.md
cat $M/estado/dominio.md $M/estado/calibracion.md
cat $M/wiki/examenes/patron.md 2>/dev/null      # si existe
grep -h "^\*\*Visto:\*\*" $M/cards/*.md 2>/dev/null | tail -50
```

## 2. Prioridad

Se ordena por **riesgo de no saber algo**, en este orden:

1. **Sobreconfianza detectada** en `calibracion.md` (confianza ≥4, acierto <60%). Es el
   riesgo más caro y el único que no se ve solo: creés que el tema está y no está.
2. **Temas con `cobertura: sin-material`** (solo en `modo: temario`). Sin material no hay nada
   que estudiar: ese ítem es `/vaciar-cola`, no `/repasar`.
3. **Puntaje en riesgo**, si hay `patron.md`: `(% que vale el tema) × (1 − dominio/5)`.
   Un tema que vale 30% con dominio 2 (riesgo 18) va antes que uno que vale 5% con dominio 1
   (riesgo 4). El porcentaje sale de la tabla "Puntaje por unidad" de `patron.md`, promediado
   sobre todos los exámenes procesados. Esto es evidencia de **cómo evalúa la cátedra**, no de
   cuándo: se usa igual haya o no un parcial a la vista.
4. **Dominio bajo** en `dominio.md`, de menor a mayor.
5. **Tiempo sin tocar el tema**, según el `Visto` de sus tarjetas y `historial.md`.

Un tema entra a la lista si algún criterio lo justifica. **Un tema que no dispara ninguno no
entra**: una lista que nombra todo no ordena nada.

## 3. Escribir `estado/plan.md`

```markdown
# Por dónde seguir

Generado 2026-08-20. Es una lista, no una agenda: si no la seguís no pasa nada.
Volvé a correr `/plan` cuando quieras y se regenera con el estado de ese momento.

1. **U3 · Reducciones** — sobreconfianza (conf 4.2 / acierto 41%)
   - `/repasar reducciones --desde-errores`   ← recuperación
   - `/resumen reducciones --perfil ciego`    ← reelaboración
2. **U5 · Autómatas de pila** — dominio 1, y vale 20% del puntaje histórico
   - `/repasar autómatas-pila`   o   `/resumen autómatas-pila --perfil anotado`
3. **U6 · Indecidibilidad** — sin material ingerido
   - `/vaciar-cola`
```

**Cada ítem ofrece las dos vías y vos elegís**: recuperar (`/repasar`, `/profesor`) o leer y
reelaborar (`/resumen` con cualquiera de sus perfiles). Ninguna es la correcta; las dos
cuentan igual.

Cerrá el archivo con los temas que quedaron afuera por `--tope`, si los hubo.

## 4. Qué NO hace

- No reparte por días ni por bloques de tiempo.
- No menciona ninguna fecha de parcial, final ni entrega.
- No marca nada como cumplido ni incumplido.
- No arrastra lo que no hiciste.
- No cuenta días seguidos ni interrumpidos.
- No te avisa nada: `plan.md` es un archivo que abrís cuando querés.

## 5. Qué actualiza

- Escribe `estado/plan.md`, pisando el anterior.
- Commit: `plan(<materia>): <N> temas priorizados`.
- No toca `dominio.md`, `calibracion.md` ni las tarjetas.

## Al terminar, decí exactamente

Cuántos temas entraron, cuál quedó primero y por qué, y con qué comando arrancarlo. Sin
insistir en que sigas el orden.
