from flask import Blueprint, request, jsonify
from ..config.database import db
from ..service.serviceSessao import SessaoService
from ..dto.dtoSessao import SessaoDTO  # Importando o DTO

sessao_bp = Blueprint('sessao_bp', __name__, template_folder='templates')

# Instância do serviço de sessão
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

    # Criando o DTO a partir dos dados recebidos
    sessao_dto = SessaoDTO(
        data=data_sessao,
        id_sala=id_sala,
        preco=preco,
        linguagem=linguagem
    )

    # Criando a sessão usando o DTO
    sessao_salva = service_sessao.criar_sessao(sessao_dto.data, sessao_dto.id_sala, sessao_dto.preco, sessao_dto.linguagem)
    
    return jsonify({"message": "Sessão criada com sucesso.", "sessao": sessao_salva.to_dict()}), 201

@sessao_bp.route('/sessao/<int:id_sessao>', methods=['GET'])
def obter_sessao(id_sessao):
    sessao = service_sessao.obter_sessao_por_id(id_sessao)
    if sessao:
        # Convertendo o objeto para DTO e retornando seus dados
        sessao_dto = SessaoDTO.from_model(sessao)
        return jsonify(sessao_dto.to_dict()), 200
    else:
        return jsonify({"error": "Sessão não encontrada."}), 404

@sessao_bp.route('/sessoes', methods=['GET'])
def listar_sessoes():
    sessoes = service_sessao.listar_sessoes()
    # Convertendo cada sessão para DTO e devolvendo a lista de dicionários
    sessoes_list = [SessaoDTO.from_model(sessao).to_dict() for sessao in sessoes]
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
        sessao_dto = SessaoDTO.from_model(sessao_atualizada)
        return jsonify({"message": "Sessão atualizada com sucesso.", "sessao": sessao_dto.to_dict()}), 200
    return jsonify({"error": "Sessão não encontrada."}), 404

@sessao_bp.route('/sessao/<int:id_sessao>', methods=['DELETE'])
def deletar_sessao(id_sessao):
    if service_sessao.deletar_sessao(id_sessao):
        return jsonify({"message": "Sessão deletada com sucesso."}), 200
    return jsonify({"error": "Sessão não encontrada."}), 404
