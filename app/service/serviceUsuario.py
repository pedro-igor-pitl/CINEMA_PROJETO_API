from ..model.modelUsuario import Usuario

class serviceUsuario:
    def __init__(self, repositoryUsuario):
        self.repositoryUsuario = repositoryUsuario

    def criar_usuario(self, nome, email, senha, cpf):
        """Cria um novo usuário e salva no banco de dados"""
        novo_usuario = Usuario(nome=nome, email=email, senha=senha, cpf=cpf)
        return self.repositoryUsuario.save(novo_usuario)

    def obter_usuario_por_id(self, id_usuario):
        """Retorna um usuário pelo ID"""
        return self.repositoryUsuario.find_by_id(id_usuario)

    def listar_usuarios(self):
        """Retorna todos os usuários"""
        return self.repositoryUsuario.find_all()

    def atualizar_usuario(self, id_usuario, nome=None, email=None, senha=None, cpf=None):
        """Atualiza as informações de um usuário existente"""
        usuario = self.repositoryUsuario.find_by_id(id_usuario)
        if usuario:
            usuario.nome = nome if nome is not None else usuario.nome
            usuario.email = email if email is not None else usuario.email
            usuario.senha = senha if senha is not None else usuario.senha
            usuario.cpf = cpf if cpf is not None else usuario.cpf
            return self.repositoryUsuario.update(usuario)
        return None

    def deletar_usuario(self, id_usuario):
        """Deleta um usuário pelo ID"""
        return self.repositoryUsuario.delete(id_usuario)
