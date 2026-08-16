# Dudas abiertas

<!-- Toda marca ⚠️ del wiki tiene que estar acá. /lint reporta las que falten. -->

| Página | Duda | Fuentes en conflicto | Estado |
|---|---|---|---|
| `wiki/programa.md` | El temario dice **Marzo 2021** y las notas de teoría **Marzo 2026**. ¿Sigue vigente ese temario? | tc_temario (2021) vs notas-conjuntos (2026) | abierta |
| `wiki/programa.md` | El corte en unidades U1-U10 es 🧠 mío: el temario es una lista plana sin numerar. Si la cátedra publica su propia numeración, hay que remapear. | tc_temario | abierta |
| `CLAUDE.md` | Correlativas sin confirmar. Previa `Fundamentos de la Computación` inferida de "como lo veíamos en fundamentos" (repartido de Haskell). Posteriores: sin datos. | repaso-haskell p.1 | abierta |
| `CLAUDE.md` | Fecha de **lectura de la tarea final**: a definir por la cátedra. | — | abierta |
| `construcciones/funciones-sobre-bool` | ⚠️ ¿Qué operación es `(>>) :: Bool -> Bool -> Bool`? El símbolo está verificado contra la página, pero el repartido no lo define. Sobre booleanos lo natural es la implicación; en Haskell estándar `>>` es secuenciación monádica. Sin resolver hasta confirmarlo. | repaso-haskell p.1 | abierta |
| `construcciones/funciones-sobre-arboles` | ⚠️ `listA :: Arb a -> [a]` no especifica orden de recorrido (in-order / pre-order / post-order) ni trae ejemplo. Las tres respuestas son defendibles. | repaso-haskell p.3 | abierta |
| `definiciones/operaciones-con-conjuntos` | ⚠️ **Errata del apunte**: la intersección está escrita `A ∩ B = {x : x ∈ A ∧ xB}`, le falta el `∈`. Verificado contra la página rasterizada: no es pérdida de extracción. | revision-conjuntos p.3 | abierta |
| `definiciones/ordenes` | ⚠️ **Errata del apunte**: dice "orden total estricto **laxo**", que se contradice a sí mismo. | revision-conjuntos p.8 | abierta |
| `definiciones/ordenes` | ⚠️ La condición de totalidad `(∀x,y ∈ A)((x,y) ∈ R ∨ (y,x) ∈ R)`, evaluada en `x = y`, exige reflexividad. Con esa definición **ningún orden estricto puede ser total**. La versión habitual usa tricotomía. Preguntarlo en clase. | revision-conjuntos p.8 | abierta |
| `demostraciones/transitividad-de-r-menor` | ⚠️ En p.7 el bloque rotulado `3 < 5` arranca en `(S Z, …)` = 1, mientras que en p.6 el mismo bloque arranca en 3. Verificado en ambas páginas rasterizadas. ¿Deliberado (ya muestra la concatenación) o error de tipeo? | revision-conjuntos p.6 vs p.7 | abierta |
