from flask import Blueprint, request, jsonify
from ..config.database import db
from ..service.serviceSala import ServiceSala
from ..dto.dtoSala import SalaDTO  # Importando o DTO

sala_bp = Blueprint('sala_bp', __name__, template_folder='templates')

# Instância do serviço de sala
service_sala = ServiceSala(db)

@sala_bp.route('/sala', methods=['POST'])
def criar_sala():
    data = request.json
    qt_poltrona = data.get('qt_poltrona')
    id_sessao = data.get('id_sessao')

    if qt_poltrona is None or id_sessao is None:
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    sala_dto = SalaDTO(qt_poltrona=qt_poltrona, id_sessao=id_sessao)  # Usando o DTO
    nova_sala = service_sala.criar_sala(sala_dto)

    return jsonify({"message": "Sala criada com sucesso.", "sala": nova_sala.to_dict()}), 201

@sala_bp.route('/sala/<int:id_sala>', methods=['GET'])
def obter_sala(id_sala):
    sala_dto = service_sala.obter_sala_por_id(id_sala)
    if sala_dto:
        return jsonify(sala_dto.to_dict()), 200  # Retornando os dados do DTO
    else:
        return jsonify({"error": "Sala não encontrada."}), 404

@sala_bp.route('/salas', methods=['GET'])
def listar_salas():
    salas_dto = service_sala.listar_salas()
    salas_list = [sala.to_dict() for sala in salas_dto]  # Convertendo cada DTO para dicionário
    return jsonify(salas_list), 200

@sala_bp.route('/sala/<int:id_sala>', methods=['PUT'])
def atualizar_sala(id_sala):
    data = request.json
    sala_existente = service_sala.obter_sala_por_id(id_sala)
    if not sala_existente:
        return jsonify({"error": "Sala não encontrada."}), 404

    # Atualizando os campos apenas se os novos valores forem fornecidos
    qt_poltrona = data.get('qt_poltrona', sala_existente.qt_poltrona)
    id_sessao = data.get('id_sessao', sala_existente.id_sessao)

    sala_dto = SalaDTO(id_sala=id_sala, qt_poltrona=qt_poltrona, id_sessao=id_sessao)
    sala_atualizada = service_sala.atualizar_sala(id_sala, sala_dto)

    return jsonify({"message": "Sala atualizada com sucesso.", "sala": sala_atualizada.to_dict()}), 200

@sala_bp.route('/sala/<int:id_sala>', methods=['DELETE'])
def deletar_sala(id_sala):
    sala_existente = service_sala.obter_sala_por_id(id_sala)
    if not sala_existente:
        return jsonify({"error": "Sala não encontrada."}), 404

    service_sala.deletar_sala(id_sala)
    return jsonify({"message": "Sala deletada com sucesso."}), 200
