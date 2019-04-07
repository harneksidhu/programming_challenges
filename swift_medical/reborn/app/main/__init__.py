from flask import Flask
from .config import config_by_name
from flask_cors import CORS
from .controller.event_controller import event_splitter

def create_app(config_name):
    print("starting app")
    print(config_name)
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    app.register_blueprint(event_splitter)
    CORS(app)
    return app
