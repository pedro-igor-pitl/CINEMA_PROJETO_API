from ..model.modelSessao import Sessao

class sessaoService:
    def __init__(self,repositorySessao):
        self.repositorySessao = repositorySessao

    def criar_sessao(self, data, id_sala, preco, linguagem):
        """Cria uma nova sessão e salva no banco de dados"""
        nova_sessao = Sessao(
            data=data,
            id_sala=id_sala,
            preco=preco,
            linguagem=linguagem
        )
        return self.repositorySessao.save(nova_sessao)

    def obter_sessao_por_id(self, id_sessao):
        """Retorna uma sessão pelo ID"""
        return self.repositorySessao.find_by_id(id_sessao)

    def listar_sessoes(self):
        """Retorna todas as sessões"""
        return self.repositorySessao.find_all()

    def atualizar_sessao(self, id_sessao, data=None, id_sala=None, preco=None, linguagem=None):
        """Atualiza as informações de uma sessão existente"""
        sessao = self.repositorySessao.find_by_id(id_sessao)
        if sessao:
            sessao.data = data if data is not None else sessao.data
            sessao.id_sala = id_sala if id_sala is not None else sessao.id_sala
            sessao.preco = preco if preco is not None else sessao.preco
            sessao.linguagem = linguagem if linguagem is not None else sessao.linguagem
            return self.repositorySessao.update(sessao)
        return None

    def deletar_sessao(self, id_sessao):
        """Deleta uma sessão pelo ID"""
        return self.repositorySessao.delete(id_sessao)
