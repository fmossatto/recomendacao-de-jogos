from recommendation.repositories.recommendation_repository import (RecommendationRepository)


class RecommendationService:

    THEME_WEIGHT = 5
    GENRE_WEIGHT = 3
    MODE_WEIGHT = 2

    @classmethod
    def recommend(cls, engine, preferences):

        games = (RecommendationRepository.get_games(engine))
        themes = (RecommendationRepository.get_game_themes(engine))
        genres = (RecommendationRepository.get_game_genres(engine))
        modes = (RecommendationRepository.get_game_modes(engine))

        recommendations = []

        for _, game in games.iterrows():
            score = 0
            matches = []

            game_themes = (themes[themes["jogo_id"] == game["id"]]["tema"].tolist())
            game_genres = (genres[genres["jogo_id"] == game["id"]]["genero"].tolist())
            game_modes = (modes[modes["jogo_id"] == game["id"]]["modo"].tolist())

            # --------------------
            # Temas
            # --------------------

            for theme in preferences.themes:
                if theme in game_themes:
                    score += cls.THEME_WEIGHT
                    matches.append(f"Tema: {theme}")

            # --------------------
            # Gêneros
            # --------------------

            for genre in preferences.genres:
                if genre in game_genres:
                    score += cls.GENRE_WEIGHT
                    matches.append(f"Gênero: {genre}")

            # --------------------
            # Modos
            # --------------------

            for mode in preferences.game_modes:
                if mode in game_modes:
                    score += cls.MODE_WEIGHT
                    matches.append(f"Modo: {mode}")

            if score > 0:
                recommendations.append(
                    {
                        "jogo_id": game["id"],
                        "nome": game["nome"],
                        "score": score,
                        "matches": matches
                    }
                )

        recommendations.sort(key=lambda item: item["score"], reverse=True)

        return recommendations[:10]