---
id: teoria-de-la-computacion/comparativas/relaciones-vs-funciones
tipo: comparativa
tema: U6
fuentes: [revision-conjuntos p.9]
estado: completo
dominio: 0
actualizado: 2026-08-15
---

# Relaciones vs funciones

## Tabla

✅ [revision-conjuntos p.9] Transcripción literal de la tabla del apunte:

| | Relaciones | Funciones |
|---|---|---|
| Tipado | `f ⊆ A × B` | `f : A → B` |
| Pertenencia / aplicación | `(x, y) ∈ f` | `f(x) = y` |
| Composición | `R ∘ S` | `s ∘ r` |

🧠 Diferencia de fondo, no de notación: ✅ [revision-conjuntos p.9] una función es una relación
"donde cada elemento del dominio está relacionado con **a lo sumo un** elemento del
codominio". Todo lo demás de la tabla es la misma idea escrita de dos maneras.

## Criterio de decisión

🧠 Lo que decide es **si necesitás aplicar o solo consultar**. Con `(x, y) ∈ f` preguntás si un
par está; con `f(x) = y` obtenés el resultado. Solo podés escribir `f(x)` si sabés que hay a lo
sumo un `y`: por eso la notación funcional exige primero probar que la relación es funcional.

## Cuándo elegir cada uno

- Usá la notación de **relaciones** mientras estés probando propiedades estructurales
  (reflexiva, transitiva, órdenes): es donde vive
  [[definiciones/propiedades-de-relaciones]].
- Usá la notación de **funciones** cuando ya sepas que es funcional y te interese calcular.
- 🧠 Al comparar cardinalidades (U6) se usa la de funciones: inyecciones y biyecciones son
  funciones, no relaciones cualquiera.

## La trampa de la composición

⚠️ **El orden se invierte y el apunte no lo explica.** La tabla pone `R ∘ S` para relaciones y
`s ∘ r` para funciones — misma operación, escritura espejada.

✅ [revision-conjuntos p.8] Para relaciones:
`R ∘ S = {(x, z) : (x, y) ∈ R ∧ (y, z) ∈ S}`, o sea **`R` primero**.

🧠 En la notación funcional habitual `(s ∘ r)(x) = s(r(x))`, o sea **`r` primero**: el de la
derecha. Por eso, para que las dos expresiones signifiquen lo mismo, las letras aparecen en
orden inverso. Si mezclás las dos convenciones en el parcial, componés al revés.

## Relacionado

- [[definiciones/relacion]] · [[definiciones/funcion]]
- [[definiciones/operaciones-con-relaciones]] — la definición de `∘` que se hereda
- [[fuentes/revision-conjuntos]]
