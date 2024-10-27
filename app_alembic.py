from ..CINEMA_PROJETO_API.app import create_app  # Substitua pelo seu aplicativo
from flask_migrate import upgrade

app = create_app()  # Crie uma instância do seu aplicativo

with app.app_context():
    upgrade()  # Execute as migrações
