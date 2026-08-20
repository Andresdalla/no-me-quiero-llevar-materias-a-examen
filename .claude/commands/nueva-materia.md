---
description: Crea una materia desde la plantilla, la perfila con la evidencia de evaluación y genera su programa
argument-hint: <slug-de-la-materia>
---

# /nueva-materia $1

Crea `materias/activas/$1/` y la deja lista para ingerir. Si `$1` está vacío, pedí el slug
(minúsculas, sin tildes, con guiones) y frená.

## 1. Copiar la plantilla

```bash
test -d materias/activas/$1 && echo "YA EXISTE" || cp -R materias/_plantilla materias/activas/$1
```

Si imprime `YA EXISTE`, frená y avisá. No sobrescribas una materia existente.

## 2. Pedir los datos de cursada

Preguntá en **un solo mensaje** y esperá la respuesta. **No preguntes fechas de parcial,
recuperatorio ni final**: este sistema no gestiona calendario.

- Nombre completo de la materia y cátedra.
- Cuatrimestre y año (ej. `2026-2C`).
- Modalidad de evaluación: escrito · oral · múltiple choice · proyecto (puede ser mixta).
- Correlativas que ya cursó y que dependen de esta.

## 3. Pedir el material de perfilado

Pedile que copie a `materias/activas/$1/ingest/`:

1. El **temario oficial** (obligatorio: sin él no hay `programa.md`).
2. **Parciales y finales viejos**, si los consiguió.
3. **Guías de ejercicios**.

Esperá confirmación y listá lo que llegó:

```bash
ls -la materias/activas/$1/ingest/
```

Si no hay temario, escribí `programa.md` con una sola unidad `U0 · sin temario` y anotá en
`wiki/dudas.md` que falta. No lo inventes.

## 4. Procesar la evidencia primero

Ejecutá `/ingest` sobre esos archivos, en este orden: parciales viejos → guías → temario.
Son la evidencia de perfilado y tienen que estar procesados antes del paso 5.

## 5. Perfilar: elegir hasta 8 tipos

Leé `plantillas/catalogo.md` (solo la tabla "Elegir tipo" y los tipos candidatos).
Elegí **como máximo 8** tipos, con esta prioridad de evidencia:

| Evidencia | Peso | Qué mirar |
|---|---|---|
| Parciales viejos (`/ingest --tipo examen`) | ★★★★★ | qué forma tienen las consignas: ¿demostrar? ¿construir? ¿comparar? ¿decidir un caso? Con `patron.md` generado, los verbos ya están contados |
| Guías de ejercicios | ★★★★ | qué se practica repetidamente |
| Índice de bibliografía | ★★★ | cómo organiza el contenido el libro de cátedra |
| Temario | ★★★ | qué temas entran |

Reglas:
- Un tipo entra si esperás **≥3 instancias** en la materia. Si no, no entra.
- Podés renombrar un tipo al vocabulario de la cátedra manteniendo su regla de verificación.
  Registrá el alias como `alias → tipo-base`.
- **Con ≥2 exámenes ingeridos**, el perfilado es `definitivo`: hay evidencia real de cómo
  evalúa la cátedra. Uno solo no alcanza para distinguir el patrón del año particular.
- **Si no hay parciales viejos**: escribí `perfilado: provisional` en el CLAUDE.md de la
  materia y programá `/reperfilar` a las **8 ingestas** (en vez de 20).
- Recordale al usuario que **el examen más reciente se reserva sin abrir** para el simulacro
  previo al parcial (ver `/ingest --tipo examen`).

Mostrá la selección con una línea de justificación por tipo y esperá el OK antes de seguir.

## 6. Generar `wiki/programa.md`

Una entrada por unidad del temario, en este formato exacto:

```markdown
## U3 · Lenguajes libres de contexto
- cobertura: sin-material
- fuentes: []
- paginas: []
- temas: gramáticas, autómatas de pila, forma normal de Chomsky
```

`cobertura` es `sin-material` | `parcial` | `cubierto`. Arranca todo en `sin-material`.
Esta es la espina dorsal: el wiki se audita contra el programa, no contra sí mismo.

## 7. Generar el `CLAUDE.md` de la materia

En `materias/activas/$1/CLAUDE.md`, máximo 60 líneas:

```markdown
# <Nombre completo> (`$1`)

- cuatrimestre: 2026-2C · schema_version: 2 · perfilado: definitivo|provisional
- evaluación: <modalidad>

## Tipos activos
| Tipo | Alias de cátedra | Por qué |
|---|---|---|
| teorema | — | 4 de 5 consignas del parcial 2024 piden enunciar y aplicar |

## Vocabulario y notación de la cátedra
- <término de cátedra> = <término estándar>
- Notación: <símbolos propios>

## Reglas propias
- <lo que esta materia hace distinto: convenciones, unidades, criterios de corrección>
```

## 8. Inicializar los archivos de estado

Verificá que existan y tengan encabezado (vienen de la plantilla; completá los que falten):

```bash
ls materias/activas/$1/wiki/{index.md,mapa.md,log.md,dudas.md,programa.md} \
   materias/activas/$1/estado/{dominio.md,errores.md,repaso.md,quiz-log.md} \
   materias/activas/$1/manifest.jsonl
```

`mapa.md` arranca vacío salvo el encabezado de columnas. `manifest.jsonl` arranca vacío.

## 9. Registrar en el índice global

Agregá una fila a `global/indice.md` con: slug, nombre, estado `activa`, cuatrimestre,
correlativas, fecha de alta.

## 10. Commit

```bash
git add -A && git commit -m "materia($1): alta · <N> tipos activos · <M> unidades"
```

## Al terminar, decí exactamente

Qué tipos quedaron activos, cuántas unidades tiene el programa (todas en `sin-material`) y
que el próximo paso es copiar apuntes a `ingest/` y correr `/vaciar-cola`.
