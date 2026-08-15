---
description: Tablero compacto de una materia: cobertura, dominio, días al parcial y una recomendación
argument-hint: [materia]
---

# /estado $1

Tablero de una pantalla. Sin `$1`, mostrá una fila por materia activa y frená ahí.

**Lee solo archivos índice**: `wiki/programa.md`, `wiki/log.md`, `estado/dominio.md`,
`estado/errores.md`, `manifest.jsonl` y el `CLAUDE.md` de la materia.
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

## Formato de salida

```
TEORÍA DE LA COMPUTACIÓN · 2026-2C · parcial 2 en 11 días

Programa    ████████░░░░  5/8 unidades cubiertas · 1 parcial · 2 sin material
Dominio     ███████░░░░░  2.8 / 5   (7 temas evaluados de 8)
Wiki        34 páginas · 6 ingestas · última: hace 3 días
Rojo        U5 lenguajes libres de contexto (0) · U7 indecidibilidad (1)
Sin material U6 · U8

→ Hoy: /profesor U5 hueco
```

Reglas del tablero:
- Las barras son de 12 caracteres, proporcionales.
- `Rojo` lista **solo** los temas con dominio ≤2, con su valor.
- Si hay un `⚠️` sin resolver en `dudas.md`, agregá una línea `Dudas N abiertas`.
- Si `manifest.jsonl` está vacío: decí que la materia no tiene material y recomendá `/loop`.

## La recomendación

**Una sola línea, un solo comando ejecutable.** Prioridad, de mayor a menor:

1. Falta ≤7 días para un parcial y hay unidades `sin-material` → `/loop` (ingerir ya).
2. Hay temas con dominio ≤2 en unidades que entran en el próximo parcial → `/profesor <U> hueco`.
3. Pasaron ≥5 ingestas desde el último `/lint` → `/lint $1`.
4. Falta ≤3 días para el parcial → `/machete <unidades del parcial>`.
5. Todo verde → `/profesor <la unidad más vieja> socratico`.

No des una lista de recomendaciones. Una.

## Qué actualiza

Nada. `/estado` es de solo lectura y no commitea.
