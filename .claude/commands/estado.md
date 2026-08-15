---
description: Tablero compacto de una materia: cobertura, dominio, días al parcial y una recomendación
argument-hint: [materia]
---

# /estado $1

Tablero de una pantalla. Sin `$1`, mostrá una fila por materia activa y frená ahí.

**Lee solo archivos índice**: `wiki/programa.md`, `wiki/log.md`, `estado/dominio.md`,
`estado/errores.md`, `estado/calibracion.md`, `estado/historial.md`, `manifest.jsonl`, el
frontmatter de `cards/*.md` y el `CLAUDE.md` de la materia.
**Nunca abre páginas de contenido.** Este comando tiene que ser barato: se corre a diario.

`M` = `materias/activas/$1`.

## Datos a juntar

```bash
grep -c "^## U" $M/wiki/programa.md                      # unidades totales
grep -c "cobertura: cubierto" $M/wiki/programa.md        # cubiertas
grep -c "cobertura: parcial" $M/wiki/programa.md         # parciales
grep -c "cobertura: sin-material" $M/wiki/programa.md    # sin material
wc -l < $M/manifest.jsonl                                # ingestas
tail -1 $M/wiki/log.md                                   # última actividad
find $M/wiki -name '*.md' | wc -l                        # páginas
```

Dominio promedio y temas en rojo (`≤2`) salen de `estado/dominio.md`.
Los días al parcial salen de las fechas del `CLAUDE.md` de la materia contra la fecha de hoy.

Para la capa de estudio:

```bash
grep -c "^## c-" $M/cards/*.md 2>/dev/null                 # tarjetas totales
grep -c "^\*\*Visto:\*\*$" $M/cards/*.md 2>/dev/null      # nunca vistas (Visto vacío)
grep -h "^\*\*Visto:\*\*" $M/cards/*.md | grep -c ":fallo" # último intento fallido
```

La brecha de calibración sale de `estado/calibracion.md`. El tiempo sin tocar cada tema sale
de la fecha más reciente en `historial.md` y en el `Visto` de las tarjetas del tema.

Si existe `wiki/examenes/patron.md`, agregá una línea de **cobertura ponderada**: qué
porcentaje del puntaje histórico del examen está cubierto por unidades con material, en vez
de contar unidades a secas. Tener 5 de 8 unidades cubiertas no dice nada si las 3 que faltan
valen el 60% del parcial.

```
Cobertura     5/8 unidades · pero solo 55% del puntaje histórico (falta U3, vale 25%)
```

## Formato de salida

```
TEORÍA DE LA COMPUTACIÓN · 2026-2C · parcial 2 en 11 días

Programa      ████████░░░░  5/8 unidades cubiertas · 1 parcial · 2 sin material
Dominio       ███████░░░░░  2.8 / 5   (7 temas evaluados de 8)
Wiki          34 páginas · 6 ingestas · última: hace 3 días
Tarjetas      142 · 38 nunca vistas · 17 con último intento fallido
Calibración   brecha +1.4 (sobreconfianza) · peor tema: Reducciones (conf 4.2 / acierto 41%)
Rojo          U5 lenguajes libres de contexto (0) · U7 indecidibilidad (1)
Sin material  U6 · U8
Sin tocar     Reducciones hace 9 días · Autómatas de pila hace 14 días

→ Sugerencia: /repasar reducciones --desde-errores   o   /resumen reducciones --perfil ciego
```

Reglas del tablero:
- Las barras son de 12 caracteres, proporcionales.
- `Rojo` lista **solo** los temas con dominio ≤2, con su valor.
- Si hay un `⚠️` sin resolver en `dudas.md`, agregá una línea `Dudas N abiertas`.
- Si `manifest.jsonl` está vacío: decí que la materia no tiene material y recomendá `/loop`.
- **`Sin tocar` es información, no reproche.** Sin emojis de alarma, sin "hace 14 días ya!",
  sin contar días perdidos ni sesiones que no hiciste. Solo el dato.
- Nunca uses las palabras *vencido*, *atrasado*, *pendiente*, *deuda* ni *racha*. No hay nada
  que se venza en este sistema.
- `Calibración` se omite si no hay ninguna medición todavía. No inventes una brecha de 0.

## La sugerencia

**Una sola línea.** Prioridad, de mayor a menor:

1. Falta ≤7 días para un parcial y hay unidades `sin-material` → `/loop` (ingerir ya).
2. Sobreconfianza detectada en una unidad que entra en el próximo parcial → ese tema.
3. Hay temas con dominio ≤2 en unidades del próximo parcial → ese tema.
4. Pasaron ≥5 ingestas desde el último `/lint` → `/lint $1`.
5. Falta ≤3 días para el parcial → `/machete <unidades del parcial>`.
6. Todo verde → el tema que hace más tiempo no tocás.

Elegido el tema, **ofrecé las dos vías** y dejá que el usuario elija:

```
→ Sugerencia: /repasar <tema> --desde-errores   o   /resumen <tema> --perfil ciego
```

Recuperar y reelaborar cuentan igual. No empujes hacia una: el usuario sabe cuál le sirve
hoy. Y es una sugerencia, no una asignación: la palabra es "sugerencia", no "hoy te toca".

## Qué actualiza

Nada. `/estado` es de solo lectura y no commitea.
