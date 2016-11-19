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

movies = [
    Movie(
        'Boudu Saved From Drowning',
        'https://upload.wikimedia.org/wikipedia/en/c/c4/Boudu_sauv%C3%A9_des_eaux.jpg',
        'https://www.youtube.com/watch?v=PYkB5W4lYsQ'
    ),
    Movie(
        'A Hard Day\'s Night',
        'https://s-media-cache-ak0.pinimg.com/236x/dc/1e/cd/dc1ecd50b2d0e8db32c95e0cda98bd09.jpg',
        'https://www.youtube.com/watch?v=q0eJEX5c1sM'
    ),
    Movie(
        'The Exploding Girl',
        'https://upload.wikimedia.org/wikipedia/en/c/c0/The_exploding_girl.jpg',
        'https://www.youtube.com/watch?v=vUB3NNbVWnA'
    )
]

if (__name__ == "__main__"):
    open_movies_page(movies)
