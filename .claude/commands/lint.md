---
description: Audita el wiki de una materia contra el programa y las reglas de fidelidad. Reporta, no corrige.
argument-hint: [materia]
---

# /lint $1

Auditoría. **Reporta; no corrige nada sin confirmación explícita.**
Corrélo cada 5 ingestas, y cuando quieras saber en qué estado real está el wiki.

Trabajá con `grep`/`ls` sobre el árbol. **No abras las páginas** salvo para confirmar un
hallazgo concreto, y en ese caso solo las señaladas.

`M` = `materias/activas/$1`.

## Chequeos

### 1. Unidades sin material
```bash
grep -A1 "^## U" $M/wiki/programa.md | grep -B1 "cobertura: sin-material"
```
Reportá cada unidad. **La severidad no depende de ninguna fecha**: una unidad sin material
es igual de crítica en marzo que en diciembre.

### 2. Páginas huérfanas (sin enlaces entrantes)
Listá los slugs y buscá quién los enlaza:
```bash
for f in $(find $M/wiki -name '*.md' -not -name 'index.md' -not -name 'mapa.md'); do
  s=$(basename $f .md)
  n=$(grep -rl "\[\[[a-z]*/$s\]\]" $M/wiki | grep -v "$f" | wc -l)
  [ "$n" -eq 0 ] && echo "HUÉRFANA: $f"
done
```

### 3. Enlaces rotos
```bash
grep -roh "\[\[[^]]*\]\]" $M/wiki | sort -u
```
Para cada `[[carpeta/slug]]`, verificá que exista `$M/wiki/<carpeta>/<slug>.md`.
Para los `[[materia/carpeta/slug]]`, verificá contra esa otra materia.

### 4. Páginas sin ninguna fuente en su procedencia
```bash
EXCL='index|mapa|log|dudas|programa|patron'   # índices y derivados: no transcriben fuentes
grep -rL "^## Procedencia" $M/wiki --include='*.md' | grep -vE "$EXCL"
grep -rLE "^- \*\*.+\*\* — [a-z0-9-]+ p\." $M/wiki --include='*.md' | grep -vE "$EXCL"
```
**Este es el chequeo más importante**: una página cuya procedencia no nombra ninguna fuente
no tiene una sola afirmación rastreable. Riesgo de alucinación horneada.

### 5. Dudas sin entrada en `dudas.md`
```bash
grep -rl "· duda" $M/wiki --include='*.md'
```
Cada página cuya procedencia menciona una duda tiene que estar nombrada en
`$M/wiki/dudas.md`. Si no está, la contradicción se está perdiendo.

### 6. Páginas de más de 150 líneas
```bash
find $M/wiki -name '*.md' -exec wc -l {} + | awk '$1 > 150 {print}'
```
Candidatas a partir: cargarlas cuesta caro y se leen mal.

### 7. Tipos muertos
Contá instancias por tipo:
```bash
grep -rh "^tipo:" $M/wiki --include='*.md' | sort | uniq -c | sort -rn
wc -l < $M/manifest.jsonl
```
Si un tipo activo tiene **0 instancias tras 10 ingestas**, proponé sacarlo con `/reperfilar`.

### 8. Páginas desactualizadas respecto de sus fuentes
Comparé el `actualizado:` de cada página contra la `fecha` de la última línea de
`manifest.jsonl` que menciona alguna de sus `fuentes:`. Si la ingesta es posterior, la página
quedó vieja: se ingirió material nuevo de esa fuente y no se revisó.

### 9. Frontmatter inválido
```bash
head -9 $(find $M/wiki -name '*.md') | grep -c "^id:\|^tipo:\|^tema:\|^estado:"
```
Toda página necesita `id`, `tipo`, `tema`, `fuentes`, `estado`, `dominio`, `actualizado`.
El `id` tiene que empezar con `$1/` (namespace correcto) y el `tipo` tiene que estar entre
los tipos activos del `CLAUDE.md` de la materia.

### 10. Consignas de examen sin cubrir — **prioridad máxima**

```bash
grep -l "Estado_wiki: HUECO" $M/wiki/examenes/*.md 2>/dev/null
grep -c "Estado_wiki: HUECO" $M/wiki/examenes/*.md 2>/dev/null
```

