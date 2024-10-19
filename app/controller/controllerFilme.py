from flask import Blueprint, jsonify, request, abort
from ..config.database import db
from ..service.serviceFilme import ServiceFilme

filme_bp = Blueprint('filme_bp', __name__, template_folder='templates')


service_filme = ServiceFilme(db)

@filme_bp.route('/filmes', methods=['GET'])
def listar_filmes():
    filmes = service_filme.listar_filmes()
    return jsonify([filme.to_dict() for filme in filmes])

# Rota para obter um filme pelo ID (GET)
@filme_bp.route('/filmes/<int:id_filme>', methods=['GET'])
def obter_filme(id_filme):
    filme = service_filme.obter_filme_por_id(id_filme)
    if filme is None:
        abort(404, description="Filme não encontrado")
    return jsonify(filme.to_dict())

# Rota para criar um novo filme (POST)
@filme_bp.route('/filmes', methods=['POST'])
def criar_filme():
    dados = request.get_json()
    nome_filme = dados.get('nome_filme')
    descricao = dados.get('descricao')
    caminho_img = dados.get('caminho_img')
    duracao = dados.get('duracao')
    genero = dados.get('genero')
    data_lancamento = dados.get('data_lancamento')

    novo_filme = service_filme.criar_filme(nome_filme, descricao, caminho_img, duracao, genero, data_lancamento)
    return jsonify(novo_filme.to_dict()), 201

# Rota para atualizar um filme existente (PUT)
@filme_bp.route('/filmes/<int:id_filme>', methods=['PUT'])
def atualizar_filme(id_filme):
    dados = request.get_json()
    nome_filme = dados.get('nome_filme')
    descricao = dados.get('descricao')
    caminho_img = dados.get('caminho_img')
    duracao = dados.get('duracao')
    genero = dados.get('genero')
    data_lancamento = dados.get('data_lancamento')

    filme_atualizado = service_filme.atualizar_filme(id_filme, nome_filme, descricao, caminho_img, duracao, genero, data_lancamento)
    if filme_atualizado is None:
        abort(404, description="Filme não encontrado")
    return jsonify(filme_atualizado.to_dict())

# Rota para deletar um filme (DELETE)
@filme_bp.route('/filmes/<int:id_filme>', methods=['DELETE'])
def deletar_filme(id_filme):
    resultado = service_filme.deletar_filme(id_filme)
    if resultado:
        abort(404, description="Filme não encontrado")
    return jsonify({"mensagem": "Filme deletado com sucesso"}), 204