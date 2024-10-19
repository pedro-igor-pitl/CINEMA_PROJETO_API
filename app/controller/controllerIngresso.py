from flask import Blueprint, request, jsonify
from ..service.serviceIngresso import ServiceIngresso

# Criação do Blueprint para o controller de ingresso
ingresso_bp = Blueprint('ingresso', __name__)

# Instância do repositório de ingresso
service_ingresso = ServiceIngresso()

@ingresso_bp.route('/ingresso', methods=['POST'])
def criar_ingresso():
    data = request.json
    id_usuario = data.get('id_usuario')
    id_sala = data.get('id_sala')
    id_poltrona = data.get('id_poltrona')
    qrcode = data.get('qrcode')
    data_pedido = data.get('data_pedido')

    if not (id_usuario and id_sala and id_poltrona and qrcode and data_pedido):
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    novo_ingresso = Ingresso(
        id_usuario=id_usuario,
        id_sala=id_sala,
        id_poltrona=id_poltrona,
        qrcode=qrcode,
        data_pedido=data_pedido
    )

    ingresso_salvo = service_ingresso.save(novo_ingresso)
    return jsonify({"message": "Ingresso criado com sucesso.", "ingresso": ingresso_salvo.id_ingresso}), 201

@ingresso_bp.route('/ingresso/<int:id_ingresso>', methods=['GET'])
def obter_ingresso(id_ingresso):
    ingresso = service_ingresso.find_by_id(id_ingresso)
    if ingresso:
        return jsonify({
            "id_ingresso": ingresso.id_ingresso,
            "id_usuario": ingresso.id_usuario,
            "id_sala": ingresso.id_sala,
            "id_poltrona": ingresso.id_poltrona,
            "qrcode": ingresso.qrcode,
            "data_pedido": ingresso.data_pedido
        }), 200
    else:
        return jsonify({"error": "Ingresso não encontrado."}), 404

@ingresso_bp.route('/ingressos', methods=['GET'])
def listar_ingressos():
    ingressos = service_ingresso.find_all()
    ingressos_list = [
        {
            "id_ingresso": ingresso.id_ingresso,
            "id_usuario": ingresso.id_usuario,
            "id_sala": ingresso.id_sala,
            "id_poltrona": ingresso.id_poltrona,
            "qrcode": ingresso.qrcode,
            "data_pedido": ingresso.data_pedido
        }
        for ingresso in ingressos
    ]
    return jsonify(ingressos_list), 200

@ingresso_bp.route('/ingresso/<int:id_ingresso>', methods=['PUT'])
def atualizar_ingresso(id_ingresso):
    data = request.json
    ingresso_existente = service_ingresso.find_by_id(id_ingresso)
    if not ingresso_existente:
        return jsonify({"error": "Ingresso não encontrado."}), 404

    ingresso_existente.id_usuario = data.get('id_usuario', ingresso_existente.id_usuario)
    ingresso_existente.id_sala = data.get('id_sala', ingresso_existente.id_sala)
    ingresso_existente.id_poltrona = data.get('id_poltrona', ingresso_existente.id_poltrona)
    ingresso_existente.qrcode = data.get('qrcode', ingresso_existente.qrcode)
    ingresso_existente.data_pedido = data.get('data_pedido', ingresso_existente.data_pedido)

    ingresso_atualizado = service_ingresso.update(ingresso_existente)
    return jsonify({"message": "Ingresso atualizado com sucesso.", "ingresso": ingresso_atualizado.id_ingresso}), 200

@ingresso_bp.route('/ingresso/<int:id_ingresso>', methods=['DELETE'])
def deletar_ingresso(id_ingresso):
    ingresso_existente = service_ingresso.find_by_id(id_ingresso)
    if not ingresso_existente:
        return jsonify({"error": "Ingresso não encontrado."}), 404

    service_ingresso.delete(id_ingresso)
    return jsonify({"message": "Ingresso deletado com sucesso."}), 200
