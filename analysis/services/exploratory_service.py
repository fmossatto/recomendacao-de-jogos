from analysis.repositories.genre_repository import GenreRepository
from analysis.repositories.theme_repository import ThemeRepository
from analysis.repositories.platform_repository import PlatformRepository
from analysis.repositories.metrics_repository import MetricsRepository

from analysis.charts.genre_chart import GenreChart
from analysis.charts.theme_chart import ThemeChart
from analysis.charts.platform_chart import PlatformChart

from analysis.insights.genre_insight import GenreInsight
from analysis.insights.theme_insight import ThemeInsight
from analysis.insights.platform_insight import PlatformInsight

from analysis.reports.report_generator import ReportGenerator


class ExploratoryService:

    @staticmethod
    def generate_report(engine):

        # -----------------------------
        # Coleta de dados
        # -----------------------------

        total_games = (
            MetricsRepository
            .get_total_games(engine)
        )

        df_genres = (
            GenreRepository
            .get_top_genres(engine)
        )

        df_themes = (
            ThemeRepository
            .get_top_themes(engine)
        )

        df_platforms = (
            PlatformRepository
            .get_top_platforms(engine)
        )

        # -----------------------------
        # Geração dos gráficos
        # -----------------------------

        GenreChart.generate(df_genres)

        ThemeChart.generate(df_themes)

        PlatformChart.generate(df_platforms)

        # -----------------------------
        # Insights
        # -----------------------------

        genre_insight = (
            GenreInsight.generate(
                df_genres,
                total_games
            )
        )

        theme_insight = (
            ThemeInsight.generate(
                df_themes,
                total_games
            )
        )

        platform_insight = (
            PlatformInsight.generate(
                df_platforms,
                total_games
            )
        )

        # -----------------------------
        # Relatório
        # -----------------------------

        report = f"""
# Game Insight

## Resumo Executivo

Foram analisados **{total_games} jogos**
com maior volume de avaliações da base.

---

## Gêneros

{genre_insight}

![Top Genres](top_genres.png)

---

## Plataformas

{platform_insight}

![Top Platforms](top_platforms.png)

---

## Temas

{theme_insight}

![Top Themes](top_themes.png)

---

## Considerações

A análise inicial demonstra forte predominância
de títulos AAA e franquias populares.

Os resultados sugerem que a utilização da dimensão
"Temas" possui maior capacidade descritiva do que
a classificação tradicional baseada apenas em gêneros.

Essa característica pode ser explorada futuramente
na construção de um sistema de recomendação baseado
em conteúdo.
"""

        ReportGenerator.save(report)