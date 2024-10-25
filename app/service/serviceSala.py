from ..model.modelSala import Sala
from ..repository.repositorySala import RepositorySala
from ..dto.dtoSala import SalaDTO  # Importando o SalaDTO

class ServiceSala:
    def __init__(self, db):
        self.RepositorySala = RepositorySala(db)

    def criar_sala(self, sala_dto: SalaDTO):
        """Cria uma nova sala a partir de um SalaDTO e salva no banco de dados"""
        nova_sala = Sala(
            qt_poltrona=sala_dto.qt_poltrona,
            id_sessao=sala_dto.id_sessao
        )
        sala_criada = self.RepositorySala.save(nova_sala)
        return SalaDTO.from_model(sala_criada)  # Retorna o DTO da nova sala criada

    def obter_sala_por_id(self, id_sala):
        """Retorna uma sala pelo ID em forma de DTO"""
        sala = self.RepositorySala.find_by_id(id_sala)
        if sala:
            return SalaDTO.from_model(sala)  # Retorna o DTO da sala
        return None

    def listar_salas(self):
        """Retorna todas as salas em forma de DTOs"""
        salas = self.RepositorySala.find_all()
        return [SalaDTO.from_model(sala) for sala in salas]  # Retorna uma lista de DTOs

    def atualizar_sala(self, id_sala, sala_dto: SalaDTO):
        """Atualiza as informações de uma sala existente a partir de um SalaDTO"""
        sala = self.RepositorySala.find_by_id(id_sala)
        if sala:
            sala.qt_poltrona = sala_dto.qt_poltrona if sala_dto.qt_poltrona is not None else sala.qt_poltrona
            sala.id_sessao = sala_dto.id_sessao if sala_dto.id_sessao is not None else sala.id_sessao
            sala_atualizada = self.RepositorySala.update(sala)
            return SalaDTO.from_model(sala_atualizada)  # Retorna o DTO da sala atualizada
        return None

    def deletar_sala(self, id_sala):
        """Deleta uma sala pelo ID"""
        return self.RepositorySala.delete(id_sala)
