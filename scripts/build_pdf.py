#!/usr/bin/env python3
"""Compila un .md del wiki a PDF.

Pipeline: leer md → renderizar bloques ```mermaid``` a SVG con `npx mmdc` →
sustituirlos por imágenes → compilar con Typst (o pandoc+LaTeX como fallback).

Degrada con elegancia: si no hay motor de PDF, deja el .md procesado y avisa.
Nunca falla entero por una herramienta opcional.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ESTILO = RAIZ / "plantillas" / "estilo.typ"
PERFILES = ("resumen", "machete", "guia")

# --------------------------------------------------------------------------- #
# Mermaid
# --------------------------------------------------------------------------- #
BLOQUE_MERMAID = re.compile(r"^```mermaid[ \t]*\n(.*?)^```[ \t]*$", re.S | re.M)


def render_mermaid(md: str, dir_figs: Path, avisos: list[str]) -> str:
    bloques = list(BLOQUE_MERMAID.finditer(md))
    if not bloques:
        return md
    if not shutil.which("npx"):
        avisos.append("npx no está en PATH: los diagramas Mermaid quedan como código.")
        return md

    dir_figs.mkdir(parents=True, exist_ok=True)
    reemplazos: dict[str, str] = {}
    for n, m in enumerate(bloques, start=1):
        fuente = dir_figs / f"mermaid-{n}.mmd"
        svg = dir_figs / f"mermaid-{n}.svg"
        fuente.write_text(m.group(1), encoding="utf-8")
        cmd = ["npx", "-y", "@mermaid-js/mermaid-cli", "-i", str(fuente), "-o", str(svg),
               "-b", "transparent"]
        try:
            proc = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        except (subprocess.TimeoutExpired, OSError) as exc:
            avisos.append(f"mermaid {n}: falló ({exc}). Queda como bloque de código.")
            continue
        if proc.returncode != 0 or not svg.exists():
            detalle = (proc.stderr or proc.stdout).strip().splitlines()
            avisos.append(f"mermaid {n}: {detalle[-1] if detalle else 'error'}")
            continue
        reemplazos[m.group(0)] = f"![]({svg})"

    for viejo, nuevo in reemplazos.items():
        md = md.replace(viejo, nuevo)
    return md


# --------------------------------------------------------------------------- #
# Markdown → Typst
# --------------------------------------------------------------------------- #
ESCAPAR = {c: "\\" + c for c in "\\#$*_@<>[]`~"}

MATE_LATEX = [
    (re.compile(r"\\frac\{([^{}]*)\}\{([^{}]*)\}"), r"frac(\1, \2)"),
    (re.compile(r"\\sqrt\{([^{}]*)\}"), r"sqrt(\1)"),
    (re.compile(r"\\text\{([^{}]*)\}"), r'"\1"'),
    (re.compile(r"\\mathbb\{([A-Z])\}"), r"\1\1"),
    (re.compile(r"\\mathcal\{([^{}]*)\}"), r"cal(\1)"),
    (re.compile(r"\\(left|right|,|;|!)"), ""),
]
MATE_PALABRAS = {
    "leq": "<=", "le": "<=", "geq": ">=", "ge": ">=", "neq": "!=", "ne": "!=",
    "to": "->", "rightarrow": "->", "longrightarrow": "-->", "Rightarrow": "=>",
    "implies": "=>", "leftrightarrow": "<->", "iff": "<=>", "mapsto": "|->",
    "cdot": "dot", "times": "times", "div": "div", "pm": "plus.minus",
    "ldots": "dots", "dots": "dots", "cdots": "dots.c",
    "subseteq": "subset.eq", "supseteq": "supset.eq", "subset": "subset",
    "notin": "in.not", "emptyset": "nothing", "varnothing": "nothing",
    "cup": "union", "cap": "sect", "setminus": "without",
    "infty": "infinity", "land": "and", "wedge": "and", "lor": "or", "vee": "or",
    "lnot": "not", "neg": "not", "equiv": "equiv", "approx": "approx",
    "sim": "tilde", "propto": "prop", "models": "tack.r", "vdash": "tack",
    "prod": "product", "bigcup": "union.big", "bigcap": "sect.big",
    "log": "log", "max": "max", "min": "min", "lim": "lim",
}


def mate_a_typst(expr: str) -> str:
    for patron, rep in MATE_LATEX:
        anterior = None
        while anterior != expr:
            anterior, expr = expr, patron.sub(rep, expr)
    expr = re.sub(r"\\\\", " ", expr)
    expr = re.sub(r"\\([A-Za-z]+)", lambda m: MATE_PALABRAS.get(m.group(1), m.group(1)), expr)
    # Agrupación de sub/superíndices: en Typst se usan paréntesis, no llaves.
    anterior = None
    while anterior != expr:
        anterior = expr
        expr = re.sub(r"([_^])\{([^{}]*)\}", r"\1(\2)", expr)
    return expr.strip()


# Reconoce, en orden de prioridad, los fragmentos inline de markdown.
PATRON_INLINE = re.compile(
    r"""(?P<code>`[^`\n]+`)
      | (?P<mateblq>\$\$.+?\$\$)
      | (?P<mate>\$[^$\n]+\$)
      | (?P<img>!\[[^\]]*\]\([^)\s]+\))
      | (?P<wiki>\[\[[^\]\n]+\]\])
      | (?P<link>\[[^\]\n]+\]\([^)\s]+\))
      | (?P<negrita>\*\*[^\n]+?\*\*)
      | (?P<enfasis>(?<![\w*])[*_](?![\s*])[^\n]+?(?<![\s*])[*_](?![\w*]))
    """,
    re.X,
)


def escapar(texto: str) -> str:
    return "".join(ESCAPAR.get(c, c) for c in texto)


def inline(texto: str) -> str:
    """Markdown inline → markup de Typst. Recursivo: el contenido anidado se reprocesa."""
    partes: list[str] = []
    pos = 0
    for m in PATRON_INLINE.finditer(texto):
        partes.append(escapar(texto[pos:m.start()]))
        clase, bruto = m.lastgroup, m.group()
        if clase == "code":
            partes.append(bruto)
        elif clase == "mateblq":
            partes.append(f"$ {mate_a_typst(bruto[2:-2])} $")
        elif clase == "mate":
            partes.append(f"${mate_a_typst(bruto[1:-1])}$")
        elif clase == "img":
            ruta = bruto[bruto.index("(") + 1 : -1]
            partes.append(f'#image("{ruta}", width: 90%)')
        elif clase == "wiki":
            partes.append(f'#text(fill: rgb("#3b6ea5"))[{inline(bruto[2:-2])}]')
        elif clase == "link":
            corte = bruto.index("](")
            partes.append(f'#link("{bruto[corte + 2 : -1]}")[{inline(bruto[1:corte])}]')
        elif clase == "negrita":
            partes.append(f"*{inline(bruto[2:-2])}*")
        else:
            partes.append(f"_{inline(bruto[1:-1])}_")
        pos = m.end()
    partes.append(escapar(texto[pos:]))
    return "".join(partes)


def tabla_typst(filas: list[str]) -> list[str]:
    celdas = [[c.strip() for c in f.strip().strip("|").split("|")] for f in filas]
    cuerpo = [c for c in celdas if not re.fullmatch(r"[:\- ]+", "".join(c))]
    if not cuerpo:
        return []
    cols = max(len(f) for f in cuerpo)
    salida = [f"#table(", f"  columns: {cols},"]
    encabezado, *resto = cuerpo
    salida.append("  table.header(" + ", ".join(f"[{inline(c)}]" for c in encabezado) + "),")
    for fila in resto:
        fila = fila + [""] * (cols - len(fila))
        salida.append("  " + ", ".join(f"[{inline(c)}]" for c in fila) + ",")
    salida.append(")")
    return salida


def md_a_typst(md: str) -> str:
    md = re.sub(r"\A---\n.*?\n---\n", "", md, flags=re.S)  # frontmatter fuera
    lineas = md.split("\n")
    salida: list[str] = []
    i = 0
    while i < len(lineas):
        linea = lineas[i]

        if linea.startswith("```"):
            lenguaje = linea[3:].strip()
            i += 1
            cuerpo = []
            while i < len(lineas) and not lineas[i].startswith("```"):
                cuerpo.append(lineas[i])
                i += 1
            i += 1
            salida += ["```" + lenguaje, *cuerpo, "```", ""]
            continue

        if linea.lstrip().startswith("|") and linea.count("|") >= 2:
            filas = []
            while i < len(lineas) and lineas[i].lstrip().startswith("|"):
                filas.append(lineas[i])
                i += 1
            salida += tabla_typst(filas) + [""]
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", linea)
        if m:
            salida += ["=" * len(m.group(1)) + " " + inline(m.group(2)), ""]
            i += 1
            continue

        if re.match(r"^\s*(---|\*\*\*|___)\s*$", linea):
            salida += ["#line(length: 100%, stroke: 0.5pt + gray)", ""]
            i += 1
            continue

        m = re.match(r"^(\s*)([-*+])\s+(.*)$", linea)
        if m:
            salida.append(f"{m.group(1)}- {inline(m.group(3))}")
            i += 1
            continue

        m = re.match(r"^(\s*)\d+[.)]\s+(.*)$", linea)
        if m:
            salida.append(f"{m.group(1)}+ {inline(m.group(2))}")
            i += 1
            continue

        m = re.match(r"^>\s?(.*)$", linea)
        if m:
            salida += [f"#quote(block: true)[{inline(m.group(1))}]", ""]
            i += 1
            continue

        salida.append(inline(linea) if linea.strip() else "")
        i += 1

    return "\n".join(salida) + "\n"


