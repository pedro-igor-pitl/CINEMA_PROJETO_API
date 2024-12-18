from flask import Blueprint, jsonify, request, abort
from ..config.database import db
from ..service.servicePoltrona import ServicePoltrona

# Define a Blueprint para poltrona
poltrona_bp = Blueprint('poltrona_bp', __name__, template_folder='templates')

# Instância do serviço de poltrona
service_poltrona = ServicePoltrona(db)

# Rota para criar uma nova poltrona (POST)
@poltrona_bp.route('/poltronas', methods=['POST'])
def criar_poltrona():
    dados = request.get_json()
    posicao = dados.get('posicao')
    tipo_poltrona = dados.get('tipo_poltrona')
    id_sala = dados.get('id_sala')

    if posicao is None or tipo_poltrona is None or id_sala is None:
        abort(400, description="Todos os campos são obrigatórios.")

    nova_poltrona_dto = service_poltrona.criar_poltrona(posicao, tipo_poltrona, id_sala)
    return jsonify(nova_poltrona_dto.to_dict()), 201

# Rota para obter uma poltrona pelo ID (GET)
@poltrona_bp.route('/poltronas/<int:id_poltrona>', methods=['GET'])
def obter_poltrona(id_poltrona):
    poltrona_dto = service_poltrona.obter_poltrona_por_id(id_poltrona)
    if poltrona_dto is None:
        abort(404, description="Poltrona não encontrada.")
    return jsonify(poltrona_dto.to_dict())

# Rota para listar todas as poltronas (GET)
@poltrona_bp.route('/poltronas', methods=['GET'])
def listar_poltronas():
    poltronas_dto = service_poltrona.listar_poltronas()
    return jsonify([poltrona.to_dict() for poltrona in poltronas_dto])

# Rota para atualizar uma poltrona existente (PUT)
@poltrona_bp.route('/poltronas/<int:id_poltrona>', methods=['PUT'])
def atualizar_poltrona(id_poltrona):
    dados = request.get_json()
    posicao = dados.get('posicao')
    tipo_poltrona = dados.get('tipo_poltrona')
    id_sala = dados.get('id_sala')

    poltrona_atualizada_dto = service_poltrona.atualizar_poltrona(id_poltrona, posicao, tipo_poltrona, id_sala)
    if poltrona_atualizada_dto is None:
        abort(404, description="Poltrona não encontrada.")
    return jsonify(poltrona_atualizada_dto.to_dict())

# Rota para deletar uma poltrona pelo ID (DELETE)
@poltrona_bp.route('/poltronas/<int:id_poltrona>', methods=['DELETE'])
def deletar_poltrona(id_poltrona):
    resultado = service_poltrona.deletar_poltrona(id_poltrona)
    
    if resultado:
        return jsonify({"mensagem": "Poltrona deletada com sucesso"}), 200
    else:
        abort(404, description="Poltrona não encontrada.")
