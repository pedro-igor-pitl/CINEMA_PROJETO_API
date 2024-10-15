class LoginDTO:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
    def __repr__(self):
        return f'<LoginDTO email={self.email}>'