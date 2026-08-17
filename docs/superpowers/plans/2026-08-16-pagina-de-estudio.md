# Página de estudio — plan de implementación

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generar `out/estudio.html`, una página autocontenida donde correr sesiones de `/repasar`, `/simulacro` y `/profesor` (modos de set fijo), copiar comandos al portapapeles y exportar dos PDFs.

**Architecture:** Un script Python de stdlib lee `cards/`, `mapa.md`, `estado/` y los sets horneados en `out/.build/sesiones/`, y los inyecta como un único bloque JSON dentro de `plantillas/estudio.html`, que contiene todo el CSS y el JS. El navegador nunca escribe en el repo: su única salida es un bloque de texto que se pega en Claude Code.

**Tech Stack:** Python 3.10+ (stdlib sola: `argparse`, `json`, `re`, `pathlib`, `datetime`, `webbrowser`), `unittest` de stdlib, HTML/CSS/JS sin frameworks ni CDN.

**Spec:** `docs/superpowers/specs/2026-08-16-pagina-de-estudio-design.md`

## Global Constraints

Aplican a todas las tareas.

- **Cero dependencias nuevas.** Ni pip ni npm. Solo stdlib de Python y HTML/CSS/JS a mano.
- **Intérprete:** `.venv/bin/python`. Los tests corren con `.venv/bin/python -m unittest`.
- **El HTML generado no puede tener ninguna referencia externa**: nada de `src="http`, `href="http`, `@import`, `//cdn`, ni fuentes web. Debe abrir offline con doble click.
- **Escala de calificación: `ok` · `parcial` · `fallo`.** Es la que ya escribe `/repasar` en el campo `Visto` de `cards/*.md`. La página no puede inventar otra.
- **Confianza 1-5, pedida siempre antes de revelar la respuesta.** Después de ver la respuesta no mide nada.
- **La página nunca escribe en el repo.** Su única salida es el portapapeles.
- **Sin lenguaje de caducidad, deuda, vencimiento ni racha.** Nada se acumula, nada reclama.
- **Todo el texto de interfaz en castellano rioplatense**, igual que el resto del sistema.
- **`out/` está gitignoreado.** El HTML generado no se commitea nunca.
- **Commits de sistema**, jamás mezclados con `ingest(...)`.
- **Degradación elegante:** ninguna pieza faltante o malformada aborta el build. Se saltea, se anota en `avisos` y el HTML los muestra.

## Design tokens (valores exactos, aprobados en el mockup)

```
--bg:    #f3f4f7      fondo de página
--card:  #ffffff      tarjeta
--ink:   #1e2230      texto principal
--mut:   #6b7280      texto secundario
--line:  #e4e7ee      bordes y separadores
--ind:   #4f46e5      acento (índigo)
--codbg: #eef1f6      fondo de `code`
--codfg: #3730a3      texto de `code`

sombra tarjeta: 0 1px 2px rgba(16,24,40,.05), 0 8px 24px -8px rgba(16,24,40,.14)
radios:  tarjeta 12px · controles 8px · chip 999px
sidebar: 186px
tipografía: system-ui, -apple-system, sans-serif · mono: ui-monospace, Menlo, monospace
```

Chips por tipo de tarjeta (fondo / texto):

```
concepto        #dbeafe / #1e40af
cloze           #ede9fe / #5b21b6
discriminacion  #fef3c7 / #92400e
aplicacion      #dcfce7 / #166534
(cualquier otro) #f1f3f7 / #4b5563
```

## File Structure

| Archivo | Responsabilidad |
|---|---|
| `scripts/build_estudio.py` | Crear. Lee el repo, arma el dict de datos, lo inyecta en la plantilla, escribe `out/estudio.html`. |
| `plantillas/estudio.html` | Crear. Toda la cáscara: CSS, marcado del sidebar y del panel, JS de sesión y de impresión. Ningún dato adentro. |
| `tests/test_build_estudio.py` | Crear. `unittest` sobre el parseo, la degradación y la ausencia de referencias externas. |
| `tests/fixtures/cards-ejemplo.md` | Crear. Mazo chico con una tarjeta completa, una con `Confundible_con` y una malformada. |
| `.claude/commands/estudio.md` | Crear. Comando nuevo: rehornea y abre. |
| `.claude/commands/repasar.md` | Modificar. Flag `--registrar`. |
| `.claude/commands/profesor.md` | Modificar. Flags `--a-la-pagina` y `--registrar`. |
| `.claude/commands/simulacro.md` | Modificar. Flags `--a-la-pagina` y `--registrar`. |
| `CLAUDE.md` | Modificar. "4 scripts Python" → 5, y `/estudio` en la tabla de comandos. |
| `materias/_plantilla/out/.build/sesiones/.gitkeep` | Crear. Que una materia nueva nazca con la carpeta. |

## Nota sobre el testeo del JavaScript

No hay runner de JS en el proyecto y agregarlo violaría la restricción de cero dependencias. Las tareas 6, 7 y 8 se verifican de dos maneras, ambas obligatorias:

1. **Tests de Python sobre invariantes estructurales del HTML generado** — que el panel de respuesta nazca con `hidden`, que existan los cinco botones de confianza, que no haya referencias externas. Esto atrapa las regresiones que importan.
2. **Checklist manual de verificación en el navegador**, escrito paso a paso dentro de cada tarea. Hay que ejecutarlo y reportar el resultado real, no asumirlo.

---

### Task 1: Parseo de los mazos de tarjetas

Convierte `cards/*.md` en dicts. Es la pieza de la que dependen todas las demás.

**Files:**
- Create: `scripts/build_estudio.py`
- Create: `tests/fixtures/cards-ejemplo.md`
- Test: `tests/test_build_estudio.py`

**Interfaces:**
- Consumes: nada.
- Produces:
  - `leer_mazos(dir_cards: Path, avisos: list[str]) -> dict[str, list[dict]]` — clave: nombre del tema (`"U6"`, del stem del archivo); valor: lista de tarjetas.
  - Cada tarjeta: `{"id": str, "tipo": str, "p": str, "r": str, "fuente": str, "bloom": str, "confundible": list[str], "visto": str}`.

- [ ] **Step 1: Crear el fixture**

Crear `tests/fixtures/cards-ejemplo.md` con exactamente este contenido:

```markdown
---
tema: U6
generado: 2026-08-16
---

## c-U6-001 · concepto
**P:** Enunciá el axioma de extensión.
**R:** Dos conjuntos son iguales si y sólo si tienen los mismos elementos.
**Fuente:** revision-conjuntos p.1
**Bloom:** recordar
**Visto:**

## c-U6-002 · concepto
**P:** Escribí la definición formal de inclusión amplia `A ⊆ B`.
**R:** `A ⊆ B ⇔ (∀x ∈ A)(x ∈ B)`
**Fuente:** revision-conjuntos p.2
**Bloom:** recordar
**Confundible_con:** [c-U6-010]
**Visto:** 2026-08-15:fallo

## c-U6-003 · cloze
**P:** Esta tarjeta no tiene respuesta a propósito, para probar el salteo.
**Fuente:** revision-conjuntos p.2
**Bloom:** recordar
**Visto:**
```

- [ ] **Step 2: Escribir los tests que fallan**

Crear `tests/test_build_estudio.py`:

