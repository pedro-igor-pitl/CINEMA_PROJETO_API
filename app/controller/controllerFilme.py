from flask import Flask, jsonify, request, abort
from app.service import serviceUsuario

@app.route('/filmes', methods=['GET'])
def listar_filmes():
    filmes = filme_service.listar_filmes()
    return jsonify([filme.__dict__ for filme in filmes])

# Rota para obter um filme pelo ID (GET)
@app.route('/filmes/<int:id_filme>', methods=['GET'])
def obter_filme(id_filme):
    filme = filme_service.obter_filme_por_id(id_filme)
    if filme is None:
        abort(404, description="Filme não encontrado")
    return jsonify(filme.__dict__)

# Rota para criar um novo filme (POST)
@app.route('/filmes', methods=['POST'])
def criar_filme():
    dados = request.get_json()
    nome_filme = dados.get('nome_filme')
    descricao = dados.get('descricao')
    caminho_img = dados.get('caminho_img')
    duracao = dados.get('duracao')
    genero = dados.get('genero')
    data_lancamento = dados.get('data_lancamento')

    novo_filme = filme_service.criar_filme(nome_filme, descricao, caminho_img, duracao, genero, data_lancamento)
    return jsonify(novo_filme.__dict__), 201

# Rota para atualizar um filme existente (PUT)
@app.route('/filmes/<int:id_filme>', methods=['PUT'])
def atualizar_filme(id_filme):
    dados = request.get_json()
    nome_filme = dados.get('nome_filme')
    descricao = dados.get('descricao')
    caminho_img = dados.get('caminho_img')
    duracao = dados.get('duracao')
    genero = dados.get('genero')
    data_lancamento = dados.get('data_lancamento')

    filme_atualizado = filme_service.atualizar_filme(id_filme, nome_filme, descricao, caminho_img, duracao, genero, data_lancamento)
    if filme_atualizado is None:
        abort(404, description="Filme não encontrado")
    return jsonify(filme_atualizado.__dict__)

# Rota para deletar um filme (DELETE)
@app.route('/filmes/<int:id_filme>', methods=['DELETE'])
def deletar_filme(id_filme):
    resultado = filme_service.deletar_filme(id_filme)
    if not resultado:
        abort(404, description="Filme não encontrado")
    return jsonify({"mensagem": "Filme deletado com sucesso"}), 204

if __name__ == '__main__':
    app.run(debug=True)