# Modelo para a tabela de relacionamento Sala e Ingresso
class SalaIngresso(db.Model):
    __tablename__ = 'salaingresso'
    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), primary_key=True)
    id_ingresso = db.Column(db.Integer, db.ForeignKey('ingresso.id_ingresso'), primary_key=True)