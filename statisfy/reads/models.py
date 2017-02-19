from database import db
from datetime import datetime

class Reads(db.Model):
    __tablename__ = 'reads'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.id"), nullable=False)
    book_id = db.Column(db.Integer, ForeignKey("book.id"), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    star_rating = db.Column(db.Integer) # should this be an enum instead? How to limit range?
    genre = db.Column(db.String(255))
    external_review = db.Column(db.Enum() #unsure of categories

    user = db.relationship("statisfy.users.models.User", uselist=False)
    book = db.relationship("statisfy.books.models.Book", uselist=False)
