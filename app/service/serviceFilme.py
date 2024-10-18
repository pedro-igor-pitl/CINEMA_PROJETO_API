from ..model.modelFilme import Filme

class serviceFilme:
    def __init__(self, repositoryFilme):
        self.repositoryFilme = repositoryFilme

    def criar_filme(self, nome_filme, descricao, caminho_img, duracao, genero, data_lancamento):
        """Cria um novo filme e salva no banco de dados"""
        novo_filme = Filme(  # Mudança aqui, usando a classe Filme
            nome_filme=nome_filme,
            descricao=descricao,
            caminho_img=caminho_img,
            duracao=duracao,
            genero=genero,
            data_lancamento=data_lancamento
        )
        return self.repositoryFilme.save(novo_filme)

    def obter_filme_por_id(self, id_filme):
        """Retorna um filme pelo ID"""
        return self.repositoryFilme.find_by_id(id_filme)

    def listar_filmes(self):
        """Retorna todos os filmes"""
        return self.repositoryFilme.find_all()

    def atualizar_filme(self, id_filme, nome_filme=None, descricao=None, caminho_img=None,
                        duracao=None, genero=None, data_lancamento=None):
        """Atualiza as informações de um filme existente"""
        filme = self.repositoryFilme.find_by_id(id_filme)
        if filme:
            filme.nome_filme = nome_filme if nome_filme is not None else filme.nome_filme
            filme.descricao = descricao if descricao is not None else filme.descricao
            filme.caminho_img = caminho_img if caminho_img is not None else filme.caminho_img
            filme.duracao = duracao if duracao is not None else filme.duracao
            filme.genero = genero if genero is not None else filme.genero
            filme.data_lancamento = data_lancamento if data_lancamento is not None else filme.data_lancamento
            return self.repositoryFilme.update(filme)
        return None

    def deletar_filme(self, id_filme):
        """Deleta um filme pelo ID"""
        return self.repositoryFilme.delete(id_filme)