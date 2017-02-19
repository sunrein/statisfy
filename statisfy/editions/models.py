from database import db

class Edition(db.Model):
    __tablename__ = 'edition'

    id = db.Column(db.Integer, primary_key=True)
    page_count = db.Column(db.Integer, nullable=False)
    format = db.Column(db.Enum('PHYSICAL', 'DIGITAL', 'AUDIOBOOK'), nullable=False)
    publisher = db.Column(db.String(255), nullable=False)
    book_id = db.Column(db.Integer, ForeignKey("book.id"), nullable=False)

    book = db.relationship('statisfy.books.models.Book', uselist=False)
