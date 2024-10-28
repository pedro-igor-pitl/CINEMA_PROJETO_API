from flask import Blueprint, request, jsonify, abort, send_file
from io import BytesIO
import base64
from PIL import Image
from ..config.database import db
from ..service.serviceIngresso import ServiceIngresso
from ..dto.dtoIngresso import IngressoDTO

# Criação do Blueprint para o controller de ingresso
ingresso_bp = Blueprint('ingresso_bp', __name__, template_folder='templates')

# Instância do serviço de ingresso
service_ingresso = ServiceIngresso(db)

from flask import abort, send_file
from io import BytesIO
import base64
from PIL import Image

# Rota para obter o QR code em base64 (GET)
@ingresso_bp.route('/ingressos/<int:id_ingresso>/qrcode', methods=['GET'])
def obter_qrcode(id_ingresso):
    ingresso_dto = service_ingresso.obter_ingresso_por_id(id_ingresso)
    
    # Verifica se o ingresso foi encontrado e se tem QR code
    if not ingresso_dto:
        abort(404, description="Ingresso não encontrado")
    
    if not ingresso_dto.qrcode:
        abort(404, description="QR code não encontrado")

    try:
        image_data = base64.b64decode(ingresso_dto.qrcode)
        image = Image.open(BytesIO(image_data))
    except Exception as e:
        abort(404, description="QR code não encontrado ou inválido.")
    
    # Retorna a imagem como resposta HTTP
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    buffered.seek(0)
    
    return send_file(buffered, mimetype="image/png", as_attachment=True, download_name="qrcode.png")


# Rota para criar um novo ingresso (POST)
@ingresso_bp.route('/ingressos', methods=['POST'])
def criar_ingresso():
    data = request.get_json()

    # Cria o DTO com os dados recebidos, sem incluir o campo qrcode
    ingresso_dto = IngressoDTO(
        id_usuario=data.get('id_usuario'),
        id_sala=data.get('id_sala'),
        id_poltrona=data.get('id_poltrona'),
        data_pedido=data.get('data_pedido')
    )

    # Verifica se todos os campos obrigatórios foram fornecidos
    if not (ingresso_dto.id_usuario and ingresso_dto.id_sala and ingresso_dto.id_poltrona and ingresso_dto.data_pedido):
        return jsonify({"error": "Todos os campos são obrigatórios."}), 400

    # Cria o ingresso usando o DTO, o qrcode será gerado automaticamente no ServiceIngresso
    novo_ingresso_dto = service_ingresso.criar_ingresso(ingresso_dto)
    
    # Decodifica o QR code em base64 para exibir
    if novo_ingresso_dto.qrcode:
        image_data = base64.b64decode(novo_ingresso_dto.qrcode)
        image = Image.open(BytesIO(image_data))

        # Exibe a imagem
        image.show()

    return jsonify(novo_ingresso_dto.to_dict()), 201


# Rota para obter um ingresso pelo ID (GET)
@ingresso_bp.route('/ingressos/<int:id_ingresso>', methods=['GET'])
def obter_ingresso(id_ingresso):
    ingresso_dto = service_ingresso.obter_ingresso_por_id(id_ingresso)
    if not ingresso_dto:
        abort(404, description="Ingresso não encontrado")
    return jsonify(ingresso_dto.to_dict())

# Rota para listar todos os ingressos (GET)
@ingresso_bp.route('/ingressos', methods=['GET'])
def listar_ingressos():
    ingressos_dtos = service_ingresso.listar_ingressos()
    return jsonify([ingresso.to_dict() for ingresso in ingressos_dtos])

# Rota para atualizar um ingresso existente (PUT)
@ingresso_bp.route('/ingressos/<int:id_ingresso>', methods=['PUT'])
def atualizar_ingresso(id_ingresso):
    data = request.get_json()

    # Cria o DTO com os dados recebidos
    ingresso_dto = IngressoDTO(
        id_usuario=data.get('id_usuario'),
        id_sala=data.get('id_sala'),
        id_poltrona=data.get('id_poltrona'),
        qrcode=data.get('qrcode'),  # Permite atualização do qrcode, se necessário
        data_pedido=data.get('data_pedido')
    )

    ingresso_atualizado_dto = service_ingresso.atualizar_ingresso(id_ingresso, ingresso_dto)

    if not ingresso_atualizado_dto:
        abort(404, description="Ingresso não encontrado")
    
    return jsonify(ingresso_atualizado_dto.to_dict()), 200

# Rota para deletar um ingresso (DELETE)
@ingresso_bp.route('/ingressos/<int:id_ingresso>', methods=['DELETE'])
def deletar_ingresso(id_ingresso):
    resultado = service_ingresso.deletar_ingresso(id_ingresso)
    if not resultado:
        abort(404, description="Ingresso não encontrado")
    return jsonify({"mensagem": "Ingresso deletado com sucesso"}), 204
