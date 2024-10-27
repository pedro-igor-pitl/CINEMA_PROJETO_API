from sqlalchemy import Integer, ForeignKey, Column
from ..config.database import db

class Sala(db.Model):
    __tablename__ = 'sala'
    id_sala = db.Column(db.Integer, primary_key=True)
    qt_poltrona = db.Column(db.Integer, nullable=False)

    '''def to_dict(self):
        return {
            'id_sala': self.id_sala,
            'qt_poltrona': self.qt_poltrona,
            'id_sessao': self.id_sessao
        }'''