from sqlalchemy import (
    Column,
    Integer,
    BigInteger,
    String,
    Text,
    Numeric,
    Date,
    ForeignKey
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(Integer, primary_key=True)

    igdb_id = Column(BigInteger, unique=True, nullable=False)

    nome = Column(String(255), nullable=False)

    slug = Column(String(255))

    resumo = Column(Text)

    data_lancamento = Column(Date)

    rating = Column(Numeric(6, 2))

    rating_count = Column(Integer)

    total_rating = Column(Numeric(6, 2))

    total_rating_count = Column(Integer)


class Genero(Base):
    __tablename__ = "generos"

    id = Column(Integer, primary_key=True)

    igdb_id = Column(BigInteger, unique=True)

    nome = Column(String(100))

    slug = Column(String(100))


class JogoGenero(Base):
    __tablename__ = "jogo_genero"

    jogo_id = Column(
        Integer,
        ForeignKey("jogos.id"),
        primary_key=True
    )

    genero_id = Column(
        Integer,
        ForeignKey("generos.id"),
        primary_key=True
    )


class Plataforma(Base):
    __tablename__ = "plataformas"

    id = Column(Integer, primary_key=True)

    igdb_id = Column(BigInteger, unique=True)

    nome = Column(String(100))

    abreviacao = Column(String(50))

    geracao = Column(Integer)


class JogoPlataforma(Base):
    __tablename__ = "jogo_plataforma"

    jogo_id = Column(
        Integer,
        ForeignKey("jogos.id"),
        primary_key=True
    )

    plataforma_id = Column(
        Integer,
        ForeignKey("plataformas.id"),
        primary_key=True
    )


class Tema(Base):
    __tablename__ = "temas"

    id = Column(Integer, primary_key=True)

    igdb_id = Column(BigInteger, unique=True)

    nome = Column(String(100))

    slug = Column(String(100))


class JogoTema(Base):
    __tablename__ = "jogo_tema"

    jogo_id = Column(
        Integer,
        ForeignKey("jogos.id"),
        primary_key=True
    )

    tema_id = Column(
        Integer,
        ForeignKey("temas.id"),
        primary_key=True
    )


class ModoJogo(Base):
    __tablename__ = "modos_jogo"

    id = Column(Integer, primary_key=True)

    igdb_id = Column(BigInteger, unique=True)

    nome = Column(String(100))

    slug = Column(String(100))


class JogoModo(Base):
    __tablename__ = "jogo_modo"

    jogo_id = Column(
        Integer,
        ForeignKey("jogos.id"),
        primary_key=True
    )

    modo_id = Column(
        Integer,
        ForeignKey("modos_jogo.id"),
        primary_key=True
    )

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True)

    igdb_id = Column(BigInteger, unique=True)

    nome = Column(String(255))


class Franquia(Base):
    __tablename__ = "franquias"

    id = Column(Integer, primary_key=True)

    igdb_id = Column(BigInteger, unique=True)

    nome = Column(String(255))

    slug = Column(String(255))