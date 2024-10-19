from flask import Blueprint, request, jsonify
from ..service.servicePoltrona import ServicePoltrona

# Define a Blueprint for poltrona
poltrona_bp = Blueprint('poltrona_bp', __name__, template_folder='templates')

# Instância do repositório de poltrona
service_poltrona = ServicePoltrona()

@poltrona_bp.route('/poltrona', methods=['POST'])
def criar_poltrona():
    data = request.json
    qt_poltrona = data.get('qt_poltrona')
    id_sessao = data.get('id_sessao')

    if qt_poltrona is None or id_sessao is None:
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    nova_poltrona = Poltrona(
        qt_poltrona=qt_poltrona,
        id_sessao=id_sessao
    )

    poltrona_salva = service_poltrona.save(nova_poltrona)
    return jsonify({"message": "Poltrona criada com sucesso.", "poltrona": poltrona_salva.id_poltrona}), 201

@poltrona_bp.route('/poltrona/<int:id_poltrona>', methods=['GET'])
def obter_poltrona(id_poltrona):
    poltrona = service_poltrona.find_by_id(id_poltrona)
    if poltrona:
        return jsonify({
            "id_poltrona": poltrona.id_poltrona,
            "qt_poltrona": poltrona.qt_poltrona,
            "id_sessao": poltrona.id_sessao
        }), 200
    else:
        return jsonify({"error": "Poltrona não encontrada."}), 404

@poltrona_bp.route('/poltronas', methods=['GET'])
def listar_poltronas():
    poltronas = service_poltrona.find_all()
    poltronas_list = [
        {
            "id_poltrona": poltrona.id_poltrona,
            "qt_poltrona": poltrona.qt_poltrona,
            "id_sessao": poltrona.id_sessao
        }
        for poltrona in poltronas
    ]
    return jsonify(poltronas_list), 200

@poltrona_bp.route('/poltrona/<int:id_poltrona>', methods=['PUT'])
def atualizar_poltrona(id_poltrona):
    data = request.json
    poltrona_existente = service_poltrona.find_by_id(id_poltrona)
    if not poltrona_existente:
        return jsonify({"error": "Poltrona não encontrada."}), 404

    poltrona_existente.qt_poltrona = data.get('qt_poltrona', poltrona_existente.qt_poltrona)
    poltrona_existente.id_sessao = data.get('id_sessao', poltrona_existente.id_sessao)

    poltrona_atualizada = service_poltrona.update(poltrona_existente)
    return jsonify({"message": "Poltrona atualizada com sucesso.", "poltrona": poltrona_atualizada.id_poltrona}), 200

@poltrona_bp.route('/poltrona/<int:id_poltrona>', methods=['DELETE'])
def deletar_poltrona(id_poltrona):
    poltrona_existente = service_poltrona.find_by_id(id_poltrona)
    if not poltrona_existente:
        return jsonify({"error": "Poltrona não encontrada."}), 404

    service_poltrona.delete(id_poltrona)
    return jsonify({"message": "Poltrona deletada com sucesso."}), 200
