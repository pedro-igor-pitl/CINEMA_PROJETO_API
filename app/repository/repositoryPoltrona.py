from ..model.modelPoltrona import Poltrona

class RepositoryPoltrona:
    def __init__(self, db):
        self.db = db

    def save(self, poltrona):
        self.db.session.add(poltrona)
        self.db.session.commit()
        return poltrona

    def find_by_id(self, id_poltrona):
        return self.db.session.query(Poltrona).get(id_poltrona)

    def find_all(self):
        return self.db.session.query(Poltrona).all()

    def update(self, poltrona):
        existing_poltrona = self.find_by_id(poltrona.id_poltrona)
        if existing_poltrona:
            existing_poltrona.posicao = poltrona.posicao
            existing_poltrona.tipo_poltrona = poltrona.tipo_poltrona
            existing_poltrona.id_sala = poltrona.id_sala
            self.db.session.commit()
        return existing_poltrona

    def delete(self, id_poltrona):
        poltrona = self.find_by_id(id_poltrona)
        if poltrona:
            self.db.session.delete(poltrona)
            self.db.session.commit()