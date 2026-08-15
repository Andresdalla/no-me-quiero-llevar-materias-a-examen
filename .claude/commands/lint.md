---
description: Audita el wiki de una materia contra el programa y las reglas de fidelidad. Reporta, no corrige.
argument-hint: [materia]
---

# /lint $1

Auditoría. **Reporta; no corrige nada sin confirmación explícita.**
Corrélo antes de cada parcial y cada 5 ingestas.

Trabajá con `grep`/`ls` sobre el árbol. **No abras las páginas** salvo para confirmar un
hallazgo concreto, y en ese caso solo las señaladas.

`M` = `materias/activas/$1`.

## Chequeos

### 1. Unidades sin material
```bash
grep -A1 "^## U" $M/wiki/programa.md | grep -B1 "cobertura: sin-material"
```
Reportá cada unidad y, si hay fecha de parcial cerca, marcala 🔴.

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

### 4. Páginas sin ninguna marca `✅`
```bash
grep -rL "✅" $M/wiki --include='*.md'
```
**Este es el chequeo más importante**: una página sin ✅ no tiene ni una afirmación
rastreable a una fuente. Riesgo de alucinación horneada.

### 5. `⚠️` sin entrada en `dudas.md`
```bash
grep -rl "⚠️" $M/wiki --include='*.md'
```
Cada página con `⚠️` tiene que estar nombrada en `$M/wiki/dudas.md`. Si no está, la
contradicción se está perdiendo.

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
reciente.

### 12. Reglas de verificación por tipo
Para cada tipo activo, aplicá su regla de `plantillas/catalogo.md`. Las más rendidoras:
- `comparativa` sin tabla markdown.
- `practica` con `## Cuándo NO aplica` vacía.
- `teorema` con `## Demostración` vacía y `estado` distinto de `sin-demo`.
- `numeros` con valores sin cita.
- `debate` con ambas posturas citando la misma fuente.

## Salida

Una tabla, ordenada por severidad:

```
🔴 CRÍTICO  2 consignas ya tomadas sin cubrir     → e2024p1-q5 (U6), e2023p2-q1 (U7)
🔴 CRÍTICO  4 páginas sin ninguna marca ✅        → conceptos/…, teoremas/…
🔴 CRÍTICO  U5 sin material · parcial en 6 días
🟡 REVISAR  3 enlaces rotos                       → [[teoremas/rice]]
🟡 REVISAR  2 páginas >150 líneas
⚪ MENOR    tipo `debate` sin instancias (12 ingestas)
```

Cerrá con **una sola** acción recomendada, la de mayor impacto.

Si el usuario pide corregir, hacelo en un **commit aislado**:
`lint(<materia>): <qué se corrigió>`.
