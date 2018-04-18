#!/usr/bin/venv python

from app import db

class Movie(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    imdb_id = db.Column(db.Integer, primary_key=True, unique=True)
    homepage = db.Column(db.String(512))
    original_language = db.Column(db.String(512))
    adult = db.Column(db.Boolean)
    imdb_rating = db.Column(db.Float)
    budget = db.Column(db.Integer)
    original_title = db.Column(db.String(512))
    overview = db.Column(db.String(512))
    popularity = db.Column(db.String(512))
    poster_path = db.Column(db.String(512))
    release_date = db.Column(db.String(512))
    revenue = db.Column(db.Integer)
    runtime = db.Column(db.Integer)
    title = db.Column(db.String(512))
    vote_average = db.Column(db.Float)
    vote_count = db.Column(db.Integer)

    spoken_languages = db.Column(db.String(512)) # comma separated string
    production_countries = db.Column(db.String(512)) # comma separated string
    genres = db.Column(db.String(512)) # comma separated string

    file_name = db.Column(db.String(512)) # movie file name with extension
    parent_dir = db.Column(db.String(512)) # movie parent director name if it is in a folder
    abs_path = db.Column(db.String(512)) # absolute path: movie_root_dir + parent_dir + file_name, this will be used for copying and updated on every upgrade


    def __repr__(self):
        return '<Movie: {}>'.format(self.name)



"""
{
  "adult": false,
  "backdrop_path": "/udx1jnORg79bAGcHNyl1ILsuP5u.jpg",
  "belongs_to_collection": null,
  "budget": 10000000,
  "genres": [
    {
      "id": 35,
      "name": "Comedy"
    },
    {
      "id": 18,
      "name": "Drama"
    }
  ],
  "homepage": "http://ladybird.movie",
  "id": 391713,
  "imdb_id": "tt4925292",
  "original_language": "en",
  "original_title": "Lady Bird",
  "overview": "A California high school student plans to escape from her family and small town by going to college in New York.",
  "popularity": 31.322793,
  "poster_path": "/iySFtKLrWvVzXzlFj7x1zalxi5G.jpg",
  "production_companies": [
    {
      "id": 41077,
      "logo_path": "/1ZXsGaFPgrgS6ZZGS37AqD5uU12.png",
      "name": "A24",
      "origin_country": "US"
    },
    {
      "id": 93105,
      "logo_path": null,
      "name": "IAC Films",
      "origin_country": ""
    }
  ],
  "production_countries": [
    {
      "iso_3166_1": "US",
      "name": "United States of America"
    }
  ],
  "release_date": "2017-09-08",
  "revenue": 43733193,
  "runtime": 94,
  "spoken_languages": [
    {
      "iso_639_1": "en",
      "name": "English"
    }
  ],
  "status": "Released",
  "tagline": "Fly Away Home.",
  "title": "Lady Bird",
  "video": false,
  "vote_average": 7.4,
  "vote_count": 1679
}
"""