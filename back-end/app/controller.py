from flask import Flask, jsonify, request, abort
from app.service import UsuarioService

app = Flask(__name__)
usuario_service = UsuarioService()

# Rota para obter todos os usuários (GET)
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = usuario_service.listar_usuarios()
    return jsonify([usuario.__dict__ for usuario in usuarios])

# Rota para obter um usuário pelo ID (GET)
@app.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obter_usuario(id_usuario):
    usuario = usuario_service.obter_usuario_por_id(id_usuario)
    if usuario is None:
        abort(404, description="Usuário não encontrado")
    return jsonify(usuario.__dict__)

# Rota para criar um novo usuário (POST)
@app.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    cpf = dados.get('cpf')

    novo_usuario = usuario_service.criar_usuario(nome, email, senha, cpf)
    return jsonify(novo_usuario.__dict__), 201

# Rota para atualizar um usuário existente (PUT)
@app.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def atualizar_usuario(id_usuario):
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    cpf = dados.get('cpf')

    usuario_atualizado = usuario_service.atualizar_usuario(id_usuario, nome, email, senha, cpf)
    if usuario_atualizado is None:
        abort(404, description="Usuário não encontrado")
    return jsonify(usuario_atualizado.__dict__)

# Rota para deletar um usuário (DELETE)
@app.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def deletar_usuario(id_usuario):
    resultado = usuario_service.deletar_usuario(id_usuario)
    if not resultado:
        abort(404, description="Usuário não encontrado")
    return jsonify({"mensagem": "Usuário deletado com sucesso"}), 204

from flask import Flask, jsonify, request, abort
from app.service import FilmeService

filme_service = FilmeService()  # Instancie com o repositório correto

# Rota para listar todos os filmes (GET)
@app.route('/filmes', methods=['GET'])
def listar_filmes():
    filmes = filme_service.listar_filmes()
    return jsonify([filme.__dict__ for filme in filmes])

# Rota para obter um filme pelo ID (GET)
@app.route('/filmes/<int:id_filme>', methods=['GET'])
def obter_filme(id_filme):
    filme = filme_service.obter_filme_por_id(id_filme)
    if filme is None:
        abort(404, description="Filme não encontrado")
    return jsonify(filme.__dict__)

# Rota para criar um novo filme (POST)
@app.route('/filmes', methods=['POST'])
def criar_filme():
    dados = request.get_json()
    nome_filme = dados.get('nome_filme')
    descricao = dados.get('descricao')
    caminho_img = dados.get('caminho_img')
    duracao = dados.get('duracao')
    genero = dados.get('genero')
    data_lancamento = dados.get('data_lancamento')

    novo_filme = filme_service.criar_filme(nome_filme, descricao, caminho_img, duracao, genero, data_lancamento)
    return jsonify(novo_filme.__dict__), 201

# Rota para atualizar um filme existente (PUT)
@app.route('/filmes/<int:id_filme>', methods=['PUT'])
def atualizar_filme(id_filme):
    dados = request.get_json()
    nome_filme = dados.get('nome_filme')
    descricao = dados.get('descricao')
    caminho_img = dados.get('caminho_img')
    duracao = dados.get('duracao')
    genero = dados.get('genero')
    data_lancamento = dados.get('data_lancamento')

    filme_atualizado = filme_service.atualizar_filme(id_filme, nome_filme, descricao, caminho_img, duracao, genero, data_lancamento)
    if filme_atualizado is None:
        abort(404, description="Filme não encontrado")
    return jsonify(filme_atualizado.__dict__)

# Rota para deletar um filme (DELETE)
@app.route('/filmes/<int:id_filme>', methods=['DELETE'])
def deletar_filme(id_filme):
    resultado = filme_service.deletar_filme(id_filme)
    if not resultado:
        abort(404, description="Filme não encontrado")
    return jsonify({"mensagem": "Filme deletado com sucesso"}), 204

if __name__ == '__main__':
    app.run(debug=True)



