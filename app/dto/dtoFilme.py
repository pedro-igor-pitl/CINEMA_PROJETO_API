class FilmeDTO:
    def __init__(self, id_filme=None, nome_filme=None, descricao=None, caminho_img=None, duracao=None, genero=None, data_lancamento=None, autor_filme=None):
        self.id_filme = id_filme
        self.nome_filme = nome_filme
        self.descricao = descricao
        self.caminho_img = caminho_img
        self.duracao = duracao
        self.genero = genero
        self.data_lancamento = data_lancamento
        self.autor_filme = autor_filme  # Novo campo adicionado

    @staticmethod
    def from_model(filme):
        return FilmeDTO(
            id_filme=filme.id_filme,
            nome_filme=filme.nome_filme,
            descricao=filme.descricao,
            caminho_img=filme.caminho_img,
            duracao=filme.duracao,
            genero=filme.genero,
            data_lancamento=filme.data_lancamento,
            autor_filme=filme.autor_filme  # Novo campo adicionado
        )

    def to_dict(self):
        return {
            'id_filme': self.id_filme,
            'nome_filme': self.nome_filme,
            'descricao': self.descricao,
            'caminho_img': self.caminho_img,
            'duracao': self.duracao,
            'genero': self.genero,
            'data_lancamento': self.data_lancamento,
            'autor_filme': self.autor_filme  # Novo campo adicionado
        }