# --------------------------------------------------------------------------- #
# Compilación
# --------------------------------------------------------------------------- #
def compilar_typst(md: str, destino_pdf: Path, perfil: str, trabajo: Path) -> tuple[bool, str]:
    fuente = trabajo / (destino_pdf.stem + ".typ")
    cabecera = (
        f'#import "{ESTILO}": aplicar\n'
        f'#show: aplicar.with(perfil: "{perfil}")\n\n'
    )
    fuente.write_text(cabecera + md_a_typst(md), encoding="utf-8")
    proc = subprocess.run(
        ["typst", "compile", "--root", "/", str(fuente), str(destino_pdf)],
        capture_output=True, text=True,
    )
    return proc.returncode == 0, (proc.stderr or proc.stdout).strip()


def compilar_pandoc(md_path: Path, destino_pdf: Path, perfil: str) -> tuple[bool, str]:
    geometria = "margin=8mm" if perfil == "machete" else "margin=2cm"
    tam = "9pt" if perfil == "machete" else "11pt"
    cmd = ["pandoc", str(md_path), "-o", str(destino_pdf),
           "-V", f"geometry:{geometria}", "-V", f"fontsize={tam}", "-V", "lang=es"]
    if perfil == "machete":
        cmd += ["-V", "classoption=twocolumn"]
    for motor in ("xelatex", "lualatex", "pdflatex"):
        if shutil.which(motor):
            cmd += [f"--pdf-engine={motor}"]
            break
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return proc.returncode == 0, (proc.stderr or proc.stdout).strip()


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="build_pdf.py",
        description="Compila un .md del wiki a PDF (Mermaid → SVG, Typst o pandoc).",
    )
    ap.add_argument("md", help="archivo markdown de entrada")
    ap.add_argument("--out", default="out", help="directorio de salida (default: out)")
    ap.add_argument("--perfil", default="resumen", choices=PERFILES,
                    help="resumen (1 col, 11pt) | machete (2 cols, 9pt) | guia (1 col, 10.5pt)")
    args = ap.parse_args()

    entrada = Path(args.md)
    if not entrada.is_file():
        sys.exit(f"error: no existe el archivo {entrada}")

    destino = Path(args.out)
    trabajo = destino / ".build"
    trabajo.mkdir(parents=True, exist_ok=True)

    avisos: list[str] = []
    md = render_mermaid(entrada.read_text(encoding="utf-8"), trabajo / "figuras", avisos)
    md_procesado = trabajo / entrada.name
    md_procesado.write_text(md, encoding="utf-8")

    pdf = destino / (entrada.stem + ".pdf")
    motor, ok, detalle = None, False, ""
    if shutil.which("typst"):
        motor = "typst"
        ok, detalle = compilar_typst(md, pdf, args.perfil, trabajo)
        if not ok:
            avisos.append(f"typst falló: {detalle.splitlines()[-1] if detalle else 'error'}")
    if not ok and shutil.which("pandoc"):
        motor = "pandoc"
        ok, detalle = compilar_pandoc(md_procesado, pdf, args.perfil)
        if not ok:
            avisos.append(f"pandoc falló: {detalle.splitlines()[-1] if detalle else 'error'}")
    if not ok and motor is None:
        avisos.append(
            "no hay motor de PDF (instalá typst: `brew install typst`). "
            f"Queda el markdown procesado en {md_procesado}"
        )

    resultado = {
        "entrada": str(entrada),
        "perfil": args.perfil,
        "motor": motor if ok else None,
        "pdf": str(pdf) if ok else None,
        "md_procesado": str(md_procesado),
        "avisos": avisos,
    }
    for aviso in avisos:
        print(f"aviso: {aviso}", file=sys.stderr)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
