// Preámbulo de los PDFs del wiki. Lo usa scripts/build_pdf.py.
// Perfiles: resumen (1 col, 11pt) · machete (2 cols, 9pt) · guia (1 col, 10.5pt)

#let perfiles = (
  resumen: (tam: 11pt, cols: 1, margen: 2cm, interlinea: 0.65em),
  machete: (tam: 9pt, cols: 2, margen: 8mm, interlinea: 0.5em),
  guia: (tam: 10.5pt, cols: 1, margen: 2.4cm, interlinea: 0.75em),
)

#let aplicar(doc, perfil: "resumen") = {
  let c = perfiles.at(perfil, default: perfiles.resumen)

  set page(
    paper: "a4",
    margin: c.margen,
    columns: c.cols,
    numbering: "1 / 1",
    number-align: center,
  )
  set text(
    size: c.tam,
    lang: "es",
    hyphenate: true,
    font: ("Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans", "Apple Color Emoji"),
  )
  set par(justify: true, leading: c.interlinea)
  set list(indent: 0.6em, spacing: c.interlinea * 1.4)
  set enum(indent: 0.6em, spacing: c.interlinea * 1.4)

  show heading.where(level: 1): it => block(
    below: 0.8em, above: 1.1em,
    text(size: 1.35em, weight: "bold", it.body),
  )
  show heading.where(level: 2): it => block(
    below: 0.6em, above: 0.9em,
    text(size: 1.15em, weight: "bold", fill: rgb("#1f3b57"), it.body),
  )
  show heading: it => it

  show raw.where(block: false): it => box(
    fill: rgb("#f0f0f3"), inset: (x: 2pt), outset: (y: 2pt), radius: 2pt, it,
  )
  show raw.where(block: true): it => block(
    fill: rgb("#f6f6f8"), inset: 6pt, radius: 3pt, width: 100%, it,
  )

  set table(
    stroke: 0.4pt + rgb("#b8b8c0"),
    inset: (x: 5pt, y: 3pt),
  )
  show table.cell.where(y: 0): set text(weight: "bold")

  set quote(block: true)
  show quote: it => block(
    inset: (left: 8pt), stroke: (left: 2pt + rgb("#c9c9d1")), it.body,
  )

  doc
}
