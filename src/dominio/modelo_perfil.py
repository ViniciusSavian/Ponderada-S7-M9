from dataclasses import dataclass

from src.dominio.modelo_titulo import RequisitoInvalidoError


@dataclass(frozen=True)
class PerfilUsuario:
    id_perfil: str
    idade: int
    generos_preferidos: tuple[str, ...]

    def __post_init__(self) -> None:
        if not self.id_perfil.strip():
            raise RequisitoInvalidoError("id_perfil não pode ser vazio")
        if self.idade < 0 or self.idade > 120:
            raise RequisitoInvalidoError("idade deve estar entre 0 e 120")
        if not self.generos_preferidos:
            raise RequisitoInvalidoError("generos_preferidos deve ter pelo menos 1 item")
        for genero in self.generos_preferidos:
            if not genero.strip():
                raise RequisitoInvalidoError("genero preferido não pode ser vazio")
