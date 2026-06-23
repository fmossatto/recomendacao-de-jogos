from sqlalchemy import create_engine
from database.connection import DATABASE_URL
from recommendation.dto.user_preferences import (UserPreferences)
from recommendation.services.recommendation_service import (RecommendationService)


def main():

    engine = create_engine(DATABASE_URL)

    preferences = UserPreferences(themes=["Horror", "Science fiction"],
        genres=["Shooter"],
        game_modes=["Single player"]
    )

    recommendations = (RecommendationService.recommend(engine,preferences))

    print("\n=== RECOMENDAÇÕES ===\n")

    for game in recommendations:

        print(f"{game['nome']} " f"(Score: {game['score']})")
        print(game["matches"])
        print("-" * 50)

if __name__ == "__main__":
    main()