import pandas as pd

from analysis.sql.genres import ( TOP_GENRES_QUERY )


class GenreRepository:

    @staticmethod
    def get_top_genres(engine):

        return pd.read_sql(
            TOP_GENRES_QUERY,
            engine
        )