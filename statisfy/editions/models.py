from app import db

class Edition(db.Model):
    __tablename__ = 'edition'

    id = db.Column(db.Integer, primary_key=True)
    page_count = db.Column(db.Integer, nullable=False)
    format = db.Column(db.Enum('PHYSICAL', 'DIGITAL', 'AUDIOBOOK', name="edition_format"), nullable=False)
    publisher = db.Column(db.String(255), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)

    book = db.relationship('statisfy.books.models.Book', uselist=False)

    def __init__(self, page_count, format, publisher, book_id):
        self.page_count = page_count
        self.format = format
        self.publisher = publisher
        self.book_id = book_id

    def __repr__(self):
        return "<Edition id: {id}>".format(id=self.id)
