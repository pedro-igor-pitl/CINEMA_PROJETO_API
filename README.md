# CINEMA_PROJETO_API

## 🎬 Tópicos Especiais em Programação Web - NP2

# 📚 Sumário
1.  [**Participantes**](#participantes)
2.  [**Descrição do Projeto**](#descrição-do-projeto)
3.  [**Arquitetura do Projeto**](#arquitetura-do-projeto-modelo-em-camadas)
4.  [**CRUD Implementado**](#crud-implementado)
5.  [**Tecnologias Utilizadas**](#tecnologias-utilizadas)
6.  [**Estrutura de Pastas**](#estrutura-de-pastas)
7.  [**Documentação com Swagger**](#documentação-com-swagger)
8.  [**Como Executar o Projeto**](#como-executar-o-projeto)
---

## Participantes

### ° Pedro Igor Torres Luz 
- **LinkedIn**: [Pedro Igor Torres Luz](https://www.linkedin.com/in/pedro-igor-torres-luz)
- **GitHub**: [pedro-igor-pitl](https://github.com/pedro-igor-pitl)

### ° Pietra Bezerra 
- **LinkedIn**: [Pietra Bezerra](https://www.linkedin.com/in/pietrabezerra/)
- **GitHub**: [piet2b](https://github.com/piet2b)



# Descrição do Projeto
### Este projeto é uma **API RESTful** desenvolvida para gerenciar informações relacionadas à compra de ingressos de um cinema. A API foi construída seguindo as melhores práticas de desenvolvimento backend, permitindo operações de **CRUD** (Criar, Ler, Atualizar, Deletar) de maneira eficiente. O sistema integra-se a um banco de dados relacional, o **PostgreSQL**, para armazenamento e manipulação dos dados.
---
# Arquitetura do Projeto: Modelo em Camadas
### A aplicação segue uma **arquitetura em camadas**, que oferece uma separação clara das responsabilidades e facilita o desenvolvimento, manutenção e escalabilidade. A divisão por camadas é uma abordagem essencial para organizar projetos maiores, pois permite que cada parte da aplicação seja alterada ou expandida sem impactar outras partes, favorecendo a reutilização e a modularidade.

### Camadas utilizadas:
1. **Configuração**: Configurações gerais do projeto e conexão com o banco de dados.
2. **Controladores (Controllers)**: Definem as rotas da API e são responsáveis por gerenciar as requisições e respostas HTTP.
3. **Documentação (Doc)**: Documentação da API utilizando Swagger, incluindo especificações e guias de uso.
4. **Data Transfer Objects (DTO)**: Objetos que ajudam na transferência de dados entre as camadas da aplicação.
5. **Modelos (Model)**: Mapeamento das entidades do banco de dados usando **SQLAlchemy**, representando as tabelas e relações.
6. **Repositórios (Repositories)**: Executam operações de CRUD no banco de dados de forma isolada, centralizando o acesso aos dados.
7. **Serviços (Services)**: Implementam a lógica de negócios e manipulam os dados recebidos dos controladores antes de serem persistidos ou retornados.
---
# CRUD Implementado
### A API permite a manipulação de dados para as seguintes entidades:
- **Filmes**
- **Sessões**
- **Ingressos**
- **Poltronas**
- **Salas**
- **Usuários**
---
# Tecnologias Utilizadas
- **Python**: Linguagem de programação utilizada para o desenvolvimento da API.
- **Flask**: Framework web que facilita a criação de APIs em Python.
- **SQLAlchemy**: ORM (Object Relational Mapping) que simplifica a interação com o banco de dados relacional.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar os dados.
- **Swagger**: Ferramenta para documentação interativa da API, permitindo a visualização das rotas disponíveis e a realização de testes.
- **Blueprint**: Organização das rotas em módulos, facilitando a modularização e o gerenciamento de endpoints.
- **JSON**: Formato de dados utilizado para comunicação entre o cliente e o servidor.
---
# Estrutura de Pastas
Clique na seta da pasta "📁 CINEMA_PROJETO_API/"
<details>
<summary>📁 CINEMA_PROJETO_API/</summary>
<details>
  <summary>📁 .idea/</summary>
  Configurações do ambiente de desenvolvimento.
</details>

<details>
  <summary>📁 app/</summary>
  Código principal da aplicação.

  <details>
    <summary>📁 __pycache__/</summary>
    Arquivos de cache do Python.
  </details>

  <details>
  <summary>📁 config/</summary>
  Configurações gerais e de banco de dados.

  <details>
    <summary>📁 __pycache__/</summary>
    Arquivos de cache do Python.
  </details>
  
  - 📄 [__init__.py](#init.py) - Inicializador do pacote `config`.
  - 🗄️ [database.py](#database.py) - Configuração e conexão com o banco de dados PostgreSQL.
</details>
  <details>
  <summary>📁 controller/</summary>
  Controladores responsáveis pelas rotas da API.

  <details>
      <summary>📁 __pycache__/</summary>
      Arquivos de cache do Python.
    </details>

  - 📄 [__init__.py](#init.py) - Inicializador do pacote `controller`.
  - 📄 [controllerFilme.py](#controllerFilme) - Controlador para as rotas relacionadas aos filmes.
  - 📄 [controllerIngresso.py](#controllerIngresso) - Controlador para as rotas relacionadas aos ingressos.
  - 📄 [controllerPoltrona.py](#controllerPoltrona) - Controlador para as rotas relacionadas às poltronas.
  - 📄 [controllerSala.py](#controllerSala) - Controlador para as rotas relacionadas às salas.
  - 📄 [controllerSessao.py](#controllerSessao) - Controlador para as rotas relacionadas às sessões.
  - 📄 [controllerUsuario.py](#controllerUsuario) - Controlador para as rotas relacionadas aos usuários.
  </details>

  <details>
    <summary>📁 doc/</summary>
    Documentação adicional da API.

  <details>
    <summary>📁 __pycache__/</summary>
      Arquivos de cache do Python.
    </details>

  - 📄 [swagger.json](#swagger.json) - Arquivo de definição das rotas da API em formato JSON para o Swagger.
  - 📄 [swagger.py](#swagger.py) - Script para configurar o Swagger na aplicação.
  </details>

  <details>
  <summary>📁 dto/</summary>
    Data Transfer Objects, que ajudam na transferência de dados entre as camadas da aplicação.

  <details>
      <summary>📁 __pycache__/</summary>
      Arquivos de cache do Python.
    </details>

  - 📄 [__init__.py](#init.py) - Inicializador do pacote `dto`.
  - 📄 [dtoFilme.py](#dtoFilme) - DTO para dados relacionados aos filmes.
  - 📄 [dtoIngresso.py](#dtoIngresso) - DTO para dados relacionados aos ingressos.
  - 📄 [dtoPoltrona.py](#dtoPoltrona) - DTO para dados relacionados às poltronas.
  - 📄 [dtoSala.py](#dtoSala) - DTO para dados relacionados às salas.
  - 📄 [dtoSessao.py](#dtoSessao) - DTO para dados relacionados às sessões.
  - 📄 [dtoUsuario.py](#dtoUsuario) - DTO para dados relacionados aos usuários.
  </details>

  <details>
  <summary>📁 model/</summary>
    Modelos que representam as tabelas do banco de dados.

  <details>
      <summary>📁 __pycache__/</summary>
      Arquivos de cache do Python.
    </details>

  - 📄 [__init__.py](#init.py) - Inicializador do pacote `model`.
  - 📄 [modelFilme.py](#modelFilme) - Modelo para a tabela de filmes.
  - 📄 [modelIngresso.py](#modelIngresso) - Modelo para a tabela de ingressos.
  - 📄 [modelPoltrona.py](#modelPoltrona) - Modelo para a tabela de poltronas.
  - 📄 [modelSala.py](#modelSala) - Modelo para a tabela de salas.
  - 📄 [modelSessao.py](#modelSessao) - Modelo para a tabela de sessões.
  - 📄 [modelUsuario.py](#modelUsuario) - Modelo para a tabela de usuários.
  </details>

  <details>
  <summary>📁 repository/</summary>
    Classes para acessar o banco de dados e executar operações CRUD.

  <details>
      <summary>📁 __pycache__/</summary>
      Arquivos de cache do Python.
    </details>

  - 📄 [__init__.py](#init.py) - Inicializador do pacote `repository`.
  - 📄 [repositoryFilme.py](#repositoryFilme) - Repositório para operações com filmes.
  - 📄 [repositoryIngresso.py](#repositoryIngresso) - Repositório para operações com ingressos.
  - 📄 [repositoryPoltrona.py](#repositoryPoltrona) - Repositório para operações com poltronas.
  - 📄 [repositorySala.py](#repositorySala) - Repositório para operações com salas.
  - 📄 [repositorySessao.py](#repositorySessao) - Repositório para operações com sessões.
  - 📄 [repositoryUsuario.py](#repositoryUsuario) - Repositório para operações com usuários.
  </details>

  <details>
  <summary>📁 service/</summary>
    Lógica de negócios e manipulação de dados.

  <details>
      <summary>📁 __pycache__/</summary>
      Arquivos de cache do Python.
    </details>

  - 📄 [__init__.py](#init.py) - Inicializador do pacote `service`.
  - 📄 [serviceFilme.py](#serviceFilme) - Serviço para lógica de negócios de filmes.
  - 📄 [serviceIngresso.py](#serviceIngresso) - Serviço para lógica de negócios de ingressos.
  - 📄 [servicePoltrona.py](#servicePoltrona) - Serviço para lógica de negócios de poltronas.
  - 📄 [serviceSala.py](#serviceSala) - Serviço para lógica de negócios de salas.
  - 📄 [serviceSessao.py](#serviceSessao) - Serviço para lógica de negócios de sessões.
  - 📄 [serviceUsuario.py](#serviceUsuario) - Serviço para lógica de negócios de usuários.
  </details>

  - 📄 [__init__.py](#init.py) - Inicializador do pacote `app`.
</details>

<details>
  <summary>📁 Banco de dados/</summary>
  Scripts e arquivos relacionados ao banco de dados.

  - 🗄️ [codigo_banco.sql](#codigo_banco.sql) - Script SQL para inicialização e estruturação do banco de dados PostgreSQL.
</details>

<details>
  <summary>📁 front-end/</summary>
  Arquivos e recursos do frontend.
</details>

<details>
  <summary>📁 Prototipo - Figma/</summary>
  Prototipação do design.
</details>

- ⚙️ [.gitattributes](#gitattributes) - Configuração de atributos para controle de versão.
- 🚀 [app.py](#app.py) - Arquivo principal que inicia a aplicação Flask.
- 📜 [LICENSE](#license) - Licença do projeto.
- 📘 [README.md](#readme.md) - Sumário do projeto.
</details>

---
# Documentação com Swagger
### A API possui uma documentação interativa gerada pelo Swagger, que facilita a visualização das rotas disponíveis e a realização de testes. Para acessar a documentação, siga os passos abaixo:

1. **Executar a aplicação**: Certifique-se de que a aplicação Flask está em execução. Você pode iniciar a aplicação com o comando:

    ```bash
    flask run
    ```

2. **Acessar a documentação**: Abra o seu navegador e navegue até o seguinte endereço:

    ```
    http://localhost:5000/swagger
    ```

Nesta interface, você encontrará informações detalhadas sobre as rotas da API, incluindo métodos HTTP, parâmetros de entrada e formatos de resposta. O Swagger permite que você teste as rotas diretamente da interface, facilitando o desenvolvimento e a integração com outras aplicações.

---
# Como Executar o Projeto

Para executar a API, siga os passos abaixo:

## Pré-requisitos

Antes de executar este projeto, certifique-se de ter os seguintes pré-requisitos instalados:

1. **Python** (versão 3.6 ou superior):
   - Você pode baixar o Python em [python.org](https://www.python.org/downloads/).

2. **pip** (gerenciador de pacotes do Python):
   - O pip geralmente é instalado automaticamente com o Python. Para verificar se você já tem o pip, execute:
     ```bash
     pip --version
     ```

3. **Visual Studio Code** (ou outro editor de código de sua preferência):
   - Faça o download em [code.visualstudio.com](https://code.visualstudio.com/).

4. **Flask**:
   - Você pode instalar o Flask usando pip:
     ```bash
     pip install Flask
     ```

5. **Flask-Swagger**:
   - Para integrar documentação Swagger, instale a biblioteca correspondente:
     ```bash
     pip install flask-swagger-ui
     ```

6. **PostgreSQL** (banco de dados):
   - Certifique-se de ter o PostgreSQL instalado e em execução. Você pode baixar em [postgresql.org](https://www.postgresql.org/download/).

7. **SQLAlchemy**:
   - Instale o SQLAlchemy usando pip:
     ```bash
     pip install SQLAlchemy
     ```

8. **Driver do PostgreSQL para SQLAlchemy**:
   - Para que o SQLAlchemy se conecte ao PostgreSQL, você precisará do driver `psycopg2`:
     ```bash
     pip install psycopg2
     ```

9. **QR Code**:
    - Para gerar códigos QR, instale a biblioteca `qrcode` com suporte a `PIL`:
      ```bash
      pip install qrcode[pil]
      ```
## Instalação

Após garantir que todos os pré-requisitos estão instalados:

# Instale as dependências
## pip install Flask flask-swagger-ui SQLAlchemy psycopg2 qrcode[pil]

### Passos para Execução

1. **Clone o Repositório**

   Clone este repositório em sua máquina local utilizando o comando:
      ```bash 
      git clone https://github.com/pedro-igor-pitl/CINEMA_PROJETO_API.git
2. **Abra o VS Code**
   Abra o Visual Studio Code e navegue até o diretório do seu projeto.

3. **Instale as Dependências**
  Com o ambiente virtual ativado, instale as dependências conforme indicado anteriormente.
  
4. **Inicie o Aplicativo**
    Execute o aplicativo com o comando:
      ```bash 
      python app.py

5. **Configuração do Banco de Dados**
    ### Crie um banco de dados: Abra o terminal do PostgreSQL e crie o banco de dados:
    ```bash
    CREATE DATABASE cinema_projeto_api;

6. **Configurar a conexão com o banco de dados: No arquivo app.py, configure as seguintes linhas com suas credenciais:**
    ```bash
        # Configuração do banco de dados
      senha = ''  # Substitua pela sua senha real
      app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://postgres:{senha}@localhost:5432/cinema_projeto_api' #Coloque o nome que tiver salvo no seu banco de dados
      app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
