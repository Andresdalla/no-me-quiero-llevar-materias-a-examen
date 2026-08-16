---
id: teoria-de-la-computacion/fuentes/revision-conjuntos
tipo: fuente
tema: U6
fuentes: [revision-conjuntos p.1-10]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Ficha · Revisión de Teoría de Conjuntos

## Qué es

✅ [revision-conjuntos p.1] Documento titulado "Revisión de Teoría de Conjuntos". 10 páginas.
Sin autor ni fecha en el PDF.

🧠 Formato de láminas: títulos, fórmulas centradas y casi nada de prosa. Es material de repaso,
no un texto autocontenido.

## Qué cubre

| Sección | Páginas | Páginas del wiki |
|---|---|---|
| Conjuntos, pertenencia, extensión, inclusión | 1-2 | [[definiciones/conjunto]] |
| Formas de definir conjuntos | 2-3 | [[comparativas/formas-de-definir-conjuntos]] |
| Operaciones con conjuntos | 3-4 | [[definiciones/operaciones-con-conjuntos]] |
| Relaciones y `R<` | 4-5 | [[definiciones/relacion]] |
| Propiedades de relaciones | 6-7 | [[definiciones/propiedades-de-relaciones]] |
| Transitividad de `R<` | 6-7 | [[teoremas/transitividad-de-r-menor]] · [[demostraciones/transitividad-de-r-menor]] |
| Órdenes laxos y estrictos | 7-8 | [[definiciones/ordenes]] |
| Operaciones con relaciones | 8 | [[definiciones/operaciones-con-relaciones]] |
| Funciones y sus propiedades | 9-10 | [[definiciones/funcion]] · [[comparativas/relaciones-vs-funciones]] |

## Cuán confiable es

**Alta para las definiciones formales**, con tres reservas concretas verificadas contra las
páginas rasterizadas:

- ⚠️ p.3 · la intersección está escrita `A ∩ B = {x : x ∈ A ∧ xB}`, **le falta el `∈`**.
- ⚠️ p.8 · dice "orden total estricto **laxo**", que se contradice; y la condición de totalidad
  que da hace que ningún orden estricto pueda ser total.
- ⚠️ p.7 · el bloque rotulado `3 < 5` arranca en `1`, distinto de cómo aparece en p.6.
- Erratas menores: "Antisimétcia", "Asimétcia" (p.6).

**Deja ejercicios sin resolver**: `|P(A)| = ?`, `A ⊆ P(A)?`, `{{1,2}} ⊆ {1,2}?`, si `R<` es
antisimétrica y asimétrica, `R⁻¹< = ?`, `R< ∘ R< = ?`. Las respuestas en este wiki son 🧠
inferidas y están marcadas.

## Nota de procesamiento

🧠 La extracción de texto pierde las ligaduras `fi`/`fl` ("denir" por "definir", "reexiva" por
"reflexiva") y **destruye por completo las barras de las reglas de inferencia**. Se
rasterizaron selectivamente las páginas 3, 5, 7 y 9 para transcribir fórmulas y árboles de
prueba contra la imagen. Todo lo marcado `✅` de esas páginas está verificado visualmente.

## Relacionado

- [[fuentes/tc-temario]] — dónde cae este material en el programa (U6)
- [[fuentes/repaso-haskell]]