```python
#!/usr/bin/env python3
"""Tests de scripts/build_estudio.py.

uso: .venv/bin/python -m unittest discover -s tests -v
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / "scripts"))

import build_estudio  # noqa: E402

FIXTURES = RAIZ / "tests" / "fixtures"


class TestLeerMazos(unittest.TestCase):
    def setUp(self):
        self.avisos: list[str] = []
        self.mazos = build_estudio.leer_mazos(FIXTURES, self.avisos)

    def test_usa_el_stem_del_archivo_como_tema(self):
        self.assertIn("cards-ejemplo", self.mazos)

    def test_saltea_la_tarjeta_sin_respuesta(self):
        ids = [t["id"] for t in self.mazos["cards-ejemplo"]]
        self.assertEqual(ids, ["c-U6-001", "c-U6-002"])

    def test_la_malformada_deja_aviso_con_su_id(self):
        self.assertEqual(len(self.avisos), 1)
        self.assertIn("c-U6-003", self.avisos[0])

    def test_parsea_la_tarjeta_completa(self):
        t = self.mazos["cards-ejemplo"][0]
        self.assertEqual(t["tipo"], "concepto")
        self.assertEqual(t["p"], "Enunciá el axioma de extensión.")
        self.assertEqual(
            t["r"], "Dos conjuntos son iguales si y sólo si tienen los mismos elementos."
        )
        self.assertEqual(t["fuente"], "revision-conjuntos p.1")
        self.assertEqual(t["bloom"], "recordar")
        self.assertEqual(t["visto"], "")

    def test_confundible_ausente_es_lista_vacia(self):
        self.assertEqual(self.mazos["cards-ejemplo"][0]["confundible"], [])

    def test_confundible_presente_se_parsea_sin_corchetes(self):
        self.assertEqual(self.mazos["cards-ejemplo"][1]["confundible"], ["c-U6-010"])

    def test_conserva_el_visto_existente(self):
        self.assertEqual(self.mazos["cards-ejemplo"][1]["visto"], "2026-08-15:fallo")

    def test_directorio_inexistente_devuelve_vacio(self):
        self.assertEqual(build_estudio.leer_mazos(RAIZ / "no-existe", []), {})


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 3: Correr los tests y verificar que fallan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: FAIL con `ModuleNotFoundError: No module named 'build_estudio'`

- [ ] **Step 4: Escribir el parseo**

Crear `scripts/build_estudio.py`:

```python
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
```

- [ ] **Step 5: Correr los tests y verificar que pasan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: PASS, 8 tests.

- [ ] **Step 6: Commit**

```bash
git add scripts/build_estudio.py tests/test_build_estudio.py tests/fixtures/cards-ejemplo.md
git commit -m "estudio: parseo de los mazos de cards/"
```

---

### Task 2: Datos de la materia y de los temas

Nombre de la materia, fecha de parcial, y la lista de temas con dominio y días sin tocar.

**Files:**
- Modify: `scripts/build_estudio.py`
- Test: `tests/test_build_estudio.py`

**Interfaces:**
- Consumes: `leer_mazos` de Task 1.
- Produces:
  - `leer_materia(dir_materia: Path, avisos: list[str]) -> dict` → `{"slug": str, "nombre": str, "parcial": str | None}`. `parcial` es ISO `"2026-12-07"` o `None`.
  - `leer_temas(dir_materia: Path, mazos: dict, avisos: list[str]) -> list[dict]` → cada tema `{"id": str, "nombre": str, "dominio": int | None, "ultimo": str | None, "tarjetas": int, "paginas": int}`, ya ordenado para el sidebar.

- [ ] **Step 1: Escribir los tests que fallan**

Agregar a `tests/test_build_estudio.py`, antes del `if __name__`:

```python
import tempfile  # arriba, junto a los otros imports


def _materia_temporal(raiz: Path, claude_md: str) -> Path:
    """Arma el esqueleto mínimo de una materia para los tests."""
    m = raiz / "materia-test"
    (m / "wiki").mkdir(parents=True)
    (m / "estado").mkdir()
    (m / "cards").mkdir()
    (m / "CLAUDE.md").write_text(claude_md, encoding="utf-8")
    (m / "wiki" / "programa.md").write_text(
        "# Programa\n\n## U6 · Cardinalidad y numerabilidad\n## U7 · Indecidibilidad\n",
        encoding="utf-8",
    )
    (m / "wiki" / "mapa.md").write_text(
        "| Página | Tipo | Unidad | Qué contiene |\n|---|---|---|---|\n"
        "| `definiciones/conjunto` | definicion | U6 | Pertenencia y extensión |\n"
        "| `teoremas/z-es-numerable` | teorema | U6 | Intercalar pares e impares |\n",
        encoding="utf-8",
    )
    return m


CLAUDE_OK = (
    "# Teoría de la Computación (`teoria-de-la-computacion`)\n\n"
    "- cuatrimestre: 2026-2C (5to semestre) · comisión m5a\n"
    "- parcial: **7/12, 9.00** · 3 horas · **con material** · 60 pts\n"
)


