# Modelo para a entidade Sala
class Sala(db.Model):
    __tablename__ = 'sala'
    id_sala = db.Column(db.Integer, primary_key=True)
    preco = db.Column(db.Float, nullable=False)
    qt_poltrona = db.Column(db.Integer, nullable=False)