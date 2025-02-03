#Start by importing these modules
import os.path as path
import csv
import argparse
import re
import sys
from datetime import datetime
from tabulate import tabulate

SCORE_TTL = "Score"
YEAR_TTL = "Year"
TITLE_TTL = "Title"
ACTORS_TTL = "Actors"


def read(filepath: str) -> list[dict]:
    """ Takes the filepath as input
     Returns a list of dictionaries """ 
     
    with open(filepath, mode = 'r', newline ='', encoding= 'UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        list_movies = [row for row in reader]
    return list_movies


def enrich_data(movies: list[dict]) -> list[dict]:
    movies_1 = add_actor(movies)
    movies_2 = add_year(movies_1)
    return movies_2


def print_movies(data: list[dict]):
    headers_table = ["score", "year", "title", "actors"]
    column_widths = {
        "score": 7,
        "year": 8,
        "title": 33,
        "actors": 50
    }

    # Print the headers
    header_str = " | ".join([header.ljust(column_widths[header]) for header in headers_table])
    print(header_str)
    print("-" * (sum(column_widths.values()) + 9))  # Adjust length based on column widths and separators

    # Print each movie row
    for movie in data:
        # Get the movie details or default values
        score = str(movie.get('score', 'N/A'))[:column_widths['score']].ljust(column_widths['score'])
        year = str(movie.get('year', 'N/A'))[:column_widths['year']].ljust(column_widths['year'])
        title = movie.get('names', 'N/A')[:column_widths['title']].ljust(column_widths['title'])
        actors = ", ".join(movie.get('actors', []))[:column_widths['actors']].ljust(column_widths['actors'])

        # Print the formatted row
        row_str = f"{score} | {year} | {title} | {actors}"
        print(row_str)


def add_year(movies: list[dict]) -> list[dict]:
    """ Adds a new key year to each movie entries whose value is extracted from the key date_x

    Args:
        movies (list[dict]): A list of dictionaries containing details of movies

    Returns:
        list[dict]: A list of dictionaries containing new key named year
    """
    for dict_movies in movies:
        date_string = dict_movies['date_x'].strip()
        
        #Convert string to date object
        date_object = datetime.strptime(date_string, "%m/%d/%Y")
        dict_movies['year'] = date_object.year
    return movies


def add_actor(movies: list[dict]) -> list[dict]:
    """ Adds a new key actors to each movie entries whose value (comma separated) is extracted from the key crew

    Args:
        movies (list[dict]): A list of dictionaries containing details of movies

    Returns:
        list[dict]: A list of dictionaries containing new key named actors
    """
    new_movies = movies
    for dict_movie in new_movies:
        list_actors = dict_movie['crew'].split(',')
        dict_movie['actors'] =list_actors[::2]
    return new_movies


def get_filtered_movies(
    movies: list[dict],
    actors: list[str] = None,
    genres: list[str] = None,
    years: list[int] = None,
    top: int = 0,
    sort_by: str = None,
    ascending: bool = False   
    
) -> list[dict]:
    print("top value", top)
    """Takes in the data list and filters the movies based on the
    given parameters

    Args:
        movies (list[dict]): List of all the movies
        actors (list[str]): List of Actors that needs to be in the movies
        genres (list[str]): List of Genres to include in the filter
        years (list[int]): List of years movies were released in
        top (int): How many movies to return
        sort_by (str): What key to sort by, default 'score'
        asc (bool): Sort ascending (e.g. the lowest score is returned first)

    Returns:
        list[dict]: The filtered list of movies
    """
    #Default to empty list if any of the arguments are None
    actors = [actor.strip().lower() for actor in (actors or [])]
    genres = genres or []
    years = years or []
    filtered_movies = []
    
    for movie in movies:
        if (not actors or all(actor in [a.strip().lower() for a in movie['actors']] for actor in actors)) and (not genres or any(genre in movie['genre'] for genre in genres)) and (not years or movie['year'] in years):
            filtered_movies.append(movie)
   
    if sort_by:
        if sort_by in ['score', 'year']:
            filtered_movies.sort(
                key=lambda movie: movie.get(sort_by, 0),  # Use movie.get() to handle missing values
                reverse=not ascending  # If ascending is False, sort in descending order
            )
    print("top ---type", type(top))
    print(top)
    if top > 0:
        filtered_movies = filtered_movies[:top]
    return filtered_movies


def main():
    # path.join() is agnostic to operating system (Windows Vs Linux)
    data = read(path.join("data", "imdb_movies.csv"))

    # -------------------------------------
    # Command line input parser
    # -------------------------------------
    arg_parser = argparse.ArgumentParser(description="Filter movies based on actors, genres, years, and more.")
    arg_parser.add_argument('--actors', nargs ='+', help ='Space-separated list of actors', required=False)
    arg_parser.add_argument('--genres', nargs ='+', help = 'Space-separated list of genres', required=False)
    arg_parser.add_argument('--years', type=int, nargs='+', help ='Space-separated list of years', required=False)
    arg_parser.add_argument('--top', type=int, default = 0, help ='Number of top movies to display', required=False)
    arg_parser.add_argument('--sort', type=str, choices=['score', 'title', 'year'], help='Sort movies by score, title, or year', required=False)
    arg_parser.add_argument('--ascending', action='store_true', help='Sort in ascending order if specified', required=False)
    # -------------------------------------
    args = arg_parser.parse_args()
    # -------------------------------------

    # Add the additional fields to the raw data
    movies = enrich_data(data)

    # Run the filter function
    movies = get_filtered_movies(
        movies,
        args.actors,
        args.genres,
        args.years,
        args.top,
        args.sort,
        args.ascending,
    )
    # And finally print a nice table
    print_movies(movies)


if __name__ == "__main__":
    main()
