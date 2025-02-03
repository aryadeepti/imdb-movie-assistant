import pytest
import os.path as path
import imdb


@pytest.fixture(scope="session")
def movies():
    return imdb.read(path.join("data", "imdb_movies.csv"))


@pytest.fixture(scope="session")
def enriched_movies():
    return imdb.enrich_data(imdb.read(path.join("data", "imdb_movies.csv")))
