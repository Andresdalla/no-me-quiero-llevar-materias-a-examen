# Log

<!-- Una línea por operación. Lo escriben /ingest, /vaciar-cola, /resumen, /machete, /puentes. -->

| Fecha | Operación | Detalle |
|---|---|---|
| 2026-08-15 | `/nueva-materia` | alta · 7 tipos activos · 10 unidades · perfilado provisional (sin exámenes) |
| 2026-08-15 | `/ingest` | `repaso-haskell` · 6 páginas nuevas, 0 actualizadas · verificación 4/4 OK · U10 → parcial · rasterizada p.1 para confirmar símbolos `(\|\|)` y `(>>)` |
| 2026-08-15 | `/ingest` | `tc-temario` · 1 página nueva (ficha) · verificación 3/3 OK · sin páginas de concepto: un temario enumera, no explica · alimentó `programa.md` (10 unidades) |
| 2026-08-15 | `/ingest` | `revision-conjuntos` · 12 páginas nuevas · verificación 5/5 OK · U6 → parcial · rasterizadas p.3,5,7,9 (barras de inferencia y fórmulas) · 4 erratas de la fuente a `dudas.md` |
| 2026-08-15 | `/ingest` | `notas-conjuntos` · 13 páginas nuevas, 1 actualizada (`definiciones/funcion`) · verificación 6/6 OK · U6 → cubierto · rasterizadas p.5,7,10,11 · **13 consignas de examen reales** de 4 fechas → `examenes/patron.md` regenerado · 5 dudas nuevas |
| 2026-08-15 | `/ingest` | `numerabilidad-diag` · 4 páginas nuevas, 7 actualizadas · verificación 6/6 OK · rasterizadas p.8,9 · **3 divergencias reales con `notas-conjuntos`** (emparejamiento de Cantor, definición de `∼`, convención de "función") → `dudas.md` |
| 2026-08-15 | `/vaciar-cola` | cola vacía: 5 archivos procesados, 0 fallidos |
| 2026-08-15 | `/lint` | 0 críticos · corregidos: disciplina de (13 → ), 4 dudas registradas, tipos estructurales declarados, 1 `sin-demo` |
| 2026-08-15 | `/resumen` | resumen todo completo · 32 páginas del wiki · 8 unidades sin material · sin PDF (falta typst) |
2026-08-16 · redacción · 12 páginas migradas al registro en prosa · definiciones/funcion partida: sale comparativas/notacion-de-funciones (tope 150 líneas)
