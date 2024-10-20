from flask import Blueprint, request, jsonify, abort
from ..config.database import db
from ..service.serviceIngresso import ServiceIngresso

# Criação do Blueprint para o controller de ingresso
ingresso_bp = Blueprint('ingresso_bp', __name__, template_folder='templates')

# Instância do serviço de ingresso
service_ingresso = ServiceIngresso(db)

# Rota para criar um novo ingresso (POST)
@ingresso_bp.route('/ingressos', methods=['POST'])
def criar_ingresso():
    data = request.get_json()
    id_usuario = data.get('id_usuario')
    id_sala = data.get('id_sala')
    id_poltrona = data.get('id_poltrona')
    qrcode = data.get('qrcode')
    data_pedido = data.get('data_pedido')

    if not (id_usuario and id_sala and id_poltrona and qrcode and data_pedido):
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    novo_ingresso = service_ingresso.criar_ingresso(
        id_usuario=id_usuario,
        id_sala=id_sala,
        id_poltrona=id_poltrona,
        qrcode=qrcode,
        data_pedido=data_pedido
    )
    return jsonify(novo_ingresso.to_dict()), 201

# Rota para obter um ingresso pelo ID (GET)
@ingresso_bp.route('/ingressos/<int:id_ingresso>', methods=['GET'])
def obter_ingresso(id_ingresso):
    ingresso = service_ingresso.obter_ingresso_por_id(id_ingresso)
    if not ingresso:
        abort(404, description="Ingresso não encontrado")
    return jsonify(ingresso.to_dict())

# Rota para listar todos os ingressos (GET)
@ingresso_bp.route('/ingressos', methods=['GET'])
def listar_ingressos():
    ingressos = service_ingresso.listar_ingressos()
    return jsonify([ingresso.to_dict() for ingresso in ingressos])

# Rota para atualizar um ingresso existente (PUT)
@ingresso_bp.route('/ingressos/<int:id_ingresso>', methods=['PUT'])
def atualizar_ingresso(id_ingresso):
    data = request.get_json()
    ingresso_atualizado = service_ingresso.atualizar_ingresso(
        id_ingresso,
        id_usuario=data.get('id_usuario'),
        id_sala=data.get('id_sala'),
        id_poltrona=data.get('id_poltrona'),
        qrcode=data.get('qrcode'),
        data_pedido=data.get('data_pedido')
    )

    if not ingresso_atualizado:
        abort(404, description="Ingresso não encontrado")
    
    return jsonify(ingresso_atualizado.to_dict()), 200

# Rota para deletar um ingresso (DELETE)
@ingresso_bp.route('/ingressos/<int:id_ingresso>', methods=['DELETE'])
def deletar_ingresso(id_ingresso):
    resultado = service_ingresso.deletar_ingresso(id_ingresso)
    if not resultado:
        abort(404, description="Ingresso não encontrado")
    return jsonify({"mensagem": "Ingresso deletado com sucesso"}), 204
