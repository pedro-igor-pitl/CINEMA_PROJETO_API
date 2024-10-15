from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from .database import db
from .dtos import LoginDTO
from .models import Usuario


def create_app():
    app = Flask(__name__)

    # Configurações do banco de dados PostgreSQL
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pedroBD@localhost:5432/cinema_projeto_api'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['SECRET_KEY'] = '2893cbbe206d16deedaa11ccdc9790a6'
    # Inicializa o SQLAlchemy com o app Flask
    db.init_app(app)

    @app.route('/', methods=['GET'])
    def cadastro():
        return render_template("cadastro.html")

    @app.route('/cadastrar', methods=['POST'])
    def cadastrar_usuario():
        nome = request.form['nome']
        cpf = request.form['cpf']
        email = request.form['email']
        senha = request.form['senha']

        # Verifique se todos os campos foram preenchidos
        if not (nome, cpf, email, senha):
            return jsonify({"error": "Todos os campos são obrigatórios."}), 400  # Bad Request

        # Verifica se o usuário já existe
        if Usuario.query.filter_by(email=email).first():
            return jsonify({"error": "Email já cadastrado."}), 409  # Conflict

        novo_usuario = Usuario(cpf=cpf, nome=nome, email=email, senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()

        flash('Usuário cadastrado com sucesso! Você pode fazer login agora.')
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']

            # Cria uma instância do LoginDTO
            login_data = LoginDTO(email=email, senha=senha)

            # Verifica se o usuário existe no banco de dados
            usuario = Usuario.query.filter_by(email=login_data.email, senha=login_data.senha).first()

            if usuario:
                flash('Login bem-sucedido! Bem-vindo, {}.'.format(usuario.nome))
                return redirect(url_for('home_filmes'))  # Redireciona para a página inicial ou dashboard do usuário
            else:
                flash('Email ou senha inválidos. Tente novamente.')
                return redirect(url_for('login'))  # Redireciona para a página de login

        return render_template("login.html")  # Renderiza a página de login

    @app.route('/home_filmes', methods=['GET'])
    def home_filmes():
        return render_template("home.html")

    return app
