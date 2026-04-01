from src.aplicacao.servico_recomendacao import Recomendacao, ServicoRecomendacao
from src.dominio.modelo_perfil import PerfilUsuario
from src.infra.repositorio_titulos_memoria import RepositorioTitulosMemoria


class APILocalRecomendacao:
    """Interface local para conectar repositório e serviço."""

    def __init__(self, repositorio: RepositorioTitulosMemoria) -> None:
        self._repositorio = repositorio
        self._servico = ServicoRecomendacao()

    def recomendar_top10(self, perfil: PerfilUsuario) -> list[Recomendacao]:
        return self._servico.gerar_recomendacoes(
            perfil=perfil,
            catalogo=self._repositorio.listar_todos(),
            limite=10,
        )
