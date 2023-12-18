# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
class Table:
    """
    Class representing a table.

    Attributes:
        material (str): The material of the table.
        color (str): The color of the table.

    Methods:
        add_item(item: str) -> None:
            Adds an item to the table.

            Example:
            >>> table = Table("wood", "brown")
            >>> table.add_item("book")
    """
    def __init__(self, material: str, color: str) -> None:
        self.material = material
        self.color = color

    def add_item(self, item: str) -> None:
        """
        Adds an item to the table.

        Args:
            item (str): The item to be added to the table.

        Returns:
            None

        Example:
            >>> table = Table("wood", "brown")
            >>> table.add_item("book")
        """
        pass

class Chair:
    """
    Class representing a chair.

    Methods:
        sit(action) -> None:
            Allows a person to sit on the chair.

            Args:
                action: The action performed while sitting.

            Returns:
                None

            Example:
                >>> chair = Chair()
                >>> chair.sit("reading")
        rotate() -> None:
            Rotates the chair.

            Returns:
                None

            Example:
                >>> chair = Chair()
                >>> chair.rotate()
    """
    def sit(self, action) -> None:
        """
        Allows a person to sit on the chair.

        Args:
            action: The action performed while sitting.

        Returns:
            None

        Example:
            >>> chair = Chair()
            >>> chair.sit("reading")
        """
        pass

    def rotate(self) -> None:
        """
        Rotates the chair.

        Returns:
            None

        Example:
            >>> chair = Chair()
            >>> chair.rotate()
        """
        pass

class Teaspoon:
    """
    Class representing a teaspoon.

    Methods:
        measure() -> Union[int, float]:
            Measures the quantity with the teaspoon.

            Returns:
                Union[int, float]: The measured quantity.

            Example:
                >>> teaspoon = Teaspoon()
                >>> teaspoon.measure()
        clean() -> None:
            Cleans the teaspoon.

            Returns:
                None

            Example:
                >>> teaspoon = Teaspoon()
                >>> teaspoon.clean()
    """
    def measure(self) -> Union[int, float]:
        """
        Measures the quantity with the teaspoon.

        Returns:
            Union[int, float]: The measured quantity.

        Example:
            >>> teaspoon = Teaspoon()
            >>> teaspoon.measure()
        """
        pass

    def clean(self) -> None:
        """
        Cleans the teaspoon.

        Returns:
            None

        Example:
            >>> teaspoon = Teaspoon()
            >>> teaspoon.clean()
        """
        pass

if __name__ == "__main__":
    #Check the functionality of class instances using doctest
    pass

