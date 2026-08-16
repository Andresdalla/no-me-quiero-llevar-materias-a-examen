---
id: teoria-de-la-computacion/teoremas/propiedades-de-conjuntos-infinitos
tipo: teorema
tema: U6
fuentes: [numerabilidad-diag p.7]
estado: sin-demo
dominio: 0
actualizado: 2026-08-15
---

# Propiedades de los conjuntos infinitos

## Enunciado

**Teorema 3.1.**

1. "`N` es el infinito "más chico", o sea: Si `A` es infinito entonces `N ⪯ A`."
2. "Si `A` es infinito y `A ⪯ B` entonces `B` es infinito."
3. "Todo conjunto finito tiene `n` elementos para cierto `n` natural. Formalmente: `A` finito
 ssi `A ∼ {1, …, n}` para cierto `n ∈ N`."

"Las demostraciones constituyen un ejercicio difícil."

## Hipótesis

- Parte 1: `A` infinito
- Parte 2: `A` infinito **y** `A ⪯ B`
- Parte 3: ninguna; es una caracterización de finito.
- "Infinito" es el de la Definición 3.1: `A ⪯ B` para algún `B ⊂ A` propio. Ver
 [[definiciones/conjunto-infinito]].

## Demostración

**Sin demostración en la fuente.** la cátedra las declara "un
ejercicio difícil" y no las da.

La parte 1 es el mismo enunciado que `notas-conjuntos` plantea **dos veces** como ejercicio
(Ejercicio 2 y Ejercicio 7: "Mostrar que `∀A infinito`, se cumple: `N ⪯ A`"). Ninguna de las
dos fuentes de la materia lo demuestra. Si lo necesitás en el parcial, citalo como resultado
de cátedra, no lo improvises.

## Cuándo se aplica

**Parte 1** es la que justifica llamar `ℵ₀` al *menor* cardinal infinito: sin ella, "menor"
no significaría nada. Ver [[definiciones/cardinales-infinitos]].

**Parte 2** es la herramienta práctica: para probar que algo es infinito, encajá adentro un
infinito conocido. Es más fácil que exhibir la inyección en un subconjunto propio.

**Parte 3** conecta el mundo finito con el infinito, y es lo que hace que
[[definiciones/numerable-y-contable]] pueda decir "contable e infinito ⇒ numerable": un
contable que no es infinito es finito, y por esta parte tiene exactamente `n` elementos.

## Errores típicos

- **Usar la parte 2 al revés.** Dice `A ⪯ B` con `A` infinito ⇒ `B` infinito. Al revés es
 falso: `B` infinito y `A ⪯ B` no dice nada sobre `A` (todo finito cumple `A ⪯ N`).
- **Dar por demostrada la parte 1.** Ninguna fuente de la materia la prueba. Es un teorema
 citable, no un paso obvio.
- La parte 3 usa `{1, …, n}` (empezando en 1), mientras que
el ejercicio sobre `Nₖ` lo define como `Nₖ = {0, 1, 2 … k}`
 (empezando en 0). Distinta convención en cada fuente: contá los elementos, no confíes en el
 subíndice.

## Relacionado

- [[definiciones/conjunto-infinito]] — la definición que este teorema explota
- [[definiciones/numerable-y-contable]] · [[definiciones/comparacion-de-cardinalidades]]
- [[definiciones/cardinales-infinitos]]
- [[fuentes/numerabilidad-diag]]

## Procedencia

- **Enunciado** — numerabilidad-diag p.7
- **Hipótesis** — numerabilidad-diag p.7 · incluye comentario del sistema
- **Demostración** — numerabilidad-diag p.7 · incluye comentario del sistema
- **Cuándo se aplica** — sin cita: comentario del sistema
- **Errores típicos** — notas-conjuntos p.9 · incluye comentario del sistema · duda registrada en `dudas.md`
