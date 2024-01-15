from typing import List, Optional

BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Class representing a book.

            Args:
                id_ (int): The identifier of the book.
                name (str): The name of the book.
                pages (int): The number of pages in the book.
        """

        self.id: int = id_
        self.name: str = name
        self.pages: int = pages

    def __str__(self) -> str:
        """
        Returns a string representation of the book.

        Returns:
            str: A string representing the book.

        Example:
            >>> book = Book(id_=1, name='test_name_1', pages=200)
            >>> print(book)
            'Книга "test_name_1"'
        """

        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Returns a string representation that can be used to recreate the book instance.

        Returns:
            str: A string representing the book instance.

        Example:
            >>> book = Book(id_=1, name='test_name_1', pages=200)
            >>> repr(book)
            'Book(id_=1, name=\'test_name_1\', pages=200)'
        """

        return f'Book(id_={self.id}, name=\'{self.name}\', pages={self.pages})'

# TODO написать класс Library
class Library:
    def __init__(self, books: Optional[List[Book]] = None):
        """
        Class representing a library.

        Args:
            books (Optional[List[Book]]): List of books in the library. Defaults to None.
        """
        self.books: List[Book] = books or []

    def get_next_book_id(self) -> int:
        """
        Gets the next available book id.

        Returns:
            int: The next available book id.

        Example:
            >>> empty_library = Library()
            >>> empty_library.get_next_book_id()
            1
        """

        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Gets the index of a book with the specified id.

        Args:
            book_id (int): The id of the book.

        Returns:
            int: The index of the book.

        Raises:
            ValueError: If the book with the specified id does not exist.

        Example:
            >>> list_books = [Book(id_=1, name='test_name_1', pages=200)]
            >>> library_with_books = Library(books=list_books)
            >>> library_with_books.get_index_by_book_id(1)
            0
        """

        for i, book in enumerate(self.books):
            if book.id == book_id:
                return i
        raise ValueError(f"Книги с id {book_id} не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
