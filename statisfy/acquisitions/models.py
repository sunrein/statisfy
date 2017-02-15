from database import db
from datetime import datetime

class Acquisition(db.Model):
    __tablename__ = 'acquisition'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey("user.user_id"), nullable=False)
    book_id = db.Column(db.Integer, ForeignKey("book.book_id"), nullable=False)
    purchase_date = db.Column(db.DateTime)
