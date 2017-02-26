import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

db.init_app(app)

app.config.from_object(os.environ['APP_SETTINGS'])

# app.register_blueprint(book_blueprint, url_prefix='/')
