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
