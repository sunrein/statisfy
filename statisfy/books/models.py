from database import db

class Book(db.Model):
	__tablename__ = 'book'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(225), nullable=False)
	author = db.Column(db.String(225), nullable=False)
	length_category = db.Column(db.Enum('NOVEL', 'NOVELETTE', 'NOVELLA', 'SHORT_STORY', 'ANTHOLOGY', 'GRAPHIC_NOVEL'), nullalbe=False)
	age_group = db.Column(db.Enum('ADULT', 'YOUNG_ADULT', 'MIDDLE_GRADE', 'EARLY_READER'), nullable=False)

	# Question - should there be any validations on the Book model?