class TestLeerMateria(unittest.TestCase):
    def test_nombre_y_fecha_de_parcial(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = _materia_temporal(Path(tmp), CLAUDE_OK)
            datos = build_estudio.leer_materia(m, [])
            self.assertEqual(datos["nombre"], "Teoría de la Computación")
            self.assertEqual(datos["parcial"], "2026-12-07")
            self.assertEqual(datos["slug"], "materia-test")

    def test_fecha_imposible_no_explota_y_avisa(self):
        malo = CLAUDE_OK.replace("7/12", "31/2")
        with tempfile.TemporaryDirectory() as tmp:
            m = _materia_temporal(Path(tmp), malo)
            avisos: list[str] = []
            datos = build_estudio.leer_materia(m, avisos)
            self.assertIsNone(datos["parcial"])
            self.assertTrue(any("parcial" in a for a in avisos))

    def test_sin_linea_de_parcial_avisa_y_sigue(self):
        sin = "# Materia Test (`materia-test`)\n\n- cuatrimestre: 2026-2C\n"
        with tempfile.TemporaryDirectory() as tmp:
            m = _materia_temporal(Path(tmp), sin)
            avisos: list[str] = []
            self.assertIsNone(build_estudio.leer_materia(m, avisos)["parcial"])
            self.assertTrue(avisos)


class TestLeerTemas(unittest.TestCase):
    def test_dominio_ausente_es_none_nunca_cero(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = _materia_temporal(Path(tmp), CLAUDE_OK)
            (m / "estado" / "dominio.md").write_text(
                "# Dominio\n\n| Tema | Dominio | Última evaluación |\n|---|---|---|\n",
                encoding="utf-8",
            )
            temas = build_estudio.leer_temas(m, {}, [])
            u6 = next(t for t in temas if t["id"] == "U6")
            self.assertIsNone(u6["dominio"])

    def test_lee_dominio_y_cuenta_paginas_y_tarjetas(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = _materia_temporal(Path(tmp), CLAUDE_OK)
            (m / "estado" / "dominio.md").write_text(
                "| Tema | Dominio | Última evaluación |\n|---|---|---|\n"
                "| U6 · Cardinalidad | 3 | 2026-08-15 |\n",
                encoding="utf-8",
            )
            temas = build_estudio.leer_temas(m, {"U6": [{"id": "c-U6-001"}]}, [])
            u6 = next(t for t in temas if t["id"] == "U6")
            self.assertEqual(u6["dominio"], 3)
            self.assertEqual(u6["paginas"], 2)
            self.assertEqual(u6["tarjetas"], 1)
            self.assertEqual(u6["nombre"], "Cardinalidad y numerabilidad")

    def test_los_temas_sin_tarjetas_van_al_final(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = _materia_temporal(Path(tmp), CLAUDE_OK)
            temas = build_estudio.leer_temas(m, {"U6": [{"id": "c-U6-001"}]}, [])
            self.assertEqual([t["id"] for t in temas], ["U6", "U7"])

    def test_ultimo_toque_sale_del_historial(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = _materia_temporal(Path(tmp), CLAUDE_OK)
            (m / "estado" / "historial.md").write_text(
                "| Fecha | Tema | Tipo | Resultado |\n|---|---|---|---|\n"
                "| 2026-08-10 | U6 | repaso | 15 tarjetas |\n"
                "| 2026-08-15 | U6 | repaso | 12 tarjetas |\n",
                encoding="utf-8",
            )
            temas = build_estudio.leer_temas(m, {"U6": []}, [])
            self.assertEqual(next(t for t in temas if t["id"] == "U6")["ultimo"], "2026-08-15")
```

- [ ] **Step 2: Correr y verificar que fallan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: FAIL con `AttributeError: module 'build_estudio' has no attribute 'leer_materia'`

- [ ] **Step 3: Implementar**

Agregar a `scripts/build_estudio.py` después de la sección Mazos:

```python
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
```

- [ ] **Step 4: Correr y verificar que pasan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: PASS, 15 tests.

- [ ] **Step 5: Commit**

```bash
git add scripts/build_estudio.py tests/test_build_estudio.py
git commit -m "estudio: lectura de materia y temas desde programa, mapa y estado"
```

---

### Task 3: Sets de sesión horneados

Levanta los JSON que `/profesor --a-la-pagina` y `/simulacro --a-la-pagina` dejan en `out/.build/sesiones/`.

**Files:**
- Modify: `scripts/build_estudio.py`
- Test: `tests/test_build_estudio.py`

**Interfaces:**
- Consumes: nada de tareas anteriores.
- Produces: `leer_sesiones(dir_out: Path, avisos: list[str]) -> list[dict]`. Cada sesión válida: `{"comando": "profesor"|"simulacro", "modo": str | None, "tema": str, "generado": str, "minutos": int | None, "items": [{"id": str, "enunciado": str, "puntos": int | None}]}`.

- [ ] **Step 1: Escribir los tests que fallan**

Agregar a `tests/test_build_estudio.py`:

```python
SESION_OK = {
    "comando": "simulacro",
    "modo": None,
    "tema": "U6",
    "generado": "2026-08-16",
    "minutos": 90,
    "items": [{"id": "s-01", "enunciado": "Justificá por qué `{1,2,2} = {2,1}`.", "puntos": 10}],
}


class TestLeerSesiones(unittest.TestCase):
    def _dir(self, tmp: str) -> Path:
        d = Path(tmp) / "out" / ".build" / "sesiones"
        d.mkdir(parents=True)
        return d

    def test_sin_carpeta_devuelve_vacio(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(build_estudio.leer_sesiones(Path(tmp) / "out", []), [])

    def test_levanta_una_sesion_valida(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = self._dir(tmp)
            (d / "s1.json").write_text(json.dumps(SESION_OK), encoding="utf-8")
            got = build_estudio.leer_sesiones(Path(tmp) / "out", [])
            self.assertEqual(len(got), 1)
            self.assertEqual(got[0]["tema"], "U6")
            self.assertEqual(got[0]["items"][0]["puntos"], 10)

    def test_json_roto_se_saltea_con_aviso(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = self._dir(tmp)
            (d / "roto.json").write_text("{no es json", encoding="utf-8")
            (d / "s1.json").write_text(json.dumps(SESION_OK), encoding="utf-8")
            avisos: list[str] = []
            got = build_estudio.leer_sesiones(Path(tmp) / "out", avisos)
            self.assertEqual(len(got), 1)
            self.assertTrue(any("roto.json" in a for a in avisos))

    def test_sesion_sin_items_se_saltea(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = self._dir(tmp)
            vacia = dict(SESION_OK, items=[])
            (d / "vacia.json").write_text(json.dumps(vacia), encoding="utf-8")
            avisos: list[str] = []
            self.assertEqual(build_estudio.leer_sesiones(Path(tmp) / "out", avisos), [])
            self.assertTrue(any("vacia.json" in a for a in avisos))
```

Agregar `import json` arriba del archivo de tests.

- [ ] **Step 2: Correr y verificar que fallan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: FAIL con `AttributeError: … has no attribute 'leer_sesiones'`

- [ ] **Step 3: Implementar**

Agregar a `scripts/build_estudio.py`:

```python
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
        except (json.JSONDecodeError, UnicodeDecodeError) as err:
            avisos.append(f"sesiones/{archivo.name}: no se pudo leer ({err}), se salteó")
            continue
        if not isinstance(datos, dict) or not datos.get("items"):
            avisos.append(f"sesiones/{archivo.name}: sin `items`, se salteó")
            continue
        sesiones.append(datos)
    return sesiones
```

- [ ] **Step 4: Correr y verificar que pasan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: PASS, 19 tests.

- [ ] **Step 5: Commit**

```bash
git add scripts/build_estudio.py tests/test_build_estudio.py
git commit -m "estudio: lectura de los sets horneados de sesión"
```

---

### Task 4: La cáscara HTML — estética y layout

La plantilla con todo el CSS, el sidebar fijo de 186 px y el panel derecho. Sin JS de sesión todavía: solo la estructura y el marcador de datos.

**Files:**
- Create: `plantillas/estudio.html`

**Interfaces:**
- Consumes: nada.
- Produces: un archivo con el marcador literal `/*__DATOS__*/` dentro de `<script id="datos" type="application/json">`, y los ids que el JS de las tareas 6 y 7 va a buscar: `#sidebar`, `#temas`, `#comandos`, `#panel`, `#avisos`.

- [ ] **Step 1: Escribir la plantilla**

Crear `plantillas/estudio.html`:

```html
<!doctype html>
<html lang="es-AR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Estudio</title>
<style>
:root{
  --bg:#f3f4f7; --card:#fff; --ink:#1e2230; --mut:#6b7280; --line:#e4e7ee;
  --ind:#4f46e5; --codbg:#eef1f6; --codfg:#3730a3;
  --sombra:0 1px 2px rgba(16,24,40,.05), 0 8px 24px -8px rgba(16,24,40,.14);
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font-family:system-ui,-apple-system,sans-serif;font-size:15px;line-height:1.5}
code{font-family:ui-monospace,Menlo,monospace;background:var(--codbg);color:var(--codfg);
  padding:2px 6px;border-radius:5px;font-size:.87em}

/* ---- estructura ---- */
#app{display:grid;grid-template-columns:186px 1fr;min-height:100vh}
body.sesion #app{grid-template-columns:0 1fr}
body.sesion #sidebar{overflow:hidden;padding:0;border-right:0}
#sidebar{background:var(--card);border-right:1px solid var(--line);padding:16px 12px;
  transition:padding .18s ease}
#contenido{padding:26px 28px 60px;max-width:760px;margin:0 auto;width:100%}

/* ---- sidebar ---- */
.marca{font-weight:650;letter-spacing:-.01em;font-size:14px;margin-bottom:2px}
.cuenta{font-size:12px;color:var(--mut);margin-bottom:18px}
.kick{font-size:11px;text-transform:uppercase;letter-spacing:.07em;color:var(--mut);
  margin:0 0 8px}
.rl{display:flex;justify-content:space-between;gap:8px;font-size:12.5px;padding:6px 9px;
  border-radius:7px;color:#374151;cursor:pointer;border:0;background:none;width:100%;
  text-align:left;font-family:inherit}
.rl:hover{background:#f6f7fb}
.rl.on{background:#eef0fe;color:var(--ind);font-weight:600}
.rl.mudo{color:var(--mut);cursor:default}
.rl .n{opacity:.6;font-variant-numeric:tabular-nums}

/* ---- tarjeta ---- */
.tarjeta{background:var(--card);border-radius:12px;padding:24px 26px;box-shadow:var(--sombra)}
.cab{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}
.contador{font-size:12.5px;color:var(--mut);font-variant-numeric:tabular-nums}
.pregunta{font-size:19px;line-height:1.55;font-weight:500;margin:0 0 20px}
.respuesta{border-top:1px solid var(--line);padding-top:16px;margin-top:4px;font-size:16px}
.fuente{font-size:12.5px;color:var(--mut);margin-top:16px}

/* ---- chips de tipo ---- */
.chip{padding:3px 10px;border-radius:999px;font-size:11.5px;font-weight:600;
  background:#f1f3f7;color:#4b5563}
.chip[data-tipo=concepto]{background:#dbeafe;color:#1e40af}
.chip[data-tipo=cloze]{background:#ede9fe;color:#5b21b6}
.chip[data-tipo=discriminacion]{background:#fef3c7;color:#92400e}
.chip[data-tipo=aplicacion]{background:#dcfce7;color:#166534}

/* ---- controles ---- */
.etiqueta{font-size:12.5px;color:var(--mut);margin-bottom:8px}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:8px;overflow:hidden;
  background:var(--card)}
.seg button{padding:8px 17px;font-size:14px;color:var(--mut);border:0;
  border-right:1px solid var(--line);background:none;cursor:pointer;font-family:inherit}
.seg button:last-child{border-right:0}
.seg button:hover{background:#f6f7fb}
.seg button.on{background:var(--ind);color:#fff}
.btn{border:1px solid var(--line);border-radius:8px;padding:9px 16px;font-size:14px;
  background:var(--card);color:var(--ink);cursor:pointer;font-family:inherit}
.btn:hover{background:#f6f7fb}
.btn.p{background:var(--ind);border-color:var(--ind);color:#fff}
.btn.p:hover{filter:brightness(1.08)}
.acciones{display:flex;gap:8px;margin-top:20px;flex-wrap:wrap}

/* ---- avisos ---- */
#avisos{background:#fffbeb;border:1px solid #fde68a;color:#92400e;border-radius:10px;
  padding:12px 14px;font-size:13px;margin-bottom:20px}
#avisos ul{margin:6px 0 0;padding-left:18px}
#avisos:empty{display:none}
</style>
</head>
<body>
<div id="app">
  <aside id="sidebar">
    <div class="marca" id="marca"></div>
    <div class="cuenta" id="cuenta"></div>
    <p class="kick">Temas</p>
    <div id="temas"></div>
    <p class="kick" style="margin-top:18px">Comandos</p>
    <div id="comandos"></div>
  </aside>
  <main id="contenido">
    <div id="avisos"></div>
    <div id="panel"></div>
  </main>
</div>

<script id="datos" type="application/json">/*__DATOS__*/</script>
<script>
const DATOS = JSON.parse(document.getElementById('datos').textContent);
</script>
</body>
</html>
```

- [ ] **Step 2: Escribir el test de la plantilla**

Agregar a `tests/test_build_estudio.py`:

```python
# Solo contextos de carga: que una tarjeta mencione una URL en su texto no es
# una referencia externa, pero un src/href/@import/url() sí lo es.
SIN_EXTERNOS = re.compile(r'src="\s*http|href="\s*http|@import|url\(\s*[\'"]?http|//cdn')


class TestPlantilla(unittest.TestCase):
    def setUp(self):
        self.html = (RAIZ / "plantillas" / "estudio.html").read_text(encoding="utf-8")

    def test_tiene_el_marcador_de_datos(self):
        self.assertIn("/*__DATOS__*/", self.html)

    def test_no_tiene_referencias_externas(self):
        hallado = SIN_EXTERNOS.search(self.html)
        self.assertIsNone(hallado, f"referencia externa: {hallado.group(0) if hallado else ''}")

    def test_tiene_los_anclajes_que_busca_el_js(self):
        for ancla in ("id=\"temas\"", "id=\"comandos\"", "id=\"panel\"", "id=\"avisos\""):
            self.assertIn(ancla, self.html)
```

Agregar `import re` arriba del archivo de tests.

- [ ] **Step 3: Correr y verificar que pasan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: PASS, 22 tests.

- [ ] **Step 4: Commit**

```bash
git add plantillas/estudio.html tests/test_build_estudio.py
git commit -m "estudio: cáscara HTML con la estética de fichas y sidebar fijo"
```

---

### Task 5: Render, CLI y build de punta a punta

Junta todo: inyecta el JSON en la plantilla y escribe `out/estudio.html`.

**Files:**
- Modify: `scripts/build_estudio.py`
- Test: `tests/test_build_estudio.py`

**Interfaces:**
- Consumes: `leer_mazos`, `leer_materia`, `leer_temas`, `leer_sesiones`.
- Produces:
  - `armar_datos(dir_materia: Path) -> dict` → `{"materia":…, "temas":[…], "mazos":{…}, "sesiones":[…], "avisos":[…]}`.
  - `render(datos: dict, plantilla: str) -> str`.
  - `main() -> int`, CLI `build_estudio.py <materia> [--abrir]`.

- [ ] **Step 1: Escribir los tests que fallan**

Agregar a `tests/test_build_estudio.py`:

```python
class TestRender(unittest.TestCase):
    def test_reemplaza_el_marcador_por_el_json(self):
        html = build_estudio.render({"a": 1}, "antes /*__DATOS__*/ después")
        self.assertIn('{"a": 1}', html)
        self.assertNotIn("/*__DATOS__*/", html)

    def test_escapa_cierres_de_script_del_contenido(self):
        """Una tarjeta que contenga </script> no puede romper la página."""
        html = build_estudio.render({"p": "mirá esto: </script><b>"}, "/*__DATOS__*/")
        self.assertNotIn("</script>", html)
        self.assertIn("<\\/script>", html)


class TestArmarDatos(unittest.TestCase):
    def test_integra_todo_y_no_deja_referencias_externas(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = _materia_temporal(Path(tmp), CLAUDE_OK)
            (m / "cards" / "U6.md").write_text(
                (FIXTURES / "cards-ejemplo.md").read_text(encoding="utf-8"), encoding="utf-8"
            )
            datos = build_estudio.armar_datos(m)
            self.assertEqual(datos["materia"]["parcial"], "2026-12-07")
            self.assertEqual(len(datos["mazos"]["U6"]), 2)
            self.assertEqual(datos["temas"][0]["id"], "U6")
            self.assertTrue(datos["avisos"])

            plantilla = (RAIZ / "plantillas" / "estudio.html").read_text(encoding="utf-8")
            html = build_estudio.render(datos, plantilla)
            hallado = SIN_EXTERNOS.search(html)
            self.assertIsNone(hallado, f"referencia externa: {hallado.group(0) if hallado else ''}")
            self.assertIn("axioma de extensión", html)
```

- [ ] **Step 2: Correr y verificar que fallan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: FAIL con `AttributeError: … has no attribute 'render'`

- [ ] **Step 3: Implementar**

Agregar al final de `scripts/build_estudio.py`, antes del `if __name__`:

```python
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
```

- [ ] **Step 4: Correr y verificar que pasan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: PASS, 25 tests.

- [ ] **Step 5: Probarlo contra la materia real**

Run: `.venv/bin/python scripts/build_estudio.py teoria-de-la-computacion`
Expected: JSON con `"temas": 10`, `"tarjetas"` mayor a 0, y `out/estudio.html` escrito. Confirmá que `git status` **no** lo lista (está gitignoreado).

- [ ] **Step 6: Commit**

```bash
git add scripts/build_estudio.py tests/test_build_estudio.py
git commit -m "estudio: render, CLI y build de punta a punta"
```

---

### Task 6: La sesión de repaso en el navegador

Sidebar poblado, mazo, confianza antes de revelar, calificación de tres niveles, y el bloque para el portapapeles.

**Files:**
- Modify: `plantillas/estudio.html`
- Test: `tests/test_build_estudio.py`

**Interfaces:**
- Consumes: `DATOS` de Task 4.
- Produces: funciones globales `pintarSidebar()`, `abrirRepaso(tema)`, `copiar(texto, boton)`; la clase `body.sesion` que colapsa el sidebar.

- [ ] **Step 1: Escribir el JS**

Reemplazar el bloque `<script>` final de `plantillas/estudio.html` por:

```html
<script>
const DATOS = JSON.parse(document.getElementById('datos').textContent);
const $ = (id) => document.getElementById(id);
const esc = (s) => String(s ?? '').replace(/[&<>]/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
const hoy = () => new Date().toISOString().slice(0, 10);

/* `código entre backticks` → <code>, que es lo único que el markdown de las
   tarjetas usa de verdad. No se interpreta nada más: el resto va escapado. */
const marcar = (s) => esc(s).replace(/`([^`]+)`/g, '<code>$1</code>');

/* ---------------- sidebar ---------------- */
function pintarSidebar() {
  $('marca').textContent = DATOS.materia.nombre;
  if (DATOS.materia.parcial) {
    const dias = Math.round((new Date(DATOS.materia.parcial) - new Date(hoy())) / 86400000);
    $('cuenta').textContent = dias >= 0 ? `parcial en ${dias} días` : 'parcial ya rendido';
  }

  $('temas').innerHTML = DATOS.temas.map((t) => {
    const dom = t.dominio === null ? '—' : `${t.dominio}/5`;
    if (!t.tarjetas) {
      return `<div class="rl mudo" title="sin tarjetas todavía">
        <span>${esc(t.id)}</span><span class="n">—</span></div>`;
    }
    return `<button class="rl" data-tema="${esc(t.id)}" onclick="abrirRepaso('${esc(t.id)}')">
      <span>${esc(t.id)} · dominio ${dom}</span><span class="n">${t.tarjetas}</span></button>`;
  }).join('');

  const tema = (DATOS.temas.find((t) => t.tarjetas) || {}).id || '';
  const slug = DATOS.materia.slug;
  const cmds = [
    `/repasar ${tema} --materia ${slug}`,
    `/profesor ${tema} hueco`,
    `/simulacro ${slug} --unidades ${tema}`,
    `/machete ${tema}`,
    `/estado ${slug}`,
  ];
  $('comandos').innerHTML = cmds.map((c) =>
    `<button class="rl mudo" style="cursor:pointer"
       onclick="copiar(${JSON.stringify(c)}, this)">${esc(c.split(' ')[0])}</button>`
  ).join('');

  $('avisos').innerHTML = DATOS.avisos.length
    ? `<strong>Al generar esta página:</strong><ul>${
        DATOS.avisos.map((a) => `<li>${esc(a)}</li>`).join('')}</ul>`
    : '';
}

/* ---------------- portapapeles ---------------- */
function copiar(texto, boton) {
  navigator.clipboard.writeText(texto).then(() => {
    const antes = boton.textContent;
    boton.textContent = 'copiado ✓';
    setTimeout(() => { boton.textContent = antes; }, 1400);
  });
}

/* ---------------- orden del mazo ---------------- */
/* Intercala solo los grupos ligados por Confundible_con. Fuera de esos grupos
   no se mezcla: el intercalado sirve cuando los ítems compiten entre sí. */
function ordenar(mazo) {
  const porId = new Map(mazo.map((t) => [t.id, t]));
  const usadas = new Set();
  const grupos = [];
  for (const t of mazo) {
    if (usadas.has(t.id)) continue;
    const grupo = [t];
    usadas.add(t.id);
    for (const id of t.confundible) {
      const otra = porId.get(id);
      if (otra && !usadas.has(otra.id)) { grupo.push(otra); usadas.add(otra.id); }
    }
    grupos.push(grupo);
  }
  /* Una tarjeta de cada grupo por ronda: los confundibles quedan separados por
     el resto de los grupos, ni pegados ni lejísimos. */
  const salida = [];
  const largo = grupos.reduce((m, g) => Math.max(m, g.length), 0);
  for (let ronda = 0; ronda < largo; ronda++) {
    for (const g of grupos) if (g[ronda]) salida.push(g[ronda]);
  }
  return salida;
}

/* ---------------- sesión de repaso ---------------- */
let sesion = null;

function abrirRepaso(tema) {
  sesion = { tema, cola: ordenar(DATOS.mazos[tema] || []), i: 0, conf: null, res: [] };
  document.body.classList.add('sesion');
  pintarTarjeta();
}

function pintarTarjeta() {
  const t = sesion.cola[sesion.i];
  if (!t) return pintarCierre();
  $('panel').innerHTML = `
    <div class="tarjeta">
      <div class="cab">
        <span class="chip" data-tipo="${esc(t.tipo)}">${esc(t.tipo)}</span>
        <span class="contador">${sesion.i + 1} de ${sesion.cola.length} · ${esc(sesion.tema)}</span>
      </div>
      <p class="pregunta">${marcar(t.p)}</p>
      <div id="paso-conf">
        <div class="etiqueta">Confianza antes de revelar</div>
        <div class="seg" id="conf">
          ${[1,2,3,4,5].map((n) => `<button onclick="elegirConf(${n},this)">${n}</button>`).join('')}
        </div>
      </div>
      <div id="paso-resp" hidden>
        <div class="respuesta">${marcar(t.r)}</div>
        <div class="fuente">${esc(t.fuente)}</div>
        <div class="acciones">
          <button class="btn p" onclick="calificar('ok')">Lo sabía</button>
          <button class="btn" onclick="calificar('parcial')">A medias</button>
          <button class="btn" onclick="calificar('fallo')">No lo sabía</button>
        </div>
      </div>
    </div>`;
}

function elegirConf(n, boton) {
  sesion.conf = n;
  [...boton.parentElement.children].forEach((b) => b.classList.remove('on'));
  boton.classList.add('on');
  $('paso-conf').hidden = true;
  $('paso-resp').hidden = false;
}

function calificar(resultado) {
  sesion.res.push({ id: sesion.cola[sesion.i].id, conf: sesion.conf, resultado });
  sesion.i += 1;
  sesion.conf = null;
  pintarTarjeta();
}

function pintarCierre() {
  const cuenta = (r) => sesion.res.filter((x) => x.resultado === r).length;
  const bloque = [`/repasar --registrar ${sesion.tema} ${hoy()}`]
    .concat(sesion.res.map((r) => `${r.id} conf:${r.conf} ${r.resultado}`))
    .join('\n');
  $('panel').innerHTML = `
    <div class="tarjeta">
      <div class="cab">
        <span class="chip">sesión terminada</span>
        <span class="contador">${sesion.res.length} tarjetas · ${esc(sesion.tema)}</span>
      </div>
      <p class="pregunta">${cuenta('ok')} ok · ${cuenta('parcial')} parcial · ${cuenta('fallo')} fallo</p>
      <div class="etiqueta">Pegá esto en Claude Code para que quede registrado.</div>
      <div class="acciones">
        <button class="btn p" onclick="copiar(${JSON.stringify(bloque)}, this)">Copiar resultado</button>
        <button class="btn" onclick="salir()">Volver</button>
      </div>
    </div>`;
}

function salir() {
  document.body.classList.remove('sesion');
  sesion = null;
  $('panel').innerHTML = '';
}

pintarSidebar();
</script>
```

- [ ] **Step 2: Agregar los tests de invariantes**

Agregar a `tests/test_build_estudio.py`, dentro de `TestPlantilla`:

```python
    def test_la_respuesta_nace_oculta(self):
        """La confianza se pide antes de revelar; si el panel no nace hidden, no se cumple."""
        self.assertIn('id="paso-resp" hidden', self.html)

    def test_ofrece_los_cinco_niveles_de_confianza(self):
        self.assertIn("[1,2,3,4,5].map", self.html)

    def test_usa_la_escala_de_tres_niveles(self):
        for grado in ("'ok'", "'parcial'", "'fallo'"):
            self.assertIn(f"calificar({grado})", self.html)

    def test_el_sidebar_se_colapsa_en_sesion(self):
        self.assertIn("body.sesion #app", self.html)
        self.assertIn("classList.add('sesion')", self.html)
```

- [ ] **Step 3: Correr y verificar que pasan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: PASS, 29 tests.

- [ ] **Step 4: Verificación manual en el navegador**

```bash
.venv/bin/python scripts/build_estudio.py teoria-de-la-computacion --abrir
```

Recorré esta lista y reportá el resultado real de cada punto:

1. El sidebar muestra la materia, la cuenta de días al parcial, U6 y U10 clickeables con su cantidad de tarjetas, y las unidades sin tarjetas en gris sin poder clickearse.
2. Al entrar a U6 el sidebar se colapsa y queda solo la tarjeta.
3. La respuesta **no** se ve hasta elegir confianza. Elegir un número la revela.
4. Los tres botones de calificación avanzan a la tarjeta siguiente.
5. Las tarjetas ligadas por `Confundible_con` no salen pegadas una atrás de la otra.
6. Al terminar, "Copiar resultado" copia un bloque cuya primera línea es `/repasar --registrar U6 <fecha de hoy>` y después una línea por tarjeta con `conf:N` y `ok|parcial|fallo`.
7. Click en un comando del sidebar lo copia y el botón dice "copiado ✓".
8. Desconectá el wifi, recargá la página: funciona igual.

- [ ] **Step 5: Commit**

```bash
git add plantillas/estudio.html tests/test_build_estudio.py
git commit -m "estudio: sesión de repaso, confianza antes de revelar y copiado"
```

---

### Task 7: Sesiones horneadas — profesor y simulacro

Los sets de preguntas con respuesta libre, cronómetro para simulacro, y su bloque de portapapeles.

**Files:**
- Modify: `plantillas/estudio.html`
- Test: `tests/test_build_estudio.py`

**Interfaces:**
- Consumes: `DATOS.sesiones`, `copiar()`, `esc()`, `marcar()`, `hoy()` de Task 6.
- Produces: `abrirSesion(indice)`, y las entradas de `DATOS.sesiones` listadas en el sidebar bajo el encabezado "Sesiones listas".

- [ ] **Step 1: Escribir el JS**

Agregar a `plantillas/estudio.html`, dentro del `<script>`, antes de la llamada final a `pintarSidebar()`:

```javascript
/* ---------------- sesiones horneadas ---------------- */
let horneada = null;

function pintarHorneadas() {
  if (!DATOS.sesiones.length) return;
  const bloque = document.createElement('div');
  bloque.innerHTML = `<p class="kick" style="margin-top:18px">Sesiones listas</p>` +
    DATOS.sesiones.map((s, i) => {
      const etiqueta = s.comando === 'simulacro'
        ? `simulacro ${esc(s.tema)}`
        : `profesor ${esc(s.modo || '')} ${esc(s.tema)}`;
      return `<button class="rl" onclick="abrirSesion(${i})">
        <span>${etiqueta}</span><span class="n">${s.items.length}</span></button>`;
    }).join('');
  $('sidebar').appendChild(bloque);
}

function abrirSesion(indice) {
  const s = DATOS.sesiones[indice];
  horneada = { s, respuestas: s.items.map(() => ({ conf: null, texto: '' })), inicio: Date.now() };
  document.body.classList.add('sesion');
  pintarHorneada();
}

function pintarHorneada() {
  const { s } = horneada;
  const titulo = s.comando === 'simulacro'
    ? `Simulacro · ${esc(s.tema)}`
    : `Profesor · ${esc(s.modo || '')} · ${esc(s.tema)}`;
  const tiempo = s.minutos ? `${s.minutos} min · sin apuntes` : '';
  $('panel').innerHTML = `
    <div class="tarjeta" style="margin-bottom:16px">
      <div class="cab">
        <span class="chip" data-tipo="aplicacion">${titulo}</span>
        <span class="contador" id="reloj">${esc(tiempo)}</span>
      </div>
      <div class="etiqueta">Escribí cada respuesta y declará la confianza antes de pasar a la
        siguiente. La corrección se hace después, en la terminal, con la rúbrica de la cátedra.</div>
    </div>
    ${s.items.map((it, i) => `
      <div class="tarjeta" style="margin-bottom:14px">
        <div class="cab">
          <span class="chip">${esc(it.id)}</span>
          <span class="contador">${it.puntos ? it.puntos + ' pts' : ''}</span>
        </div>
        <p class="pregunta">${marcar(it.enunciado)}</p>
        <textarea id="r${i}" rows="5" style="width:100%;border:1px solid var(--line);
          border-radius:8px;padding:11px;font:inherit;resize:vertical"
          oninput="horneada.respuestas[${i}].texto = this.value"></textarea>
        <div class="etiqueta" style="margin-top:12px">Confianza</div>
        <div class="seg">
          ${[1,2,3,4,5].map((n) =>
            `<button onclick="confItem(${i},${n},this)">${n}</button>`).join('')}
        </div>
      </div>`).join('')}
    <div class="acciones">
      <button class="btn p" onclick="cerrarHorneada(this)">Copiar respuestas</button>
      <button class="btn" onclick="window.print()" data-print="parte">Imprimir</button>
      <button class="btn" onclick="salirHorneada()">Volver</button>
    </div>`;
  if (s.minutos) arrancarReloj(s.minutos);
}

function confItem(i, n, boton) {
  horneada.respuestas[i].conf = n;
  [...boton.parentElement.children].forEach((b) => b.classList.remove('on'));
  boton.classList.add('on');
}

/* El reloj informa, no interrumpe: nunca corta la sesión ni bloquea nada. */
function arrancarReloj(minutos) {
  const fin = Date.now() + minutos * 60000;
  const tic = () => {
    if (!horneada) return;
    const resta = Math.max(0, Math.round((fin - Date.now()) / 60000));
    const reloj = $('reloj');
    if (reloj) reloj.textContent = resta ? `quedan ${resta} min` : 'tiempo cumplido';
    if (resta) setTimeout(tic, 15000);
  };
  tic();
}

function cerrarHorneada(boton) {
  const { s } = horneada;
  const min = Math.round((Date.now() - horneada.inicio) / 60000);
  const cab = s.comando === 'simulacro'
    ? `/simulacro --registrar ${s.tema} ${hoy()} ${min}min`
    : `/profesor --registrar ${s.tema} ${s.modo} ${hoy()} ${min}min`;
  const cuerpo = s.items.map((it, i) => {
    const r = horneada.respuestas[i];
    return `## ${it.id} conf:${r.conf ?? '-'}\n${r.texto.trim() || '(sin responder)'}`;
  });
  copiar([cab, ...cuerpo].join('\n'), boton);
}

function salirHorneada() {
  document.body.classList.remove('sesion');
  horneada = null;
  $('panel').innerHTML = '';
}
```

Y cambiar la última línea del script de `pintarSidebar();` a:

```javascript
pintarSidebar();
pintarHorneadas();
```

- [ ] **Step 2: Agregar los tests de invariantes**

Agregar a `TestPlantilla` en `tests/test_build_estudio.py`:

```python
    def test_los_items_horneados_piden_confianza(self):
        self.assertIn("confItem(", self.html)

    def test_el_bloque_de_registro_usa_el_prefijo_de_item(self):
        self.assertIn("## ${it.id} conf:", self.html)

    def test_el_reloj_no_corta_la_sesion(self):
        """El cronómetro informa; nada en el código debe cerrar ni bloquear al vencer."""
        self.assertIn("tiempo cumplido", self.html)
        self.assertNotIn("salirHorneada()", self.html.split("function arrancarReloj")[1].split("function cerrarHorneada")[0])
```

- [ ] **Step 3: Correr y verificar que pasan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: PASS, 32 tests.

- [ ] **Step 4: Verificación manual con una sesión de prueba**

```bash
mkdir -p materias/activas/teoria-de-la-computacion/out/.build/sesiones
cat > materias/activas/teoria-de-la-computacion/out/.build/sesiones/prueba.json <<'JSON'
{"comando":"simulacro","modo":null,"tema":"U6","generado":"2026-08-16","minutos":90,
 "items":[{"id":"s-01","enunciado":"Justificá por qué `{1, 2, 2} = {2, 1}`.","puntos":10},
          {"id":"s-02","enunciado":"¿Por qué `{{1,2}} ⊆ {1,2}` es falso?","puntos":15}]}
JSON
.venv/bin/python scripts/build_estudio.py teoria-de-la-computacion --abrir
```

Verificá y reportá:

1. El sidebar muestra "Sesiones listas" con `simulacro U6` y el número 2.
2. Al abrirla aparecen los dos enunciados con su puntaje y un textarea cada uno.
3. El reloj arranca en `quedan 90 min` y baja. Al llegar a cero dice "tiempo cumplido" y **no pasa nada más**: no se cierra, no bloquea.
4. "Copiar respuestas" copia un bloque que empieza con `/simulacro --registrar U6 <hoy> <N>min` y tiene `## s-01 conf:N` con el texto debajo.
5. Un ítem sin responder sale como `(sin responder)` y su confianza como `conf:-`.
6. Borrá el JSON de prueba y rehorneá: el encabezado "Sesiones listas" desaparece sin errores en la consola.

```bash
rm materias/activas/teoria-de-la-computacion/out/.build/sesiones/prueba.json
```

- [ ] **Step 5: Commit**

```bash
git add plantillas/estudio.html tests/test_build_estudio.py
git commit -m "estudio: sesiones horneadas de profesor y simulacro con cronómetro"
```

---

### Task 8: Impresión — simulacro en blanco y parte de la sesión

Los dos PDF, vía `window.print()` y una hoja `@media print`.

**Files:**
- Modify: `plantillas/estudio.html`
- Test: `tests/test_build_estudio.py`

**Interfaces:**
- Consumes: `horneada`, `sesion`, `esc()`, `marcar()` de las tareas 6 y 7.
- Produces: `imprimir(modo)` con `modo` en `"simulacro"` o `"parte"`; el atributo `data-print` en `<html>`; el contenedor `#impresion`.

- [ ] **Step 1: Agregar el CSS de impresión**

Agregar al final del `<style>` de `plantillas/estudio.html`:

```css
/* ---- impresión ---- */
#impresion{display:none}
@media print{
  @page{margin:18mm 16mm}
  body{background:#fff;font-size:11pt}
  #sidebar,.acciones,.seg,#avisos,.btn{display:none !important}
  #app{display:block}
  #contenido{max-width:none;padding:0;margin:0}
  #panel{display:none}
  #impresion{display:block;color:#141414}
  .tarjeta{box-shadow:none;border:0;padding:0}
  code{background:#f1f1f3;color:#141414}
  .hoja h1{font-size:15pt;margin:0 0 2mm;border-bottom:1.5pt solid #141414;padding-bottom:2mm}
  .hoja .sub{font-size:9pt;color:#555;margin-bottom:6mm;display:flex;justify-content:space-between}
  .hoja .item{break-inside:avoid;margin-bottom:7mm}
  .hoja .item h2{font-size:11pt;margin:0 0 1.5mm}
  .hoja .renglon{border-bottom:.4pt solid #b9b9bf;height:8mm}
  .hoja table{width:100%;border-collapse:collapse;font-size:9.5pt}
  .hoja th{text-align:left;border-bottom:1pt solid #141414;padding:2mm 1mm;font-size:8.5pt;
    text-transform:uppercase;letter-spacing:.05em}
  .hoja td{border-bottom:.4pt solid #dcdce2;padding:2mm 1mm}
  .hoja .pie{border-top:.4pt solid #b9b9bf;margin-top:5mm;padding-top:2mm;font-size:8.5pt;color:#555}
}
```

Y agregar `<div id="impresion"></div>` dentro de `<main id="contenido">`, después de `<div id="panel"></div>`.

- [ ] **Step 2: Agregar el JS de impresión**

Agregar al `<script>`, antes de las llamadas finales:

```javascript
/* ---------------- impresión ---------------- */
/* Dos salidas distintas del mismo HTML. `data-print` en <html> decide cuál se
   muestra, y el title fija el nombre de archivo que propone el navegador. */
function imprimir(modo) {
  const titulo = document.title;
  document.documentElement.setAttribute('data-print', modo);
  $('impresion').innerHTML = modo === 'simulacro' ? hojaSimulacro() : hojaParte();
  document.title = modo === 'simulacro'
    ? `simulacro-${horneada.s.tema}-${hoy()}`
    : `sesion-${sesion.tema}-${hoy()}`;
  window.print();
  document.title = titulo;
  document.documentElement.removeAttribute('data-print');
}

function hojaSimulacro() {
  const { s } = horneada;
  return `<div class="hoja">
    <h1>Simulacro · ${esc(s.tema)}</h1>
    <div class="sub"><span>${s.minutos ? s.minutos + ' minutos · sin apuntes' : 'sin apuntes'}</span>
      <span>Nombre: ______________________</span></div>
    ${s.items.map((it, i) => `<div class="item">
      <h2>${i + 1}. ${it.puntos ? '(' + it.puntos + ' pts)' : ''}</h2>
      <div>${marcar(it.enunciado)}</div>
      ${'<div class="renglon"></div>'.repeat(it.puntos && it.puntos > 12 ? 6 : 4)}
    </div>`).join('')}
    <div class="pie">${esc(DATOS.materia.nombre)} · generado ${hoy()}</div>
  </div>`;
}

function hojaParte() {
  const r = sesion ? sesion.res : [];
  const brecha = (x) => x.conf - (x.resultado === 'ok' ? 5 : x.resultado === 'parcial' ? 3 : 0);
  const orden = [...r].sort((a, b) => brecha(b) - brecha(a));
  const media = r.length ? (r.reduce((s, x) => s + brecha(x), 0) / r.length).toFixed(1) : '0';
  const cuenta = (g) => r.filter((x) => x.resultado === g).length;
  return `<div class="hoja">
    <h1>Sesión · ${esc(sesion.tema)} · ${hoy()}</h1>
    <div class="sub"><span>${r.length} tarjetas</span>
      <span>${cuenta('ok')} ok · ${cuenta('parcial')} parcial · ${cuenta('fallo')} fallo</span></div>
    <table>
      <tr><th>Tarjeta</th><th>Confianza</th><th>Resultado</th><th>Brecha</th></tr>
      ${orden.map((x) => `<tr><td>${esc(x.id)}</td><td>${x.conf}</td>
        <td>${esc(x.resultado)}</td><td>${brecha(x) > 0 ? '+' : ''}${brecha(x)}</td></tr>`).join('')}
    </table>
    <div class="pie">Brecha media ${media > 0 ? '+' : ''}${media}.
      Positiva es sobreconfianza: creíste saberlo más de lo que lo sabías.</div>
  </div>`;
}
```

Cambiar el botón de impresión de Task 7 de `onclick="window.print()" data-print="parte"` a `onclick="imprimir('simulacro')"`, y agregar en `pintarCierre()` de Task 6, dentro de `.acciones`, antes del botón "Volver":

```javascript
        <button class="btn" onclick="imprimir('parte')">Imprimir parte</button>
```

- [ ] **Step 3: Agregar los tests**

Agregar a `TestPlantilla`:

```python
    def test_la_impresion_apaga_sidebar_y_controles(self):
        impresion = self.html.split("@media print")[1]
        for oculto in ("#sidebar", ".acciones", ".seg", "#avisos"):
            self.assertIn(oculto, impresion)

    def test_las_dos_salidas_de_impresion_existen(self):
        self.assertIn("function hojaSimulacro()", self.html)
        self.assertIn("function hojaParte()", self.html)

    def test_el_titulo_fija_el_nombre_de_archivo(self):
        self.assertIn("`simulacro-${horneada.s.tema}-${hoy()}`", self.html)

    def test_la_brecha_positiva_es_sobreconfianza(self):
        self.assertIn("Positiva es sobreconfianza", self.html)
```

- [ ] **Step 4: Correr y verificar que pasan**

Run: `.venv/bin/python -m unittest discover -s tests -v`
Expected: PASS, 36 tests.

- [ ] **Step 5: Verificación manual de la impresión**

Rehorneá con la sesión de prueba de Task 7 y verificá en la vista previa de impresión (Cmd+P):

1. Desde un simulacro abierto, "Imprimir": salen los enunciados numerados con renglones, encabezado con minutos y "Nombre: ____", sin sidebar ni botones, y el nombre propuesto es `simulacro-U6-<hoy>.pdf`.
2. Los ejercicios de más de 12 puntos traen 6 renglones; los otros, 4.
3. Desde el cierre de un repaso, "Imprimir parte": sale la tabla ordenada por brecha descendente, con la brecha media al pie, y el nombre propuesto es `sesion-U6-<hoy>.pdf`.
4. Ningún fondo gris ni sombra sobrevive en la vista previa.
5. Después de cerrar el diálogo de impresión, la página vuelve a verse normal y el título de la pestaña vuelve a "Estudio".

- [ ] **Step 6: Commit**

```bash
git add plantillas/estudio.html tests/test_build_estudio.py
git commit -m "estudio: impresión del simulacro en blanco y del parte de sesión"
```

---

### Task 9: Comandos y documentación

Cierra el circuito: el comando que hornea, los flags que hornean y registran, y el contrato del sistema actualizado.

**Files:**
- Create: `.claude/commands/estudio.md`
- Create: `materias/_plantilla/out/.build/sesiones/.gitkeep`
- Modify: `.claude/commands/repasar.md`
- Modify: `.claude/commands/profesor.md`
- Modify: `.claude/commands/simulacro.md`
- Modify: `CLAUDE.md`

**Interfaces:**
- Consumes: la CLI `scripts/build_estudio.py <materia> [--abrir]` de Task 5 y los formatos de portapapeles de las tareas 6 y 7.
- Produces: nada que consuman otras tareas. Es la última.

- [ ] **Step 1: Crear `.claude/commands/estudio.md`**

```markdown
---
description: Rehornea la página de estudio de una materia y la abre en el navegador
argument-hint: <materia>
---

# /estudio $ARGUMENTS

Genera `materias/activas/<materia>/out/estudio.html` y lo abre.

```bash
.venv/bin/python scripts/build_estudio.py <materia> --abrir
```

La página lee `cards/`, `mapa.md`, `programa.md`, `estado/` y los sets horneados de
`out/.build/sesiones/`. **No escribe nada en el repo**: lo que hacés ahí vuelve pegando el
bloque que copia al terminar, con `/repasar --registrar`, `/profesor --registrar` o
`/simulacro --registrar`.

Al terminar, decí la ruta del HTML, cuántos temas y tarjetas entraron, y los avisos si hubo.
**No sugieras qué estudiar.** La página muestra el dominio; elegir es del usuario.

El HTML vive en `out/`, que está gitignoreado: no lo commitees nunca.
```

- [ ] **Step 2: Agregar `--registrar` a `.claude/commands/repasar.md`**

Cambiar el `argument-hint` del frontmatter a:

```yaml
argument-hint: <tema> [--n 15] [--tipos concepto,cloze] [--desde-errores] [--materia <slug>] [--registrar]
```

Y agregar como sección nueva antes de `## Al terminar, decí exactamente`:

````markdown
## `--registrar`: sesión hecha en la página

Cuando la sesión la corriste en `out/estudio.html`, el usuario pega un bloque así:

```
/repasar --registrar U6 2026-08-16
c-U6-002 conf:5 fallo
c-U6-007 conf:3 parcial
c-U6-004 conf:4 ok
```

No hay sesión que conducir: ya pasó. Verificá primero que **todas** las líneas parseen
(`<id> conf:<1-5> <ok|parcial|fallo>`) y que los ids existan en `cards/<tema>.md`. Si una
sola falla, decí cuál y **no escribas nada**: es preferible perder el registro a dejar
`estado/` a medias entre archivos.

Si parsea entero, aplicá el paso 5 completo, tal cual, con esos datos. La confianza declarada
alimenta `calibracion.md` igual que si la hubieras pedido vos.
````

- [ ] **Step 3: Agregar los flags a `.claude/commands/profesor.md`**

Cambiar el `argument-hint` a:

```yaml
argument-hint: <tema> [modo] [--a-la-pagina] [--registrar]
```

Y agregar antes de `## Al terminar, decí exactamente`:

````markdown
## `--a-la-pagina`: hornear el set en vez de preguntar acá

Solo para `hueco`, `parcial` y `caso`. **`socratico` y `feynman` no se hornean**: su valor es
repreguntar según lo que contestás, y un HTML generado no puede branchear. Si te lo piden,
decilo y ofrecé correrlos en la terminal.

Armá las preguntas como siempre, desde secciones con fuente, y en vez de preguntarlas escribí

`materias/activas/<materia>/out/.build/sesiones/profesor-<tema>-<modo>.json`:

```json
{"comando":"profesor","modo":"hueco","tema":"U6","generado":"2026-08-16","minutos":null,
 "items":[{"id":"p-01","enunciado":"…","puntos":null}]}
```

Después rehorneá: `.venv/bin/python scripts/build_estudio.py <materia> --abrir`.

## `--registrar`: respuestas hechas en la página

El usuario pega un bloque así:

```
/profesor --registrar U6 hueco 2026-08-16 34min
## p-01 conf:4
La respuesta que escribió, que puede ocupar varias líneas.
## p-02 conf:2
No me salió.
```

Cada ítem abre con `## <id> conf:<1-5>` y su respuesta va debajo hasta el `##` siguiente.
Corregí como siempre, sin complacencia, y aplicá el paso 4 completo. Si un `##` no matchea
un id del JSON horneado, decilo y no escribas nada.
````

- [ ] **Step 4: Agregar los flags a `.claude/commands/simulacro.md`**

Cambiar el `argument-hint` a:

```yaml
argument-hint: <materia> [--reservado] [--unidades U3,U5] [--a-la-pagina] [--registrar]
```

Y agregar antes de `## Al terminar, decí exactamente`:

````markdown
## `--a-la-pagina`: rendirlo en la página

Armá el examen como siempre —imitando `wiki/examenes/patron.md` si existe— y en vez de
tomarlo acá, escribí

`materias/activas/<materia>/out/.build/sesiones/simulacro-<fecha>.json`:

```json
{"comando":"simulacro","modo":null,"tema":"U6","generado":"2026-08-16","minutos":180,
 "items":[{"id":"s-01","enunciado":"…","puntos":25}]}
```

`minutos` y `puntos` salen de la modalidad declarada en el `CLAUDE.md` de la materia.
Después rehorneá: `.venv/bin/python scripts/build_estudio.py <materia> --abrir`.

El cronómetro de la página **informa, no interrumpe**: al llegar a cero avisa y nada más,
igual que la regla de no interrumpir para avisar el tiempo.

## `--registrar`: examen rendido en la página

El usuario pega el bloque con la cabecera `/simulacro --registrar <tema> <fecha> <N>min` y un
`## <id> conf:<1-5>` por ejercicio con la respuesta debajo. Corregí con los pasos 3, 4 y 5
tal cual: rúbrica de la cátedra, cruce con calibración usando la confianza que ya viene
declarada, y las cinco actualizaciones de estado.

Si un id no matchea el JSON horneado, decilo y no escribas nada.
````

- [ ] **Step 5: Actualizar el `CLAUDE.md` raíz**

Cambiar la línea de la cabecera:

```
No es una app: son carpetas markdown + 4 scripts Python + comandos slash.
```

por:

```
No es una app: son carpetas markdown + 5 scripts Python + comandos slash.
```

Y agregar a la tabla de comandos, después de la fila de `/profesor`:

```
| `/estudio <materia>` | Genera y abre `out/estudio.html`: sesiones y comandos en el navegador. |
```

- [ ] **Step 6: Preparar la plantilla de materia nueva**

```bash
mkdir -p materias/_plantilla/out/.build/sesiones
touch materias/_plantilla/out/.build/sesiones/.gitkeep
git add -f materias/_plantilla/out/.build/sesiones/.gitkeep
```

`out/` está gitignoreado pero `.gitignore` tiene `!**/.gitkeep`, así que el `.gitkeep` entra igual. Verificá con `git status --short` que aparezca.

- [ ] **Step 7: Verificar la suite completa y el build real**

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/build_estudio.py teoria-de-la-computacion
git status --short
```

Expected: 36 tests PASS, JSON de salida sin error, y `out/estudio.html` **ausente** de `git status`.

- [ ] **Step 8: Commit**

```bash
git add .claude/commands/ CLAUDE.md materias/_plantilla/
git commit -m "estudio: comando /estudio, flags de página y contrato actualizado"
```

---

## Verificación final

Antes de dar el trabajo por terminado, correr y reportar el resultado real:

```bash
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python scripts/build_estudio.py teoria-de-la-computacion --abrir
```

Y confirmar en el navegador, con el wifi desconectado: la página abre, una sesión de U6 corre entera, el bloque se copia, y la vista previa de impresión sale limpia.
