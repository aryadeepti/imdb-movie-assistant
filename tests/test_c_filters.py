import imdb
import copy

# ------------------
# Actors filter
# ------------------


def test_filter_single_actor(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)

    # Given the enriched movies
    # When extract all movies with "Tom Cruise"
    filtered_movies = imdb.get_filtered_movies(enriched_movies, actors=["Tom Cruise"])
    actual_movie_names = [movie["names"] for movie in filtered_movies][:4]
    expected_movie_name = [
        "Top Gun: Maverick",
        "Top Gun",
        "Jack Reacher",
        "Mission: Impossible - Ghost Protocol",
    ]
    # Then we expect 40 movies
    assert len(filtered_movies) == 40, "There should be 40 movies with Tom Cruise"
    # And we'll check the first 4 of them
    assert actual_movie_names == expected_movie_name


def test_filter_multiple_actors(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)

    # Given the enriched movies
    # When extract all movies with that have both "Elijah Wood" and "Ian McKellen"
    filtered_movies = imdb.get_filtered_movies(
        enriched_movies, actors=["Elijah Wood", "Ian McKellen"]
    )
    actual_movie_names = [movie["names"] for movie in filtered_movies]
    # Then we expect 3 movies
    expected_movie_name = [
        "The Lord of the Rings: The Fellowship of the Ring",
        "The Lord of the Rings: The Return of the King",
        "The Lord of the Rings: The Two Towers",
    ]
    assert len(filtered_movies) == len(
        expected_movie_name
    ), "There should be 3 LOTR movies"
    assert actual_movie_names == expected_movie_name


# ------------------
# Genre filter
# ------------------


def test_filter_single_genre(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)

    # Given the enriched movies
    # When extract all the "Science Fiction" movies
    filtered_movies = imdb.get_filtered_movies(
        enriched_movies, genres=["Science Fiction"]
    )
    scifi_titles = [movie["names"] for movie in filtered_movies]

    expected_scifi_movies = 1192
    assert (
        len(scifi_titles) == expected_scifi_movies
    ), "There should be 1192 Sci-Fi movies"
    assert "Frozen" not in scifi_titles, "Frozen is not a Sci-Fi movie"

    # There are a few other titles with Star Wars in their name, so 16 in total
    expected_num_star_wars_titled_movies = 16
    star_wars_titles = [title for title in scifi_titles if "Star Wars" in title]
    assert (
        len(star_wars_titles) == expected_num_star_wars_titled_movies
    ), "There is 16 Star Wars movies in the set"


def test_filter_multiple_genres(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given the enriched movies
    # When extract all the "Science Fiction" and "Action" movies
    filtered_movies = imdb.get_filtered_movies(
        enriched_movies, genres=["Science Fiction", "Action"]
    )
    action_and_scifi_titles = [movie["names"] for movie in filtered_movies]

    expected_action_and_scifi_titles = 3149
    assert (
        len(action_and_scifi_titles) == expected_action_and_scifi_titles
    ), "There should be 3149 Sci-Fi + Action movies"
    assert (
        "Frozen" not in action_and_scifi_titles
    ), "Frozen is not a Sci-Fi movie or Action movie"

    # How many Avengers movies
    expected_avengers_movies = 10
    avengers_titles = [
        title for title in action_and_scifi_titles if "Avengers" in title
    ]
    assert len(avengers_titles) == expected_avengers_movies


# ------------------
# Years filter
# ------------------


def test_filter_single_year(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given the enriched movies
    # Fiind all movies from 2013 only
    filtered_movies = imdb.get_filtered_movies(enriched_movies, years=[2013])
    print(filtered_movies)
    titles = [movie["names"] for movie in filtered_movies]

    expected_num_movies = 284
    assert len(titles) == expected_num_movies

    assert "Frozen" in titles, "Frozen was made in 2013"
    assert "Top Gun" not in titles, "Top Gun was not made in 2013"


def test_filter_multiple_years(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given the enriched movies
    # When extract all the "Science Fiction" movies with
    filtered_movies = imdb.get_filtered_movies(
        enriched_movies, years=[2010, 2011, 2012]
    )
    titles = [movie["names"] for movie in filtered_movies]

    expected_num_movies = 765
    assert len(titles) == expected_num_movies

    assert "Frozen" not in titles, "Frozen was made in 2013"
    assert "Inception" in titles, "Inception was made in 2010"


# --------------------
# All filters together
# --------------------


def test_all_filters(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given the enriched movies
    # Apply multiple filters to limit selection
    filtered_movies = imdb.get_filtered_movies(
        enriched_movies,
        actors=["Morgan Freeman"],
        genres=["Science Fiction"],
        years=[2013],
    )
    scifi_titles = [movie["names"] for movie in filtered_movies]

    expected_scifi_movies = 1
    assert len(scifi_titles) == expected_scifi_movies
    assert (
        "Oblivion" == scifi_titles[0]
    ), "Oblivion was made in 2013, is a Sci-Fi movie with Morgan Freeman"
