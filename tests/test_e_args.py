from contextlib import redirect_stdout
import io
import imdb
import copy
import sys


def test_parse_actors(mocker):
    # Mock all other calls
    mocker.patch("imdb.read")
    mocker.patch("imdb.enrich_data")
    mocker.patch("imdb.get_filtered_movies")
    mocker.patch("imdb.print_movies")

    sys.argv = ["imdb.py", "--actors", "Nanna List"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert type(args[1]) == list, "the --actors argument should be a list"
    assert args[1] == ["Nanna List"]

    sys.argv = ["imdb.py", "--actors", "Nanna List", "Tom Cruise"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert args[1] == [
        "Nanna List",
        "Tom Cruise",
    ], 'imdb.py --actors "Nanna List" "Tom Cruise" should yield 2 actors'


def test_parse_genres(mocker):
    # Mock all other calls
    mocker.patch("imdb.read")
    mocker.patch("imdb.enrich_data")
    mocker.patch("imdb.get_filtered_movies")
    mocker.patch("imdb.print_movies")

    sys.argv = ["imdb.py", "--genres", "Action"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert type(args[2]) == list, "the --genres argument should be a list"
    assert args[2] == ["Action"]

    sys.argv = ["imdb.py", "--genres", "Action", "Science Fiction"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert args[2] == ["Action", "Science Fiction"]


def test_parse_years(mocker):
    # Mock all other calls
    mocker.patch("imdb.read")
    mocker.patch("imdb.enrich_data")
    mocker.patch("imdb.get_filtered_movies")
    mocker.patch("imdb.print_movies")

    sys.argv = ["imdb.py", "--years", "2011"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert type(args[3]) == list, "the --years argument should be a list"
    assert args[3] == [2011]

    sys.argv = ["imdb.py", "--years", "2011", "2012"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert args[3] == [2011, 2012]


def test_parse_top(mocker):
    # Mock all other calls
    mocker.patch("imdb.read")
    mocker.patch("imdb.enrich_data")
    mocker.patch("imdb.get_filtered_movies")
    mocker.patch("imdb.print_movies")

    sys.argv = ["imdb.py", "--top", "7"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert type(args[4]) == int, "the --top argument should be an integer"
    assert args[4] == 7


def test_parse_sort(mocker):
    # Mock all other calls
    mocker.patch("imdb.read")
    mocker.patch("imdb.enrich_data")
    mocker.patch("imdb.get_filtered_movies")
    mocker.patch("imdb.print_movies")

    sys.argv = ["imdb.py", "--sort", "score"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert type(args[5]) == str, "the --sort argument should be a string"
    assert args[5] == "score"

    sys.argv = ["imdb.py", "--sort", "year"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert args[5] == "year"


def test_parse_ascending(mocker):
    # Mock all other calls
    mocker.patch("imdb.read")
    mocker.patch("imdb.enrich_data")
    mocker.patch("imdb.get_filtered_movies")
    mocker.patch("imdb.print_movies")

    sys.argv = ["imdb.py"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert args[6] == False, "If --ascending is not given, input should be False"

    sys.argv = ["imdb.py", "--ascending"]
    imdb.main()

    args = imdb.get_filtered_movies.call_args[0]
    assert args[6] == True, "If --ascending is given, input should be True"
