from .database import db

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)

class Filme(db.Model):
    __tablename__ = 'filme'
    id_filme = db.Column(db.Integer, primary_key=True)
    nome_filme = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    caminho_img = db.Column(db.String(255))
    duracao = db.Column(db.String, nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    data_lancamento = db.Column(db.String(20))