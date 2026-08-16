---
id: teoria-de-la-computacion/comparativas/formas-de-definir-conjuntos
tipo: comparativa
tema: U6
fuentes: [revision-conjuntos p.2, revision-conjuntos p.3, revision-conjuntos p.5]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Extensión vs comprensión vs inducción

🧠 Esta es la página bisagra del apunte: la elección de método **no es de estilo**, es lo que
decide si un conjunto infinito se puede definir o no. De acá sale toda la maquinaria de
numerabilidad de U6.

## Tabla

| Criterio | Por extensión | Por comprensión | Por inducción / constructivamente |
|---|---|---|---|
| Cómo se da | ✅ [p.2] "Enumerar sus elementos" | ✅ [p.2] "Nos basamos en conjunto A anteriormente definido, y cierta propiedad que satisfacen sus elementos" | ✅ [p.3] una regla base y una regla inductiva |
| Forma | `A = {1, 2, 3}` | `B = {x ∈ A : x > 2}` | `(rz) Z ∈ ℕ` · `(rs) n ∈ ℕ ⇒ S n ∈ ℕ` |
| ¿Sirve para infinitos? | **no** | sí, si ya tenés el `A` de base | sí |
| Requiere | nada | un conjunto previo + una propiedad | constructores |
| Da además | — | — | 🧠 un **árbol de prueba** por cada elemento |

Todas las citas de esta tabla son ✅ [revision-conjuntos].

## Criterio de decisión

✅ [revision-conjuntos p.5] Ante la pregunta "Mediante qué método podemos definir esta
relación ?" para `R<`, el apunte responde:

✅ [revision-conjuntos p.5] "Es un conjunto infinito, imposible definirlo por extensión"

🧠 Ese es el criterio, y es el único que importa: **la cardinalidad del conjunto descarta
métodos**. Si es infinito, extensión queda afuera y quedan dos. Entre esas dos, comprensión
necesita un conjunto anterior ya definido; inducción no necesita nada previo, se construye a
sí mismo desde los constructores.

## Cuándo elegir cada uno

- **Extensión**: solo si es finito y chico. Es la única que no exige nada previo pero no
  escala.
- **Comprensión**: cuando ya tenés un universo definido y querés recortarlo con una propiedad.
  ✅ [revision-conjuntos p.5] Para `R<` "podría ser teniendo definidas las operaciones de
  igual, mayor que cero y suma": `R< = {(x, y) : x, y ∈ ℕ ∧ (∃z ∈ ℕ)(z > 0 ∧ x + z = y)}`
- **Inducción**: cuando querés **razonar** sobre el conjunto, no solo describirlo. 🧠 Es la
  única que te deja demostrar por inducción estructural después — ver
  [[demostraciones/transitividad-de-r-menor]].

## Las dos notaciones de una definición inductiva

✅ [revision-conjuntos p.3] Con implicaciones:

```
(rz) Z ∈ ℕ
(rs) n ∈ ℕ ⇒ S n ∈ ℕ
```

✅ [revision-conjuntos p.3] "Otra forma de escribirlo" — reglas de inferencia, premisas
arriba de la barra y conclusión abajo:

```
     ─────────            n ∈ ℕ
 rz   Z ∈ ℕ          rs ───────────
                        S n ∈ ℕ
```

🧠 `rz` no tiene premisas: por eso la barra está vacía arriba. Esa es la marca de un caso base.

⚠️ La extracción de texto destruye estas barras horizontales. Están transcriptas contra la
página rasterizada, no contra el texto plano.

## Relacionado

- [[definiciones/conjunto]] — qué es un conjunto y cuándo dos son iguales
- [[definiciones/relacion]] — `R<` definida por los tres métodos
- [[demostraciones/transitividad-de-r-menor]] — para qué sirve haberla definido por inducción
- [[fuentes/revision-conjuntos]]
