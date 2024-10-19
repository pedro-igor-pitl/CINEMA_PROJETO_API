from flask import Blueprint, request, jsonify
from ..config.database import db
from ..service.serviceSala import ServiceSala

sala_bp = Blueprint('sala_bp', __name__, template_folder='templates')

# Instância do repositório de sala
service_sala = ServiceSala(db)

@sala_bp.route('/sala', methods=['POST'])
def criar_sala():
    data = request.json
    qt_poltrona = data.get('qt_poltrona')
    id_sessao = data.get('id_sessao')

    if qt_poltrona is None or id_sessao is None:
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    nova_sala = Sala(
        qt_poltrona=qt_poltrona,
        id_sessao=id_sessao
    )

    sala_salva = service_sala.save(nova_sala)
    return jsonify({"message": "Sala criada com sucesso.", "sala": sala_salva.id_sala}), 201

@sala_bp.route('/sala/<int:id_sala>', methods=['GET'])
def obter_sala(id_sala):
    sala = service_sala.find_by_id(id_sala)
    if sala:
        return jsonify({
            "id_sala": sala.id_sala,
            "qt_poltrona": sala.qt_poltrona,
            "id_sessao": sala.id_sessao
        }), 200
    else:
        return jsonify({"error": "Sala não encontrada."}), 404

@sala_bp.route('/salas', methods=['GET'])
def listar_salas():
    salas = service_sala.listar_salas()
    salas_list = [
        {
            "id_sala": sala.id_sala,
            "qt_poltrona": sala.qt_poltrona,
            "id_sessao": sala.id_sessao
        }
        for sala in salas
    ]
    return jsonify(salas_list), 200

@sala_bp.route('/sala/<int:id_sala>', methods=['PUT'])
def atualizar_sala(id_sala):
    data = request.json
    sala_existente = service_sala.find_by_id(id_sala)
    if not sala_existente:
        return jsonify({"error": "Sala não encontrada."}), 404

    sala_existente.qt_poltrona = data.get('qt_poltrona', sala_existente.qt_poltrona)
    sala_existente.id_sessao = data.get('id_sessao', sala_existente.id_sessao)

    sala_atualizada = service_sala.update(sala_existente)
    return jsonify({"message": "Sala atualizada com sucesso.", "sala": sala_atualizada.id_sala}), 200

@sala_bp.route('/sala/<int:id_sala>', methods=['DELETE'])
def deletar_sala(id_sala):
    sala_existente = service_sala.find_by_id(id_sala)
    if not sala_existente:
        return jsonify({"error": "Sala não encontrada."}), 404

    service_sala.delete(id_sala)
    return jsonify({"message": "Sala deletada com sucesso."}), 200
