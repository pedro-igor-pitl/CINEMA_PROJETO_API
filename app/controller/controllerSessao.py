from flask import Blueprint, request, jsonify
from ..service.serviceSessao import SessaoService


# Criação do Blueprint para o controller de sessão
sessao_bp = Blueprint('sessao_bp', __name__, template_folder='templates')

# Instância do repositório de sessão
service_sessao = SessaoService()

@sessao_bp.route('/sessao', methods=['POST'])
def criar_sessao():
    data = request.json
    data_sessao = data.get('data')
    id_sala = data.get('id_sala')
    preco = data.get('preco')
    linguagem = data.get('linguagem')

    if not (data_sessao and id_sala and preco and linguagem):
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    nova_sessao = Sessao(
        data=data_sessao,
        id_sala=id_sala,
        preco=preco,
        linguagem=linguagem
    )

    sessao_salva = service_sessao.save(nova_sessao)
    return jsonify({"message": "Sessão criada com sucesso.", "sessao": sessao_salva.id_sessao}), 201

@sessao_bp.route('/sessao/<int:id_sessao>', methods=['GET'])
def obter_sessao(id_sessao):
    sessao = service_sessao.find_by_id(id_sessao)
    if sessao:
        return jsonify({
            "id_sessao": sessao.id_sessao,
            "data": sessao.data,
            "id_sala": sessao.id_sala,
            "preco": sessao.preco,
            "linguagem": sessao.linguagem
        }), 200
    else:
        return jsonify({"error": "Sessão não encontrada."}), 404

@sessao_bp.route('/sessoes', methods=['GET'])
def listar_sessoes():
    sessoes = service_sessao.find_all()
    sessoes_list = [
        {
            "id_sessao": sessao.id_sessao,
            "data": sessao.data,
            "id_sala": sessao.id_sala,
            "preco": sessao.preco,
            "linguagem": sessao.linguagem
        }
        for sessao in sessoes
    ]
    return jsonify(sessoes_list), 200

@sessao_bp.route('/sessao/<int:id_sessao>', methods=['PUT'])
def atualizar_sessao(id_sessao):
    data = request.json
    sessao_existente = service_sessao.find_by_id(id_sessao)
    if not sessao_existente:
        return jsonify({"error": "Sessão não encontrada."}), 404

    sessao_existente.data = data.get('data', sessao_existente.data)
    sessao_existente.id_sala = data.get('id_sala', sessao_existente.id_sala)
    sessao_existente.preco = data.get('preco', sessao_existente.preco)
    sessao_existente.linguagem = data.get('linguagem', sessao_existente.linguagem)

    sessao_atualizada = service_sessao.update(sessao_existente)
    return jsonify({"message": "Sessão atualizada com sucesso.", "sessao": sessao_atualizada.id_sessao}), 200

@sessao_bp.route('/sessao/<int:id_sessao>', methods=['DELETE'])
def deletar_sessao(id_sessao):
    sessao_existente = service_sessao.find_by_id(id_sessao)
    if not sessao_existente:
        return jsonify({"error": "Sessão não encontrada."}), 404

    service_sessao.delete(id_sessao)
    return jsonify({"message": "Sessão deletada com sucesso."}), 200