Cada `HUECO` es una consigna que **ya tomaron** y que el wiki no puede responder. No es un
agujero hipotético como una unidad sin cobertura: es uno comprobado. Van primero en el
reporte, antes que cualquier otro hallazgo.

### 11. Reserva ciega

```bash
ls $M/raw/examenes/ 2>/dev/null | grep -v '^_' | wc -l
ls $M/raw/examenes/_reservado/ 2>/dev/null | wc -l
```

Si hay **2 o más exámenes procesados y la reserva está vacía**, reportalo: el próximo
simulacro no va a medir nada porque ya viste todas las consignas. Sugerí reservar el más
reciente. Es un problema de medición, no de calendario: no lo ates a ninguna fecha.

### 12. Reglas de verificación por tipo
Para cada tipo activo, aplicá su regla de `plantillas/catalogo.md`. Las más rendidoras:
- `comparativa` sin tabla markdown.
- `practica` con `## Cuándo NO aplica` vacía.
- `teorema` con `## Demostración` vacía y `estado` distinto de `sin-demo`.
- `numeros` con valores sin cita.
- `debate` con ambas posturas citando la misma fuente.

### 13. Páginas escritas como fichas

Dos síntomas de que la regla de redacción no se aplicó (`global/metodo/redaccion.md`).

**Párrafos que son solo una etiqueta en negrita y una cita**, sin una palabra propia alrededor:

```bash
grep -rnE '^\*\*[^*]+\.\*\*[[:space:]]*["«`]' $M/wiki --include='*.md'
```

El `grep` es el primer filtro y **sobre-reporta**: hay que descartar a mano dos casos que no
son falta. Primero, cuando la etiqueta es la numeración de la propia fuente (`**Teorema 4.**`,
`**Definición 12.**`, `**Proposición 7.**`, `**Observación 2.**`, `**Ejercicio 1.**`,
`**Ejemplo 3.2.**`): citar un resultado por su número es correcto y además útil. Segundo,
cuando después de cerrar la cita sigue prosa propia en el mismo párrafo — ahí la cita no está
flotando. Solo queda como hallazgo lo que es etiqueta inventada + cita + nada.

Páginas donde más de la mitad de los párrafos de cuerpo son de ≤12 palabras:

```bash
EXCL='index|mapa|log|dudas|programa|patron|examenes/'
for f in $(find $M/wiki -name '*.md' | grep -vE "$EXCL"); do
  awk -v F="$f" '
    /^```/ {inc=!inc; next} inc {next}
    /^## Procedencia/ {done=1} done {next}
    /^[[:space:]]*$/ {if (b!="") {n++; if (split(b,w," ")<=12) frag++}; b=""; next}
    /^[#|>]|^[[:space:]]*[-*+][[:space:]]|^[[:space:]]*[0-9]+\./ {b=""; next}
    {b = b " " $0}
    END {if (b!="") {n++; if (split(b,w," ")<=12) frag++}
         if (n>0 && frag*2>n) printf "  %s  %d/%d bloques cortos\n", F, frag, n}' "$f"
done
```

Es una señal, no una falta: un `numeros` o una `comparativa` pueden dar positivo con razón.
Severidad 🟡, y la recomendación es reescribir la página, nunca borrar contenido.

## Salida

Una tabla, ordenada por severidad:

```
🔴 CRÍTICO  2 consignas ya tomadas sin cubrir     → e2024p1-q5 (U6), e2023p2-q1 (U7)
🔴 CRÍTICO  4 páginas sin ninguna fuente          → conceptos/…, teoremas/…
🔴 CRÍTICO  2 unidades sin material                → U5, U8
🟡 REVISAR  3 enlaces rotos                       → [[teoremas/rice]]
🟡 REVISAR  2 páginas >150 líneas
🟡 REVISAR  5 páginas escritas como fichas         → definiciones/conjunto, …
⚪ MENOR    tipo `debate` sin instancias (12 ingestas)
```

Cerrá con **una sola** acción recomendada, la de mayor impacto.

Si el usuario pide corregir, hacelo en un **commit aislado**:
`lint(<materia>): <qué se corrigió>`.
