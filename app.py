from app.config.database import db
from app.controller.controllerUsuario import usuario_bp
from flask import Flask  

def create_app():
    app = Flask(__name__)
    
    senha = '1234'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{senha}@localhost:5432/cinema_api'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = '9d6a0f900ca80f21e659c6bcba698913'
    db.init_app(app)
    app.register_blueprint(usuario_bp)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

