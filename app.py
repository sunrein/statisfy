import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
# from   flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required, roles_accepted
from flask_login import LoginManager

from database import db
from statisfy.books.controllers import book_blueprint
from statisfy.users.controllers import user_blueprint

app = Flask(__name__)

db.app = app
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_message = "You must be logged in to access this page."
login_manager.login_view = "auth.login"

app.config.from_object(os.environ['APP_SETTINGS'])

app.register_blueprint(book_blueprint, url_prefix='/')
app.register_blueprint(user_blueprint, url_prefix='/')
