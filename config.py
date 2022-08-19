import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.getenv("SECRET_KEY") or "Bheri very the eesi to understand kee"
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
