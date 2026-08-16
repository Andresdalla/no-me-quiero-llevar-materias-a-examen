---
id: teoria-de-la-computacion/definiciones/propiedades-de-relaciones
tipo: definicion
tema: U6
fuentes: [revision-conjuntos p.6, revision-conjuntos p.7]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Definición de las propiedades de una relación

Todas sobre `R ⊆ A × A`, es decir relaciones **binarias**.

## Enunciado

✅ [revision-conjuntos p.6] Transcripción literal de las cinco:

| Propiedad | Enunciado |
|---|---|
| Reflexiva | `(∀x ∈ A)((x, x) ∈ R)` |
| Simétrica | `(∀x, y ∈ A)((x, y) ∈ R ⇒ (y, x) ∈ R)` |
| Antisimétrica | `(∀x, y ∈ A)((x, y) ∈ R ∧ (y, x) ∈ R ⇒ x = y)` |
| Asimétrica | `(∀x, y ∈ A)((x, y) ∈ R ⇒ (y, x) ∉ R)` |
| Transitiva | `(∀x, y, z ∈ A)((x, y) ∈ R ∧ (y, z) ∈ R ⇒ (x, z) ∈ R)` |

**De equivalencia.** ✅ [revision-conjuntos p.7] "Si R es reflexiva, simétrica y transitiva."

⚠️ El apunte escribe "Antisimétcia" y "Asimétcia" en los títulos. Es un error de tipeo de la
fuente; las fórmulas están bien.

## Notación

- `∉` es la negación de `∈`. En la extracción de texto aparece como `/∈`.
- 🧠 La cátedra enuncia todo con cuantificadores explícitos, nunca en prosa. En el parcial
  conviene responder en el mismo formato.

## Ejemplo

✅ [revision-conjuntos p.6] "`R<` es transitiva ? Sí" — ver
[[teoremas/transitividad-de-r-menor]].

🧠 `R≤` sí es reflexiva, simétrica no, antisimétrica sí y transitiva sí: es el orden parcial
laxo del que habla [[definiciones/ordenes]].

## Contraejemplo

✅ [revision-conjuntos p.6] El apunte usa `R<` como contraejemplo de casi todas:

- "`R<` es reflexiva ? No, dado que `(0, 0) ∉ R<`"
- "`R<` es simétrica ? No, dado que `(0, 1) ∈ R<` pero `(1, 0) ∉ R<`"

✅ [revision-conjuntos p.7] "`R<` es de equivalencia ? No, por no ser reflexiva ni simétrica."

✅ [revision-conjuntos p.6] Quedan **dos preguntas sin responder** en el apunte: "`R<` es
antisimétrica ?" y "`R<` es asimétrica ?"

🧠 Las dos son **sí**. Asimétrica: si `x < y` entonces nunca `y < x`. Antisimétrica: la premisa
`(x,y) ∈ R< ∧ (y,x) ∈ R<` no se cumple nunca, así que la implicación es **verdadera por
vacuidad**. Ese razonamiento por vacuidad es el que más se falla.

## Confusiones frecuentes

- **Antisimétrica vs asimétrica.** No son lo mismo y el apunte las pone seguidas a propósito.
  Asimétrica prohíbe `(y,x)` siempre; antisimétrica la permite **solo si `x = y`**. Toda
  relación asimétrica es antisimétrica, no al revés: `R≤` es antisimétrica pero no asimétrica.
- **"No es simétrica" ≠ "es antisimétrica".** Son propiedades independientes, no opuestas.
- **Vacuidad.** Una propiedad universal sobre una premisa que nunca se cumple es verdadera.
  Ver [[definiciones/relacion]] para por qué `(x,y)` y `(y,x)` nunca coexisten en `R<`.

## Relacionado

- [[definiciones/relacion]] — qué es una relación binaria
- [[definiciones/ordenes]] — las combinaciones de estas propiedades que tienen nombre
- [[teoremas/transitividad-de-r-menor]] · [[demostraciones/transitividad-de-r-menor]]
- [[fuentes/revision-conjuntos]]
