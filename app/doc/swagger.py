from flask import Blueprint, jsonify, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
import os

SWAGGER_URL = '/swagger'  # URL onde o Swagger estará disponível
API_URL = '/doc/swagger.json'  # Caminho para o arquivo swagger.json

swagger_bp = Blueprint('swagger_bp', __name__)

# Configuração do blueprint para o Swagger
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Cinema API"  # Nome da aplicação que aparecerá no Swagger
    }
)

swagger_bp.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Rota para servir o arquivo swagger.json
@swagger_bp.route('/doc/swagger.json')
def swagger_json():
    return send_from_directory(os.path.dirname(__file__), 'swagger.json')
