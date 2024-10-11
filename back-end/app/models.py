
from app.database import db  # Certifique-se de importar o db corretamente

class Usuario(db.Model):  # A classe herda de db.Model

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Modelo para a entidade Usuario
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f'<Usuario {self.id_usuario}>'

# Modelo para a entidade Filme
class Filme(db.Model):
    __tablename__ = 'filme'
    id_filme = db.Column(db.Integer, primary_key=True)
    nome_filme = db.Column(db.String(200), nullable=False)
    data_filme = db.Column(db.String(20), nullable=False) 
    duracao = db.Column(db.String(20), nullable=False)  
    genero = db.Column(db.String(50), nullable=False)
    caminho_img = db.Column(db.String(255), nullable=True)
    descricao = db.Column(db.Text, nullable=True)

# Modelo para a entidade Sala
class Sala(db.Model):
    __tablename__ = 'sala'
    id_sala = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float, nullable=False)
    qt_poltrona = db.Column(db.Integer, nullable=False)

# Modelo para a entidade Poltrona
class Poltrona(db.Model):
    __tablename__ = 'poltrona'
    id_poltrona = db.Column(db.Integer, primary_key=True)
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), nullable=False)
    tipo_poltrona = db.Column(db.String(50), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)

# Modelo para a entidade Sessao
class Sessao(db.Model):
    __tablename__ = 'sessao'
    id_sessao = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(20), nullable=False)
    preco = db.Column(db.Float, nullable=False)
    linguagem = db.Column(db.String(50), nullable=False)
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), nullable=False)

# Modelo para a tabela de relacionamento Sessao e Filme
class SessaoFilme(db.Model):
    __tablename__ = 'sessaofilme'
    id_sessao = db.Column(db.Integer, db.ForeignKey('sessao.id_sessao'), primary_key=True)
    id_filme = db.Column(db.Integer, db.ForeignKey('filme.id_filme'), primary_key=True)

# Modelo para a entidade Ingresso
class Ingresso(db.Model):
    __tablename__ = 'ingresso'
    id_ingresso = db.Column(db.Integer, primary_key=True)
    qr_code = db.Column(db.String(200), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    data_pedido = db.Column(db.DateTime, nullable=False)

# Modelo para a tabela de relacionamento Sala e Ingresso
class SalaIngresso(db.Model):
    __tablename__ = 'salaingresso'
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), primary_key=True)
    id_ingresso = db.Column(db.Integer, db.ForeignKey('ingresso.id_ingresso'), primary_key=True)

