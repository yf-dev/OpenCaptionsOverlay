# noinspection PyUnresolvedReferences
from app import app, db
from flask_migrate import MigrateCommand
from flask_script import Manager

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def drop_all():
    db.drop_all()


if __name__ == '__main__':
    manager.run()
