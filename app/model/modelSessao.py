from ..config.database import db

class Sessao(db.Model):
    __tablename__ = 'sessao'
    id_sessao = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(20), nullable=False)
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    linguagem = db.Column(db.String(50), nullable=False)