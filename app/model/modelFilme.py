from ..config.database import db

class Filme(db.Model):
    __tablename__ = 'filme'
    id_filme = db.Column(db.Integer, primary_key=True)
    nome_filme = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    caminho_img = db.Column(db.String(255))
    duracao = db.Column(db.String, nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    data_lancamento = db.Column(db.String(20))

class Ingresso(db.Model):
    __tablename__ = 'ingresso'
    id_ingresso = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), nullable=False)
    id_poltrona = db.Column(db.Integer, db.ForeignKey('poltrona.id_poltrona'), nullable=False)
    qrcode = db.Column(db.String(255), nullable=True)
    data_pedido = db.Column(db.String, nullable=True)

class Poltrona(db.Model):
    __tablename__ = 'poltrona'
    id_poltrona = db.Column(db.Integer, primary_key=True)
    posicao = db.Column(db.String(50), nullable=False)
    tipo_poltrona = db.Column(db.String(50), nullable=False)
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), nullable=False)

class Sessao(db.Model):
    __tablename__ = 'sessao'
    id_sessao = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(20), nullable=False)
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), nullable=False)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    linguagem = db.Column(db.String(50), nullable=False)

class Sala(db.Model):
    __tablename__ = 'sala'
    id_sala = db.Column(db.Integer, primary_key=True)
    qt_poltrona = db.Column(db.Integer, nullable=False)
    id_sessao = db.Column(db.Integer, db.ForeignKey('sessao.id_sessao'), nullable=False)
