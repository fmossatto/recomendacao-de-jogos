from datetime import datetime

from database.connection import SessionLocal
from database.models import (
    Jogo,
    Genero,
    JogoGenero,
    Plataforma,
    JogoPlataforma,
    Tema,
    JogoTema,
    ModoJogo,
    JogoModo
)

from etl.igdb_client import execute_query
from etl.game_queries import GAME_IMPORT_QUERY


def timestamp_to_date(timestamp):
    if not timestamp:
        return None

    return datetime.fromtimestamp(timestamp).date()


def importar_jogos():

    session = SessionLocal()

    jogos = execute_query(
        "games",
        GAME_IMPORT_QUERY
    )

    total = 0

    print(f"Total retornado pela API: {len(jogos)}")
    print(jogos[:2])

    for game in jogos:

        igdb_id = game["id"]

        existente = (
            session.query(Jogo)
            .filter_by(igdb_id=igdb_id)
            .first()
        )

        if existente:
            continue

        novo_jogo = Jogo(
            igdb_id=igdb_id,
            nome=game.get("name"),
            slug=game.get("slug"),
            resumo=game.get("summary"),
            data_lancamento=timestamp_to_date(
                game.get("first_release_date")
            ),
            rating=game.get("rating"),
            total_rating=game.get("total_rating"),
            rating_count=game.get("rating_count"),
            total_rating_count=game.get("total_rating_count")
        )

        session.add(novo_jogo)
        session.flush()

        for genero_data in game.get("genres", []):
            genero = (
                session.query(Genero)
                .filter_by(igdb_id=genero_data["id"])
                .first()
            )

            if not genero:
                genero = Genero(
                    igdb_id=genero_data["id"],
                    nome=genero_data["name"],
                    slug=genero_data["slug"]
                )

                session.add(genero)
                session.flush()

            relacao = (
                session.query(JogoGenero)
                .filter_by(
                    jogo_id=novo_jogo.id,
                    genero_id=genero.id
                )
                .first()
            )

            if not relacao:
                session.add(
                    JogoGenero(
                        jogo_id=novo_jogo.id,
                        genero_id=genero.id
                    )
                )
        

        for plataforma_data in game.get("platforms", []):
            plataforma = (
                session.query(Plataforma)
                .filter_by(igdb_id=plataforma_data["id"])
                .first()
            )

            if not plataforma:
                plataforma = Plataforma(
                    igdb_id=plataforma_data["id"],
                    nome=plataforma_data["name"],
                    abreviacao=plataforma_data.get("abbreviation"),
                    geracao=plataforma_data.get("generation")
                )

                session.add(plataforma)
                session.flush()

            relacao = (
                session.query(JogoPlataforma)
                .filter_by(
                    jogo_id=novo_jogo.id,
                    plataforma_id=plataforma.id
                )
                .first()
            )

            if not relacao:
                session.add(
                    JogoPlataforma(
                        jogo_id=novo_jogo.id,
                        plataforma_id=plataforma.id
                    )
                )
        

        for tema_data in game.get("themes", []):
            tema = (
                session.query(Tema)
                .filter_by(igdb_id=tema_data["id"])
                .first()
            )

            if not tema:
                tema = Tema(
                    igdb_id=tema_data["id"],
                    nome=tema_data["name"],
                    slug=tema_data["slug"]
                )

                session.add(tema)
                session.flush()

            relacao = (
                session.query(JogoTema)
                .filter_by(
                    jogo_id=novo_jogo.id,
                    tema_id=tema.id
                )
                .first()
            )

            if not relacao:
                session.add(
                    JogoTema(
                        jogo_id=novo_jogo.id,
                        tema_id=tema.id
                    )
                )

        
        for modo_data in game.get("game_modes", []):
            modo = (
                session.query(ModoJogo)
                .filter_by(igdb_id=modo_data["id"])
                .first()
            )

            if not modo:
                modo = ModoJogo(
                    igdb_id=modo_data["id"],
                    nome=modo_data["name"],
                    slug=modo_data["slug"]
                )

                session.add(modo)
                session.flush()

            relacao = (
                session.query(JogoModo)
                .filter_by(
                    jogo_id=novo_jogo.id,
                    modo_id=modo.id
                )
                .first()
            )

            if not relacao:
                session.add(
                    JogoModo(
                        jogo_id=novo_jogo.id,
                        modo_id=modo.id
                    )
                )

        total += 1

    session.commit()

    print(f"{total} jogos importados.")

    session.close()


if __name__ == "__main__":
    importar_jogos()