import pytest
import imdb
import copy


def test_top(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given the enriched movies
    # Limit the number of returned results
    filtered_movies = imdb.get_filtered_movies(enriched_movies, top=11)
    titles = [movie["names"] for movie in filtered_movies]

    expected_num_titles = 11
    assert len(titles) == expected_num_titles
    assert "Creed III" == titles[0], "The first (unsorted) movie is Creed III"
    assert "Winnie the Pooh: Blood and Honey" == titles[10]


@pytest.mark.parametrize(
    "asc, expected_titles",
    [
        (None, ["The Comeback Trail", "Just Getting Started"]),
        (False, ["The Comeback Trail", "Just Getting Started"]),
        (True, ["Just Getting Started", "The Comeback Trail"]),
    ],
)
def test_sort_by_score_two_movies(enriched_movies, asc, expected_titles):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given the enriched movies
    # Limit the number of returned results
    filtered_movies = imdb.get_filtered_movies(
        enriched_movies,
        actors=["Morgan Freeman", "Tommy Lee Jones"],
        sort_by="score",
        ascending=asc,
    )
    titles = [movie["names"] for movie in filtered_movies]

    expected_num_titles = 2
    assert len(titles) == expected_num_titles
    assert (
        expected_titles == titles
    ), "Check that your score sort is ordering in the correct direction"


@pytest.mark.parametrize(
    "asc, expected_titles",
    [
        (None, ["The Comeback Trail", "Just Getting Started"]),
        (False, ["The Comeback Trail", "Just Getting Started"]),
        (True, ["Just Getting Started", "The Comeback Trail"]),
    ],
)
def test_sort_by_year_two_movies(enriched_movies, asc, expected_titles):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given the enriched movies
    # Limit the number of returned results
    filtered_movies = imdb.get_filtered_movies(
        enriched_movies,
        actors=["Morgan Freeman", "Tommy Lee Jones"],
        sort_by="year",
        ascending=asc,
    )
    titles = [movie["names"] for movie in filtered_movies]

    expected_num_titles = 2
    assert len(titles) == expected_num_titles
    assert (
        expected_titles == titles
    ), "Check that your year sort is ordering in the correct direction"


def test_top_scoring_movies_w_morgan_freeman(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given the enriched movies
    # Limit the number of returned results
    filtered_movies = imdb.get_filtered_movies(
        enriched_movies, actors=["Morgan Freeman"], sort_by="score", top=10
    )
    titles = [movie["names"] for movie in filtered_movies]

    expected_num_titles = 10
    assert len(titles) == expected_num_titles

    expected_titles = [
        "The Shawshank Redemption",
        "The Dark Knight",
        "Se7en",
        "Million Dollar Baby",
        "Unforgiven",
        "The Dark Knight Rises",
        "Glory",
        "Lucky Number Slevin",
        "The Lego Movie",
        "Now You See Me",
    ]
    assert expected_titles == titles


def test_harry_potter_movies_order_by_release_year(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given the enriched movies
    # Find the first 8 Harry Potter movies using actors and order by year (acsending)
    filtered_movies = imdb.get_filtered_movies(
        enriched_movies,
        actors=["Daniel Radcliffe"],
        sort_by="year",
        top=8,
        ascending=True,
    )
    titles = [movie["names"] for movie in filtered_movies]

    expected_num_titles = 8
    assert (
        len(titles) == expected_num_titles
    ), "There should be 8 movies with Daniel Radcliffe when selecting top 8"

    expected_titles = [
        "Harry Potter and the Philosopher's Stone",
        "Harry Potter and the Chamber of Secrets",
        "Harry Potter and the Prisoner of Azkaban",
        "Harry Potter and the Goblet of Fire",
        "Harry Potter and the Order of the Phoenix",
        "Harry Potter and the Half-Blood Prince",
        "Harry Potter and the Deathly Hallows: Part 1",
        "Harry Potter and the Deathly Hallows: Part 2",
    ]
    assert (
        expected_titles == titles
    ), "The first 8 movies with Daniel Radcliffe should be the Harry Potter movies, and sorted by year they should start with the Philosopher's Stone and end with the Deathly Hallows: Part 2"
