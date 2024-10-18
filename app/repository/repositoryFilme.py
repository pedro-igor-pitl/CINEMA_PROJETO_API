from ..model.modelFilme import Filme

class repositoryFilme:
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, filme):
        self.db_session.add(filme)
        self.db_session.commit()
        return filme

    def find_by_id(self, id_filme):
        return self.db_session.query(Filme).get(id_filme)

    def find_all(self):
        return self.db_session.query(Filme).all()

    def update(self, filme):
        existing_filme = self.find_by_id(filme.id_filme)
        if existing_filme:
            existing_filme.nome_filme = filme.nome_filme
            existing_filme.descricao = filme.descricao
            existing_filme.caminho_img = filme.caminho_img
            existing_filme.duracao = filme.duracao
            existing_filme.genero = filme.genero
            existing_filme.data_lancamento = filme.data_lancamento
            self.db_session.commit()
        return existing_filme

    def delete(self, id_filme):
        filme = self.find_by_id(id_filme)
        if filme:
            self.db_session.delete(filme)
            self.db_session.commit()