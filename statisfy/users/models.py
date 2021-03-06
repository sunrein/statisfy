from database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(225), nullable=False, unique=True)
    password = db.Column(db.String(225), nullable=False)
    email = db.Column(db.String(225), nullable=False, unique=True)

    reads = db.relationship('statisfy.reads.models.Reads', uselist=True)
    acquisitions = db.relationship('statisfy.acquisitions.models.Acquisition', uselist=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return "<User id: {id}>".format(id=self.id)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)
