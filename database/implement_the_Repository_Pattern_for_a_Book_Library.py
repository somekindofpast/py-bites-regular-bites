from abc import ABC, abstractmethod
from sqlmodel import SQLModel, Field, create_engine, Session, select
import csv


class Book(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    title: str
    author: str


class IBookRepository(ABC):
    @abstractmethod
    def add(self, book: Book):
        """Add a book to the repository"""

    @abstractmethod
    def get_by_title(self, title: str) -> Book | None:
        """Retrieve a book by title"""


class SQLBookRepository(IBookRepository):
    def __init__(self, db_string="sqlite:///books.db"):
        """Initialize database connection"""
        self.engine = create_engine(db_string)
        SQLModel.metadata.create_all(self.engine)

    def add(self, book: Book):
        """Implement adding a book to the database"""
        with Session(self.engine) as session:
            session.add(book)
            session.commit()

    def get_by_title(self, title: str) -> Book | None:
        """Implement retrieving a book by title from the database"""
        with Session(self.engine) as session:
            statement = select(Book).where(Book.title == title)
            return session.exec(statement).first()


class CsvBookRepository(IBookRepository):
    def __init__(self, file_path="books.csv"):
        """Initialize the CSV file path"""
        self.file_path = file_path
        self.fieldnames = ['id', 'title', 'author']
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writeheader()

    def add(self, book: Book):
        """Implement adding a book to the CSV file"""
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
            writer.writerow({'id': book.id, 'title': book.title, 'author': book.author})

    def get_by_title(self, title: str) -> Book | None:
        """Implement retrieving a book by title from the CSV file"""
        with open(self.file_path, 'r', newline='') as csvfile:
            csv_lines = csv.DictReader(csvfile, fieldnames=self.fieldnames)
            for line in csv_lines:
                if line["title"] == title:
                    return Book(id=line["id"], title=line["title"], author=line["author"])
        return None


class MemoryBookRepository(IBookRepository):
    def __init__(self):
        """Initialize in-memory storage"""
        self.storage = []

    def add(self, book: Book):
        """Implement adding a book to memory"""
        self.storage.append(book)

    def get_by_title(self, title: str) -> Book | None:
        """Implement retrieving a book by title from memory"""
        res = list(filter(lambda book: book.title == title, self.storage))
        return None if not res else res[0]