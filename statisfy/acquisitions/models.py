from database import db
from datetime import datetime

class Acquisition(db.Model):
    __tablename__ = 'acquisition'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey("book.id"), nullable=False)
    purchase_date = db.Column(db.DateTime)

    user = db.relationship('statisfy.user.models.User', uselist=False)
    book = db.relationship('statisfy.book.models.Book', uselist=False)
