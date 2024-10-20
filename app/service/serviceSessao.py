from ..model.modelSessao import Sessao
from ..repository.repositorySessao import RepositorySessao

class SessaoService:
    def __init__(self, db):
        self.repository = RepositorySessao(db)

    def criar_sessao(self, data, id_sala, preco, linguagem):
        nova_sessao = Sessao(
            data=data,
            id_sala=id_sala,
            preco=preco,
            linguagem=linguagem
        )
        return self.repository.save(nova_sessao)

    def obter_sessao_por_id(self, id_sessao):
        return self.repository.find_by_id(id_sessao)

    def listar_sessoes(self):
        return self.repository.find_all()

    def atualizar_sessao(self, id_sessao, data=None, id_sala=None, preco=None, linguagem=None):
        sessao = self.repository.find_by_id(id_sessao)
        if sessao:
            sessao.data = data if data is not None else sessao.data
            sessao.id_sala = id_sala if id_sala is not None else sessao.id_sala
            sessao.preco = preco if preco is not None else sessao.preco
            sessao.linguagem = linguagem if linguagem is not None else sessao.linguagem
            return self.repository.update(sessao)
        return None

    def deletar_sessao(self, id_sessao):
        return self.repository.delete(id_sessao)
