from flask import Flask
from books.controllers import book_blueprint

# Import models for alembic tracking
from statisfy.books.models import Book
from statisfy.acquisitions.models import Acquisition
from statisfy.editions.models import Edition
from statisfy.reads.models import Reads
from statisfy.users.models import User

app = Flask(__name__)

app.register_blueprint(book_blueprint, url_prefix='/')
