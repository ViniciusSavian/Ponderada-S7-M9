from dataclasses import dataclass

from src.dominio.modelo_perfil import PerfilUsuario
from src.dominio.modelo_titulo import RequisitoInvalidoError, Titulo

PESO_PREFERENCIA_GENERO = 0.6
PESO_POPULARIDADE = 0.4


@dataclass(frozen=True)
class Recomendacao:
    titulo: Titulo
    score: float


class ServicoRecomendacao:
    """RF-01: gerar Top N por perfil e gênero com filtro etário."""

    def gerar_recomendacoes(
        self,
        perfil: PerfilUsuario,
        catalogo: list[Titulo],
        limite: int = 10,
    ) -> list[Recomendacao]:
        if limite <= 0 or limite > 10:
            raise RequisitoInvalidoError("limite deve estar entre 1 e 10")
        if not isinstance(catalogo, list):
            raise RequisitoInvalidoError("catalogo deve ser uma lista")

        generos_normalizados = {g.strip().lower() for g in perfil.generos_preferidos}

        elegiveis: list[Recomendacao] = []
        for titulo in catalogo:
            if perfil.idade < titulo.classificacao_etaria_minima:
                continue

            genero_match = 1.0 if titulo.genero.strip().lower() in generos_normalizados else 0.0
            popularidade_normalizada = titulo.nota_popularidade / 10.0
            score = (PESO_PREFERENCIA_GENERO * genero_match) + (
                PESO_POPULARIDADE * popularidade_normalizada
            )
            elegiveis.append(Recomendacao(titulo=titulo, score=round(score, 6)))

        elegiveis.sort(
            key=lambda item: (item.score, item.titulo.nota_popularidade, item.titulo.nome),
            reverse=True,
        )
        return elegiveis[:limite]
