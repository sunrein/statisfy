from database import db

class Book(db.Model):
	__tablename__ = 'book'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(225), nullable=False)
	author = db.Column(db.String(225), nullable=False)
	length_category = db.Column(db.Enum('NOVEL', 'NOVELETTE', 'NOVELLA', 'SHORT_STORY', 'ANTHOLOGY', 'GRAPHIC_NOVEL', name='book_length_category'), nullable=False)
	age_group = db.Column(db.Enum('ADULT', 'YOUNG_ADULT', 'MIDDLE_GRADE', 'EARLY_READER', name='book_age_group'), nullable=False)

	editions = db.relationship('statisfy.editions.models.Edition', uselist=True)


	def __init__(self, title, author, length_category, age_group):
		self.title = title
		self.author = author
		self.length_category = length_category
		self.age_group = age_group

	def __repr__(self):
		return "<Book id: {id}>".format(id=self.id)
