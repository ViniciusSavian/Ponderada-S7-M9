import unittest

from src.benchmark_rnf import (
    RNF_MEDIA_MS_MAX,
    RNF_MEMORIA_MB_MAX,
    RNF_P95_MS_MAX,
    aferir_rnf_desempenho,
)


class TestDesempenhoRecomendacao(unittest.TestCase):
    def test_rnf01_desempenho_deve_ser_atendido(self) -> None:
        resultado = aferir_rnf_desempenho(qtd_titulos=5000, iteracoes=200)

        self.assertLessEqual(resultado.media_ms, RNF_MEDIA_MS_MAX)
        self.assertLessEqual(resultado.p95_ms, RNF_P95_MS_MAX)
        self.assertLessEqual(resultado.pico_memoria_mb, RNF_MEMORIA_MB_MAX)


if __name__ == "__main__":
    unittest.main()
