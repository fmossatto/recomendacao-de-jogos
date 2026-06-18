import pandas as pd
from analysis.sql.themes import (TOP_THEMES_QUERY)


class ThemeRepository:

    @staticmethod
    def get_top_themes(engine):
        return pd.read_sql(TOP_THEMES_QUERY, engine)