import os

class Config(object):
    if os.getenv('DEBUG_MODE'):
        DEBUG = os.getenv('DEBUG_MODE')
    else:
        DEBUG = False
    if os.getenv('TESTING_MODE'):
        TESTING = os.getenv('TESTING_MODE')
    else:
        TESTING = False
    DATABASE_URI = None
    RAPIDPRO_TOKEN = os.getenv('RAPIDPRO_TOKEN')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:' + \
        os.getenv('PRODIWEBHOOKS_MYSQL_ENV_MYSQL_ROOT_PASSWORD') + \
        '@' + os.getenv('PRODIWEBHOOKS_MYSQL_PORT_3306_TCP_ADDR') + \
        '/dependencia'

class ProductionConfig(Config):
    PRODUCTION = True

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    COVERALL_TOKEN = os.getenv('COVERALLS_REPO_TOKEN')
