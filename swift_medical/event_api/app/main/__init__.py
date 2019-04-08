from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config_by_name
from flask_cors import CORS
from .controller.event_controller import event_splitter
from .model.event import db

def create_app(config_name):
    print("starting app")
    print(config_name)
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(event_splitter)
    db.init_app(app)
    CORS(app)
    return app
