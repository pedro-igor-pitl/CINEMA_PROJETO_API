from ..config.database import db

class Sala(db.Model):
    __tablename__ = 'sala'
    id_sala = db.Column(db.Integer, primary_key=True)
    qt_poltrona = db.Column(db.Integer, nullable=False)
    id_sessao = db.Column(db.Integer, db.ForeignKey('sessao.id_sessao'), nullable=False)