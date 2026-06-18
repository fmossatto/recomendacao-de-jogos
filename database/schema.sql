CREATE TABLE franquias (
    id SERIAL PRIMARY KEY,

    igdb_id BIGINT UNIQUE,

    nome VARCHAR(255),

    slug VARCHAR(255)
);

CREATE TABLE covers (
    id SERIAL PRIMARY KEY,

    igdb_id BIGINT UNIQUE NOT NULL,

    jogo_id INTEGER NOT NULL,

    image_id VARCHAR(100),

    largura INTEGER,
    altura INTEGER,

    FOREIGN KEY (jogo_id)
        REFERENCES jogos(id)
        ON DELETE CASCADE
);

CREATE TABLE screenshots (
    id SERIAL PRIMARY KEY,

    igdb_id BIGINT UNIQUE NOT NULL,

    jogo_id INTEGER NOT NULL,

    image_id VARCHAR(100),

    largura INTEGER,
    altura INTEGER,

    FOREIGN KEY (jogo_id)
        REFERENCES jogos(id)
        ON DELETE CASCADE
);

CREATE TABLE generos (
    id SERIAL PRIMARY KEY,

    igdb_id BIGINT UNIQUE NOT NULL,

    nome VARCHAR(100),
    slug VARCHAR(100)
);

CREATE TABLE plataformas (
    id SERIAL PRIMARY KEY,

    igdb_id BIGINT UNIQUE NOT NULL,

    nome VARCHAR(100),

    abreviacao VARCHAR(50),

    geracao INTEGER
);

CREATE TABLE temas (
    id SERIAL PRIMARY KEY,

    igdb_id BIGINT UNIQUE NOT NULL,

    nome VARCHAR(100),

    slug VARCHAR(100)
);

CREATE TABLE modos_jogo (
    id SERIAL PRIMARY KEY,

    igdb_id BIGINT UNIQUE NOT NULL,

    nome VARCHAR(100),

    slug VARCHAR(100)
);

CREATE TABLE empresas (
    id SERIAL PRIMARY KEY,

    igdb_id BIGINT UNIQUE NOT NULL,

    nome VARCHAR(255)
);

CREATE TABLE franquias (
    id SERIAL PRIMARY KEY,

    igdb_id BIGINT UNIQUE NOT NULL,

    nome VARCHAR(255),

    slug VARCHAR(255)
);

CREATE TABLE jogo_genero (
    jogo_id INTEGER NOT NULL,
    genero_id INTEGER NOT NULL,

    PRIMARY KEY (jogo_id, genero_id),

    FOREIGN KEY (jogo_id)
        REFERENCES jogos(id)
        ON DELETE CASCADE,

    FOREIGN KEY (genero_id)
        REFERENCES generos(id)
        ON DELETE CASCADE
);

CREATE TABLE jogo_plataforma (
    jogo_id INTEGER NOT NULL,
    plataforma_id INTEGER NOT NULL,

    PRIMARY KEY (jogo_id, plataforma_id),

    FOREIGN KEY (jogo_id)
        REFERENCES jogos(id)
        ON DELETE CASCADE,

    FOREIGN KEY (plataforma_id)
        REFERENCES plataformas(id)
        ON DELETE CASCADE
);

CREATE TABLE jogo_tema (
    jogo_id INTEGER NOT NULL,
    tema_id INTEGER NOT NULL,

    PRIMARY KEY (jogo_id, tema_id)
);

CREATE TABLE jogo_modo (
    jogo_id INTEGER NOT NULL,
    modo_id INTEGER NOT NULL,

    PRIMARY KEY (jogo_id, modo_id)
);

CREATE TABLE jogo_empresa (
    jogo_id INTEGER NOT NULL,
    empresa_id INTEGER NOT NULL,

    PRIMARY KEY (jogo_id, empresa_id)
);

CREATE TABLE jogo_franquia (
    jogo_id INTEGER NOT NULL,
    franquia_id INTEGER NOT NULL,

    PRIMARY KEY (jogo_id, franquia_id)
);

CREATE TABLE jogo_similar (
    jogo_id INTEGER NOT NULL,
    jogo_similar_igdb_id BIGINT NOT NULL,

    PRIMARY KEY (jogo_id, jogo_similar_igdb_id)
);




-- CONSULTAS DE ANALISES

-- JOGOS POR CATEGORIA
select
    g.nome,
    count(*) as total
from jogo_genero jg
join generos g
    on g.id = jg.genero_id
group by g.nome
order by total desc;

--JOGOS POR PLATAFORMA
select
    p.nome,
    count(*) as total
from jogo_plataforma jp
join plataformas p
    on p.id = jp.plataforma_id
group by p.nome
order by total desc
limit 20;