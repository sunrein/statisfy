from database import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(225), nullable=False, unique=True)
    password = db.Column(db.String(225), nullable=False)
    email = db.Column(db.String(225), nullable=False, unique=True)

    reads = db.relationship('statisfy.reads.models.Reads', uselist=True)
    acquisitions = db.relationship('statisfy.acquisitions.models.Acquisition', uselist=True)
