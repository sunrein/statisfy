from database import db

class Edition(db.Model):
    __tablename__ = 'edition'

    id = db.Column(db.Integer, primary_key=True)
    page_count = db.Column(db.Integer, nullable=False)
    format = db.Column(db.Enum('PHYSICAL', 'DIGITAL', 'AUDIOBOOK'), nullable=False)
    publisher = db.Column(db.String(255), nullable=False)
    book_id = db.Column(db.Integer, ForeignKey("book.id"), nullable=False)

    book = db.relationship('statisfy.books.models.Book', uselist=False)

    def __init__(page_count, format, publisher, book_id):
        self.page_count = page_count
        self.format = format
        self.publisher = publisher
        self.book_id = book.id

    def __repr__():
        return "<Edition id: {id}>".format(id=self.id)
        return "<Edition page count: {page_count}>".format(page_count=self.page_count)
        return "<Edition format: {format}>".format(format=self.format)
        return "<Edition publisher: {publisher}>".format(publisher=self.publisher)
        return <"Edition book_id: {book_id}>".format(book_id=self.book_id)
