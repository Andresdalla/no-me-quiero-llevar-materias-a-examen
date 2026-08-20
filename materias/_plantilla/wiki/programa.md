# Programa
modo: <temario | emergente>

<!-- Espina dorsal: el wiki se audita contra este archivo, no contra sí mismo.
     La línea `modo:` decide cómo se llena y qué audita /lint. Lo genera /nueva-materia.

     modo: temario — hay temario oficial. Una entrada por unidad, de arriba hacia
     abajo, y `cobertura` dice qué falta:

         ## U1 · Título de la unidad
         - cobertura: sin-material        # sin-material | parcial | cubierto
         - fuentes: []
         - paginas: []
         - temas: lista del temario oficial, textual

     modo: emergente — no hay temario. Este archivo arranca SIN ejes y los escribe
     /ingest, de abajo hacia arriba, con lo que encuentra en el material. No hay
     `cobertura`: un eje existe porque hay material, y nadie dijo qué entra.

         ## microservicios
         - fuentes: [fowler-cap2, clase-03]
         - paginas: [conceptos/saga, patrones/api-gateway]
         - temas: descomposición, límites de contexto, sagas
-->
