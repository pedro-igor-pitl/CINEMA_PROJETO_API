from ..model.modelIngresso import Ingresso

class RepositoryIngresso:
    def __init__(self, db):
        self.db = db

    def save(self, ingresso):
        self.db.session.add(ingresso)
        self.db.session.commit()
        return ingresso

    def find_by_id(self, id_ingresso):
        return self.db.session.query(Ingresso).get(id_ingresso)

    def find_all(self):
        return self.db.session.query(Ingresso).all()

    def update(self, ingresso):
        existing_ingresso = self.find_by_id(ingresso.id_ingresso)
        if existing_ingresso:
            existing_ingresso.id_usuario = ingresso.id_usuario
            existing_ingresso.id_sala = ingresso.id_sala
            existing_ingresso.id_poltrona = ingresso.id_poltrona
            existing_ingresso.qrcode = ingresso.qrcode
            existing_ingresso.data_pedido = ingresso.data_pedido
            self.db.session.commit()
        return existing_ingresso

    def delete(self, id_ingresso):
        ingresso = self.find_by_id(id_ingresso)
        if ingresso:
            self.db.session.delete(ingresso)
            self.db.session.commit()
            return True  # Retorna True indicando que a poltrona foi excluída
        return False  # Retorna False se a poltrona não foi encontrada