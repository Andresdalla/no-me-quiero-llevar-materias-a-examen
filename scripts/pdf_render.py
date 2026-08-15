#!/usr/bin/env python3
"""Rasteriza páginas puntuales de un PDF a PNG.

Solo las páginas pedidas: rasterizar un PDF entero cuesta ~1.5k tokens por página
al mirarlo. `--paginas` es obligatorio a propósito.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def error(msg: str) -> None:
    sys.exit(f"error: {msg}")


def cargar_fitz():
    try:
        import pymupdf  # PyMuPDF >= 1.24
    except ImportError:
        try:
            import fitz as pymupdf  # nombre histórico
        except ImportError:
            error(
                "falta PyMuPDF. Instalalo con `uv pip install pymupdf` "
                "o `python3 -m pip install pymupdf`"
            )
    return pymupdf


def parsear_paginas(spec: str, total: int) -> list[int]:
    """'12,13,20' o '12-15' → índices 0-based, validados contra `total`."""
    idx: list[int] = []
    for parte in spec.split(","):
        parte = parte.strip()
        if not parte:
            continue
        if "-" in parte:
            a, _, b = parte.partition("-")
            try:
                ini, fin = int(a), int(b)
            except ValueError:
                error(f"rango inválido: {parte!r}")
            if ini > fin:
                error(f"rango invertido: {parte!r}")
            idx.extend(range(ini - 1, fin))
        else:
            try:
                idx.append(int(parte) - 1)
            except ValueError:
                error(f"página inválida: {parte!r}")
    fuera = [i + 1 for i in idx if i < 0 or i >= total]
    if fuera:
        error(f"páginas fuera de rango (el PDF tiene {total}): {fuera}")
    return sorted(set(idx))


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="pdf_render.py",
        description="Rasteriza a PNG solo las páginas indicadas de un PDF.",
    )
    ap.add_argument("pdf", help="ruta al PDF")
    ap.add_argument(
        "--paginas",
        required=True,
        help="obligatorio. Lista o rangos 1-based, ej. 12,13,20 o 12-15",
    )
    ap.add_argument("--out", required=True, help="directorio de salida")
    ap.add_argument("--dpi", type=int, default=150, help="resolución (default: 150)")
    args = ap.parse_args()

    if args.dpi < 36 or args.dpi > 600:
        error("--dpi fuera de rango razonable (36-600)")

    fitz = cargar_fitz()
    ruta = Path(args.pdf)
    if not ruta.is_file():
        error(f"no existe el archivo {ruta}")
    try:
        doc = fitz.open(ruta)
    except Exception as exc:
        error(f"no se pudo abrir {ruta}: {exc}")

    indices = parsear_paginas(args.paginas, doc.page_count)
    if not indices:
        error("--paginas no seleccionó ninguna página")

    destino = Path(args.out)
    destino.mkdir(parents=True, exist_ok=True)

    generados = []
    for i in indices:
        pix = doc[i].get_pixmap(dpi=args.dpi)
        archivo = destino / f"p{i + 1:03d}.png"
        pix.save(archivo)
        generados.append(
            {"pagina": i + 1, "archivo": str(archivo), "ancho": pix.width, "alto": pix.height}
        )
    doc.close()

    print(json.dumps({"dpi": args.dpi, "imagenes": generados}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
