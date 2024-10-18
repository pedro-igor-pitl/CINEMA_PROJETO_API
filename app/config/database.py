from flask import Flask
from flasksqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createapp():
    app = Flask(__name__)

    senha = 'Souz@105696'
    # Configurações do banco de dados PostgreSQL105696localhost
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{senha}@localhost:5432/cinema_api'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = '9d6a0f900ca80f21e659c6bcba698913'
    # Inicializa o SQLAlchemy com o app Flask
    db.init_app(app)

    return app