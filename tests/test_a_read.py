import os.path as path
import imdb


def test_read():
    # Given the data
    movies = imdb.read(path.join("data", "imdb_movies.csv"))
    # Then length should be
    assert len(movies) == 9640, "There should be 9640 movies in the list"

    # Each movie should have 12 fields
    assert len(movies[0].values()) == 12, "Each movie dict should have 12 fields"

    # When checking first 3 movies
    first_names = [movie["names"] for movie in movies][:3]
    first_revenues = [float(movie["revenue"]) for movie in movies][:3]

    # Expected
    expected_names = [
        "Creed III",
        "Avatar: The Way of Water",
        "The Super Mario Bros. Movie",
    ]
    expected_revenues = [271616668, 2316794914, 724459031]

    # Then names should be
    assert first_names == expected_names
    # Then revenue shuold be
    assert first_revenues == expected_revenues
