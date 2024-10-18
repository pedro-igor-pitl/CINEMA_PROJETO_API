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

