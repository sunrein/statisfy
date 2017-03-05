from flask import Blueprint
from statisfy.books.models import Book
from statisfy.templates import template_env

book_blueprint = Blueprint("book", __name__)

@book_blueprint.route("books", methods=["GET"])
def index():
    books = Book.query.all()
    book_template = template_env.get_template('_show_books.html')
    page_view = book_template.render(books=books)
    return page_view
