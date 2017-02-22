from database import db
from datetime import datetime

class Reads(db.Model):
    __tablename__ = 'reads'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    star_rating = db.Column(db.Integer) # should this be an enum instead? How to limit range?
    genre = db.Column(db.String(255))
    external_review = db.Column(db.Enum()) #unsure of categories

    user = db.relationship("statisfy.users.models.User", uselist=False)
    book = db.relationship("statisfy.books.models.Book", uselist=False)


    def __init__(user_id, book_id, start_date, end_date, star_ratig, genre, external_review):
        self.user_id = user_id
        self.book_id = book_id
        self.start_state = start_date
        self.end_date = end_date
        self.star_rating = star_rating
        self.genre = genre
        self.external_review = external_review

    # def __repr__():
    #     return "<Reads id: {id}>".format(id=self.id)
    #     return "<Reads user_id: {user_id}>".format(user_id=user.id)
    #     return "<Reads book_id: {book_id}>".format(book_id=self.book_id)
    #     return "<Reads start_date: {start_date}>".format(start_date=self.start_date)
    #     return "<Reads end_date: {end_date}>".format(end_date=self.end_date)
    #     return "<Reads star_rating: {star_rating}>".format(star_rating=self.star_rating)
    #     return "<Reads genre: {genre}>".format(genre=self.genre)
    #     return "<Reads external_review: {external_review}>".format(external_review=self.external_review)
