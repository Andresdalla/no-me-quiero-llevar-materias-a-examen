#!/usr/bin/env python3
"""Tests de scripts/build_estudio.py.

uso: .venv/bin/python -m unittest discover -s tests -v
"""
from __future__ import annotations

import json
import re
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
        "# Programa\nmodo: temario\n\n"
        "## U6 · Cardinalidad y numerabilidad\n- fuentes: []\n\n"
        "## U7 · Indecidibilidad\n- fuentes: []\n",
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
    def test_lee_el_nombre_y_el_slug(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = _materia_temporal(Path(tmp), CLAUDE_OK)
            datos = build_estudio.leer_materia(m)
            self.assertEqual(datos["nombre"], "Teoría de la Computación")
            self.assertEqual(datos["slug"], "materia-test")

    def test_ignora_las_fechas_de_evaluacion_del_claude_md(self):
        """El CLAUDE.md de arriba declara un parcial: no tiene que llegar a los datos.

        Las fechas son dato de referencia de la materia, nunca insumo de la
        página de estudio.
        """
        with tempfile.TemporaryDirectory() as tmp:
            datos = build_estudio.leer_materia(_materia_temporal(Path(tmp), CLAUDE_OK))
            self.assertEqual(set(datos), {"slug", "nombre"})


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


class TestProgramaEmergente(unittest.TestCase):
    """Una materia sin temario nombra sus ejes con slug en vez de `U<n>`."""

    def _materia(self, tmp: str, programa: str, mapa: str) -> Path:
        m = _materia_temporal(Path(tmp), CLAUDE_OK)
        (m / "wiki" / "programa.md").write_text(programa, encoding="utf-8")
        (m / "wiki" / "mapa.md").write_text(mapa, encoding="utf-8")
        return m

    def test_los_ejes_con_slug_son_temas(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = self._materia(
                tmp,
                "# Programa\nmodo: emergente\n\n"
                "## microservicios\n- fuentes: [fowler-cap2]\n\n"
                "## calidad-y-atributos\n- fuentes: [clase-01]\n",
                "| Página | Tipo | Tema | Qué contiene |\n|---|---|---|---|\n"
                "| `conceptos/saga` | concepto | microservicios | Transacción distribuida |\n",
            )
            temas = build_estudio.leer_temas(m, {}, [])
            self.assertEqual(
                [t["id"] for t in temas], ["calidad-y-atributos", "microservicios"]
            )
            micro = next(t for t in temas if t["id"] == "microservicios")
            self.assertEqual(micro["paginas"], 1)
            self.assertEqual(micro["nombre"], "")

    def test_las_unidades_numeradas_van_antes_que_los_slugs(self):
        """Una materia puede quedar mixta durante una migración: el orden no puede explotar."""
        with tempfile.TemporaryDirectory() as tmp:
            m = self._materia(
                tmp,
                "# Programa\n\n## U10 · Décima\n- fuentes: []\n\n"
                "## U2 · Segunda\n- fuentes: []\n\n"
                "## microservicios\n- fuentes: []\n\n"
                "## arquitectura\n- fuentes: []\n",
                "| Página | Tipo | Tema | Qué contiene |\n|---|---|---|---|\n",
            )
            temas = build_estudio.leer_temas(m, {}, [])
            self.assertEqual(
                [t["id"] for t in temas], ["U2", "U10", "arquitectura", "microservicios"]
            )

    def test_la_fila_separadora_del_mapa_no_es_un_tema(self):
        """Regresión: aceptar slugs hace que `|---|---|---|` sea candidato a tema."""
        with tempfile.TemporaryDirectory() as tmp:
            m = self._materia(
                tmp,
                "# Programa\nmodo: emergente\n\n## microservicios\n- fuentes: []\n",
                "| Página | Tipo | Tema | Qué contiene |\n|---|---|---|---|\n"
                "| `conceptos/saga` | concepto | microservicios | Transacción distribuida |\n",
            )
            self.assertEqual(
                [t["id"] for t in build_estudio.leer_temas(m, {}, [])], ["microservicios"]
            )

    def test_un_encabezado_sin_entrada_no_es_un_tema(self):
        """`## Bibliografía` al final del programa no es un eje de estudio."""
        with tempfile.TemporaryDirectory() as tmp:
            m = self._materia(
                tmp,
                "# Programa\nmodo: emergente\n\n"
                "## microservicios\n- fuentes: []\n\n## Bibliografía\n- Fowler, 2019\n",
                "| Página | Tipo | Tema | Qué contiene |\n|---|---|---|---|\n",
            )
            self.assertEqual(
                [t["id"] for t in build_estudio.leer_temas(m, {}, [])], ["microservicios"]
            )

    def test_un_marcador_transversal_del_mapa_no_es_un_tema(self):
        """La columna de tema del mapa admite `todas` y rangos: describen alcance."""
        with tempfile.TemporaryDirectory() as tmp:
            m = self._materia(
                tmp,
                "# Programa\nmodo: temario\n\n## U1 · Primera\n- fuentes: []\n",
                "| Página | Tipo | Unidad | Qué contiene |\n|---|---|---|---|\n"
                "| `fuentes/temario` | fuente | todas | Ficha del temario oficial |\n"
                "| `conceptos/x` | concepto | U1-U5 | Atraviesa media materia |\n"
                "| `conceptos/y` | concepto | U1 | Una sola unidad |\n",
            )
            temas = build_estudio.leer_temas(m, {}, [])
            self.assertEqual([t["id"] for t in temas], ["U1"])
            self.assertEqual(temas[0]["paginas"], 1)

    def test_el_dominio_de_un_eje_con_slug_se_lee(self):
        with tempfile.TemporaryDirectory() as tmp:
            m = self._materia(
                tmp,
                "# Programa\nmodo: emergente\n\n## microservicios\n- fuentes: []\n",
                "| Página | Tipo | Tema | Qué contiene |\n|---|---|---|---|\n",
            )
            (m / "estado" / "dominio.md").write_text(
                "| Tema | Dominio | Última evaluación |\n|---|---|---|\n"
                "| microservicios | 2 | 2026-08-18 |\n",
                encoding="utf-8",
            )
            (m / "estado" / "historial.md").write_text(
                "| Fecha | Tema | Tipo | Resultado |\n|---|---|---|---|\n"
                "| 2026-08-18 | microservicios | repaso | 9 tarjetas |\n",
                encoding="utf-8",
            )
            tema = build_estudio.leer_temas(m, {}, [])[0]
            self.assertEqual(tema["dominio"], 2)
            self.assertEqual(tema["ultimo"], "2026-08-18")


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


# Solo contextos de carga: que una tarjeta mencione una URL en su texto no es
# una referencia externa, pero un src/href/@import/url() que apunta afuera sí.
SIN_EXTERNOS = re.compile(
    r"""(?:src|href)\s*=\s*['"]?\s*(?:https?:)?//"""
    r"""|@import"""
    r"""|url\(\s*['"]?\s*(?:https?:)?//"""
)


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

    def test_sin_externos_detecta_referencias_de_carga_en_cualquier_forma(self):
        deben_matchear = (
            '<script src="https://cdn.example.com/x.js">',
            "<script src='http://x/y.js'>",
            "<link href=https://x/y.css>",
            '<style>@import "x.css"</style>',
            "background:url(//fonts.example.com/f.woff)",
        )
        for texto in deben_matchear:
            self.assertIsNotNone(SIN_EXTERNOS.search(texto), f"no detectó: {texto}")

        no_deben_matchear = (
            '<a href="#temas">',
            "url(#gradiente)",
            "La fuente está en https://example.com/paper.pdf",
        )
        for texto in no_deben_matchear:
            hallado = SIN_EXTERNOS.search(texto)
            self.assertIsNone(hallado, f"falso positivo en: {texto} -> {hallado.group(0) if hallado else ''}")

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

    def test_el_sidebar_no_cuenta_dias_para_ninguna_evaluacion(self):
        """Sin cuenta regresiva: la página informa lo que hay, no lo que falta."""
        for prohibido in ("parcial en ", "ya rendido", "materia.parcial"):
            self.assertNotIn(prohibido, self.html)


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
            self.assertNotIn("parcial", datos["materia"])
            self.assertEqual(len(datos["mazos"]["U6"]), 2)
            self.assertEqual(datos["temas"][0]["id"], "U6")
            self.assertTrue(datos["avisos"])

            plantilla = (RAIZ / "plantillas" / "estudio.html").read_text(encoding="utf-8")
            html = build_estudio.render(datos, plantilla)
            hallado = SIN_EXTERNOS.search(html)
            self.assertIsNone(hallado, f"referencia externa: {hallado.group(0) if hallado else ''}")
            self.assertIn("axioma de extensión", html)


if __name__ == "__main__":
    unittest.main()
