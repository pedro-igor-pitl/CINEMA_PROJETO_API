from ..model.modelPoltrona import Poltrona

class servicePoltrona:
    def __init__(self, repositoryPoltrona):
        self.repositoryPoltrona = repositoryPoltrona

    def criar_poltrona(self, posicao, tipo_poltrona, id_sala):
        """Cria uma nova poltrona e salva no banco de dados"""
        nova_poltrona = Poltrona(
            posicao=posicao,
            tipo_poltrona=tipo_poltrona,
            id_sala=id_sala
        )
        return self.repositoryPoltrona.save(nova_poltrona)

    def obter_poltrona_por_id(self, id_poltrona):
        """Retorna uma poltrona pelo ID"""
        return self.repositoryPoltrona.find_by_id(id_poltrona)

    def listar_poltronas(self):
        """Retorna todas as poltronas"""
        return self.repositoryPoltrona.find_all()

    def atualizar_poltrona(self, id_poltrona, posicao=None, tipo_poltrona=None, id_sala=None):
        """Atualiza as informações de uma poltrona existente"""
        poltrona = self.repositoryPoltrona.find_by_id(id_poltrona)
        if poltrona:
            poltrona.posicao = posicao if posicao is not None else poltrona.posicao
            poltrona.tipo_poltrona = tipo_poltrona if tipo_poltrona is not None else poltrona.tipo_poltrona
            poltrona.id_sala = id_sala if id_sala is not None else poltrona.id_sala
            return self.repositoryPoltrona.update(poltrona)
        return None

    def deletar_poltrona(self, id_poltrona):
        """Deleta uma poltrona pelo ID"""
        return self.repositoryPoltrona.delete(id_poltrona)

