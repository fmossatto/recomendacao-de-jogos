from dataclasses import dataclass


@dataclass
class UserPreferences:

    themes: list[str]

    genres: list[str]

    game_modes: list[str]