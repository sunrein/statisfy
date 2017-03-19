from flask import Blueprint, request, redirect, render_template, url_for
from statisfy.books.models import Book
from statisfy.templates import template_env

from app import db

book_blueprint = Blueprint("book", __name__)

@book_blueprint.route("books", methods=["GET"])
def index():
    books = Book.query.all()
    book_template = template_env.get_template('_show_books.html')
    page_view = book_template.render(books=books)
    return page_view

@book_blueprint.route("books/new", methods=["GET", "POST"])
def create():
    if request.method == 'POST':
        book = Book(
                    title=request.form['title'],
                    author=request.form['author'],
                    length_category=request.form['length_category'],
                    age_group=request.form['age_group']
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('book.show', book_id=book.id))
    create_form = template_env.get_template("_create_books.html")
    return render_template(create_form)

@book_blueprint.route("book/<int:book_id>", methods=["GET"])
def show(book_id):
    book = Book.query.get(book_id)
    book_template = template_env.get_template('_get_book.html')
    page_view = book_template.render(book=book)
    return page_view

@book_blueprint.route("book/<int:book_id>", methods=["PATCH"])
def update(book_id):
    book = Book.query.get(book_id)
    book.title=request.form['title']
    book.author=request.form['author']
    book.length_category=request.form['length_category']
    book.age_group=request.form['age_group']
    db.session.add(book)
    db.session.commit()
    return redirect(url_for('book.show', book_id=book.id))

@book_blueprint.route("book/<int:book_id>/edit", methods=['GET'])
def edit(book_id):
    book = Book.query.get(book_id)
    book_template = template_env.get_template('_edit_book.html')
    page_view = book_template.render(book=book)
    return page_view

@book_blueprint.route("book/<int:book_id>/delete", methods=["GET"])
def destroy(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return redirect(url_for('book.index'))
