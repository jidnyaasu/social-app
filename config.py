import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    ADMINS = [os.getenv("SOCIAL_APP_ADMIN")]
    POSTS_PER_PAGE = 5
    LANGUAGES = ["en", "es", "mr", "hi"]
    TRANSLATOR_URL = os.getenv("TRANSLATOR_URL")
    # ELASTICSEARCH_URL = os.getenv("ELASTICSEARCH_URL")
    # ELASTIC_CA_CERTS = os.getenv("ELASTIC_CA_CERTS")
    # ELASTIC_USERNAME = os.getenv("ELASTIC_USERNAME")
    # ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD")
