from flask import Flask
from flask_bcrypt import Bcrypt
import logging

from .config import config_by_name

flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    flask_bcrypt.init_app(app)
    app.logger.addHandler(logging.StreamHandler())
    app.logger.setLevel(logging.INFO)
    return app
