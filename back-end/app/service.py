from app.repository import UsuarioRepository, FilmeRepository, IngressoRepository, PoltronaRepository, SessaoRepository, SalaRepository

class UsuarioService:
    def __init__(self, usuario_repository):
        self.usuario_repository = usuario_repository

    def criar_usuario(self, nome, email, senha, cpf):
        """Cria um novo usuário e salva no banco de dados"""
        novo_usuario = UsuarioRepository(nome=nome, email=email, senha=senha, cpf=cpf)
        return self.usuario_repository.save(novo_usuario)

    def obter_usuario_por_id(self, id_usuario):
        """Retorna um usuário pelo ID"""
        return self.usuario_repository.find_by_id(id_usuario)

    def listar_usuarios(self):
        """Retorna todos os usuários"""
        return self.usuario_repository.find_all()

    def atualizar_usuario(self, id_usuario, nome=None, email=None, senha=None, cpf=None):
        """Atualiza as informações de um usuário existente"""
        usuario = self.usuario_repository.find_by_id(id_usuario)
        if usuario:
            usuario.nome = nome if nome is not None else usuario.nome
            usuario.email = email if email is not None else usuario.email
            usuario.senha = senha if senha is not None else usuario.senha
            usuario.cpf = cpf if cpf is not None else usuario.cpf
            return self.usuario_repository.update(usuario)
        return None

    def deletar_usuario(self, id_usuario):
        """Deleta um usuário pelo ID"""
        return self.usuario_repository.delete(id_usuario)


class FilmeService:
    def __init__(self, filme_repository):
        self.filme_repository = filme_repository

    def criar_filme(self, nome_filme, descricao, caminho_img, duracao, genero, data_lancamento):
        """Cria um novo filme e salva no banco de dados"""
        novo_filme = FilmeRepository(nome_filme=nome_filme, descricao=descricao, 
                           caminho_img=caminho_img, duracao=duracao, 
                           genero=genero, data_lancamento=data_lancamento)
        return self.filme_repository.save(novo_filme)

    def obter_filme_por_id(self, id_filme):
        """Retorna um filme pelo ID"""
        return self.filme_repository.find_by_id(id_filme)

    def listar_filmes(self):
        """Retorna todos os filmes"""
        return self.filme_repository.find_all()

    def atualizar_filme(self, id_filme, nome_filme=None, descricao=None, caminho_img=None, 
                        duracao=None, genero=None, data_lancamento=None):
        """Atualiza as informações de um filme existente"""
        filme = self.filme_repository.find_by_id(id_filme)
        if filme:
            filme.nome_filme = nome_filme if nome_filme is not None else filme.nome_filme
            filme.descricao = descricao if descricao is not None else filme.descricao
            filme.caminho_img = caminho_img if caminho_img is not None else filme.caminho_img
            filme.duracao = duracao if duracao is not None else filme.duracao
            filme.genero = genero if genero is not None else filme.genero
            filme.data_lancamento = data_lancamento if data_lancamento is not None else filme.data_lancamento
            return self.filme_repository.update(filme)
        return None

    def deletar_filme(self, id_filme):
        """Deleta um filme pelo ID"""
        return self.filme_repository.delete(id_filme)


class IngressoService:
    def __init__(self, ingresso_repository):
        self.ingresso_repository = ingresso_repository

    def criar_ingresso(self, id_usuario, id_sala, id_poltrona, qrcode, data_pedido):
        """Cria um novo ingresso e salva no banco de dados"""
        novo_ingresso = IngressoRepository(
            id_usuario=id_usuario,
            id_sala=id_sala,
            id_poltrona=id_poltrona,
            qrcode=qrcode,
            data_pedido=data_pedido
        )
        return self.ingresso_repository.save(novo_ingresso)

    def obter_ingresso_por_id(self, id_ingresso):
        """Retorna um ingresso pelo ID"""
        return self.ingresso_repository.find_by_id(id_ingresso)

    def listar_ingressos(self):
        """Retorna todos os ingressos"""
        return self.ingresso_repository.find_all()

    def atualizar_ingresso(self, id_ingresso, id_usuario=None, id_sala=None, 
                           id_poltrona=None, qrcode=None, data_pedido=None):
        """Atualiza as informações de um ingresso existente"""
        ingresso = self.ingresso_repository.find_by_id(id_ingresso)
        if ingresso:
            ingresso.id_usuario = id_usuario if id_usuario is not None else ingresso.id_usuario
            ingresso.id_sala = id_sala if id_sala is not None else ingresso.id_sala
            ingresso.id_poltrona = id_poltrona if id_poltrona is not None else ingresso.id_poltrona
            ingresso.qrcode = qrcode if qrcode is not None else ingresso.qrcode
            ingresso.data_pedido = data_pedido if data_pedido is not None else ingresso.data_pedido
            return self.ingresso_repository.update(ingresso)
        return None

    def deletar_ingresso(self, id_ingresso):
        """Deleta um ingresso pelo ID"""
        return self.ingresso_repository.delete(id_ingresso)


