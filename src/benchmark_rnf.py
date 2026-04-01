import random
import statistics
import time
import tracemalloc
from dataclasses import dataclass

from src.aplicacao.servico_recomendacao import ServicoRecomendacao
from src.dominio.modelo_perfil import PerfilUsuario
from src.dominio.modelo_titulo import Titulo

RNF_P95_MS_MAX = 120.0
RNF_MEDIA_MS_MAX = 80.0
RNF_MEMORIA_MB_MAX = 150.0


@dataclass(frozen=True)
class ResultadoRNF:
    media_ms: float
    p95_ms: float
    pico_memoria_mb: float

    def aprovado(self) -> bool:
        return (
            self.media_ms <= RNF_MEDIA_MS_MAX
            and self.p95_ms <= RNF_P95_MS_MAX
            and self.pico_memoria_mb <= RNF_MEMORIA_MB_MAX
        )


def _gerar_catalogo(qtd_titulos: int) -> list[Titulo]:
    generos = ["drama", "comedia", "acao", "ficcao", "documentario"]
    random.seed(42)
    return [
        Titulo(
            id_titulo=f"tt-{i}",
            nome=f"Titulo {i}",
            genero=random.choice(generos),
            classificacao_etaria_minima=random.choice([10, 12, 14, 16, 18]),
            nota_popularidade=round(random.uniform(5.0, 10.0), 2),
        )
        for i in range(qtd_titulos)
    ]


def aferir_rnf_desempenho(
    qtd_titulos: int = 5000,
    iteracoes: int = 200,
) -> ResultadoRNF:
    servico = ServicoRecomendacao()
    catalogo = _gerar_catalogo(qtd_titulos=qtd_titulos)
    perfil = PerfilUsuario(id_perfil="u-1", idade=18, generos_preferidos=("drama", "acao"))

    tempos_ms: list[float] = []
    tracemalloc.start()

    for _ in range(iteracoes):
        inicio = time.perf_counter()
        servico.gerar_recomendacoes(perfil=perfil, catalogo=catalogo, limite=10)
        fim = time.perf_counter()
        tempos_ms.append((fim - inicio) * 1000)

    _, pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    media_ms = statistics.mean(tempos_ms)
    p95_ms = statistics.quantiles(tempos_ms, n=100)[94]
    pico_memoria_mb = pico / (1024 * 1024)

    return ResultadoRNF(media_ms=media_ms, p95_ms=p95_ms, pico_memoria_mb=pico_memoria_mb)


if __name__ == "__main__":
    resultado = aferir_rnf_desempenho()
    print("=== Aferição RNF-01 (Desempenho) ===")
    print(f"Média: {resultado.media_ms:.2f} ms (limite <= {RNF_MEDIA_MS_MAX:.2f} ms)")
    print(f"P95: {resultado.p95_ms:.2f} ms (limite <= {RNF_P95_MS_MAX:.2f} ms)")
    print(
        f"Pico de memória: {resultado.pico_memoria_mb:.2f} MB "
        f"(limite <= {RNF_MEMORIA_MB_MAX:.2f} MB)"
    )
    print(f"Status: {'APROVADO' if resultado.aprovado() else 'REPROVADO'}")
