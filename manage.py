import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from config import DevelopmentConfig
from app import app, db

app.config.from_object(DevelopmentConfig)

db.create_all()

def load_models():
    from statisfy.books.models import Book
    from statisfy.acquisitions.models import Acquisition
    from statisfy.editions.models import Edition
    from statisfy.users.models import User
    # from statisfy.reads.models import Reads

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    load_models()
    manager.run()
