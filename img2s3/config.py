import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
postegres_uri_template = 'postgresql://{}:{}@{}:{}/{}'


class Config:
    def __init__(self):
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    def __init__(self):
        super(DevelopmentConfig, self).__init__()
        self.DEBUG = True
        self.ENV = 'development'
        self.SQLALCHEMY_DATABASE_URI = postegres_uri_template.format(
            os.environ['DEV_DB_USERNAME'],
            os.environ['DEV_DB_PASSWORD'],
            os.environ['DEV_DB_ADDRESS'],
            os.environ['DEV_DB_PORT'],
            os.environ['DEV_DB_NAME']
        )


class TestConfig(Config):
    def __init__(self):
        super(TestConfig, self).__init__()
        self.TESTING = True
        self.ENV = 'development'
        self.SQLALCHEMY_DATABASE_URI = postegres_uri_template.format(
            os.environ['TEST_DB_USERNAME'],
            os.environ['TEST_DB_PASSWORD'],
            os.environ['TEST_DB_ADDRESS'],
            os.environ['TEST_DB_PORT'],
            os.environ['TEST_DB_NAME']
        )


class ProductionConfig(Config):
    def __init__(self):
        super(ProductionConfig, self).__init__()
        self.SQLALCHEMY_DATABASE_URI = postegres_uri_template.format(
            os.environ['DB_USERNAME'],
            os.environ['DB_PASSWORD'],
            os.environ['DB_ADDRESS'],
            os.environ['DB_PORT'],
            os.environ['DB_NAME']
        )


def create_config() -> Config:
    if os.getenv('TEST') == '1' or os.getenv('TRAVIS') == 'true':
        return TestConfig()
    elif os.getenv('DEV') == '1':
        return DevelopmentConfig()
    else:
        return ProductionConfig()
