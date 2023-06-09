import os

class Config(object):
    FLASK_DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_SETTINGS = os.environ.get("APP_SETTINGS")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SCHEDULER_API_ENABLED = True


class ProductionConfig(Config):
    FLASK_DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    FLASK_DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
