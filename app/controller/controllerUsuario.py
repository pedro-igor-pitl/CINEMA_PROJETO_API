from flask import Blueprint, jsonify, request, abort
from ..config.database import db
from ..service.serviceUsuario import ServiceUsuario

usuario_bp = Blueprint('usuario_bp', __name__, template_folder='templates')

service_usuario = ServiceUsuario(db)

# Rota para obter todos os usuários (GET)
@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios = service_usuario.listar_usuarios()
    return jsonify([usuario.to_dict() for usuario in usuarios])

# Rota para obter um usuário pelo ID (GET)
@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obter_usuario(id_usuario):
    usuario = service_usuario.obter_usuario_por_id(id_usuario)
    if usuario is None:
        abort(404, description="Usuário não encontrado")
    return jsonify(usuario.to_dict())

# Rota para criar um novo usuário (POST)
@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    cpf = dados.get('cpf')

    novo_usuario = service_usuario.criar_usuario(nome, email, senha, cpf)
    return jsonify(novo_usuario.to_dict()), 201

# Rota para atualizar um usuário existente (PUT)
@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def atualizar_usuario(id_usuario):
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    cpf = dados.get('cpf')

    usuario_atualizado = service_usuario.atualizar_usuario(id_usuario, nome, email, senha, cpf)
    if usuario_atualizado is None:
        abort(404, description="Usuário não encontrado")
    return jsonify(usuario_atualizado.to_dict())

# Rota para deletar um usuário (DELETE)
@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def deletar_usuario(id_usuario):
    resultado = service_usuario.deletar_usuario(id_usuario)
    if not resultado:
        abort(404, description="Usuário não encontrado")
    return jsonify({"mensagem": "Usuário deletado com sucesso"}), 204
