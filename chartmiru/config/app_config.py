import os

#from dotenv import load_dotenc, find_dotenv

class Config:
    # request header
    REQUEST_UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    REQUEST_URI = 'https://kabuoji3.com/stock/file.php'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')

    @staticmethod
    def init_app(app):
        Config.init_app(app)

config = {
    'development': DevelopmentConfig,
}
