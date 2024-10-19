from sqlalchemy import Column, Integer, String
from ..config.database import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'cpf': self.cpf,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha 
        }
