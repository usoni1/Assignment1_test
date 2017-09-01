from flask import Flask
from flask_bootstrap import Bootstrap
from config import config
from pymongo import MongoClient
from main import main as main_blueprint

bootstrap = Bootstrap()
db = None

def create_app(config_name):
    global db
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap = Bootstrap(app)
    client = MongoClient(app.config['PYMONGO_DATABASE_URI'])
    db = client[app.config['PYMONGO_DB']]
    app.register_blueprint(main_blueprint)

    return app