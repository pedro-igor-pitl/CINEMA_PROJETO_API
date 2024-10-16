from ..model.modelUsuario import Usuario


class repositoryUsuario:
    def __init__(self, db_session):
        self.db_session = db_session

    def save(self, usuario):
        """Salva um novo usuário no banco de dados"""
        self.db_session.add(usuario)
        self.db_session.commit()
        return usuario

    def find_by_id(self, id_usuario):
        """Encontra um usuário pelo ID"""
        return self.db_session.query(Usuario).filter_by(id_usuario=id_usuario).first()

    def find_all(self):
        """Retorna todos os usuários"""
        return self.db_session.query(Usuario).all()

    def update(self, usuario):
        """Atualiza as informações de um usuário existente"""
        existing_usuario = self.find_by_id(usuario.id_usuario)
        if existing_usuario:
            existing_usuario.nome = usuario.nome
            existing_usuario.email = usuario.email
            existing_usuario.senha = usuario.senha
            existing_usuario.cpf = usuario.cpf
            self.db_session.commit()
        return existing_usuario

    def delete(self, id_usuario):
        """Deleta um usuário pelo ID"""
        usuario = self.find_by_id(id_usuario)
        if usuario:
            self.db_session.delete(usuario)
            self.db_session.commit()
        return usuario


