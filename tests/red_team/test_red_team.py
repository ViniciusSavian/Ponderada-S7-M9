import unittest

from src.aplicacao.servico_recomendacao import ServicoRecomendacao
from src.dominio.modelo_perfil import PerfilUsuario
from src.dominio.modelo_titulo import RequisitoInvalidoError, Titulo


class TestRedTeam(unittest.TestCase):
    def setUp(self) -> None:
        self.servico = ServicoRecomendacao()

    def test_deve_bloquear_idade_maliciosa_negativa(self) -> None:
        with self.assertRaises(RequisitoInvalidoError):
            PerfilUsuario("inv", -1, ("drama",))

    def test_deve_bloquear_nota_fora_do_intervalo(self) -> None:
        with self.assertRaises(RequisitoInvalidoError):
            Titulo("x", "Exploit Score", "acao", 16, 42.0)

    def test_deve_resistir_catalogo_extenso_sem_falhar(self) -> None:
        perfil = PerfilUsuario("u1", 18, ("drama", "acao"))
        catalogo = [
            Titulo(str(i), f"Titulo {i}", "drama" if i % 2 == 0 else "acao", 16, 8.0)
            for i in range(5000)
        ]

        recomendacoes = self.servico.gerar_recomendacoes(perfil, catalogo, limite=10)

        self.assertEqual(10, len(recomendacoes))


if __name__ == "__main__":
    unittest.main()
