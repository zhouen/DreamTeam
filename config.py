
class Config(object):
    """
    Common configurations
    """

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}

fields_to_remove = [
    'production_companies',
    'backdrop_path',
    'belongs_to_collection',
    'status',
    'tagline',
    'video'
]

fields_recreate = [
    'spoken_languages',
    'production_countries',
    'genres'
]

"""
"spoken_languages": [
    {
        "iso_639_1": "en",
        "name": "English"
    }
]

"production_countries": [
    {
      "iso_3166_1": "US",
      "name": "United States of America"
    }
]

"genres": [
    {
        "id": 35,
        "name": "Comedy"
    },
    {
        "id": 18,
        "name": "Drama"
    }
]
"""
