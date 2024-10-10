from flask import Flask

from app.database import db  # Importando a instância db


def create_app():
    app = Flask(__name__)

    # Configurações do aplicativo (exemplo com PostgreSQL)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://meuusuario:senhadobanco@localhost:5432/meubanco'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Para desabilitar um aviso

    db.init_app(app)  # Inicializando o db com o app

    # Importar e registrar blueprints ou modelos
    with app.app_context():
        from app.models import Filme, Sala  # Isso deve incluir todos os modelos
        db.create_all()  # Cria todas as tabelas definidas

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app import routes
    app.register_blueprint(routes.bp)

    return app
