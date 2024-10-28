from sqlalchemy import Column, Integer, String, Text
from ..config.database import db

class Ingresso(db.Model):
    __tablename__ = 'ingresso'

    id_ingresso = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, nullable=False)
    id_sala = db.Column(db.Integer, nullable=False)
    id_poltrona = db.Column(db.Integer, nullable=False)
    qrcode = db.Column(db.Text, nullable=False)
    data_pedido = db.Column(db.String(20), nullable=False)

    '''def to_dict(self):
        return {
            'id_ingresso': self.id_ingresso,
            'id_usuario': self.id_usuario,
            'id_sala': self.id_sala,
            'id_poltrona': self.id_poltrona,
            'qrcode': self.qrcode,
            'data_pedido': self.data_pedido,
        }'''
