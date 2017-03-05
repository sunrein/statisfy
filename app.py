import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from database import db
from statisfy.books.controllers import book_blueprint

app = Flask(__name__)

db.app = app
db.init_app(app)

app.config.from_object(os.environ['APP_SETTINGS'])

app.register_blueprint(book_blueprint, url_prefix='/')
