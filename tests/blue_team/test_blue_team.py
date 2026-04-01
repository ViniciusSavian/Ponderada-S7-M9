import unittest

from src.aplicacao.servico_recomendacao import ServicoRecomendacao
from src.dominio.modelo_perfil import PerfilUsuario
from src.dominio.modelo_titulo import RequisitoInvalidoError, Titulo


class TestBlueTeam(unittest.TestCase):
    def setUp(self) -> None:
        self.servico = ServicoRecomendacao()

    def test_cenario_esperado_usuario_maior_idade(self) -> None:
        perfil = PerfilUsuario("adulto", 21, ("drama",))
        catalogo = [
            Titulo("1", "Drama 18", "drama", 18, 9.0),
            Titulo("2", "Comédia 10", "comedia", 10, 8.5),
        ]

        recomendacoes = self.servico.gerar_recomendacoes(perfil, catalogo)

        self.assertEqual(2, len(recomendacoes))
        self.assertEqual("Drama 18", recomendacoes[0].titulo.nome)

    def test_validacao_de_limite_invalido(self) -> None:
        perfil = PerfilUsuario("u", 21, ("drama",))
        catalogo = [Titulo("1", "Drama", "drama", 18, 9.0)]

        with self.assertRaises(RequisitoInvalidoError):
            self.servico.gerar_recomendacoes(perfil, catalogo, limite=0)


if __name__ == "__main__":
    unittest.main()
