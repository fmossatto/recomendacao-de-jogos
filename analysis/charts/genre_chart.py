import matplotlib.pyplot as plt
from analysis.charts.base_chart import (BaseChart)


class GenreChart(BaseChart):

    @staticmethod
    def generate(df):
        plt.figure(figsize=(10, 6))

        plt.bar(df["nome"], df["total"])

        plt.title("Top 10 Gêneros")

        plt.xticks(rotation=45)

        GenreChart.save("top_genres.png")