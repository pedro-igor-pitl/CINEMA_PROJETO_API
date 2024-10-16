from ..model.modelSala import Sala

class serviceSala:
    def __init__(self, repositorySala):
        self.repositorySala = repositorySala

    def criar_sala(self, qt_poltrona, id_sessao):
        """Cria uma nova sala e salva no banco de dados"""
        nova_sala = Sala(
            qt_poltrona=qt_poltrona,
            id_sessao=id_sessao
        )
        return self.repositorySala.save(nova_sala)

    def obter_sala_por_id(self, id_sala):
        """Retorna uma sala pelo ID"""
        return self.repositorySala.find_by_id(id_sala)

    def listar_salas(self):
        """Retorna todas as salas"""
        return self.repositorySala.find_all()

    def atualizar_sala(self, id_sala, qt_poltrona=None, id_sessao=None):
        """Atualiza as informações de uma sala existente"""
        sala = self.repositorySala.find_by_id(id_sala)
        if sala:
            sala.qt_poltrona = qt_poltrona if qt_poltrona is not None else sala.qt_poltrona
            sala.id_sessao = id_sessao if id_sessao is not None else sala.id_sessao
            return self.repositorySala.update(sala)
        return None

    def deletar_sala(self, id_sala):
        """Deleta uma sala pelo ID"""
        return self.repositorySala.delete(id_sala)
