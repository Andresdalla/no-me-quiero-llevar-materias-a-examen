---
id: teoria-de-la-computacion/demostraciones/transitividad-de-r-menor
tipo: demostracion
tema: U6
fuentes: [revision-conjuntos p.6, revision-conjuntos p.7]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Demostración de que `R<` es transitiva

## Qué prueba

[[teoremas/transitividad-de-r-menor]]

## Técnica

**Inducción** — estructural, sobre el árbol de prueba.

✅ [revision-conjuntos p.7] "Dados `(x, y) ∈ R<` y `(y, z) ∈ R<`, hacemos inducción en la
segunda relación `R<`, esto es, en el **árbol de prueba** de `(y, z) ∈ R<`"

## La intuición primero

✅ [revision-conjuntos p.6] "Idea de la demostración: Veamos dadas evidencias de que `1 < 3` y
`3 < 5`, cómo podemos inferir que `1 < 5`"

✅ [revision-conjuntos p.7] "Idea de la demostración: **"concatenar las demostraciones"**"

🧠 La derivación de `3 < 5` se re-ejecuta empezando desde `1` en vez de desde `3`: cada
aplicación de `(r2)` avanza el segundo componente sin tocar el primero, así que el mismo
esqueleto de derivación sirve con otro punto de partida.

⚠️ En p.7 el bloque rotulado `3 < 5` arranca en `(S Z, ...)`, o sea en **1**, no en 3 —
mientras que en p.6 el mismo bloque arranca en `(S (S (S Z)), ...)`, o sea en 3. Verificado
contra las dos páginas rasterizadas: no es pérdida de extracción. Puede ser deliberado (ya
muestra la derivación *concatenada*) o un error de tipeo. Anotado en `wiki/dudas.md`.

## Pasos

Sean `(x, y) ∈ R<` y `(y, z) ∈ R<`. Inducción sobre el árbol de prueba de `(y, z) ∈ R<`.

1. **Caso base.** ✅ [revision-conjuntos p.7] "Caso base: `(y, S y) ∈ R<`, entonces"

   El árbol de `(y, z) ∈ R<` es la sola aplicación de `(r1)`, con `z = S y`. De la hipótesis
   `(x, y) ∈ R<` se aplica `(r2)`:

   ```
     (x,   y) ∈ R<
   ─────────────────  (r2)
     (x, S y) ∈ R<
   ```

   Y `S y = z`, que es lo que se quería.

2. **Caso inductivo.** ✅ [revision-conjuntos p.7] "Caso inductivo:"

   ```
     (y,   z) ∈ R<
   ─────────────────  (r2)
     (y, S z) ∈ R<
   ```

   ✅ [revision-conjuntos p.7] "Dado que `(x, y) ∈ R<` y `(y, z) ∈ R<` podemos aplicar el paso
   inductivo y tener que `x < z`, entonces:"

   ```
     (x,   z) ∈ R<
   ─────────────────  (r2)
     (x, S z) ∈ R<
   ```

3. ✅ [revision-conjuntos p.7] `□`

🧠 Las barras de inferencia están transcriptas contra las páginas rasterizadas: la extracción
de texto las destruye por completo. Ver [[fuentes/revision-conjuntos]].

## Dónde suele fallar el estudiante

- 🧠 **Inducir sobre el número y no sobre la derivación.** Es el paso que todos dan por obvio.
  La hipótesis inductiva habla del **árbol de prueba** de `(y, z) ∈ R<`, no de `z` como
  natural. Si escribís "supongamos que vale para z, veamos para z+1" estás haciendo otra
  demostración.
- 🧠 **Inducir sobre la relación equivocada.** El apunte lo dice explícito: sobre la
  **segunda**. Con la primera, la hipótesis inductiva no aplica al caso que necesitás.
- 🧠 **Saltear el caso base.** Es donde `(r1)` fuerza `z = S y`; sin eso no sabés de dónde sale
  la primera aplicación de `(r2)`.
- 🧠 **Confundir el `(r2)` de la hipótesis con el `(r2)` de la conclusión.** En los dos casos
  se aplica la misma regla, pero a pares distintos: uno mueve `(x, ·)`, el otro `(y, ·)`.

## Relacionado

- [[teoremas/transitividad-de-r-menor]] — el enunciado
- [[definiciones/relacion]] — las reglas `(r1)` y `(r2)` que definen `R<`
- [[definiciones/propiedades-de-relaciones]] — qué es transitiva
- [[comparativas/formas-de-definir-conjuntos]] — por qué la definición inductiva habilita esto
- [[fuentes/revision-conjuntos]]
