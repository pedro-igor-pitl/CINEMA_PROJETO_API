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