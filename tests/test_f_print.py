from contextlib import redirect_stdout
import io
import imdb
import copy


def test_print_movies_titles(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given all movies
    # Call the print movies and catch the output
    printed = io.StringIO()
    with redirect_stdout(printed):
        imdb.print_movies(enriched_movies)
    out = printed.getvalue()

    # Extract all the Harry Potter movies
    hp_movies = "\n".join(
        [line for line in out.split("\n") if "Harry Potter and" in line]
    )

    # and Check that there are 8 lines with Harry Potter
    assert (
        hp_movies.count("Harry Potter and") == 8
    ), "Printing all movies should contain all the 8 'Harry Potter and ...' movies"


def test_print_movies_years(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given all movies
    # Call the print movies and catch the output
    printed = io.StringIO()
    with redirect_stdout(printed):
        imdb.print_movies(enriched_movies)
    out = printed.getvalue()

    # Extract all the Harry Potter movies
    hp_movies = "\n".join(
        [line for line in out.split("\n") if "Harry Potter and" in line]
    )

    # Then check that all the years are printed
    years = [2001, 2002, 2004, 2005, 2007, 2009, 2010, 2011]
    for year in years:
        assert str(year) in hp_movies


### IGNORE BEGIN


def get_header_line(lines):
    for line in lines:
        if all([t in line.lower() for t in ["score", "year", "title", "actors"]]):
            return line
    return None


def test_print_movies_header(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given all movies
    # Call the print movies and catch the output
    printed = io.StringIO()
    with redirect_stdout(printed):
        imdb.print_movies(enriched_movies)
    out = printed.getvalue()

    header_line = get_header_line(out.split("\n"))

    assert header_line


def test_print_movies_only_actors(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given all movies
    # Call the print movies and catch the output
    printed = io.StringIO()
    with redirect_stdout(printed):
        imdb.print_movies(enriched_movies)
    out = printed.getvalue()

    # Extract all the Harry Potter movies
    top_gun_movie = "\n".join(
        [line for line in out.split("\n") if "Top Gun" in line and "1986" in line]
    )

    assert top_gun_movie.lower().count("tom cruise") == 1
    # Should not print the characther name Maverick
    assert top_gun_movie.lower().count("maverick") == 0


def test_print_movies_alignment(enriched_movies):
    enriched_movies = copy.deepcopy(enriched_movies)
    # Given all movies
    # Call the print movies and catch the output
    printed = io.StringIO()
    with redirect_stdout(printed):
        imdb.print_movies(enriched_movies)
    out = printed.getvalue()

    # Extract all the Harry Potter movies
    top_gun_movie = "\n".join(
        [
            line
            for line in out.split("\n")
            if "Mission: Impos" in line and "2011" in line
        ]
    )
    header_line = get_header_line(out.split("\n"))

    header_title_idx = header_line.lower().find("title")
    movie_title_idx = top_gun_movie.lower().find("mission:")
    assert header_title_idx == movie_title_idx

    header_actors_idx = header_line.lower().find("actors")
    movie_actors_idx = top_gun_movie.lower().find("tom cruise")

    assert header_actors_idx == movie_actors_idx


### IGNORE END
