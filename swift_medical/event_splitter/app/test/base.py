from flask_testing import TestCase

from app.main import create_app
from manage import app


class BaseTestCase(TestCase):
  """ Base Tests """

  def create_app(self):
    app = create_app('unit')
    return app
