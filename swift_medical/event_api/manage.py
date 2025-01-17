import os
import unittest

from flask_script import Manager

from app.main import create_app, db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

manager = Manager(app)

@manager.command
def create_db():
    db.create_all()

@manager.command
def run():
    app.run(host='0.0.0.0')

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
