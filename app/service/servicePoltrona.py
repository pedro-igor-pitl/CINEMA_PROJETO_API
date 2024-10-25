from ..model.modelPoltrona import Poltrona
from ..repository.repositoryPoltrona import RepositoryPoltrona
from ..dto.dtoPoltrona import PoltronaDTO

class ServicePoltrona:
    def __init__(self, db):
        self.RepositoryPoltrona = RepositoryPoltrona(db)

    def criar_poltrona(self, posicao, tipo_poltrona, id_sala):
        """Cria uma nova poltrona e salva no banco de dados, retornando como DTO"""
        nova_poltrona = Poltrona(
            posicao=posicao,
            tipo_poltrona=tipo_poltrona,
            id_sala=id_sala
        )
        poltrona_salva = self.RepositoryPoltrona.save(nova_poltrona)
        return PoltronaDTO.from_model(poltrona_salva)

    def obter_poltrona_por_id(self, id_poltrona):
        """Retorna uma poltrona pelo ID, como DTO"""
        poltrona = self.RepositoryPoltrona.find_by_id(id_poltrona)
        if poltrona:
            return PoltronaDTO.from_model(poltrona)
        return None

    def listar_poltronas(self):
        """Retorna todas as poltronas como uma lista de DTOs"""
        poltronas = self.RepositoryPoltrona.find_all()
        return [PoltronaDTO.from_model(poltrona) for poltrona in poltronas]

    def atualizar_poltrona(self, id_poltrona, posicao=None, tipo_poltrona=None, id_sala=None):
        """Atualiza as informações de uma poltrona existente e retorna como DTO"""
        poltrona = self.RepositoryPoltrona.find_by_id(id_poltrona)
        if poltrona:
            poltrona.posicao = posicao if posicao is not None else poltrona.posicao
            poltrona.tipo_poltrona = tipo_poltrona if tipo_poltrona is not None else poltrona.tipo_poltrona
            poltrona.id_sala = id_sala if id_sala is not None else poltrona.id_sala
            poltrona_atualizada = self.RepositoryPoltrona.update(poltrona)
            return PoltronaDTO.from_model(poltrona_atualizada)
        return None

    def deletar_poltrona(self, id_poltrona):
        """Deleta uma poltrona pelo ID"""
        return self.RepositoryPoltrona.delete(id_poltrona)
