from ..config.database import db

class Ingresso(db.Model):
    __tablename__ = 'ingresso'
    id_ingresso = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), nullable=False)
    id_poltrona = db.Column(db.Integer, db.ForeignKey('poltrona.id_poltrona'), nullable=False)
    qrcode = db.Column(db.String(255), nullable=True)
    data_pedido = db.Column(db.String, nullable=True)