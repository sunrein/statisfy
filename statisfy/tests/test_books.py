import unittest

from statisfy.books.models import Book
from database import db


class BookTestCase(unittest.TestCase):
    def setUp(self):
        self.book = Book(
            title="A Book",
            author="Someone Something",
            length_category="NOVEL",
            age_group="ADULT"
        )
        db.session.add(self.book)

    def test_book_creation(self):
        self.assertIsNone(self.book.id)
        db.session.commit(self.book)
        self.assertIsInstance(self.book, Book)
        self.assertIsNotNone(self.book.id)
        self.assertIsInstance(self.book.id, int)
