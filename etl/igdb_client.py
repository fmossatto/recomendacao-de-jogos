import os
import requests

from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("IGDB_CLIENT_ID")
CLIENT_SECRET = os.getenv("IGDB_CLIENT_SECRET")


def get_access_token():
    response = requests.post(
        "https://id.twitch.tv/oauth2/token",
        params={
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "client_credentials"
        }
    )

    response.raise_for_status()

    return response.json()["access_token"]


def get_headers():
    token = get_access_token()

    return {
        "Client-ID": CLIENT_ID,
        "Authorization": f"Bearer {token}"
    }


def execute_query(endpoint, query):
    response = requests.post(
        f"https://api.igdb.com/v4/{endpoint}",
        headers=get_headers(),
        data=query
    )

    response.raise_for_status()

    return response.json()