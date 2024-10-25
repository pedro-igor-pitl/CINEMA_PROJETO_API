from sqlalchemy import Column, Integer, String, Text
from ..config.database import db

class Filme(db.Model):
    __tablename__ = 'filme'
    
    id_filme = Column(Integer, primary_key=True)
    nome_filme = Column(String(200), nullable=False)
    descricao = Column(Text, nullable=True)
    caminho_img = Column(String(255))
    duracao = Column(String, nullable=False)
    genero = Column(String(100), nullable=False)
    data_lancamento = Column(String(20))

    '''def to_dict(self):
        return {
            'id_filme': self.id_filme,
            'nome_filme': self.nome_filme,
            'descricao': self.descricao,
            'caminho_img': self.caminho_img,
            'duracao': self.duracao,
            'genero': self.genero,
            'data_lancamento': self.data_lancamento,
        }'''
