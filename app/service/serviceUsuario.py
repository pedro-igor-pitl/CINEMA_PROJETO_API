from ..model.modelUsuario import Usuario
from ..repository.repositoryUsuario import RepositoryUsuario
from ..dto.dtoUsuario import UsuarioDTO

class ServiceUsuario:
    def __init__(self, db):
        self.RepositoryUsuario = RepositoryUsuario(db)

    def criar_usuario(self, nome, email, senha, cpf):
        """Cria um novo usuário e salva no banco de dados"""
        novo_usuario = Usuario(nome=nome, email=email, senha=senha, cpf=cpf)
        usuario_criado = self.RepositoryUsuario.save(novo_usuario)
        return UsuarioDTO.from_model(usuario_criado)

    def obter_usuario_por_id(self, id_usuario):
        """Retorna um usuário pelo ID"""
        usuario = self.RepositoryUsuario.find_by_id(id_usuario)
        if usuario:
            return UsuarioDTO.from_model(usuario)
        return None

    def listar_usuarios(self):
        """Retorna todos os usuários"""
        usuarios = self.RepositoryUsuario.find_all()
        return [UsuarioDTO.from_model(usuario) for usuario in usuarios]

    def atualizar_usuario(self, id_usuario, nome=None, email=None, senha=None, cpf=None):
        """Atualiza as informações de um usuário existente"""
        usuario = self.RepositoryUsuario.find_by_id(id_usuario)
        if usuario:
            usuario.nome = nome if nome is not None else usuario.nome
            usuario.email = email if email is not None else usuario.email
            usuario.senha = senha if senha is not None else usuario.senha
            usuario.cpf = cpf if cpf is not None else usuario.cpf
            usuario_atualizado = self.RepositoryUsuario.update(usuario)
            return UsuarioDTO.from_model(usuario_atualizado)
        return None

    def deletar_usuario(self, id_usuario):
        """Deleta um usuário pelo ID"""
        return self.RepositoryUsuario.delete(id_usuario)
