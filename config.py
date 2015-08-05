class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = None
    RAPIDPRO_TOKEN = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    
class ProductionConfig(Config):
    DATABASE_URI = None

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    COVERALL_TOKEN = 'AflqEfge180scOPSHqXvdecsGIJJdZejt' #previos token