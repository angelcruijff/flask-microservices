import unittest

from flask_script import Manager

from __init__ import create_app, db
from api.models import User


app = create_app()
manager = Manager(app)


@manager.command
def test():
    """Runs the unit tests without test coverage."""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def recreate_db():
    """Recreates a database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def seed_db():
    """Seeds the database."""
    db.session.add(User(username='mhidalgo', email="miguel.hidalgo@ikusi.com"))
    db.session.add(User(username='miguelhidalgo', email="mhidalgo@ikusi.com"))
    db.session.commit()



if __name__ == '__main__':
    manager.run()