class PoltronaService:
    def __init__(self, poltrona_repository):
        self.poltrona_repository = poltrona_repository

    def criar_poltrona(self, posicao, tipo_poltrona, id_sala):
        """Cria uma nova poltrona e salva no banco de dados"""
        nova_poltrona = PoltronaRepository(
            posicao=posicao,
            tipo_poltrona=tipo_poltrona,
            id_sala=id_sala
        )
        return self.poltrona_repository.save(nova_poltrona)

    def obter_poltrona_por_id(self, id_poltrona):
        """Retorna uma poltrona pelo ID"""
        return self.poltrona_repository.find_by_id(id_poltrona)

    def listar_poltronas(self):
        """Retorna todas as poltronas"""
        return self.poltrona_repository.find_all()

    def atualizar_poltrona(self, id_poltrona, posicao=None, tipo_poltrona=None, id_sala=None):
        """Atualiza as informações de uma poltrona existente"""
        poltrona = self.poltrona_repository.find_by_id(id_poltrona)
        if poltrona:
            poltrona.posicao = posicao if posicao is not None else poltrona.posicao
            poltrona.tipo_poltrona = tipo_poltrona if tipo_poltrona is not None else poltrona.tipo_poltrona
            poltrona.id_sala = id_sala if id_sala is not None else poltrona.id_sala
            return self.poltrona_repository.update(poltrona)
        return None

    def deletar_poltrona(self, id_poltrona):
        """Deleta uma poltrona pelo ID"""
        return self.poltrona_repository.delete(id_poltrona)

class SessaoService:
    def __init__(self, sessao_repository):
        self.sessao_repository = sessao_repository

    def criar_sessao(self, data, id_sala, preco, linguagem):
        """Cria uma nova sessão e salva no banco de dados"""
        nova_sessao = SessaoRepository(
            data=data,
            id_sala=id_sala,
            preco=preco,
            linguagem=linguagem
        )
        return self.sessao_repository.save(nova_sessao)

    def obter_sessao_por_id(self, id_sessao):
        """Retorna uma sessão pelo ID"""
        return self.sessao_repository.find_by_id(id_sessao)

    def listar_sessoes(self):
        """Retorna todas as sessões"""
        return self.sessao_repository.find_all()

    def atualizar_sessao(self, id_sessao, data=None, id_sala=None, preco=None, linguagem=None):
        """Atualiza as informações de uma sessão existente"""
        sessao = self.sessao_repository.find_by_id(id_sessao)
        if sessao:
            sessao.data = data if data is not None else sessao.data
            sessao.id_sala = id_sala if id_sala is not None else sessao.id_sala
            sessao.preco = preco if preco is not None else sessao.preco
            sessao.linguagem = linguagem if linguagem is not None else sessao.linguagem
            return self.sessao_repository.update(sessao)
        return None

    def deletar_sessao(self, id_sessao):
        """Deleta uma sessão pelo ID"""
        return self.sessao_repository.delete(id_sessao)


class SalaService:
    def __init__(self, sala_repository):
        self.sala_repository = sala_repository

    def criar_sala(self, qt_poltrona, id_sessao):
        """Cria uma nova sala e salva no banco de dados"""
        nova_sala = SalaRepository(
            qt_poltrona=qt_poltrona,
            id_sessao=id_sessao
        )
        return self.sala_repository.save(nova_sala)

    def obter_sala_por_id(self, id_sala):
        """Retorna uma sala pelo ID"""
        return self.sala_repository.find_by_id(id_sala)

    def listar_salas(self):
        """Retorna todas as salas"""
        return self.sala_repository.find_all()

    def atualizar_sala(self, id_sala, qt_poltrona=None, id_sessao=None):
        """Atualiza as informações de uma sala existente"""
        sala = self.sala_repository.find_by_id(id_sala)
        if sala:
            sala.qt_poltrona = qt_poltrona if qt_poltrona is not None else sala.qt_poltrona
            sala.id_sessao = id_sessao if id_sessao is not None else sala.id_sessao
            return self.sala_repository.update(sala)
        return None

    def deletar_sala(self, id_sala):
        """Deleta uma sala pelo ID"""
        return self.sala_repository.delete(id_sala)
