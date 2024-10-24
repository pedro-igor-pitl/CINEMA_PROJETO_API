class UsuarioDTO:
    def __init__(self, id_usuario=None, cpf=None, nome=None, email=None, senha=None):
        self.id_usuario = id_usuario
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.senha = senha  # Armazenar senha, se necessário

    @staticmethod
    def from_model(usuario):
        return UsuarioDTO(
            id_usuario=usuario.id_usuario,
            cpf=usuario.cpf,
            nome=usuario.nome,
            email=usuario.email,
            senha=usuario.senha  # Inclui a senha do modelo
        )

    def to_dict(self):
        # Retorna um dicionário, se necessário omitir a senha, você pode removê-la aqui
        return {
            'id_usuario': self.id_usuario,
            'cpf': self.cpf,
            'nome': self.nome,
            'email': self.email,
            'senha': self.senha  # Inclua senha se necessário, ou remova para ocultar
        }
