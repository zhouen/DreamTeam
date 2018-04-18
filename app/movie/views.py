from flask import render_template

from . import movie
from ..models import Movie


@movie.route('/')
def list_movies():
    """
    List all movies
    """
    movies = Movie.query.all()
    return render_template('movie/index.html', movies=movies, title='Movies')