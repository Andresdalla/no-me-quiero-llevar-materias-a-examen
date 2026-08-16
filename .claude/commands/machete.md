---
description: Arma un machete de 1-2 páginas a dos columnas: fórmulas, enunciados, tablas y procedimientos
argument-hint: [tema] [--materia <slug>]
---

# /machete $ARGUMENTS

Lo que entra en una hoja. Si no entra, no es un machete.

`PY` = `.venv/bin/python` si existe, si no `python3`. Sin `[tema]`, cubre toda la materia.

## 1. De dónde lee

Igual que `/resumen`: `CLAUDE.md` de la materia → `wiki/mapa.md` → solo las páginas
filtradas por tema. Nunca el directorio entero.

Priorizá, en este orden, las páginas de tipo: `numeros` → `teorema` → `definicion` →
`comparativa` → `construccion` → `protocolo`. El resto entra solo si sobra lugar.

## 2. Qué entra y qué no

| Entra | No entra |
|---|---|
| Fórmulas y notación | Prosa explicativa |
| Enunciados de teoremas (recortados a su condición operativa) | Demostraciones |
| Tablas comparativas | Ejemplos largos |
| Procedimientos en pasos numerados | Motivación e historia |
| Valores numéricos con unidad | Contenido sin fuente |
| Diagramas Mermaid de ≤6 nodos | Diagramas grandes |

**Nada sin fuente va al machete.** En el parcial no querés copiarte de una inferencia del
sistema.

**La regla de redacción del repo no rige acá.** `global/metodo/redaccion.md` pide prosa
conectada para las páginas y los resúmenes; el machete es lo contrario por diseño y su propia
guía lo dice: la prosa explicativa está en la columna *No entra*. No lo "mejores" agregándole
oraciones de hilado.

La procedencia se abrevia a una línea al pie: `Fuentes: sipser-cap1 p.77, p.80 · apunte p.4`.
El machete es dos columnas a 9pt: cada carácter cuesta.

## 3. Tope de tamaño

Objetivo: 2 páginas A4 a dos columnas, 9pt (≈ 9000 caracteres).

Antes de compilar, contá:

```bash
wc -c materias/activas/<materia>/out/machete-<tema>.md
```

Si supera ~9000: cortá por lo menos prioritario según la tabla del paso 1 hasta entrar.
Decí qué sacaste. No compiles un machete de 5 páginas: deja de ser un machete.

## 4. Salida

```bash
$PY scripts/build_pdf.py materias/activas/<materia>/out/machete-<tema>.md \
  --out materias/activas/<materia>/out/ --perfil machete
```

El perfil `machete` es dos columnas, 9pt, márgenes de 8 mm.

## 5. Qué actualiza

- Escribe: `out/machete-<tema>.md` (+ `.pdf` si hay motor).
- Anexa a `wiki/log.md`: `<fecha> · machete <tema> · N caracteres`.
- No toca `estado/` ni el wiki.

## Al terminar, decí exactamente

Ruta del archivo, caracteres finales, cuántas páginas del wiki entraron y qué dejaste afuera
por espacio.
