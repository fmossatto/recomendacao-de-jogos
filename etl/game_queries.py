GAME_IMPORT_QUERY = """
fields
    id,
    name,
    slug,
    summary,
    first_release_date,

    rating,
    rating_count,

    total_rating,
    total_rating_count,

    genres.id,
    genres.name,
    genres.slug,

    platforms.id,
    platforms.name,
    platforms.abbreviation,
    platforms.generation,

    themes.id,
    themes.name,
    themes.slug,

    game_modes.id,
    game_modes.name,
    game_modes.slug;

where total_rating != null;

sort total_rating_count desc;

limit 100;
"""