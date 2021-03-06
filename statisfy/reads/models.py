from datetime import datetime

from database import db

class Reads(db.Model):
    __tablename__ = 'reads'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    star_rating = db.Column(db.Integer)
    genre = db.Column(db.String(255))
    external_review = db.Column(db.String(255))

    user = db.relationship("statisfy.users.models.User", uselist=False)
    book = db.relationship("statisfy.books.models.Book", uselist=False)

    def __init__(self, user_id, book_id, start_date=None, end_date=None, star_rating=None, genre=None, external_review=None):
        self.user_id = user_id
        self.book_id = book_id
        self.start_state = start_date
        self.end_date = end_date
        self.star_rating = star_rating
        self.genre = genre
        self.external_review = external_review

    def __repr__(self):
        return "<Reads id: {id}>".format(id=self.id)
