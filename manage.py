from flask_script import Manager

from __init__ import app

manager = Manager(app)

if __name__ == '__main__':
	manager.run()