from dataclasses import dataclass


class RequisitoInvalidoError(ValueError):
    """Erro de validação para entrada fora dos requisitos."""


@dataclass(frozen=True)
class Titulo:
    id_titulo: str
    nome: str
    genero: str
    classificacao_etaria_minima: int
    nota_popularidade: float

    def __post_init__(self) -> None:
        if not self.id_titulo.strip():
            raise RequisitoInvalidoError("id_titulo não pode ser vazio")
        if not self.nome.strip():
            raise RequisitoInvalidoError("nome não pode ser vazio")
        if not self.genero.strip():
            raise RequisitoInvalidoError("genero não pode ser vazio")
        if self.classificacao_etaria_minima < 0 or self.classificacao_etaria_minima > 21:
            raise RequisitoInvalidoError("classificacao_etaria_minima deve estar entre 0 e 21")
        if self.nota_popularidade < 0 or self.nota_popularidade > 10:
            raise RequisitoInvalidoError("nota_popularidade deve estar entre 0 e 10")
