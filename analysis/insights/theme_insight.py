from analysis.metrics.metrics_service import (MetricsService)


class ThemeInsight:

    @staticmethod
    def generate(df, total_games):

        top = df.iloc[0]

        percentage = (MetricsService.calculate_percentage(top["total"], total_games))

        return f"""
O tema mais frequente foi
{top['nome']},
presente em
{top['total']} jogos
({percentage}% da amostra).

Esse resultado sugere forte
presença de elementos de ação
nos jogos mais populares.
"""