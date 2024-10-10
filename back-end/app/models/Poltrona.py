# Modelo para a entidade Poltrona
class Poltrona(db.Model):
    __tablename__ = 'poltrona'
    id_poltrona = db.Column(db.Integer, primary_key=True)
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), nullable=False)
    tipo_poltrona = db.Column(db.String(50), nullable=False)
    posicao = db.Column(db.String(50), nullable=False)