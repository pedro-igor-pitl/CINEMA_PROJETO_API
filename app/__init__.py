from flask import Flask
from flask_migrate import Migrate
from .config.database import db
from .controller.controllerUsuario import usuario_bp
from .controller.controllerFilme import filme_bp
from .controller.controllerIngresso import ingresso_bp
from .controller.controllerPoltrona import poltrona_bp
from .controller.controllerSala import sala_bp
from .controller.controllerSessao import sessao_bp

def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados
    senha = 'pedroBD'  # Alterar conforme necessário
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{senha}@localhost:5432/cinema_projeto_api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = '159b46e8db762436db3b2e7f545e8dfc'

    db.init_app(app)
    
    # Inicializa o Flask-Migrate
    migrate = Migrate(app, db)

    # Registra blueprints
    app.register_blueprint(usuario_bp)
    app.register_blueprint(filme_bp)
    app.register_blueprint(ingresso_bp)
    app.register_blueprint(poltrona_bp)
    app.register_blueprint(sala_bp)
    app.register_blueprint(sessao_bp)

    return app
