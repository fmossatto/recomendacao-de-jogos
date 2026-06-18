from analysis.metrics.metrics_service import (MetricsService)


class PlatformInsight:

    @staticmethod
    def generate(df, total_games):

        top = df.iloc[0]

        percentage = (MetricsService.calculate_percentage(top["total"], total_games))

        return f"""
A plataforma com maior presença
foi {top['nome']},
com {top['total']} jogos
({percentage}% da amostra).

Isso reforça a predominância do
ecossistema PC entre os títulos
mais populares da base analisada.
"""