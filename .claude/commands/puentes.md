---
description: Detecta conexiones entre materias leyendo solo los mapa.md, y escribe páginas puente que solo enlazan
argument-hint: [--materias a,b,c]
---

# /puentes $ARGUMENTS

Conecta materias sin duplicar contenido.

## Regla de lectura — no negociable

**Este comando lee únicamente los `wiki/mapa.md` de las materias activas.**
No abre páginas de contenido. No abre `index.md`. No abre `programa.md`.

El motivo es económico: los mapas de 5 materias son ~1000 líneas; las páginas son 200k
tokens. Un mapa alcanza para detectar una conexión, y confirmarla es tarea tuya cuando
estudies, no del comando.

Única excepción: si una conexión candidata es `⚠️ tensión`, podés abrir **como máximo una
página por materia** para confirmar que la contradicción existe antes de escribirla.

```bash
ls materias/activas/                                    # materias activas
head -200 materias/activas/<m>/wiki/mapa.md             # una por materia
```

## 1. Detectar candidatas

Buscá en los mapas:
- **Mismo término, materias distintas** → casi siempre glosario, a veces puente.
- **Mismo objeto, distinto nivel de abstracción** (un `mecanismo` en una, un `modelo` en otra).
- **Una materia usa lo que la otra construye** (autómatas → compiladores; grafos → redes).
- **Dos materias afirman cosas incompatibles** sobre lo mismo.

## 2. Clasificar

| Marca | Significa | Cuándo escribir la página |
|---|---|---|
| `⚡ fuerte` | Una materia usa directamente el resultado de la otra | siempre |
| `○ media` | Analogía útil, no dependencia | si ayuda a recordar |
| `⚠️ tensión` | Se contradicen o usan el término con sentidos incompatibles | **siempre, es lo más valioso** |

Las tensiones son oro para un final oral: es exactamente donde el tribunal pregunta.

## 3. Proponer antes de escribir

Mostrá la lista completa clasificada y esperá el OK. Nada se escribe sin confirmación.

```
⚡ fuerte   teoria-computacion/construcciones/afd-minimo ←→ compiladores/mecanismos/lexer
○ media    arquitectura/mecanismos/cache ←→ bases-datos/mecanismos/buffer-pool
⚠️ tensión ing-software/practicas/estimacion ←→ gestion/frameworks/cascada
```

## 4. Escribir la página puente

En `global/puentes/<slug>.md`, **máximo 15 líneas**:

```markdown
---
id: global/puentes/automatas-y-lexers
tipo: puente
fuerza: fuerte
materias: [teoria-computacion, compiladores]
actualizado: 2026-08-15
---

# Autómatas finitos ←→ análisis léxico

⚡ El lexer **es** un AFD ejecutado sobre el código fuente.

- [[teoria-computacion/construcciones/afd-minimo]]
- [[compiladores/mecanismos/lexer]]

🧠 Estudiar la minimización sirve dos veces: acá se ve por qué el lexer generado es chico.
```

Reglas duras:
- **Solo enlaces y una línea de por qué.** Cero contenido propio.
- Si una página puente pasa de 15 líneas, ese contenido **pertenece a una materia**: movelo
  a la materia que corresponda y dejá el enlace.
- Los enlaces van siempre en forma completa `[[materia/carpeta/slug]]`.
- Toda afirmación tuya sobre la relación va marcada `🧠`: no salió de ninguna fuente.

## 5. Términos colisionados

Si dos materias usan el mismo término con sentidos distintos, **no es un puente: es una
entrada de glosario**. Agregala a `global/glosario.md` con las dos acepciones y sus enlaces.

## 6. Qué actualiza

- Escribe: `global/puentes/<slug>.md`, y filas nuevas en `global/glosario.md`.
- Anexa a `wiki/log.md` de **cada** materia tocada: `<fecha> · puente <slug> con <materia>`.
- Commit: `puentes: <slug> · <materia-a> ←→ <materia-b>`.

## Al terminar, decí exactamente

Cuántos puentes se escribieron por tipo, cuántas entradas de glosario, y cuál tensión es la
más probable de que te la pregunten en un final.
