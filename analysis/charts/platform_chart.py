import matplotlib.pyplot as plt
from analysis.charts.base_chart import (BaseChart)


class PlatformChart(BaseChart):

    @staticmethod
    def generate(df):
        plt.figure(figsize=(10, 6))

        plt.bar(df["nome"], df["total"])

        plt.title("Top 10 Plataformas")

        plt.xticks(rotation=45)

        PlatformChart.save("top_platforms.png")