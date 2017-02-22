import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from config import DevelopmentConfig
from app import app
from database import db

app.config.from_object(DevelopmentConfig)

db.create_all()

def load_models():
    from statisfy.books.models import Book
    from statisfy.acquisitions.models import Acquisition
    from statisfy.editions.models import Edition
    from statisfy.reads.models import Reads
    from statisfy.users.models import User

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    load_models()
    manager.run()
