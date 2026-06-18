import pandas as pd
from analysis.sql.platforms import (TOP_PLATFORMS_QUERY)


class PlatformRepository:

    @staticmethod
    def get_top_platforms(engine):
        return pd.read_sql(TOP_PLATFORMS_QUERY, engine)