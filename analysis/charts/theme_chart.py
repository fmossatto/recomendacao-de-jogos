import matplotlib.pyplot as plt
from analysis.charts.base_chart import (BaseChart)


class ThemeChart(BaseChart):

    @staticmethod
    def generate(df):
        plt.figure(figsize=(10, 6))

        plt.bar(df["nome"], df["total"])

        plt.title("Top 10 Temas")

        plt.xticks(rotation=45)

        ThemeChart.save("top_themes.png")