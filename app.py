from app.config.database import db
from app.controller.controllerUsuario import usuario_bp
from app.controller.controllerFilme import filme_bp
from app.controller.controllerIngresso import ingresso_bp
from app.controller.controllerPoltrona import poltrona_bp
from app.controller.controllerSala import sala_bp
from app.controller.controllerSessao import sessao_bp
from app.doc.swagger import swagger_bp
from flask import Flask  

def create_app():
    app = Flask(__name__)
    
    senha = '1234' #PIETRA
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{senha}@localhost:5432/cinema_api' #PIETRA

    # senha = 'pedroBD' #PEDRO
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{senha}@localhost:5432/cinema_projeto_api' #PEDRO
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #python -c "import secrets; print(secrets.token_hex(16))" #gerar chave no terminal

    # app.config['SECRET_KEY'] = '159b46e8db762436db3b2e7f545e8dfc' #PEDRO
    app.config['SECRET_KEY'] = '9d6a0f900ca80f21e659c6bcba698913' #PIETRA
    

    db.init_app(app)
    app.register_blueprint(usuario_bp)
    app.register_blueprint(filme_bp)
    app.register_blueprint(ingresso_bp)
    app.register_blueprint(poltrona_bp)
    app.register_blueprint(sala_bp)
    app.register_blueprint(sessao_bp)
    app.register_blueprint(swagger_bp) 

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

