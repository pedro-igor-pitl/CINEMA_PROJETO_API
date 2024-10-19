from ..model.modelSessao import Sessao

class RepositorySessao:
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, sessao):
        self.db_session.add(sessao)
        self.db_session.commit()
        return sessao

    def find_by_id(self, id_sessao):
        return self.db_session.query(Sessao).get(id_sessao)

    def find_all(self):
        return self.db_session.query(Sessao).all()

    def update(self, sessao):
        existing_sessao = self.find_by_id(sessao.id_sessao)
        if existing_sessao:
            existing_sessao.data = sessao.data
            existing_sessao.id_sala = sessao.id_sala
            existing_sessao.preco = sessao.preco
            existing_sessao.linguagem = sessao.linguagem
            self.db_session.commit()
        return existing_sessao

    def delete(self, id_sessao):
        sessao = self.find_by_id(id_sessao)
        if sessao:
            self.db_session.delete(sessao)
            self.db_session.commit()