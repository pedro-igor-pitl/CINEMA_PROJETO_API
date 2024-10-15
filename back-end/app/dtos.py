class LoginDTO:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
    def __repr__(self):
        return f'<LoginDTO email={self.email}>'

class filmeDestaqueDTO:
    def __init__(self, caminho_img):
        self.caminho_img = caminho_img
    def __repr__(self):
        return f'<filmeDestaqueDTO caminho_img={self.caminho_img}>'

class filmeEmCartazDTO:
    def __init__(self, caminho_img, nome_filme):
        self.caminho_img = caminho_img
        self.nome_filme = nome_filme
    def __repr__(self):
        return f'<filmeEmCartazDTO caminho_img={self.caminho_img}>'