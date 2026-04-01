from src.dominio.modelo_titulo import Titulo


class RepositorioTitulosMemoria:
    def __init__(self, titulos: list[Titulo]) -> None:
        self._titulos = list(titulos)

    def listar_todos(self) -> list[Titulo]:
        return list(self._titulos)
