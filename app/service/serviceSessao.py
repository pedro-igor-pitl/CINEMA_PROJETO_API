from ..model.modelSessao import Sessao
from ..repository.repositorySessao import RepositorySessao
from ..dto.dtoSessao import SessaoDTO  # Importando o DTO criado

class SessaoService:
    def __init__(self, db):
        self.repository = RepositorySessao(db)

    def criar_sessao(self, data, id_sala, preco, linguagem):
        # Cria uma nova instância do modelo Sessao a partir dos dados fornecidos
        nova_sessao = Sessao(
            data=data,
            id_sala=id_sala,
            preco=preco,
            linguagem=linguagem
        )
        # Salva a sessão e retorna um DTO
        sessao_criada = self.repository.save(nova_sessao)
        return SessaoDTO.from_model(sessao_criada)  # Converte o modelo em DTO antes de retornar

    def obter_sessao_por_id(self, id_sessao):
        # Busca o modelo Sessao pelo ID
        sessao = self.repository.find_by_id(id_sessao)
        # Se a sessão for encontrada, converte para DTO e retorna
        if sessao:
            return SessaoDTO.from_model(sessao)
        return None  # Se não encontrar, retorna None

    def listar_sessoes(self):
        # Lista todas as sessões e as converte para DTO
        sessoes = self.repository.find_all()
        return [SessaoDTO.from_model(sessao) for sessao in sessoes]  # Converte cada sessão em DTO

    def atualizar_sessao(self, id_sessao, data=None, id_sala=None, preco=None, linguagem=None):
        # Busca a sessão pelo ID
        sessao = self.repository.find_by_id(id_sessao)
        if sessao:
            # Atualiza os campos conforme necessário
            sessao.data = data if data is not None else sessao.data
            sessao.id_sala = id_sala if id_sala is not None else sessao.id_sala
            sessao.preco = preco if preco is not None else sessao.preco
            sessao.linguagem = linguagem if linguagem is not None else sessao.linguagem
            # Salva a sessão atualizada e retorna um DTO
            sessao_atualizada = self.repository.update(sessao)
            return SessaoDTO.from_model(sessao_atualizada)
        return None  # Se a sessão não for encontrada, retorna None

    def deletar_sessao(self, id_sessao):
        # Tenta deletar a sessão pelo ID
        return self.repository.delete(id_sessao)
