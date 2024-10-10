CREATE TABLE Usuario (
    id_usuario SERIAL PRIMARY KEY, 
    cpf VARCHAR(11) NOT NULL, 
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE, 
    senha VARCHAR(100) NOT NULL
);

CREATE TABLE Sala (
    id_sala SERIAL PRIMARY KEY,
    preco DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Poltrona (
    id_poltrona SERIAL PRIMARY KEY,
    posicao VARCHAR(50) NOT NULL,
    tipo_poltrona VARCHAR(50) NOT NULL,
    id_sala INT NOT NULL,
    FOREIGN KEY (id_sala) REFERENCES Sala(id_sala)
);

CREATE TABLE Filme (
    id_filme SERIAL PRIMARY KEY,
    nome_filme VARCHAR(200) NOT NULL,
    descricao TEXT,
    caminho_img VARCHAR(255),
    duracao TIME NOT NULL,
    genero VARCHAR(100) NOT NULL
);

CREATE TABLE Sessao (
    id_sessao SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    id_filme INT NOT NULL,
    id_sala INT NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    linguagem VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_filme) REFERENCES Filme(id_filme),
    FOREIGN KEY (id_sala) REFERENCES Sala(id_sala)
);

CREATE TABLE Ingresso (
    id_ingresso SERIAL PRIMARY KEY,
    id_usuario INT NOT NULL,
    id_sessao INT NOT NULL,
    id_sala INT NOT NULL,
    id_poltrona INT,
    qrcode VARCHAR(255),
    data_pedido DATE NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_sessao) REFERENCES Sessao(id_sessao),
    FOREIGN KEY (id_sala) REFERENCES Sala(id_sala),
    FOREIGN KEY (id_poltrona) REFERENCES Poltrona(id_poltrona)
);
CREATE TABLE SalaPoltrona (
    id_sala INT NOT NULL,
    id_poltrona INT NOT NULL,
    PRIMARY KEY (id_sala, id_poltrona),
    FOREIGN KEY (id_sala) REFERENCES Sala(id_sala),
    FOREIGN KEY (id_poltrona) REFERENCES Poltrona(id_poltrona)
);
CREATE TABLE SessaoFilme (
    id_sessao INT NOT NULL,
    id_filme INT NOT NULL,
    PRIMARY KEY (id_sessao, id_filme),
    FOREIGN KEY (id_sessao) REFERENCES Sessao(id_sessao),
    FOREIGN KEY (id_filme) REFERENCES Filme(id_filme)
);
CREATE TABLE SalaIngresso (
    id_sala INT NOT NULL,
    id_ingresso INT NOT NULL,
    PRIMARY KEY (id_sala, id_ingresso),
    FOREIGN KEY (id_sala) REFERENCES Sala(id_sala),
    FOREIGN KEY (id_ingresso) REFERENCES Ingresso(id_ingresso)
);
