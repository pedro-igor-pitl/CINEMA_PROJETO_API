from ..model.modelSala import Sala

class RepositorySala:
    def __init__(self, db):
        self.db = db

    def save(self, sala):
        self.db.session.add(sala)
        self.db.session.commit()
        return sala

    def find_by_id(self, id_sala):
        return self.db.session.query(Sala).get(id_sala)

    def find_all(self):
        return self.db.session.query(Sala).all()

    def update(self, sala):
        existing_sala = self.find_by_id(sala.id_sala)
        if existing_sala:
            existing_sala.qt_poltrona = sala.qt_poltrona
            existing_sala.id_sessao = sala.id_sessao
            self.db.session.commit()
        return existing_sala

    def delete(self, id_sala):
        sala = self.find_by_id(id_sala)
        if sala:
            self.db.session.delete(sala)
            self.db.session.commit()