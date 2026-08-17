#!/usr/bin/env python3
"""Genera la página de estudio de una materia: un HTML autocontenido.

Lee cards/, mapa.md, programa.md, estado/ y los sets horneados de
out/.build/sesiones/, y los inyecta como un único bloque JSON dentro de
plantillas/estudio.html. El resultado abre con doble click, sin servidor y
sin conexión.

Degrada con elegancia: una tarjeta malformada se saltea con aviso, un tema sin
tarjetas aparece igual, y una fecha de parcial ilegible solo quita la cuenta
regresiva. Nunca falla entero.

uso: .venv/bin/python scripts/build_estudio.py teoria-de-la-computacion --abrir
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import webbrowser
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PLANTILLA = RAIZ / "plantillas" / "estudio.html"
MARCADOR = "/*__DATOS__*/"

# --------------------------------------------------------------------------- #
# Mazos
# --------------------------------------------------------------------------- #
CABECERA = re.compile(r"^##\s+(c-[\w.-]+)\s+·\s+(\S+)\s*$", re.M)
CAMPO = re.compile(r"^\*\*(P|R|Fuente|Bloom|Confundible_con|Visto):\*\*[ \t]*(.*)$", re.M)


def _lista(bruto: str) -> list[str]:
    """`[c-U6-010, c-U6-011]` → ['c-U6-010', 'c-U6-011']."""
    return [x.strip() for x in bruto.strip("[] \t").split(",") if x.strip()]


def _tarjetas(texto: str, origen: str, avisos: list[str]) -> list[dict]:
    tarjetas: list[dict] = []
    marcas = list(CABECERA.finditer(texto))
    for i, m in enumerate(marcas):
        fin = marcas[i + 1].start() if i + 1 < len(marcas) else len(texto)
        campos = {k: v.strip() for k, v in CAMPO.findall(texto[m.end():fin])}
        ident, tipo = m.group(1), m.group(2)
        if not campos.get("P") or not campos.get("R"):
            avisos.append(f"{origen} · {ident} sin **P:** o **R:**, se salteó")
            continue
        tarjetas.append(
            {
                "id": ident,
                "tipo": tipo,
                "p": campos["P"],
                "r": campos["R"],
                "fuente": campos.get("Fuente", ""),
                "bloom": campos.get("Bloom", ""),
                "confundible": _lista(campos.get("Confundible_con", "")),
                "visto": campos.get("Visto", ""),
            }
        )
    return tarjetas


def leer_mazos(dir_cards: Path, avisos: list[str]) -> dict[str, list[dict]]:
    """cards/*.md → {tema: [tarjeta, …]}. README.md se ignora."""
    mazos: dict[str, list[dict]] = {}
    if not dir_cards.is_dir():
        return mazos
    for archivo in sorted(dir_cards.glob("*.md")):
        if archivo.name == "README.md":
            continue
        mazos[archivo.stem] = _tarjetas(
            archivo.read_text(encoding="utf-8"), f"cards/{archivo.name}", avisos
        )
    return mazos
