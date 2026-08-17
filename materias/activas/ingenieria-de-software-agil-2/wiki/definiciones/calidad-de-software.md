---
id: ingenieria-de-software-agil-2/definiciones/calidad-de-software
tipo: definicion
tema: U1
fuentes: [ut1-calidad-devops p.10, p.11, p.14]
estado: completo
dominio: 0
actualizado: 2026-08-16
---

# Calidad de software

La materia arranca con una mala noticia útil: no hay una definición única de calidad de
software, y por eso todo lo que viene después se apoya en estándares que proponen medirla en
vez de definirla. Entender que la definición es plural es lo que hace inteligible el salto a
un modelo de calidad como ISO 25010.

## Enunciado

La cátedra lo plantea así: "No existe una definición universal de calidad de software, pero
contamos con estándares y documentos que pueden servir como punto de partida". De ahí toma
dos puntos de partida concretos. "Según el SWEBOK, calidad se alcanza a través de la
conformidad de todos los requerimientos, sin importar el carácter de ellos" y "Según la norma
ISO25000:2016, la calidad de software se alcanza midiendo características de calidad definidas
en un modelo de calidad". La diferencia entre ambos no es de matiz: SWEBOK ancla la calidad en
lo que se pidió, mientras que ISO la ancla en un catálogo de características que existe antes
del proyecto y contra el que se mide.

Las tres formulaciones del siglo XX que la cátedra pone como antecedente empujan todas hacia
el mismo lado. "Deming, calidad implica satisfacer necesidades y expectativas de los clientes
a lo largo de la vida del producto", "Juran, calidad es sinónimo de adecuación al uso" e
"Ishikawa, calidad es una noción que debe ser definida desde la óptica del cliente". Las tres
sacan la definición de manos del que construye y la ponen en manos del que usa, que es
precisamente el supuesto que después justifica medir en producción y no en la entrega.

## Notación

`SWEBOK` es el Software Engineering Body of Knowledge. `ISO 25000` es la familia de normas de
calidad de producto de software, e `ISO 25010` es la norma de esa familia que contiene el
modelo de calidad propiamente dicho. Cuando la cátedra dice "un modelo de calidad" sin más,
se refiere a [[modelos/iso25010]].

## Ejemplo

Un servicio que cumple todos los requerimientos funcionales pactados pero tarda ocho segundos
en responder ilustra por qué SWEBOK dice "sin importar el carácter de ellos": el tiempo de
respuesta es un requerimiento igual que los demás, y si estaba pactado, incumplirlo es un
defecto de calidad y no una molestia menor.

## Contraejemplo

Un equipo que declara alcanzada la calidad porque la suite de pruebas está en verde no cumple
ninguna de las dos definiciones. Ni cubre la conformidad con todos los requerimientos, porque
las pruebas solo verifican los que alguien codificó como caso, ni mide característica alguna
de un modelo de calidad. Es el contraste exacto con el ejemplo de arriba, donde el atributo
incumplido estaba explícitamente pactado.

## Confusiones frecuentes

La confusión más cara es tratar la calidad como una propiedad fija que se alcanza y se
conserva. La cátedra insiste en lo contrario para servicios digitales: la calidad es "una
característica viva, igual que el software en producción", "dinámica: puede crecer y decrecer",
"amplia y multifactorial: distintos interesados pueden percibir la calidad de manera diferente"
y "dependiente del contexto", con incertidumbre y variabilidad. De ahí que la respuesta de la
materia sea medir de forma continua y no certificar una vez.

La segunda confusión es leer conformidad como conformidad funcional. Los atributos que la
cátedra llama emergentes —usabilidad y accesibilidad universales, seguridad, disponibilidad,
observabilidad y telemetría, confiabilidad frente a resiliencia— son requerimientos con el
mismo estatus, y son los que [[modelos/iso25010]] organiza. No confundir tampoco con
[[definiciones/deuda-tecnica]], que es calidad interna: invisible para el cliente y aun así
determinante del tiempo de reparación.

## Relacionado

- [[modelos/iso25010]] — el modelo contra el que ISO propone medir.
- [[definiciones/deuda-tecnica]] — la cara interna de la calidad.
- [[definiciones/devops]] — la respuesta organizativa a esta demanda de calidad.

## Procedencia

- **Enunciado** — ut1-calidad-devops p.10, p.11 · incluye comentario del sistema
- **Notación** — sin cita: comentario del sistema
- **Ejemplo** — sin cita: comentario del sistema
- **Contraejemplo** — sin cita: comentario del sistema
- **Confusiones frecuentes** — ut1-calidad-devops p.9, p.14 · incluye comentario del sistema
