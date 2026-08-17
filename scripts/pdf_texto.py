#!/usr/bin/env python3
"""Extrae texto estructurado de un PDF y detecta páginas con contenido visual.

Escribe <out>/texto.md (con marcadores `<!-- p.N -->`) y <out>/analisis.json.
Los marcadores de página son la base de toda la citación del wiki: sin ellos
no se puede escribir `[fuente-id p.N]`.
"""
from __future__ import annotations

import argparse
import collections
import contextlib
import json
import re
import sys
from pathlib import Path

# Símbolos que delatan una fórmula cuando aparecen en densidad alta.
SIMBOLOS_MATE = set(
    "∑∏∫√≤≥≠≈≡∈∉⊂⊆⊃⊇∪∩∅∀∃∄¬∧∨⊕→⇒⇔↔↦∞±×÷·∂∇°"
    "ℕℤℚℝℂΔΩΣΠΛΓΦΨΘαβγδεζηθικλμνξπρστυφχψω"
    "⟨⟩⌈⌉⌊⌋≪≫∼≅⊢⊨"
)
FUENTES_MATE = ("cmmi", "cmsy", "mathit", "mathematical", "symbol", "euclid")
VINETAS = re.compile(r"^\s*([-–—•▪·*]|\(?\d{1,2}[.)]|[a-z][.)])\s+")


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
    """'1-20' o '3,7,9-11' → índices 0-based, validados contra `total`."""
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


def union(rects):
    acc = None
    for r in rects:
        acc = r if acc is None else acc | r
    return acc


def redondear(rect) -> list[float]:
    return [round(v, 1) for v in (rect.x0, rect.y0, rect.x1, rect.y1)]


# --------------------------------------------------------------------------- #
# Jerarquía de títulos
# --------------------------------------------------------------------------- #
def histograma_tamanos(doc, indices) -> collections.Counter:
    """Tamaño de fuente → cantidad de caracteres. Define qué es cuerpo y qué título."""
    cont: collections.Counter = collections.Counter()
    for i in indices:
        for b in doc[i].get_text("dict")["blocks"]:
            if b.get("type") != 0:
                continue
            for linea in b["lines"]:
                for span in linea["spans"]:
                    texto = span["text"].strip()
                    if texto:
                        cont[round(span["size"], 1)] += len(texto)
    return cont


def niveles_titulo(cont: collections.Counter) -> tuple[float, dict[float, int]]:
    """Devuelve (tamaño del cuerpo, {tamaño: nivel de heading})."""
    if not cont:
        return 10.0, {}
    cuerpo = cont.most_common(1)[0][0]
    mayores = sorted((t for t in cont if t >= cuerpo * 1.12), reverse=True)
    return cuerpo, {t: min(i + 1, 4) for i, t in enumerate(mayores)}


def texto_bloque(bloque) -> tuple[list[str], float]:
    lineas, tam = [], 0.0
    for linea in bloque["lines"]:
        crudo = "".join(s["text"] for s in linea["spans"]).strip()
        if crudo:
            lineas.append(crudo)
            tam = max(tam, max(s["size"] for s in linea["spans"]))
    return lineas, round(tam, 1)


def unir_lineas(lineas: list[str]) -> str:
    """Une líneas de un párrafo deshaciendo la partición silábica del PDF."""
    salida = ""
    for linea in lineas:
        if not salida:
            salida = linea
        elif salida.endswith("-") and linea[:1].islower():
            salida = salida[:-1] + linea
        else:
            salida += " " + linea
    return salida


def markdown_pagina(page, mapa_niveles: dict[float, int]) -> list[str]:
    partes: list[str] = []
    for bloque in page.get_text("dict")["blocks"]:
        if bloque.get("type") != 0:
            continue
        lineas, tam = texto_bloque(bloque)
        if not lineas:
            continue
        nivel = mapa_niveles.get(tam)
        texto = unir_lineas(lineas)
        if nivel and len(texto) <= 120 and not texto.endswith("."):
            partes.append("#" * nivel + " " + texto)
        elif any(VINETAS.match(l) for l in lineas):
            partes.append("\n".join(VINETAS.sub("- ", l, count=1) for l in lineas))
        else:
            partes.append(texto)
    return partes


