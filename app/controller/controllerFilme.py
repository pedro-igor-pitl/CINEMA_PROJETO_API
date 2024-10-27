from flask import Blueprint, request, jsonify, abort
from ..config.database import db
from ..service.serviceFilme import ServiceFilme
from ..repository.repositoryFilme import RepositoryFilme
from ..dto.dtoFilme import FilmeDTO

# Criação do Blueprint para o controller de filme
filme_bp = Blueprint('filme_bp', __name__, template_folder='templates')

# Instância do repositório de filme
repository_filme = RepositoryFilme(db)
# Instância do serviço de filme
service_filme = ServiceFilme(repository_filme)

# Rota para criar um novo filme (POST)
@filme_bp.route('/filmes', methods=['POST'])
def criar_filme():
    data = request.get_json()
    
    # Cria o DTO com os dados recebidos
    filme_dto = FilmeDTO(
        nome_filme=data.get('nome_filme'),
        descricao=data.get('descricao'),
        caminho_img=data.get('caminho_img'),
        duracao=data.get('duracao'),
        genero=data.get('genero'),
        data_lancamento=data.get('data_lancamento')
    )

    if not (filme_dto.nome_filme and filme_dto.descricao and filme_dto.caminho_img and filme_dto.duracao and filme_dto.genero and filme_dto.data_lancamento):
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    # Cria o filme usando o DTO
    novo_filme_dto = service_filme.criar_filme(filme_dto)
    return jsonify(novo_filme_dto.to_dict()), 201

# Rota para obter um filme pelo ID (GET)
@filme_bp.route('/filmes/<int:id_filme>', methods=['GET'])
def obter_filme(id_filme):
    filme_dto = service_filme.obter_filme_por_id(id_filme)
    if not filme_dto:
        abort(404, description="Filme não encontrado")
    return jsonify(filme_dto.to_dict())

# Rota para listar todos os filmes (GET)
@filme_bp.route('/filmes', methods=['GET'])
def listar_filmes():
    filmes_dtos = service_filme.listar_filmes()
    return jsonify([filme.to_dict() for filme in filmes_dtos])

# Rota para atualizar um filme existente (PUT)
@filme_bp.route('/filmes/<int:id_filme>', methods=['PUT'])
def atualizar_filme(id_filme):
    data = request.get_json()

    # Cria o DTO com os dados recebidos
    filme_dto = FilmeDTO(
        nome_filme=data.get('nome_filme'),
        descricao=data.get('descricao'),
        caminho_img=data.get('caminho_img'),
        duracao=data.get('duracao'),
        genero=data.get('genero'),
        data_lancamento=data.get('data_lancamento'),
        autor_filme=data.get('autor_filme')
    )

    filme_atualizado_dto = service_filme.atualizar_filme(id_filme, filme_dto)

    if not filme_atualizado_dto:
        abort(404, description="Filme não encontrado")
    
    return jsonify(filme_atualizado_dto.to_dict()), 200

# Rota para deletar um filme (DELETE)
@filme_bp.route('/filmes/<int:id_filme>', methods=['DELETE'])
def deletar_filme(id_filme):
    resultado = service_filme.deletar_filme(id_filme)
    if not resultado:
        abort(404, description="Filme não encontrado")
    return jsonify({"mensagem": "Filme deletado com sucesso"}), 204
