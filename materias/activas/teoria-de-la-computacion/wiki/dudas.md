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
| `examenes/notas-conjuntos-ejercicios` | ⚠️ **Falta el operador** en la consigna de febrero 2026: "entonces A ␣ B es no numerable". El hueco está en el PDF, verificado por rasterización. Casi seguro es la diferencia (`A \ B`), pero no lo doy por hecho. | notas-conjuntos p.10 | abierta |
| `definiciones/funcion` | ⚠️ **Notación divergente entre los dos apuntes**: función parcial es `f : A ⇸ B` en `revision-conjuntos` y `f : A ↬ B` en `notas-conjuntos`. La cátedra lo reconoce (Observación 1: "diferentes docentes pueden usar notaciones diferentes"). ¿Cuál se espera en el parcial? | revision-conjuntos p.9 vs notas-conjuntos p.2 | abierta |
| `definiciones/conjunto-infinito` | ⚠️ `notas-conjuntos` usa `⊂` para subconjunto propio en la Definición 14 y `⊊` en la sección 3, en el mismo documento. | notas-conjuntos p.3 | abierta |
| `definiciones/cardinales-infinitos` | La sección 10 está marcada "(Extra pero muy recomendado)". ¿Entra al parcial del 7/12 o no? | notas-conjuntos p.9 | abierta |
| `construcciones/emparejamiento-de-cantor` | ⚠️ **Las dos fuentes dan emparejamientos de Cantor DISTINTOS**: `(Σ[k=0..i+j] k) + i` vs `(i+j)(i+j+1)/2 + j`. Difieren en `+i` contra `+j`: `f(1,0)` vale 2 en una y 1 en la otra. Verificado contra ambas páginas rasterizadas. ¿Cuál se usa en el parcial? | numerabilidad-diag p.8 vs notas-conjuntos p.6 | abierta |
| `definiciones/comparacion-de-cardinalidades` | ⚠️ **Dos definiciones distintas de `∼`**: `A ⪯ B ∧ B ⪯ A` (Copello Def 2.2) vs "existe biyección total" (Acuña Def 13). Equivalentes por Schröder-Bernstein, pero cambia qué hay que demostrar. | numerabilidad-diag p.5 vs notas-conjuntos p.3 | abierta |
| `definiciones/funcion` | ⚠️ `numerabilidad-diag` reserva la palabra "función" para **función parcial**; las otras dos fuentes no fijan convención. Y llama "dominio" solo a donde `f` está definida, mientras `revision-conjuntos` llama "dominio" al conjunto de entrada entero. | numerabilidad-diag p.3 vs revision-conjuntos p.4 | abierta |
| `definiciones/numerable-y-contable` | ⚠️ El ejercicio `?14` usa "**enumerable**", palabra que no se define en ningún lado del repartido. ¿Es un desliz por "numerable"? | numerabilidad-diag p.7 | abierta |
