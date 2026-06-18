from analysis.metrics.metrics_service import (MetricsService)


class GenreInsight:

    @staticmethod
    def generate(df, total_games):

        top = df.iloc[0]

        percentage = (MetricsService.calculate_percentage(top["total"], total_games))

        return f"""
O gênero predominante foi
{top['nome']},
presente em
{top['total']} jogos
({percentage}% da amostra).

Isso indica que esse gênero possui
caráter abrangente e está presente
em diferentes estilos de jogo.
"""