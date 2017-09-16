import os
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:29654387@localhost/python_lms'


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:29654387@localhost/python_lms'

config_options ={"production":ProdConfig,"default":DevConfig}
