---
id: ingenieria-de-software-agil-2/definiciones/deuda-tecnica
tipo: definicion
tema: U1
fuentes: [ut1-calidad-devops p.15, p.16]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Deuda técnica

Es el concepto que conecta la calidad interna, que nadie fuera del equipo ve, con la calidad
externa que el cliente sí percibe. Importa en esta materia porque explica por qué la velocidad
de entrega se degrada sola con el tiempo si nadie hace nada, que es justamente lo que las
prácticas de U2 en adelante buscan evitar.

## Enunciado

La cátedra la define como "Metáfora para explicar descuidos en la calidad interna de un
producto". La palabra que hace todo el trabajo es metáfora: no es un defecto puntual sino una
forma de razonar sobre decisiones que se toman hoy y se pagan después, y esa forma de razonar
es la que permite discutirla con quien decide el presupuesto.

Cuatro propiedades la caracterizan. "Las decisiones que generan deuda técnica son más difíciles
de enmendar a medida que pasa el tiempo (generan 'interés')". "Existe deuda técnica inherente
a la complejidad de los sistemas de software". "Probablemente los responsables del producto la
perciban más fácilmente que un observador externo (calidad interna)". Y la que cierra el
argumento de la materia: "La calidad interna tiene impacto en la calidad externa: especialmente
cuando nos interesa reducir tiempos de reparación y mantenimiento".

## Notación

`Calidad interna` es la que se observa en el código y la arquitectura: modularidad,
analizabilidad, modificabilidad, testabilidad. `Calidad externa` es la que percibe quien usa
el servicio. La cuarta propiedad de arriba dice que la primera acota a la segunda, y es el
puente que conecta esta página con la métrica de tiempo de recuperación de
[[modelos/dora-core]].

## Ejemplo

Un módulo de facturación sin pruebas automáticas se puede modificar rápido las primeras veces.
Cada cambio posterior obliga a verificar a mano lo que ya funcionaba, así que el costo por
cambio sube aunque el módulo no haya cambiado de tamaño. Eso es el interés: no se paga el
descuido una vez, se paga en cada modificación futura.

## Contraejemplo

Un bug reportado en producción no es deuda técnica: es un defecto de calidad externa,
localizable y cerrable. Ilustra por contraste la parte "calidad interna" del enunciado, porque
un defecto lo ve cualquiera desde afuera mientras que la deuda solo la percibe quien trabaja
sobre el código. Tampoco es deuda técnica la complejidad inherente que la propia cátedra
reconoce como inevitable: llamar deuda a todo lo que cuesta vacía el término.

## Confusiones frecuentes

La confusión más común es tratar la deuda técnica como sinónimo de código feo, cuando el
criterio de la definición es económico y no estético. Lo que la vuelve deuda es que encarece
los cambios futuros, no que incomode leerla.

La segunda es creer que es siempre indeseable. Como parte de la deuda es inherente a la
complejidad del sistema, la decisión relevante no es tener cero deuda sino saber cuál se
tomó y cuándo se paga. Se conecta directamente con [[definiciones/calidad-de-software]]: la
deuda no aparece en la conformidad con los requerimientos, y por eso un producto puede estar
conforme y ser inviable de mantener a la vez.

## Relacionado

- [[definiciones/calidad-de-software]] — la calidad externa, donde la deuda termina impactando.
- [[modelos/iso25010]] — las características de mantenibilidad que la deuda degrada.
- [[modelos/dora-core]] — la mantenibilidad del código figura como capacidad que predice rendimiento.

## Procedencia

- **Enunciado** — ut1-calidad-devops p.15, p.16 · incluye comentario del sistema
- **Notación** — sin cita: comentario del sistema
- **Ejemplo** — sin cita: comentario del sistema
- **Contraejemplo** — sin cita: comentario del sistema
- **Confusiones frecuentes** — sin cita: comentario del sistema
