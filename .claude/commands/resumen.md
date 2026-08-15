---
description: Genera un resumen de un tema (o de todo) rastreando el wiki por mapa.md, y lo compila a PDF
argument-hint: <tema|todo> [--perfil breve|completo|guia-parcial] [--materia <slug>]
---

# /resumen $ARGUMENTS

`PY` = `.venv/bin/python` si existe, si no `python3`. Perfil por defecto: `completo`.

## 1. Ruteo (de dónde lee)

1. `materias/activas/<materia>/CLAUDE.md` → tipos activos, notación de la cátedra.
2. `materias/activas/<materia>/wiki/mapa.md` → **acá se decide qué abrir**.
3. `materias/activas/<materia>/wiki/programa.md` → solo la unidad pedida, para saber qué
   debería estar cubierto.

Filtrá en `mapa.md` las páginas cuya unidad o tema coincida con `<tema>`. Recién entonces
abrí **esas** páginas, por ruta. Nunca leas el directorio entero.

Si el filtro no devuelve nada: decí qué unidades sí tienen material (según `programa.md`) y
frená.

## 2. Alcance

- `<tema>` = una unidad (`U3`), un tema del mapa, o `todo`.
- Con `todo` y más de ~40 páginas: generá **por unidad** y concatená al final. No cargues
  las 40 juntas.
- Si alguna unidad del alcance tiene `cobertura: sin-material`, el resumen la incluye igual
  con la línea `⚠️ Sin material ingerido para esta unidad.` No la omitas en silencio.

## 3. Perfiles

| Perfil | Largo | Qué entra |
|---|---|---|
| `breve` | 1-2 páginas | enunciados y definiciones nada más, sin demostraciones ni ejemplos |
| `completo` | sin tope | todo el tema, con diagramas Mermaid y ejemplos resueltos |
| `guia-parcial` | 3-6 páginas | ordenado por probabilidad de que lo tomen |
| `esqueleto` | igual que `completo` | la estructura, con el contenido vacío para que lo completes vos |
| `anotado` | igual que `completo` | el resumen entero + preguntas al margen |

Para `guia-parcial`, la probabilidad sale de los parciales viejos ingeridos: buscá en
`manifest.jsonl` las fuentes cuyo `fuente_id` empiece con `parcial-` o `final-`, y ordená los
temas por cuántas veces aparecen. Encabezá cada sección con `tomado N veces ✅ [parcial-… p.N]`.
Si no hay parciales ingeridos, decilo en la primera línea del resumen y ordená por unidad.
Si existe `wiki/examenes/patron.md`, el orden sale de ahí: es la misma cuenta, ya hecha.

### `esqueleto`

Escribí el resumen `completo` y después **vaciá el contenido**, dejando en pie:

- Todos los títulos y subtítulos, en su orden.
- Los **nombres** de teoremas, definiciones y construcciones, sin su enunciado.
- Los encabezados de cada tabla, con las filas vacías.
- Las etiquetas de las secciones obligatorias del tipo (`Hipótesis`, `Contraejemplo`,
  `Cuándo NO aplica`), sin su contenido.
- Los bloques de diagrama como `<!-- diagrama: qué relaciona -->`, sin el Mermaid.

Debajo de cada hueco, dejá una línea `> ` para escribir. El archivo sale a
`out/resumen-<tema>-esqueleto.md` y **se completa a mano, con el wiki cerrado**.

Cuando el usuario lo termine y lo pida, corregilo contra las páginas del wiki con el mismo
formato de tres listas de `/resumen-ciego`.

### `anotado`

El resumen `completo`, con preguntas intercaladas después de cada bloque, en cita:

```markdown
✅ [sipser-cap1 p.77] Si A es regular, existe p tal que toda s ∈ A con |s| ≥ p…

> **¿Por qué vale?** ¿Qué propiedad del autómata obliga a que exista ese p?
> **¿Y si sacamos una hipótesis?** ¿Qué pasa con el enunciado si |s| < p?
```

Reglas de las preguntas:

- **Sobre el porqué y las consecuencias**, no sobre el dato. "¿Cómo se llama el lema?" no
  sirve; "¿por qué la partición la elige el adversario?" sí.
- Una o dos por bloque, no más. Un resumen con más preguntas que contenido no se lee.
- **No las respondas.** Si el usuario quiere la respuesta, pregunta.
- Las preguntas son tuyas, no de la fuente: van en cita, nunca marcadas `✅`.

## 4. Reglas de escritura

- **Las marcas se preservan tal cual**: `✅ [fuente p.N]`, `🧠`, `⚠️`. Un resumen sin
  trazabilidad no sirve para estudiar: si no podés verificarlo, no lo estudiás.
- Los enunciados literales se copian **de la página del wiki**, que ya los transcribió de la
  fuente. No los reescribas: cada reescritura es una oportunidad de introducir un error.
- Todo lo que agregues para hilar el resumen va marcado `🧠`.
- Los `⚠️` se listan juntos al final, bajo `## Dudas abiertas`, con enlace a `dudas.md`.
- Cerrá con `## Origen`: lista de las páginas del wiki usadas, para poder volver.

## 5. Salida

```bash
# escribí el markdown primero
materias/activas/<materia>/out/resumen-<tema>-<perfil>.md

$PY scripts/build_pdf.py materias/activas/<materia>/out/resumen-<tema>-<perfil>.md \
  --out materias/activas/<materia>/out/ --perfil resumen
```

Si `build_pdf.py` avisa que no hay motor de PDF: **no es un fallo**. El `.md` ya está escrito;
informalo y seguí.

## 6. Qué actualiza

- Escribe: `out/resumen-<tema>-<perfil>.md` (+ `.pdf` si compiló).
- Anexa a `wiki/log.md`: `<fecha> · resumen <tema> <perfil> · N páginas del wiki`.
- **No toca** `estado/`: el dominio lo mueve `/profesor`, no leer un resumen.
- `out/` está en `.gitignore`: no commitea nada salvo la línea del log.

## Al terminar, decí exactamente

Ruta del `.md` y del `.pdf`, cuántas páginas del wiki entraron, cuántas unidades del alcance
quedaron sin material, y cuántos `⚠️` arrastra.
