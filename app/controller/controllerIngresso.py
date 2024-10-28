from flask import Blueprint, request, jsonify, abort
from ..config.database import db
from ..service.serviceIngresso import ServiceIngresso
from ..dto.dtoIngresso import IngressoDTO

# Criação do Blueprint para o controller de ingresso
ingresso_bp = Blueprint('ingresso_bp', __name__, template_folder='templates')

# Instância do serviço de ingresso
service_ingresso = ServiceIngresso(db)

# Rota para criar um novo ingresso (POST)
@ingresso_bp.route('/ingressos', methods=['POST'])
def criar_ingresso():
    data = request.get_json()

    # Cria o DTO com os dados recebidos, sem incluir o campo qrcode
    ingresso_dto = IngressoDTO(
        id_usuario=data.get('id_usuario'),
        id_sala=data.get('id_sala'),
        id_poltrona=data.get('id_poltrona'),
        data_pedido=data.get('data_pedido')
    )

    # Verifica se todos os campos obrigatórios foram fornecidos
    if not (ingresso_dto.id_usuario and ingresso_dto.id_sala and ingresso_dto.id_poltrona and ingresso_dto.data_pedido):
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    # Cria o ingresso usando o DTO, o qrcode será gerado automaticamente no ServiceIngresso
    novo_ingresso_dto = service_ingresso.criar_ingresso(ingresso_dto)
    
    return jsonify(novo_ingresso_dto.to_dict()), 201

# Rota para obter um ingresso pelo ID (GET)
@ingresso_bp.route('/ingressos/<int:id_ingresso>', methods=['GET'])
def obter_ingresso(id_ingresso):
    ingresso_dto = service_ingresso.obter_ingresso_por_id(id_ingresso)
    if not ingresso_dto:
        abort(404, description="Ingresso não encontrado")
    return jsonify(ingresso_dto.to_dict())

# Rota para listar todos os ingressos (GET)
@ingresso_bp.route('/ingressos', methods=['GET'])
def listar_ingressos():
    ingressos_dtos = service_ingresso.listar_ingressos()
    return jsonify([ingresso.to_dict() for ingresso in ingressos_dtos])

# Rota para atualizar um ingresso existente (PUT)
@ingresso_bp.route('/ingressos/<int:id_ingresso>', methods=['PUT'])
def atualizar_ingresso(id_ingresso):
    data = request.get_json()

    # Cria o DTO com os dados recebidos
    ingresso_dto = IngressoDTO(
        id_usuario=data.get('id_usuario'),
        id_sala=data.get('id_sala'),
        id_poltrona=data.get('id_poltrona'),
        qrcode=data.get('qrcode'),  # Permite atualização do qrcode, se necessário
        data_pedido=data.get('data_pedido')
    )

    ingresso_atualizado_dto = service_ingresso.atualizar_ingresso(id_ingresso, ingresso_dto)

    if not ingresso_atualizado_dto:
        abort(404, description="Ingresso não encontrado")
    
    return jsonify(ingresso_atualizado_dto.to_dict()), 200

# Rota para deletar um ingresso (DELETE)
@ingresso_bp.route('/ingressos/<int:id_ingresso>', methods=['DELETE'])
def deletar_ingresso(id_ingresso):
    resultado = service_ingresso.deletar_ingresso(id_ingresso)
    if not resultado:
        abort(404, description="Ingresso não encontrado")
    return jsonify({"mensagem": "Ingresso deletado com sucesso"}), 204
