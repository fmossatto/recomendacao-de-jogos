import json
import requests

from etl.igdb_client import get_headers

query = """
fields
    id,
    name,
    slug,

    first_release_date,

    genres.*,
    platforms.*,

    cover.*,

    franchises.*,

    game_modes.*,

    themes.*,

    involved_companies.company.name,

    similar_games,

    rating,
    total_rating;

search "resident evil";

limit 1;
"""

response = requests.post(
    "https://api.igdb.com/v4/games",
    headers=get_headers(),
    data=query
)

response.raise_for_status()

games = response.json()

print(json.dumps(games, indent=4))