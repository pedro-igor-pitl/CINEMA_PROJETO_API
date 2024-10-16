CREATE DATABASE CINEMA_API

CREATE TABLE IF NOT EXISTS public.filme
(
    id_filme serial NOT NULL,
    nome_filme character varying(200) COLLATE pg_catalog."default" NOT NULL,
    descricao text COLLATE pg_catalog."default",
    caminho_img character varying(255) COLLATE pg_catalog."default",
    duracao character varying COLLATE pg_catalog."default" NOT NULL,
    genero character varying(100) COLLATE pg_catalog."default" NOT NULL,
    data_lancamento character varying(20) COLLATE pg_catalog."default",
    CONSTRAINT filme_pkey PRIMARY KEY (id_filme)
);

CREATE TABLE IF NOT EXISTS public.ingresso
(
    id_ingresso serial NOT NULL,
    id_usuario integer NOT NULL,
    id_sala integer NOT NULL,
    id_poltrona integer,
    qrcode character varying(255) COLLATE pg_catalog."default",
    data_pedido character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT ingresso_pkey PRIMARY KEY (id_ingresso)
);

CREATE TABLE IF NOT EXISTS public.poltrona
(
    id_poltrona serial NOT NULL,
    posicao character varying(50) COLLATE pg_catalog."default" NOT NULL,
    tipo_poltrona character varying(50) COLLATE pg_catalog."default" NOT NULL,
    id_sala integer NOT NULL,
    CONSTRAINT poltrona_pkey PRIMARY KEY (id_poltrona)
);

CREATE TABLE IF NOT EXISTS public.sala
(
    id_sala serial NOT NULL,
    qt_poltrona integer NOT NULL,
    id_sessao integer,
    CONSTRAINT sala_pkey PRIMARY KEY (id_sala)
);

CREATE TABLE IF NOT EXISTS public.salaingresso
(
    id_sala integer NOT NULL,
    id_ingresso integer NOT NULL,
    CONSTRAINT salaingresso_pkey PRIMARY KEY (id_sala, id_ingresso)
);

CREATE TABLE IF NOT EXISTS public.salasessao
(
    id_sala integer NOT NULL,
    id_sessao integer NOT NULL,
    CONSTRAINT salasessao_pkey PRIMARY KEY (id_sala, id_sessao)
);

CREATE TABLE IF NOT EXISTS public.sessao
(
    id_sessao serial NOT NULL,
    data character varying(20) COLLATE pg_catalog."default" NOT NULL,
    id_sala integer NOT NULL,
    preco numeric(10, 2) NOT NULL,
    linguagem character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT sessao_pkey PRIMARY KEY (id_sessao)
);

CREATE TABLE IF NOT EXISTS public.sessaofilme
(
    id_sessao integer NOT NULL,
    id_filme integer NOT NULL,
    CONSTRAINT sessaofilme_pkey PRIMARY KEY (id_sessao, id_filme)
);

CREATE TABLE IF NOT EXISTS public.usuario
(
    id_usuario serial NOT NULL,
    cpf character varying(11) COLLATE pg_catalog."default" NOT NULL,
    nome character varying(100) COLLATE pg_catalog."default" NOT NULL,
    email character varying(100) COLLATE pg_catalog."default" NOT NULL,
    senha character varying(100) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario),
    CONSTRAINT cliente_cpf_unique UNIQUE (cpf),
    CONSTRAINT usuario_email_key UNIQUE (email)
);

ALTER TABLE IF EXISTS public.ingresso
    ADD CONSTRAINT ingresso_id_poltrona_fkey FOREIGN KEY (id_poltrona)
    REFERENCES public.poltrona (id_poltrona) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;


ALTER TABLE IF EXISTS public.ingresso
    ADD CONSTRAINT ingresso_id_sala_fkey FOREIGN KEY (id_sala)
    REFERENCES public.sala (id_sala) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION;