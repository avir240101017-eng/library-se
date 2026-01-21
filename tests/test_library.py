import unittest
from src.library import Library, LibraryError


class TestLibrarySprint1(unittest.TestCase):

    def test_add_book_success(self):
        lib = Library()
        lib.add_book("B1", "1984", "George Orwell")
        self.assertIn("B1", lib.books)

    def test_add_duplicate_book(self):
        lib = Library()
        lib.add_book("B1", "1984", "George Orwell")
        with self.assertRaises(LibraryError):
            lib.add_book("B1", "Animal Farm", "George Orwell")
class TestLibrarySprint2(unittest.TestCase):

    def test_borrow_available_book(self):
        lib = Library()
        lib.add_book("B1", "1984", "George Orwell")
        lib.borrow_book("B1")
        self.assertTrue(lib.books["B1"]["borrowed"])

    def test_borrow_unavailable_book(self):
        lib = Library()
        lib.add_book("B1", "1984", "George Orwell")
        lib.borrow_book("B1")
        with self.assertRaises(LibraryError):
            lib.borrow_book("B1")

    def test_return_book(self):
        lib = Library()
        lib.add_book("B1", "1984", "George Orwell")
        lib.borrow_book("B1")
        lib.return_book("B1")
        self.assertFalse(lib.books["B1"]["borrowed"])
class TestLibrarySprint3(unittest.TestCase):

    def test_report_contains_header(self):
        lib = Library()
        report = lib.generate_report()
        self.assertIn("Book ID | Title | Author | Status", report)

    def test_report_contains_book(self):
        lib = Library()
        lib.add_book("B1", "1984", "George Orwell")
        report = lib.generate_report()
        self.assertIn("1984", report)

