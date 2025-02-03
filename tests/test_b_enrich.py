import imdb
import copy

EXPECTED_ACTORS = [
    "Michael B. Jordan",
    "Tessa Thompson",
    "Jonathan Majors",
    "Wood Harris",
    "Phylicia Rashād",
    "Mila Davis-Kent",
    "Florian Munteanu",
    "José Benavidez Jr.",
    "Selenis Leyva",
]

EXPECTED_YEARS = [2023, 2022, 2023, 2023, 2023]


def get_actors(actors):
    if isinstance(actors, list):
        return [a.strip() for a in actors]
    else:
        return [a.strip() for a in actors.split(",")]


def test_add_actors(movies):
    movies = copy.deepcopy(movies)
    # Given movies
    # When add actors
    movies = imdb.add_actor(movies)
    # Then expect 9 actors in first movie
    actual = get_actors(movies[0]["actors"])
    assert len(actual) == 9, "There should be 9 actors listed in the movie Creed III"
    assert actual == EXPECTED_ACTORS


def test_add_year(movies):
    movies = copy.deepcopy(movies)
    # Given movies
    # When add year
    movies = imdb.add_year(movies)
    # Then expect
    first_years = [movie["year"] for movie in movies][:5]
    assert first_years == EXPECTED_YEARS


def test_enrich_data(movies):
    movies = copy.deepcopy(movies)
    # Given movies
    # When add year
    movies = imdb.enrich_data(movies)
    # Then expect
    first_years = [movie["year"] for movie in movies][:5]
    assert first_years == EXPECTED_YEARS

    actual = get_actors(movies[0]["actors"])
    assert actual == EXPECTED_ACTORS
