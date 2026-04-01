import unittest

from src.aplicacao.servico_recomendacao import ServicoRecomendacao
from src.dominio.modelo_perfil import PerfilUsuario
from src.dominio.modelo_titulo import Titulo


class TestServicoRecomendacao(unittest.TestCase):
    def setUp(self) -> None:
        self.servico = ServicoRecomendacao()
        self.catalogo = [
            Titulo("1", "Drama Forte", "drama", 16, 9.5),
            Titulo("2", "Comédia Leve", "comedia", 10, 8.0),
            Titulo("3", "Ação Noturna", "acao", 18, 9.0),
            Titulo("4", "Drama Clássico", "drama", 12, 7.5),
        ]

    def test_deve_retornar_top_n_ordenado_por_score(self) -> None:
        perfil = PerfilUsuario("u1", 18, ("drama", "acao"))

        recomendacoes = self.servico.gerar_recomendacoes(perfil, self.catalogo, limite=3)

        self.assertEqual(3, len(recomendacoes))
        self.assertGreaterEqual(recomendacoes[0].score, recomendacoes[1].score)
        self.assertGreaterEqual(recomendacoes[1].score, recomendacoes[2].score)
        self.assertEqual("Drama Forte", recomendacoes[0].titulo.nome)

    def test_deve_aplicar_filtro_etario(self) -> None:
        perfil = PerfilUsuario("u2", 13, ("acao", "drama"))

        recomendacoes = self.servico.gerar_recomendacoes(perfil, self.catalogo, limite=10)
        nomes = [r.titulo.nome for r in recomendacoes]

        self.assertNotIn("Drama Forte", nomes)
        self.assertNotIn("Ação Noturna", nomes)


if __name__ == "__main__":
    unittest.main()
