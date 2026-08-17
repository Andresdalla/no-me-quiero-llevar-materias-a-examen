#!/usr/bin/env python3
"""Tests de scripts/build_estudio.py.

uso: .venv/bin/python -m unittest discover -s tests -v
"""
from __future__ import annotations

import json
import sys
import tempfile
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

    def test_archivo_ilegible_se_saltea_con_aviso(self):
        with tempfile.TemporaryDirectory() as tmp:
            d = self._dir(tmp)
            (d / "carpeta.json").mkdir()
            (d / "s1.json").write_text(json.dumps(SESION_OK), encoding="utf-8")
            avisos: list[str] = []
            got = build_estudio.leer_sesiones(Path(tmp) / "out", avisos)
            self.assertEqual(len(got), 1)
            self.assertTrue(any("carpeta.json" in a for a in avisos))


if __name__ == "__main__":
    unittest.main()
