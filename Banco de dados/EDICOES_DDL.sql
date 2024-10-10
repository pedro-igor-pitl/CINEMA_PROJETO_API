
ALTER TABLE Sala
ADD COLUMN qt_poltrona INT NOT NULL;

ALTER TABLE Sala
ADD COLUMN id_sessao INT,
ADD CONSTRAINT fk_sessao
FOREIGN KEY (id_sessao) REFERENCES Sessao(id_sessao);

ALTER TABLE Filme
ADD COLUMN data_filme DATE;

ALTER TABLE Ingresso
DROP COLUMN id_usuario;

ALTER TABLE Ingresso
ADD COLUMN id_filme INT,
ADD CONSTRAINT fk_filme
FOREIGN KEY (id_filme) REFERENCES Filme(id_filme);

ALTER TABLE Sessao
DROP COLUMN id_filme;

CREATE TABLE SalaSessao (
    id_sala INT NOT NULL,
    id_sessao INT NOT NULL,
    PRIMARY KEY (id_sala, id_sessao),
    FOREIGN KEY (id_sala) REFERENCES Sala(id_sala),
    FOREIGN KEY (id_sessao) REFERENCES Sessao(id_sessao)
);

ALTER TABLE Ingresso
DROP COLUMN id_sessao;

DROP TABLE IF EXISTS SalaPoltrona;

ALTER TABLE filme
    ALTER COLUMN duracao TYPE VARCHAR;  

ALTER TABLE sessao
    ALTER COLUMN data TYPE VARCHAR;      

ALTER TABLE ingresso
    ALTER COLUMN data_pedido TYPE VARCHAR; 

ALTER TABLE usuario
    ALTER COLUMN email TYPE VARCHAR;    

ALTER TABLE sala
DROP COLUMN preco;

ALTER TABLE filme
<<<<<<< Updated upstream
ADD COLUMN data_lancamento DATE;
=======
ADD COLUMN data_lancamento DATE;

ALTER TABLE usuario
ADD CONSTRAINT cliente_cpf_unique UNIQUE (cpf);

ALTER TABLE usuario
ALTER COLUMN email TYPE VARCHAR(100),
ALTER COLUMN email SET NOT NULL;

ALTER TABLE filme
ALTER COLUMN data_lancamento TYPE VARCHAR(20);

ALTER TABLE sessao
ALTER COLUMN data TYPE VARCHAR(20);
>>>>>>> Stashed changes
