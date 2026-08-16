---
description: Genera tarjetas de recuperación de un tema, solo desde contenido verificado
argument-hint: <tema> [--tipos concepto,aplicacion,discriminacion,cloze] [--max N] [--materia <slug>]
---

# /cards $ARGUMENTS

Genera el material del que vas a tirar cuando quieras repasar. **No es una cola**: las
tarjetas quedan ahí, no vencen, no te reclaman nada. `/repasar` las usa cuando vos lo pedís.

## 1. De dónde lee

1. `materias/activas/<materia>/CLAUDE.md` → tipos activos y notación de la cátedra.
2. `wiki/mapa.md` → **filtrá acá** las páginas del tema.
3. Solo esas páginas, por ruta. Nunca el directorio entero.
4. `cards/<tema>.md` si ya existe, para no duplicar ni pisar el historial.

## 2. Regla no negociable: solo desde secciones con fuente

**Leé primero el bloque `## Procedencia` de la página.** Cada tarjeta sale de una sección
cuya procedencia nombra una fuente, y la tarjeta lleva esa cita.

- Secciones marcadas `sin cita: comentario del sistema`: **nunca**. Memorizar una inferencia
  del sistema es el peor modo de falla que tiene todo el repo: te aprenderías una alucinación
  con confianza.
- Secciones con `duda:`: tampoco. Están en disputa; primero se resuelven en `dudas.md`.
- Secciones con fuente que dicen `incluye comentario del sistema`: se pueden usar, pero la
  tarjeta tiene que salir de lo que respalda la fuente, no del comentario.
- Si una página del tema no tiene ninguna sección con fuente, saltala y **reportalo al final**:
  es un hallazgo de `/lint`, no un problema de las tarjetas.

## 3. Los cuatro tipos

| Tipo | Qué pregunta | De qué páginas sale |
|---|---|---|
| `concepto` | definición o enunciado, recuperación literal | `definicion`, `teorema`, `numeros` |
| `aplicacion` | usar el concepto en un caso concreto | `construccion`, `reduccion`, `caso`, consignas de `wiki/examenes/` |
| `discriminacion` | distinguir dos cosas parecidas: "¿por qué esto NO es X sino Y?" | `comparativa` y todo par ligado por `Confundible_con` |
| `cloze` | huecos en un enunciado formal o un procedimiento | `teorema`, `protocolo`, `mecanismo` |

No hay un quinto tipo. Si algo no entra en estos cuatro, no es una tarjeta.

## 4. Formato

Escribí en `materias/activas/<materia>/cards/<tema>.md`:

```markdown
---
tema: U3
generado: 2026-08-15
fuente_paginas: [teoremas/bombeo-regulares, definiciones/lenguaje-regular]
---

## c-U3-001 · concepto
**P:** Enunciá el lema de bombeo para lenguajes regulares.
**R:** Si L es regular, existe p≥1 tal que toda w∈L con |w|≥p se escribe w=xyz con
(1) |y|>0, (2) |xy|≤p, (3) ∀i≥0: xy^i z ∈ L.
**Fuente:** sipser-cap1 p.78
**Bloom:** recordar
**Confundible_con:** [c-U3-004]
**Visto:**
```

- El id es `c-<tema>-<NNN>`, correlativo y estable. **Nunca se reusa** un id liberado.
- `Visto` es **historial, no agenda**: lo escribe `/repasar` como `2026-08-15:ok`.
  Arranca vacío. **No existe ningún campo de fecha futura en todo el sistema.**
- `Bloom` etiqueta el nivel de la pregunta: `recordar | comprender | aplicar | analizar |
  evaluar | crear`. Es un framework de generación, no un hallazgo (`global/metodo/evidencia.md`).

## 4b. Tarjetas desde consignas reales

Si existe `wiki/examenes/<id>.md`, generá tarjetas `aplicacion` **desde las consignas ya
tomadas**, con el campo extra `**Origen:** examen`:

```markdown
## c-U3-012 · aplicacion
**P:** Probá que {a^n b^n} no es regular. (consigna real, parcial 2024-1, 20 pts)
**R:** Aplicar el lema de bombeo: dado p, tomar s = a^p b^p …
**Fuente:** parcial-2024-1 p.2
**Bloom:** aplicar
**Origen:** examen
```

- La consigna se copia **literal** del archivo de examen, no se reformula.
- Si la resolución del examen está marcada `inferida`, la tarjeta lleva
  `**Resolución:** inferida` y **no se usa para evaluar**: sirve para practicar el
  procedimiento, no para verificar.
- `/repasar` les da prioridad alta: son literalmente lo que te van a tomar.
- **Nunca desde el examen reservado.** Ese no se abrió.

## 5. `Confundible_con` — lo que hace útil el intercalado

Después de generar, cruzá las tarjetas del tema **y de los temas hermanos** y ligá las que
se confunden entre sí: mismo nombre distinto objeto, hipótesis que se parecen, dos
construcciones con el mismo diagrama, conceptos que `global/glosario.md` marca como
colisionados.

Sin este campo, intercalar es ruido: el efecto del intercalado depende de que los ítems sean
confundibles entre sí, no de mezclar por mezclar.

La relación es **simétrica**: si ligás `c-U3-001` a `c-U3-004`, actualizá también la otra.

## 6. Topes y calidad

- **Máximo 12 tarjetas por página fuente.** Si el tema da para más, avisá: es señal de que
  la página debería partirse, no de generar 30 tarjetas.
- `--max N` limita el total del tema.

Rechazá la tarjeta si:

- Se responde con sí/no, o se adivina por eliminación.
- La respuesta está contenida en el enunciado de la pregunta.
- La respuesta tiene más de ~4 elementos → **partila en varias**. Una tarjeta = un ítem
  recuperable.
- La sección de la que sale no tiene fuente en su procedencia → no se crea. Sin excepción.

**La regla de redacción del repo no rige acá.** Las páginas se escriben en prosa; una tarjeta
con un párrafo de respuesta no se recupera. La respuesta va corta y recuperable.

## 7. Qué actualiza

- Escribe `cards/<tema>.md`. Si el archivo ya existía: **agregá tarjetas nuevas y conservá
  el `Visto` de las existentes.** Nunca regeneres el archivo desde cero.
- Anexa a `wiki/log.md`: `<fecha> · cards <tema> · N nuevas, M existentes`.
- Commit propio: `cards(<materia>): <tema> · N tarjetas`.
- No toca `estado/`: generar tarjetas no es estudiar, y no mueve el dominio.

## Al terminar, decí exactamente

Cuántas tarjetas por tipo, cuántos pares `Confundible_con` quedaron ligados, qué páginas se
saltearon por no tener ninguna sección con fuente, y que podés repasarlas cuando quieras con
`/repasar <tema>` — sin sugerir cuándo.
