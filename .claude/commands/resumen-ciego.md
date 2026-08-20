---
description: Escribís el resumen de un tema con el wiki cerrado y el sistema lo corrige contra las fuentes
argument-hint: <tema> [--materia <slug>] [--corregir]
---

# /resumen-ciego $ARGUMENTS

Vos escribís el resumen de memoria; el sistema te dice qué faltó, qué está mal y qué te
inventaste. Produce un artefacto que te queda, igual que `/resumen`.

Tiene **dos invocaciones**: la primera abre el archivo, la segunda (`--corregir`) lo corrige.

## Fase 1 — abrir

1. Leé **solo** `wiki/mapa.md` para saber qué páginas cubren el tema. **No las abras**:
   si las leés ahora, la corrección posterior va a estar contaminada por lo que acabás de ver.
2. Creá `out/ciego-<tema>.md`:

```markdown
---
tema: U3                # unidad o eje, según el modo del programa
materia: teoria-computacion
escrito: <fecha en que lo termines>
paginas_a_contrastar: [teoremas/lema-bombeo, definiciones/lenguaje-regular]
---

# U3 · Lenguajes regulares — de memoria

<!-- Escribí acá todo lo que te acordás del tema, con el wiki cerrado.
     No importa el orden ni la prolijidad. Enunciados, procedimientos, ejemplos,
     lo que sea que te venga. Cuando termines: /resumen-ciego U3 --corregir -->
```

3. Decile al usuario: el archivo está listo, escribilo con el wiki cerrado, y cuando termine
   corra `/resumen-ciego <tema> --corregir`. **Frená ahí.** No sigas a la fase 2.

## Fase 2 — corregir (`--corregir`)

1. Leé `out/ciego-<tema>.md`.
2. Recién **ahora** abrí las páginas del wiki listadas en `paginas_a_contrastar`.
3. Devolvé exactamente estas tres listas, en este orden:

### Qué te faltó

Todo lo que está en el wiki y no en tu resumen, con su enlace. Ordenado por importancia: lo
que aparece en `patron.md` o tiene tarjetas primero.

```
- El caso |xy| ≤ p del lema de bombeo → [[teoremas/lema-bombeo]]
- La construcción del producto cartesiano → [[construcciones/afd-producto]]
```

### Qué pusiste mal

Lo que escribiste y contradice al wiki, **con la cita correcta al lado**. Sin suavizar:
si el enunciado que escribiste invierte los cuantificadores, eso se dice.

```
- Escribiste "para toda partición xyz"; es "existe una partición".
  Dice: "…puede escribirse s = xyz cumpliendo…" (sipser-cap1 p.77)
```

### Qué agregaste que no está en ninguna fuente

**La lista más informativa de las tres.** Lo que escribiste y no aparece en ninguna página
del wiki de esta materia. Suele ser una de tres cosas:

- Algo que sabés de otra materia y estás mezclando (chequealo contra `global/glosario.md`).
- Algo que la cátedra no da y estás trayendo de afuera: no está mal, pero no lo cites en el
  parcial como si fuera de la cátedra.
- Algo que inventaste sin darte cuenta. Esto es lo que hay que cazar.

Marcá cada ítem con cuál de las tres es, si podés distinguirlo. Si no está en el wiki pero
tampoco podés afirmar que sea falso, decilo así: **no confundas "no está en el wiki" con
"es incorrecto"** — el wiki puede tener huecos, y eso es un hallazgo para `/lint`.

## 4. Qué actualiza

- `estado/dominio.md`: si faltó más de la mitad de lo importante, bajá el dominio del tema.
  Si estaba casi todo, subilo como máximo 1 punto.
- `estado/historial.md`: `| <fecha> | <tema> | resumen-ciego | faltó N · mal M · sin fuente K |`
- Si algo de "lo que agregaste" resulta ser correcto y el wiki no lo tiene: anotalo en
  `wiki/dudas.md` como hueco a verificar contra la fuente.
- Commit: `ciego(<materia>): <tema> · N faltantes, M errores`.

## Al terminar, decí exactamente

Los números de las tres listas, el error más caro de los que cometiste, y que el archivo te
queda en `out/` como material de estudio. No sugieras cuándo repetirlo.
