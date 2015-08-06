import os

class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = None
    RAPIDPRO_TOKEN = os.getenv('RAPIDPRO_TOKEN')
    
class ProductionConfig(Config):
    DATABASE_URI = None

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    COVERALL_TOKEN = os.getenv('COVERALLS_REPO_TOKEN')