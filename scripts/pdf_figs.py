#!/usr/bin/env python3
"""Extrae figuras de una página del PDF hacia assets/.

Dos modos:
  recorte : --bbox x0,y0,x1,y1  → recorta esa región a 300 dpi (--out = archivo .png)
  auto    : --auto              → extrae las imágenes embebidas (--out = directorio)
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


def parsear_bbox(spec: str) -> tuple[float, float, float, float]:
    partes = [p.strip() for p in spec.split(",")]
    if len(partes) != 4:
        error("--bbox espera 4 números: x0,y0,x1,y1")
    try:
        x0, y0, x1, y1 = (float(p) for p in partes)
    except ValueError:
        error(f"--bbox no es numérico: {spec!r}")
    if x1 <= x0 or y1 <= y0:
        error("--bbox vacío o invertido (se espera x0<x1 e y0<y1)")
    return x0, y0, x1, y1


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="pdf_figs.py",
        description="Recorta una región de una página, o extrae sus imágenes embebidas.",
    )
    ap.add_argument("pdf", help="ruta al PDF")
    ap.add_argument("--pagina", type=int, required=True, help="número de página (1-based)")
    ap.add_argument("--bbox", help="x0,y0,x1,y1 en puntos PDF")
    ap.add_argument(
        "--auto",
        action="store_true",
        help="extrae las imágenes embebidas de la página en vez de recortar",
    )
    ap.add_argument(
        "--out",
        required=True,
        help="archivo .png destino (modo recorte) o directorio (modo --auto)",
    )
    ap.add_argument("--dpi", type=int, default=300, help="resolución del recorte (default: 300)")
    args = ap.parse_args()

    if bool(args.bbox) == bool(args.auto):
        error("elegí exactamente uno: --bbox x0,y0,x1,y1 o --auto")

    fitz = cargar_fitz()
    ruta = Path(args.pdf)
    if not ruta.is_file():
        error(f"no existe el archivo {ruta}")
    try:
        doc = fitz.open(ruta)
    except Exception as exc:
        error(f"no se pudo abrir {ruta}: {exc}")

    if args.pagina < 1 or args.pagina > doc.page_count:
        error(f"página {args.pagina} fuera de rango (el PDF tiene {doc.page_count})")
    page = doc[args.pagina - 1]
    generados = []

    if args.auto:
        destino = Path(args.out)
        destino.mkdir(parents=True, exist_ok=True)
        for n, info in enumerate(page.get_images(full=True), start=1):
            xref = info[0]
            try:
                datos = doc.extract_image(xref)
            except Exception as exc:
                print(f"aviso: no se pudo extraer xref {xref}: {exc}", file=sys.stderr)
                continue
            archivo = destino / f"p{args.pagina:03d}-img{n}.{datos['ext']}"
            archivo.write_bytes(datos["image"])
            generados.append(
                {"archivo": str(archivo), "ancho": datos["width"], "alto": datos["height"]}
            )
        if not generados:
            print(f"aviso: la página {args.pagina} no tiene imágenes embebidas", file=sys.stderr)
    else:
        rect = fitz.Rect(*parsear_bbox(args.bbox))
        recorte = rect & page.rect
        if recorte.is_empty:
            error("el --bbox no intersecta la página")
        destino = Path(args.out)
        if destino.suffix.lower() != ".png":
            error("--out debe terminar en .png en modo recorte")
        destino.parent.mkdir(parents=True, exist_ok=True)
        pix = page.get_pixmap(clip=recorte, dpi=args.dpi)
        pix.save(destino)
        generados.append(
            {"archivo": str(destino), "ancho": pix.width, "alto": pix.height,
             "bbox": [round(v, 1) for v in (recorte.x0, recorte.y0, recorte.x1, recorte.y1)]}
        )

    doc.close()
    print(json.dumps({"pagina": args.pagina, "figuras": generados}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