# --------------------------------------------------------------------------- #
# Candidatas visuales
# --------------------------------------------------------------------------- #
def candidatas_pagina(page, fitz) -> list[dict]:
    n = page.number + 1
    area_pag = abs(page.rect) or 1.0
    hallazgos: list[dict] = []

    # 1. Imágenes embebidas.
    rects = []
    for info in page.get_images(full=True):
        try:
            rects.extend(page.get_image_rects(info[0]))
        except Exception:
            pass
    if rects:
        caja = union(rects)
        hallazgos.append(
            {
                "pagina": n,
                "razon": "imagen_embebida",
                "confianza": 0.9,
                "bbox": redondear(caja if caja else page.rect),
            }
        )

    # 2. Dibujo vectorial denso → diagrama. Ignora rectángulos de fondo.
    # Se cuentan segmentos (`items`), no paths: un círculo es un path pero 4 curvas,
    # y una línea suelta (regla, subrayado) no debe disparar nada.
    trazos = [
        d for d in page.get_drawings()
        if abs(d["rect"]) < area_pag * 0.85
    ]
    segmentos = sum(len(d.get("items", ())) for d in trazos)
    if len(trazos) >= 3 and segmentos >= 12:
        caja = union([d["rect"] for d in trazos])
        hallazgos.append(
            {
                "pagina": n,
                "razon": "diagrama",
                "confianza": round(min(0.95, 0.5 + segmentos / 60), 2),
                "bbox": redondear(caja),
            }
        )

    # 3. Tablas: detector nativo; si no está, grilla de líneas.
    cajas_tabla = []
    try:
        cajas_tabla = [fitz.Rect(t.bbox) for t in page.find_tables().tables]
    except Exception:
        horiz = sum(1 for d in trazos if d["rect"].height < 2 and d["rect"].width > 40)
        vert = sum(1 for d in trazos if d["rect"].width < 2 and d["rect"].height > 20)
        if horiz >= 3 and vert >= 3:
            cajas_tabla = [union([d["rect"] for d in trazos])]
    if cajas_tabla:
        hallazgos.append(
            {
                "pagina": n,
                "razon": "tabla",
                "confianza": 0.8,
                "bbox": redondear(union(cajas_tabla)),
            }
        )

    # 4. Fórmulas: densidad de símbolos matemáticos o fuente matemática.
    total = simbolos = 0
    cajas_formula = []
    for bloque in page.get_text("dict")["blocks"]:
        if bloque.get("type") != 0:
            continue
        marcado = False
        for linea in bloque["lines"]:
            for span in linea["spans"]:
                txt = span["text"]
                total += len(txt)
                hits = sum(1 for c in txt if c in SIMBOLOS_MATE)
                simbolos += hits
                fuente = span.get("font", "").lower()
                if hits or any(f in fuente for f in FUENTES_MATE):
                    marcado = True
        if marcado:
            cajas_formula.append(fitz.Rect(bloque["bbox"]))
    if cajas_formula and total and simbolos / total > 0.008:
        hallazgos.append(
            {
                "pagina": n,
                "razon": "formula",
                "confianza": round(min(0.9, 0.6 + simbolos / max(total, 1) * 6), 2),
                "bbox": redondear(union(cajas_formula)),
            }
        )
    return hallazgos


def titulo_documento(doc, indices, mapa_niveles) -> str:
    meta = (doc.metadata or {}).get("title") or ""
    if meta.strip():
        return meta.strip()
    if not indices:
        return ""
    grandes = [t for t, nivel in mapa_niveles.items() if nivel == 1]
    if grandes:
        for bloque in doc[indices[0]].get_text("dict")["blocks"]:
            if bloque.get("type") != 0:
                continue
            lineas, tam = texto_bloque(bloque)
            if lineas and tam in grandes:
                return unir_lineas(lineas)[:120]
    return Path(doc.name or "").stem


def main() -> int:
    ap = argparse.ArgumentParser(
        prog="pdf_texto.py",
        description="Extrae texto estructurado y candidatas visuales de un PDF.",
    )
    ap.add_argument("pdf", help="ruta al PDF")
    ap.add_argument("--out", default=None, help="directorio de salida (default: .cache/<nombre>)")
    ap.add_argument("--paginas", default=None, help="subconjunto, ej. 1-20 o 3,7,9-11")
    args = ap.parse_args()

    fitz = cargar_fitz()
    ruta = Path(args.pdf)
    if not ruta.is_file():
        error(f"no existe el archivo {ruta}")
    try:
        doc = fitz.open(ruta)
    except Exception as exc:
        error(f"no se pudo abrir {ruta}: {exc}")

    indices = (
        parsear_paginas(args.paginas, doc.page_count)
        if args.paginas
        else list(range(doc.page_count))
    )
    salida = Path(args.out) if args.out else Path(".cache") / ruta.stem
    salida.mkdir(parents=True, exist_ok=True)

    piezas: list[str] = [f"<!-- fuente: {ruta.name} -->"]
    candidatas: list[dict] = []
    caracteres = 0
    # PyMuPDF escribe avisos por stdout; stdout es solo para el JSON del resultado.
    with contextlib.redirect_stdout(sys.stderr):
        cont = histograma_tamanos(doc, indices)
        _, mapa_niveles = niveles_titulo(cont)
        for i in indices:
            page = doc[i]
            piezas.append(f"\n<!-- p.{i + 1} -->")
            bloques = markdown_pagina(page, mapa_niveles)
            caracteres += sum(len(b) for b in bloques)
            piezas.append("\n\n".join(bloques) if bloques else "*(sin texto extraíble)*")
            candidatas.extend(candidatas_pagina(page, fitz))

    (salida / "texto.md").write_text("\n".join(piezas) + "\n", encoding="utf-8")

    # Densidad: caracteres por página contra ~1800 de una página de texto corrido.
    densidad = round(min(1.0, caracteres / max(len(indices), 1) / 1800), 2)
    with contextlib.redirect_stdout(sys.stderr):
        titulo = titulo_documento(doc, indices, mapa_niveles)
    analisis = {
        "archivo": str(ruta),
        "paginas": doc.page_count,
        "paginas_extraidas": [i + 1 for i in indices],
        "titulo_detectado": titulo,
        "candidatas_visuales": sorted(candidatas, key=lambda c: (c["pagina"], c["razon"])),
        "densidad_texto": densidad,
        "probable_escaneado": densidad < 0.03,
    }
    (salida / "analisis.json").write_text(
        json.dumps(analisis, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    doc.close()

    if analisis["probable_escaneado"]:
        print(
            "aviso: densidad de texto ≈ 0. El PDF parece escaneado; hace falta OCR. "
            "No uses texto.md como si fuera la fuente.",
            file=sys.stderr,
        )
    print(json.dumps({**analisis, "out": str(salida)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
