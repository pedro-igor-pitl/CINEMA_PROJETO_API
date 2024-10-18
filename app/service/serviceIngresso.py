from ..model.modelIngresso import Ingresso

class serviceIngresso:
    def __init__(self, repositoryIngresso):
        self.repositoryIngresso = repositoryIngresso

    def criar_ingresso(self, id_usuario, id_sala, id_poltrona, qrcode, data_pedido):
        """Cria um novo ingresso e salva no banco de dados"""
        novo_ingresso = Ingresso(
            id_usuario=id_usuario,
            id_sala=id_sala,
            id_poltrona=id_poltrona,
            qrcode=qrcode,
            data_pedido=data_pedido
        )
        return self.repositoryIngresso.save(novo_ingresso)

    def obter_ingresso_por_id(self, id_ingresso):
        """Retorna um ingresso pelo ID"""
        return self.repositoryIngresso.find_by_id(id_ingresso)

    def listar_ingressos(self):
        """Retorna todos os ingressos"""
        return self.repositoryIngresso.find_all()

    def atualizar_ingresso(self, id_ingresso, id_usuario=None, id_sala=None,
                           id_poltrona=None, qrcode=None, data_pedido=None):
        """Atualiza as informações de um ingresso existente"""
        ingresso = self.repositoryIngresso.find_by_id(id_ingresso)
        if ingresso:
            ingresso.id_usuario = id_usuario if id_usuario is not None else ingresso.id_usuario
            ingresso.id_sala = id_sala if id_sala is not None else ingresso.id_sala
            ingresso.id_poltrona = id_poltrona if id_poltrona is not None else ingresso.id_poltrona
            ingresso.qrcode = qrcode if qrcode is not None else ingresso.qrcode
            ingresso.data_pedido = data_pedido if data_pedido is not None else ingresso.data_pedido
            return self.repositoryIngresso.update(ingresso)
        return None

    def deletar_ingresso(self, id_ingresso):
        """Deleta um ingresso pelo ID"""
        return self.repositoryIngresso.delete(id_ingresso)
