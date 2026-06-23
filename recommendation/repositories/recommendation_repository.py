import pandas as pd


class RecommendationRepository:

    @staticmethod
    def get_games(engine):

        query = """
        select
            j.id,
            j.nome
        from jogos j
        """

        return pd.read_sql(
            query,
            engine
        )
    

    @staticmethod
    def get_game_themes(engine):

        query = """
        select
            j.id as jogo_id,
            t.nome as tema
        from jogo_tema jt
        join jogos j
            on j.id = jt.jogo_id
        join temas t
            on t.id = jt.tema_id
        """

        return pd.read_sql(
            query,
            engine
        )
    


    @staticmethod
    def get_game_genres(engine):

        query = """
        select
            j.id as jogo_id,
            g.nome as genero
        from jogo_genero jg
        join jogos j
            on j.id = jg.jogo_id
        join generos g
            on g.id = jg.genero_id
        """

        return pd.read_sql(
            query,
            engine
        )
    


    @staticmethod
    def get_game_modes(engine):

        query = """
        select
            j.id as jogo_id,
            m.nome as modo
        from jogo_modo jm
        join jogos j
            on j.id = jm.jogo_id
        join modos_jogo m
            on m.id = jm.modo_id
        """

        return pd.read_sql(
            query,
            engine
        )