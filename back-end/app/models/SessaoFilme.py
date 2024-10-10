# Modelo para a tabela de relacionamento Sessao e Filme
class SessaoFilme(db.Model):
    __tablename__ = 'sessaofilme'
    id_sessao = db.Column(db.Integer, db.ForeignKey('sessao.id_sessao'), primary_key=True)
    id_filme = db.Column(db.Integer, db.ForeignKey('filme.id_filme'), primary_key=True)