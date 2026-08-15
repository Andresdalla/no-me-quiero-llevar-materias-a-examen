#!/usr/bin/env python3
"""Genera tests/fixtures/fixture-tc.pdf: 3 páginas para probar el pipeline entero.

p.1 una definición · p.2 un teorema con enunciado · p.3 un diagrama vectorial
(el diagrama tiene que disparar `candidatas_visuales` en pdf_texto.py).

uso: .venv/bin/python tests/fixtures/gen_fixture.py
"""
from __future__ import annotations

import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:  # pragma: no cover
    sys.exit("error: falta PyMuPDF. `uv pip install --python .venv/bin/python pymupdf`")

DESTINO = Path(__file__).resolve().parent / "fixture-tc.pdf"


def escribir(page, y, texto, tam=11, fuente="helv"):
    page.insert_text((60, y), texto, fontsize=tam, fontname=fuente)
    return y + tam * 1.6


def main() -> int:
    doc = pymupdf.open()

    # --- p.1: definición -------------------------------------------------- #
    p = doc.new_page()
    y = escribir(p, 80, "Unidad 2. Lenguajes regulares", 18, "hebo")
    y = escribir(p, y + 14, "Definicion 2.1 (Automata finito determinista)", 13, "hebo")
    for linea in [
        "Un automata finito determinista es una quintupla M = (Q, S, d, q0, F)",
        "donde Q es un conjunto finito de estados, S es el alfabeto de entrada,",
        "d: Q x S -> Q es la funcion de transicion, q0 pertenece a Q es el estado",
        "inicial y F, subconjunto de Q, es el conjunto de estados de aceptacion.",
    ]:
        y = escribir(p, y, linea)
    y = escribir(p, y + 10, "Notacion. Escribimos L(M) para el lenguaje reconocido por M.")

    # --- p.2: teorema ----------------------------------------------------- #
    p = doc.new_page()
    y = escribir(p, 80, "Teorema 2.7 (Cerradura bajo union)", 13, "hebo")
    for linea in [
        "Si A1 y A2 son lenguajes regulares, entonces A1 union A2 tambien lo es.",
        "",
        "Demostracion. Sean M1 y M2 automatas que reconocen A1 y A2. Se construye",
        "M que simula ambos en paralelo sobre el producto cartesiano de estados,",
        "y acepta si alguno de los dos acepta. Como M es finito, la union es regular.",
    ]:
        y = escribir(p, y, linea)
    y = escribir(p, y + 14, "Observacion. La misma tecnica no sirve para la interseccion", 11)
    y = escribir(p, y, "de lenguajes libres de contexto.", 11)

    # --- p.3: diagrama vectorial ------------------------------------------ #
    p = doc.new_page()
    escribir(p, 80, "Figura 2.3. Automata que acepta cadenas con cantidad par de ceros", 12, "hebo")
    centros = [(130, 220), (300, 220), (470, 220)]
    for i, (cx, cy) in enumerate(centros):
        p.draw_circle(pymupdf.Point(cx, cy), 26, color=(0, 0, 0), width=1.2)
        p.insert_text((cx - 9, cy + 4), f"q{i}", fontsize=11, fontname="helv")
        if i < len(centros) - 1:
            x0, x1 = cx + 26, centros[i + 1][0] - 26
            p.draw_line(pymupdf.Point(x0, cy), pymupdf.Point(x1, cy))
            p.draw_line(pymupdf.Point(x1, cy), pymupdf.Point(x1 - 8, cy - 5))
            p.draw_line(pymupdf.Point(x1, cy), pymupdf.Point(x1 - 8, cy + 5))
            p.insert_text(((x0 + x1) / 2 - 3, cy - 8), "0", fontsize=10, fontname="helv")
    p.draw_circle(pymupdf.Point(*centros[0]), 31, color=(0, 0, 0), width=1.0)

    doc.set_metadata({"title": "Fixture Teoria de la Computacion"})
    doc.save(DESTINO)
    doc.close()
    print(f"escrito: {DESTINO} ({DESTINO.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
