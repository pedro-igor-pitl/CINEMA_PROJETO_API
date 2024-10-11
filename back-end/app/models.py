from app.database import db  # Certifique-se de importar o db corretamente

class Usuario(db.Model):  # A classe herda de db.Model
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Usuario {self.id_usuario}>'
