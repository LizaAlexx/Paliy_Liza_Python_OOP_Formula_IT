from typing import List

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

if __name__ == '__main__':
    # инициализируем список книг
    list_books: List[Book] = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__


