---
description: Audita el esquema de tipos de una materia contra el wiki real y propone cambios con su costo
argument-hint: <materia>
---

# /reperfilar $1

Se corre a las **20 ingestas**, o a las **8** si el perfilado quedó `provisional` (materia sin
parciales viejos al momento del alta). También después de conseguir parciales viejos.

`M` = `materias/activas/$1`.

## 1. Medir el uso real

```bash
grep -rh "^tipo:" $M/wiki --include='*.md' | sort | uniq -c | sort -rn
wc -l < $M/manifest.jsonl
grep -rh "^estado:" $M/wiki --include='*.md' | sort | uniq -c
```

Comparé contra los tipos declarados en `$M/CLAUDE.md`.

## 2. Buscar tres desajustes

### a. Tipos infrautilizados
Tipo activo con **<3 instancias** tras 20 ingestas. Ocupa un lugar de los 8 y no rinde.

### b. Patrones sin tipo propio
Páginas que repiten la misma estructura de secciones y no encajan en su tipo declarado.
Detectalas por los encabezados:
```bash
grep -rh "^## " $M/wiki --include='*.md' | sort | uniq -c | sort -rn | head -20
```
Si aparece una sección frecuente que no pertenece a ningún tipo activo, hay un tipo latente.
Se propone solo si cumple las tres condiciones del catálogo: ningún primitivo encaja,
≥3 instancias esperadas, y regla de verificación escrita.

### c. Desalineación con la evaluación
Releé qué pide la cátedra: si el último parcial ingerido pide sobre todo construir y el wiki
está lleno de `definicion`, el esquema está mirando para otro lado.

```bash
grep "parcial\|final" $M/manifest.jsonl
```

## 3. Proponer con costo de migración explícito

Toda propuesta lleva su precio, medido, no estimado a ojo:

```bash
grep -rl "^tipo: debate" $M/wiki --include='*.md' | wc -l     # archivos a tocar
grep -ro "\[\[[a-z]*/[a-z-]*\]\]" $M/wiki | grep -c "debates/" # enlaces a reapuntar
```

Formato:

```
SACAR   debate      → 1 instancia en 22 ingestas · migra a comparativa · 1 archivo, 3 enlaces
RENOMBRAR construccion → maquinas (vocabulario de la cátedra) · 9 archivos, 0 enlaces rotos
AGREGAR ejercicio-tipo → 11 páginas repiten "Consigna/Estrategia/Trampa" · 0 migración
```

Esperá el OK. Sin confirmación no se migra nada.

## 4. Migrar

Por cada cambio aceptado:

1. Actualizá `$M/CLAUDE.md`: tipos activos, alias, y **`schema_version` +1**.
2. Movés los archivos a la carpeta nueva y reescribís su `tipo:` e `id:`.
3. Reapuntá **todos** los enlaces `[[...]]` que los referencian.
4. Actualizá `wiki/mapa.md` (los ids cambiaron).
5. Verificá que no quedaron enlaces rotos:
   ```bash
   grep -roh "\[\[[^]]*\]\]" $M/wiki | sort -u
   ```
6. Si se agregó un tipo nuevo, escribí su plantilla en `plantillas/paginas/<tipo>.md` y su
   entrada con regla de verificación en `plantillas/catalogo.md`.

## 5. Commit aislado

**Un commit por migración, y nada más en ese commit.** Es lo que hace que sea revertible:

```bash
git add -A && git commit -m "reperfilar($1): schema v2 · <cambio> · N archivos"
```

Si algo sale mal: `git revert <hash>` y el esquema vuelve al anterior.

## Al terminar, decí exactamente

`schema_version` nueva, qué tipos entraron y salieron, cuántos archivos y enlaces se
tocaron, y el hash del commit para poder revertirlo.
