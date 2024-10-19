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
    qt_poltrona = dados.get('qt_poltrona')
    id_sessao = dados.get('id_sessao')

    if qt_poltrona is None or id_sessao is None:
        abort(400, description="Todos os campos são obrigatórios.")

    nova_poltrona = service_poltrona.criar_poltrona(qt_poltrona, id_sessao)
    return jsonify(nova_poltrona.to_dict()), 201

# Rota para obter uma poltrona pelo ID (GET)
@poltrona_bp.route('/poltronas/<int:id_poltrona>', methods=['GET'])
def obter_poltrona(id_poltrona):
    poltrona = service_poltrona.obter_poltrona_por_id(id_poltrona)
    if poltrona is None:
        abort(404, description="Poltrona não encontrada.")
    return jsonify(poltrona.to_dict())

# Rota para listar todas as poltronas (GET)
@poltrona_bp.route('/poltronas', methods=['GET'])
def listar_poltronas():
    poltronas = service_poltrona.listar_poltronas()
    return jsonify([poltrona.to_dict() for poltrona in poltronas])

# Rota para atualizar uma poltrona existente (PUT)
@poltrona_bp.route('/poltronas/<int:id_poltrona>', methods=['PUT'])
def atualizar_poltrona(id_poltrona):
    dados = request.get_json()
    qt_poltrona = dados.get('qt_poltrona')
    id_sessao = dados.get('id_sessao')

    poltrona_atualizada = service_poltrona.atualizar_poltrona(id_poltrona, qt_poltrona, id_sessao)
    if poltrona_atualizada is None:
        abort(404, description="Poltrona não encontrada.")
    return jsonify(poltrona_atualizada.to_dict())

# Rota para deletar uma poltrona (DELETE)
@poltrona_bp.route('/poltronas/<int:id_poltrona>', methods=['DELETE'])
def deletar_poltrona(id_poltrona):
    resultado = service_poltrona.deletar_poltrona(id_poltrona)
    if not resultado:
        abort(404, description="Poltrona não encontrada.")
    return jsonify({"mensagem": "Poltrona deletada com sucesso"}), 204
