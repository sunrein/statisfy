import unittest

from books.models import Book

class BookTestCase(unittest.TestCase):
	def setUp():
		book = Book(
			title="A Book",
			author="Someone Something",
			length_category="NOVEL",
			age_group="ADULT"
		)
		db.session.add(book)

	def test_book_creation(self):
		self.assertIsNone(book.id)
		db.session.commit(book)
		self.assertIsInstance(book, Book)
		self.assertIsNotNone(book.id)
		self.assertIsInstance(book.id, int)
