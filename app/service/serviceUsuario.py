from ..model.modelUsuario import Usuario
from ..repository.repositoryUsuario import RepositoryUsuario
from ..dto.dtoUsuario import UsuarioDTO

class ServiceUsuario:
    def __init__(self, db):
        self.repository_usuario = RepositoryUsuario(db)

    def criar_usuario(self, usuario_dto):
        """Cria um novo usuário e salva no banco de dados"""
        novo_usuario = Usuario(
            nome=usuario_dto.nome,
            email=usuario_dto.email,
            senha=usuario_dto.senha,
            cpf=usuario_dto.cpf
        )
        usuario_criado = self.repository_usuario.save(novo_usuario)
        return UsuarioDTO.from_model(usuario_criado)

    def obter_usuario_por_id(self, id_usuario):
        """Retorna um usuário pelo ID"""
        usuario = self.repository_usuario.find_by_id(id_usuario)
        if usuario:
            return UsuarioDTO.from_model(usuario)
        return None

    def listar_usuarios(self):
        """Retorna todos os usuários"""
        usuarios = self.repository_usuario.find_all()
        return [UsuarioDTO.from_model(usuario) for usuario in usuarios]

    def atualizar_usuario(self, id_usuario, usuario_dto):
        """Atualiza as informações de um usuário existente"""
        usuario = self.repository_usuario.find_by_id(id_usuario)
        if usuario:
            usuario.nome = usuario_dto.nome if usuario_dto.nome is not None else usuario.nome
            usuario.email = usuario_dto.email if usuario_dto.email is not None else usuario.email
            usuario.senha = usuario_dto.senha if usuario_dto.senha is not None else usuario.senha
            usuario.cpf = usuario_dto.cpf if usuario_dto.cpf is not None else usuario.cpf
            usuario_atualizado = self.repository_usuario.update(usuario)
            return UsuarioDTO.from_model(usuario_atualizado)
        return None

    def deletar_usuario(self, id_usuario):
        """Deleta um usuário pelo ID"""
        return self.repository_usuario.delete(id_usuario)
