# Modelo para a entidade Ingresso
class Ingresso(db.Model):
    __tablename__ = 'ingresso'
    id_ingresso = db.Column(db.Integer, primary_key=True)
    qr_code = db.Column(db.String(200), nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    data_pedido = db.Column(db.DateTime, nullable=False)