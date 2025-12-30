import json
import os

class Book:
    def __init__(self, title, author, isbn, genre, is_available=True):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.is_available = is_available

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "genre": self.genre,
            "is_available": self.is_available
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["author"], data["isbn"], data["genre"], data["is_available"])

class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Member(Person):
    def __init__(self, name, email, member_id, borrowed_books=None):
        super().__init__(name, email)
        self.member_id = member_id
        self.borrowed_books = borrowed_books if borrowed_books else []

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["email"], data["member_id"], data.get("borrowed_books", []))

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.books_file = "data/books.json"
        self.members_file = "data/members.json"
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def register_member(self, member):
        self.members.append(member)
        self.save_data()

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def borrow_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member and book and book.is_available:
            book.is_available = False
            member.borrowed_books.append(book.to_dict())
            self.save_data()
            return True, "Book borrowed successfully!"
        elif not book.is_available:
            return False, "Book is currently unavailable."
        else:
            return False, "Member or Book not found."

    def return_book(self, member_id, isbn):
        member = self.find_member(member_id)
        book = self.find_book(isbn)

        if member and book:
            # Check if member actually has this book
            for borrowed in member.borrowed_books:
                if borrowed['isbn'] == isbn:
                    book.is_available = True
                    member.borrowed_books.remove(borrowed)
                    self.save_data()
                    return True, "Book returned successfully!"
            return False, "Member does not have this book."
        return False, "Member or Book not found."

    def save_data(self):
        with open(self.books_file, 'w') as f:
            json.dump([book.to_dict() for book in self.books], f, indent=4)
        with open(self.members_file, 'w') as f:
            json.dump([member.to_dict() for member in self.members], f, indent=4)

    def load_data(self):
        if os.path.exists(self.books_file):
            with open(self.books_file, 'r') as f:
                try:
                    books_data = json.load(f)
                    self.books = [Book.from_dict(b) for b in books_data]
                except json.JSONDecodeError:
                    self.books = []
        
        if os.path.exists(self.members_file):
            with open(self.members_file, 'r') as f:
                try:
                    members_data = json.load(f)
                    self.members = [Member.from_dict(m) for m in members_data]
                except json.JSONDecodeError:
                    self.members = []
