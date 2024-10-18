from flask import Flask
from flasksqlalchemy import SQLAlchemy

db = SQLAlchemy()

def createapp():
    app = Flask(__name__)

    senha = 'pedroBD'
    # Configurações do banco de dados PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{senha}@localhost:5432/cinema_projeto_api'
    print("Chegou aqui")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = '2893cbbe206d16deedaa11ccdc9790a6'
    # Inicializa o SQLAlchemy com o app Flask
    db.init_app(app)

    return app