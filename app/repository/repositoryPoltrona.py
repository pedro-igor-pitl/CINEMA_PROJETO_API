from ..model.modelPoltrona import Poltrona

class RepositoryPoltrona:
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, poltrona):
        self.db_session.add(poltrona)
        self.db_session.commit()
        return poltrona

    def find_by_id(self, id_poltrona):
        return self.db_session.query(Poltrona).get(id_poltrona)

    def find_all(self):
        return self.db_session.query(Poltrona).all()

    def update(self, poltrona):
        existing_poltrona = self.find_by_id(poltrona.id_poltrona)
        if existing_poltrona:
            existing_poltrona.posicao = poltrona.posicao
            existing_poltrona.tipo_poltrona = poltrona.tipo_poltrona
            existing_poltrona.id_sala = poltrona.id_sala
            self.db_session.commit()
        return existing_poltrona

    def delete(self, id_poltrona):
        poltrona = self.find_by_id(id_poltrona)
        if poltrona:
            self.db_session.delete(poltrona)
            self.db_session.commit()