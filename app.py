"""The entry point to the Movie Trailer Website application

Attributes:
    movies (:obj:`list` of :obj:`Movie`): The list of movies with which to
        populate the Movie Trailer Website

Example:
    The application can be run from the terminal::

        $ python app.py

"""

from movie import Movie
from fresh_tomatoes import open_movies_page

movies = [Movie('x', 'y', 'z')]

if (__name__ == "__main__"):
    open_movies_page(movies)
