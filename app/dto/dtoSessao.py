class SessaoDTO:
    def __init__(self, id_sessao=None, data=None, id_sala=None, preco=None, linguagem=None):
        self.id_sessao = id_sessao
        self.data = data
        self.id_sala = id_sala
        self.preco = preco
        self.linguagem = linguagem

    @staticmethod
    def from_model(sessao):
        return SessaoDTO(
            id_sessao=sessao.id_sessao,
            data=sessao.data,
            id_sala=sessao.id_sala,
            preco=sessao.preco,
            linguagem=sessao.linguagem
        )

    def to_dict(self):
        return {
            'id_sessao': self.id_sessao,
            'data': self.data,
            'id_sala': self.id_sala,
            'preco': self.preco,
            'linguagem': self.linguagem
        }
