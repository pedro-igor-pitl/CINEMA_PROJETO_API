from sqlalchemy import Column, Integer, String, ForeignKey
from ..config.database import db

class Poltrona(db.Model):
    __tablename__ = 'poltrona'
    id_poltrona = db.Column(db.Integer, primary_key=True)
    posicao = db.Column(db.String(50), nullable=False)
    tipo_poltrona = db.Column(db.String(50), nullable=False)
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), nullable=False)

    def to_dict(self):
        return {
            'id_poltrona': self.id_poltrona,
            'posicao': self.posicao,
            'tipo_poltrona': self.tipo_poltrona,
            'id_sala': self.id_sala
        }
