from datetime import datetime

from database import db

class Acquisition(db.Model):
    __tablename__ = 'acquisition'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    purchase_date = db.Column(db.DateTime)

    user = db.relationship('statisfy.users.models.User', uselist=False)
    book = db.relationship('statisfy.books.models.Book', uselist=False)

    def __init__(self, user_id, book_id, purchase_date=None):
        self.user_id = user_id
        self.book_id = book_id
        self.purchase_date = purchase_date

    def __repr__(self):
        return "Acquisition id:{id}".format(id=self.id)
