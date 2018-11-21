from flask import Flask

from chartmiru.config import app_config
from chartmiru.database import Database, db

__version__ = '0.1'
app = Flask(__name__)

def create_app(env_name):
    app.config.from_object(app_config.config[env_name])
    app_config.config[env_name].init_app(app)

    db.init_app(app)
    Database(app)