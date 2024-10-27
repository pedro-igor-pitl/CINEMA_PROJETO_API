from ..model.modelFilme import Filme
from ..repository.repositoryFilme import RepositoryFilme
from ..dto.dtoFilme import FilmeDTO  # Importa o DTO

class ServiceFilme:
    def __init__(self, repository_filme):
        self.repository_filme = repository_filme

    def listar_filmes(self):
        # Obtém todos os filmes do repositório
        filmes = self.repository_filme.find_all()
        # Converte os filmes para DTOs
        return [FilmeDTO.from_model(filme) for filme in filmes]

    def deletar_filme(self, id_filme):
        # Tenta encontrar o filme pelo ID
        filme = self.repository_filme.find_by_id(id_filme)
        if filme:
            # Se o filme existir, chama o método delete passando o ID
            self.repository_filme.delete(id_filme)
            return True
        return False

    def obter_filme_por_id(self, id_filme):
        # Tenta encontrar o filme pelo ID e converte para DTO
        filme = self.repository_filme.find_by_id(id_filme)
        if filme:
            return FilmeDTO.from_model(filme)  # Convertendo para DTO
        return None

    def criar_filme(self, filme_dto):
        # Cria uma nova instância de Filme a partir do DTO
        filme = Filme(
            nome_filme=filme_dto.nome_filme,
            descricao=filme_dto.descricao,
            caminho_img=filme_dto.caminho_img,
            duracao=filme_dto.duracao,
            genero=filme_dto.genero,
            data_lancamento=filme_dto.data_lancamento
        )
        # Salva o filme no repositório
        self.repository_filme.save(filme)
        return FilmeDTO.from_model(filme)  # Retorna o DTO do filme criado

    def atualizar_filme(self, id_filme, filme_dto):
        # Tenta encontrar o filme pelo ID
        filme = self.repository_filme.find_by_id(id_filme)
        if filme:
            # Atualiza os atributos do filme com os dados do DTO
            filme.nome_filme = filme_dto.nome_filme
            filme.descricao = filme_dto.descricao
            filme.caminho_img = filme_dto.caminho_img
            filme.duracao = filme_dto.duracao
            filme.genero = filme_dto.genero
            filme.data_lancamento = filme_dto.data_lancamento
            filme.autor_filme = filme_dto.autor_filme
            # Salva as alterações no repositório
            self.repository_filme.save(filme)
            return FilmeDTO.from_model(filme)  # Retorna o DTO do filme atualizado
        return None
