---
description: Cinco preguntas sobre un tema ANTES de estudiarlo. Fallar es lo esperado.
argument-hint: <tema> [--materia <slug>]
---

# /pre-test $ARGUMENTS

Cinco preguntas sobre un tema que **todavía no estudiaste**.

## Lo primero que decís, antes de la pregunta 1

Literalmente esto, sin suavizarlo:

> Vas a fallar casi todas y está bien: ese es el punto. Intentar responder algo que no sabés
> deja el terreno preparado para cuando lo estudies. No cuenta para tu dominio ni queda
> registrado como error.

Sin este aviso el pre-test desmoraliza y no lo volvés a usar.

## 1. De dónde salen las preguntas

**De `wiki/programa.md`, no del wiki.** El tema puede no estar ingerido todavía: ese es el
caso normal de este comando.

```bash
grep -A5 "^## <tema>" materias/activas/<materia>/wiki/programa.md
```

Usá la lista de `temas:` de esa unidad —que salió del temario oficial— para formular
preguntas. Si la unidad tiene páginas en el wiki, **no las abras**: leerlas te haría preguntar
lo que el wiki ya sabe, y acá se trata de lo que vos no sabés todavía.

## 2. Las preguntas

- **5, ni más ni menos.** Es una preparación, no una evaluación.
- Formulables desde el título del tema: "¿Qué creés que significa X?", "¿Para qué serviría Y?",
  "¿Qué diferencia esperarías entre A y B?".
- Nivel `comprender` o `aplicar`. Preguntar definiciones textuales de algo que nunca viste no
  produce ningún intento: produce silencio.
- Una por mensaje. Aceptá "no sé" como respuesta válida, pero pedí una conjetura primero:
  **el intento fallido es el mecanismo, no la respuesta correcta.**

## 3. Después de las 5

Mostrá, para cada pregunta:

- Qué respondió el usuario.
- Qué dice el programa oficial sobre ese punto (una línea).
- Si hay página en el wiki, el enlace para cuando estudie.

Sin corregir con dureza y sin puntaje. No hubo nada que aprobar.

## 4. Qué actualiza

- **Nada de `estado/dominio.md`.** Un pre-test no mide dominio: mide que todavía no estudiaste.
- **Nada de `estado/errores.md`.** Fallar acá no es un error tuyo.
- **Nada de `calibracion.md`**: no se pide confianza en un pre-test.
- Anexá una línea a `estado/historial.md`: `| <fecha> | <tema> | pre-test | 5 preguntas |`.
- Sin commit propio; entra en el próximo.

## Al terminar, decí exactamente

Qué conceptos aparecieron que el usuario ya intuía y cuáles le resultaron completamente
nuevos —esa distinción es útil para saber por dónde empezar— y el comando para estudiar el
tema: `/resumen <tema>` o `/vaciar-cola` si la unidad todavía no tiene material.
