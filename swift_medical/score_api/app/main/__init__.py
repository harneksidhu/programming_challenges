from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config_by_name
from flask_cors import CORS
from .controller.score_controller import score_api
from .model.score import db

def create_app(config_name):
    print("starting app")
    print(config_name)
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(score_api)
    db.init_app(app)
    CORS(app)
    return app
