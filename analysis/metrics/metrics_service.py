class MetricsService:

    @staticmethod
    def calculate_percentage(value, total):

        if total == 0:
            return 0

        return round((value / total) * 100, 2)