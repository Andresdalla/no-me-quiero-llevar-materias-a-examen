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


# --------------------------------------------------------------------------- #
# Materia y temas
# --------------------------------------------------------------------------- #
TITULO = re.compile(r"^#\s+(.+?)\s*\(`", re.M)
CUATRIMESTRE = re.compile(r"^-\s*cuatrimestre:\s*(\d{4})", re.M)
FECHA_PARCIAL = re.compile(r"^-\s*parcial:.*?\b(\d{1,2})/(\d{1,2})\b", re.M)
UNIDAD_PROGRAMA = re.compile(r"^##\s+(U\d+)\s*·\s*(.+?)\s*$", re.M)
FILA_MAPA = re.compile(r"^\|[^|]*\|[^|]*\|\s*(U\d+)\s*\|", re.M)
FILA_DOMINIO = re.compile(r"^\|\s*(U\d+)[^|]*\|\s*([0-5])\s*\|", re.M)
FILA_HISTORIAL = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(U\d+)\s*\|", re.M)


def _texto(archivo: Path) -> str:
    return archivo.read_text(encoding="utf-8") if archivo.is_file() else ""


def leer_materia(dir_materia: Path, avisos: list[str]) -> dict:
    """Nombre y fecha de parcial desde el CLAUDE.md de la materia.

    La fecha viene como `- parcial: **7/12, …**` (día/mes) y el año sale de
    `- cuatrimestre: 2026-2C`. Si no se puede armar, queda None y el
    encabezado omite la cuenta regresiva en vez de inventar un número.
    """
    texto = _texto(dir_materia / "CLAUDE.md")
    titulo = TITULO.search(texto)
    parcial = None
    fecha, anio = FECHA_PARCIAL.search(texto), CUATRIMESTRE.search(texto)
    if fecha and anio:
        try:
            parcial = date(int(anio.group(1)), int(fecha.group(2)), int(fecha.group(1))).isoformat()
        except ValueError:
            avisos.append(
                f"fecha de parcial ilegible ({fecha.group(1)}/{fecha.group(2)}), "
                "se omite la cuenta regresiva"
            )
    elif texto:
        avisos.append("no se pudo leer `- parcial:` del CLAUDE.md de la materia")
    return {
        "slug": dir_materia.name,
        "nombre": titulo.group(1) if titulo else dir_materia.name,
        "parcial": parcial,
    }


def leer_temas(dir_materia: Path, mazos: dict[str, list[dict]], avisos: list[str]) -> list[dict]:
    """Une programa, mapa, dominio e historial en la lista del sidebar.

    Orden: primero los temas con tarjetas, por dominio ascendente (sin medir
    va primero, porque no hay nada que informar sobre él) y a igual dominio
    el que hace más días que no se toca. Al final, los temas sin tarjetas,
    por número de unidad. No es una cola: es un orden de presentación.
    """
    programa = dict(UNIDAD_PROGRAMA.findall(_texto(dir_materia / "wiki" / "programa.md")))
    paginas: dict[str, int] = {}
    for unidad in FILA_MAPA.findall(_texto(dir_materia / "wiki" / "mapa.md")):
        paginas[unidad] = paginas.get(unidad, 0) + 1
    dominio = {u: int(d) for u, d in FILA_DOMINIO.findall(_texto(dir_materia / "estado" / "dominio.md"))}
    ultimo: dict[str, str] = {}
    for fecha, unidad in FILA_HISTORIAL.findall(_texto(dir_materia / "estado" / "historial.md")):
        if fecha > ultimo.get(unidad, ""):
            ultimo[unidad] = fecha

    ids = sorted(set(programa) | set(paginas) | set(mazos), key=lambda u: int(u[1:]))
    if not ids:
        avisos.append("no se encontró ninguna unidad en programa.md ni en mapa.md")

    temas = [
        {
            "id": u,
            "nombre": programa.get(u, ""),
            "dominio": dominio.get(u),
            "ultimo": ultimo.get(u),
            "tarjetas": len(mazos.get(u, [])),
            "paginas": paginas.get(u, 0),
        }
        for u in ids
    ]
    temas.sort(
        key=lambda t: (
            t["tarjetas"] == 0,
            -1 if t["dominio"] is None else t["dominio"],
            t["ultimo"] or "",
            int(t["id"][1:]),
        )
    )
    return temas


# --------------------------------------------------------------------------- #
# Sesiones horneadas
# --------------------------------------------------------------------------- #
def leer_sesiones(dir_out: Path, avisos: list[str]) -> list[dict]:
    """Sets de preguntas que /profesor y /simulacro dejaron listos.

    Un archivo ilegible o sin `items` se saltea con aviso: una sesión rota no
    puede impedir que el resto de la página se genere.
    """
    sesiones: list[dict] = []
    carpeta = dir_out / ".build" / "sesiones"
    if not carpeta.is_dir():
        return sesiones
    for archivo in sorted(carpeta.glob("*.json")):
        try:
            datos = json.loads(archivo.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError, OSError) as err:
            avisos.append(f"sesiones/{archivo.name}: no se pudo leer ({err}), se salteó")
            continue
        if not isinstance(datos, dict) or not datos.get("items"):
            avisos.append(f"sesiones/{archivo.name}: sin `items`, se salteó")
            continue
        sesiones.append(datos)
    return sesiones


# --------------------------------------------------------------------------- #
# Armado y render
# --------------------------------------------------------------------------- #
def armar_datos(dir_materia: Path) -> dict:
    avisos: list[str] = []
    mazos = leer_mazos(dir_materia / "cards", avisos)
    return {
        "materia": leer_materia(dir_materia, avisos),
        "temas": leer_temas(dir_materia, mazos, avisos),
        "mazos": mazos,
        "sesiones": leer_sesiones(dir_materia / "out", avisos),
        "avisos": avisos,
    }


def render(datos: dict, plantilla: str) -> str:
    """Inyecta el JSON en la plantilla.

    El escape de `</` es lo que impide que una tarjeta con `</script>` adentro
    cierre el bloque antes de tiempo y rompa la página entera.
    """
    bruto = json.dumps(datos, ensure_ascii=False).replace("</", "<\\/")
    return plantilla.replace(MARCADOR, bruto)


def main() -> int:
    ap = argparse.ArgumentParser(description="Genera la página de estudio de una materia.")
    ap.add_argument("materia", help="slug de la materia, p. ej. teoria-de-la-computacion")
    ap.add_argument("--abrir", action="store_true", help="abre el HTML en el navegador")
    args = ap.parse_args()

    dir_materia = RAIZ / "materias" / "activas" / args.materia
    if not dir_materia.is_dir():
        sys.exit(f"error: no existe la materia {args.materia} en materias/activas/")
    if not PLANTILLA.is_file():
        sys.exit(f"error: falta la plantilla {PLANTILLA}")

    datos = armar_datos(dir_materia)
    destino = dir_materia / "out" / "estudio.html"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(
        render(datos, PLANTILLA.read_text(encoding="utf-8")), encoding="utf-8"
    )

    abierto = False
    if args.abrir:
        abierto = webbrowser.open(destino.as_uri())

    for aviso in datos["avisos"]:
        print(f"aviso: {aviso}", file=sys.stderr)
    print(
        json.dumps(
            {
                "html": str(destino),
                "temas": len(datos["temas"]),
                "tarjetas": sum(len(m) for m in datos["mazos"].values()),
                "sesiones": len(datos["sesiones"]),
                "abierto": abierto,
                "avisos": datos["avisos"],
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
