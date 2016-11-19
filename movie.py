"""A published movie

Args:
    title (str): The formal title of the movie
    poster_image_url (str): A string representation of the URL that points to
        a poster image for the movie
    trailer_youtube_url (str): A string representation of the URL that points
        to the YouTube-hosted video of the movie's trailer

"""


class Movie():

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
