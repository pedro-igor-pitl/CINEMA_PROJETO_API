from ..model.modelIngresso import Ingresso

class repositoryIngresso:
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, ingresso):
        self.db_session.add(ingresso)
        self.db_session.commit()
        return ingresso

    def find_by_id(self, id_ingresso):
        return self.db_session.query(Ingresso).get(id_ingresso)

    def find_all(self):
        return self.db_session.query(Ingresso).all()

    def update(self, ingresso):
        existing_ingresso = self.find_by_id(ingresso.id_ingresso)
        if existing_ingresso:
            existing_ingresso.id_usuario = ingresso.id_usuario
            existing_ingresso.id_sala = ingresso.id_sala
            existing_ingresso.id_poltrona = ingresso.id_poltrona
            existing_ingresso.qrcode = ingresso.qrcode
            existing_ingresso.data_pedido = ingresso.data_pedido
            self.db_session.commit()
        return existing_ingresso

    def delete(self, id_ingresso):
        ingresso = self.find_by_id(id_ingresso)
        if ingresso:
            self.db_session.delete(ingresso)
            self.db_session.commit()