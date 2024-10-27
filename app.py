from app import create_app  # Importa a função create_app do pacote app

app = create_app()  # Inicializa a aplicação

if __name__ == '__main__':
    app.run(debug=True)  # Executa a aplicação
