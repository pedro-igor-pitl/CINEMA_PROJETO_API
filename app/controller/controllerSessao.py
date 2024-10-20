from flask import Blueprint, request, jsonify
from ..config.database import db
from ..service.serviceSessao import SessaoService
from ..model.modelSessao import Sessao  # Certifique-se de que esta importação está correta

sessao_bp = Blueprint('sessao_bp', __name__, template_folder='templates')

# Instância do repositório de sessão
service_sessao = SessaoService(db)

@sessao_bp.route('/sessao', methods=['POST'])
def criar_sessao():
    data = request.json
    data_sessao = data.get('data')
    id_sala = data.get('id_sala')
    preco = data.get('preco')
    linguagem = data.get('linguagem')

    if not (data_sessao and id_sala and preco and linguagem):
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    sessao_salva = service_sessao.criar_sessao(data_sessao, id_sala, preco, linguagem)
    return jsonify({"message": "Sessão criada com sucesso.", "sessao": sessao_salva.id_sessao}), 201

@sessao_bp.route('/sessao/<int:id_sessao>', methods=['GET'])
def obter_sessao(id_sessao):
    sessao = service_sessao.obter_sessao_por_id(id_sessao)
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
    sessoes = service_sessao.listar_sessoes()
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
    sessao_atualizada = service_sessao.atualizar_sessao(
        id_sessao,
        data.get('data'),
        data.get('id_sala'),
        data.get('preco'),
        data.get('linguagem')
    )
    if sessao_atualizada:
        return jsonify({"message": "Sessão atualizada com sucesso.", "sessao": sessao_atualizada.id_sessao}), 200
    return jsonify({"error": "Sessão não encontrada."}), 404

@sessao_bp.route('/sessao/<int:id_sessao>', methods=['DELETE'])
def deletar_sessao(id_sessao):
    if service_sessao.deletar_sessao(id_sessao):
        return jsonify({"message": "Sessão deletada com sucesso."}), 200
    return jsonify({"error": "Sessão não encontrada."}), 404
