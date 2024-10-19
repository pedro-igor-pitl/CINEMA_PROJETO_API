from ..model.modelUsuario import Usuario

class RepositoryUsuario:
    def __init__(self, db):
        self.db = db

    def save(self, usuario):
        """Salva um novo usuário no banco de dados"""
        self.db.session.add(usuario)
        self.db.session.commit()
        return usuario

    def find_by_id(self, id_usuario):
        """Encontra um usuário pelo ID"""
        return self.db.session.query(Usuario).filter_by(id_usuario=id_usuario).first()

    def find_all(self):
        """Retorna todos os usuários"""
        return self.db.session.query(Usuario).all()

    def update(self, usuario):
        """Atualiza as informações de um usuário existente"""
        existing_usuario = self.find_by_id(usuario.id_usuario)
        if existing_usuario:
            existing_usuario.nome = usuario.nome
            existing_usuario.email = usuario.email
            existing_usuario.senha = usuario.senha
            existing_usuario.cpf = usuario.cpf
            self.db.session.commit()
        return existing_usuario

    def delete(self, id_usuario):
        """Deleta um usuário pelo ID"""
        usuario = self.find_by_id(id_usuario)
        if usuario:
            self.db.session.delete(usuario)
            self.db.session.commit()
        return usuario


