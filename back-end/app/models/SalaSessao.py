class SalaSessao(db.Model):
    __tablename__ = 'salaseccao'  # Corrigido para __tablename__

    id_sala = db.Column(db.Integer, db.ForeignKey('sala.id_sala'), primary_key=True)
    id_sessao = db.Column(db.Integer, db.ForeignKey('sessao.id_sessao'), primary_key=True)

    # Se quiser, você pode adicionar relacionamentos (opcional)
    sala = db.relationship('Sala', backref='salasessao')  # Adiciona relacionamento com a tabela Sala
    sessao = db.relationship('Sessao', backref='salasessao')  # Adiciona relacionamento com a tabela Sessao
