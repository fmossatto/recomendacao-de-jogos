import pandas as pd


class MetricsRepository:

    @staticmethod
    def get_total_games(engine):

        query = """
        select count(*) as total
        from jogos
        """

        df = pd.read_sql(query, engine)

        return int(df.iloc[0]["total"])