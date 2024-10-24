# dtos.py
class UsuarioDTO:
    def __init__(self, id_usuario, cpf, nome, email):
        self.id_usuario = id_usuario
        self.cpf = cpf
        self.nome = nome
        self.email = email

    @staticmethod
    def from_model(usuario):
        return UsuarioDTO(
            id_usuario=usuario.id_usuario,
            cpf=usuario.cpf,
            nome=usuario.nome,
            email=usuario.email
        )

    def to_dict(self):
        return {
            'id_usuario': self.id_usuario,
            'cpf': self.cpf,
            'nome': self.nome,
            'email': self.email
        }
