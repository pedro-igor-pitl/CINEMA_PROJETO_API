from flask import Blueprint, jsonify, request, abort
from ..config.database import db
from ..service.serviceUsuario import ServiceUsuario
from ..dto.dtoUsuario import UsuarioDTO  # Certifique-se de ter o DTO definido

usuario_bp = Blueprint('usuario_bp', __name__, template_folder='templates')

service_usuario = ServiceUsuario(db)

# Rota para obter todos os usuários (GET)
@usuario_bp.route('/usuarios', methods=['GET'])
def listar_usuarios():
    usuarios_dto = service_usuario.listar_usuarios()
    return jsonify([usuario.to_dict() for usuario in usuarios_dto])

# Rota para obter um usuário pelo ID (GET)
@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['GET'])
def obter_usuario(id_usuario):
    usuario_dto = service_usuario.obter_usuario_por_id(id_usuario)
    if usuario_dto is None:
        abort(404, description="Usuário não encontrado")
    return jsonify(usuario_dto.to_dict())

# Rota para criar um novo usuário (POST)
@usuario_bp.route('/usuarios', methods=['POST'])
def criar_usuario():
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    cpf = dados.get('cpf')

    novo_usuario_dto = UsuarioDTO(nome=nome, email=email, senha=senha, cpf=cpf)  # Usando o DTO
    usuario_salvo = service_usuario.criar_usuario(novo_usuario_dto)
    return jsonify(usuario_salvo.to_dict()), 201

# Rota para atualizar um usuário existente (PUT)
@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['PUT'])
def atualizar_usuario(id_usuario):
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    cpf = dados.get('cpf')

    usuario_dto = UsuarioDTO(nome=nome, email=email, senha=senha, cpf=cpf)  # Usando o DTO
    usuario_atualizado_dto = service_usuario.atualizar_usuario(id_usuario, usuario_dto)
    if usuario_atualizado_dto is None:
        abort(404, description="Usuário não encontrado")
    return jsonify(usuario_atualizado_dto.to_dict())

# Rota para deletar um usuário (DELETE)
@usuario_bp.route('/usuarios/<int:id_usuario>', methods=['DELETE'])
def deletar_usuario(id_usuario):
    resultado = service_usuario.deletar_usuario(id_usuario)
    if not resultado:
        abort(404, description="Usuário não encontrado")
    return jsonify({"mensagem": "Usuário deletado com sucesso"}), 204
