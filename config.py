class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://james:29654387@localhost/python_lms'

config_options ={"production":ProdConfig,"default":DevConfig}
