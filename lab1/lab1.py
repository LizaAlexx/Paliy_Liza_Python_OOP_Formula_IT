# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union

class Table:
    def __init__ (self, material: str, color: str):
        self.material = material
        self.color = color
    def add_item (self, item: str) -> None:
        pass

class Chair:
    def sit(self, action) -> None:
        pass
    def rotate(self) -> None:
        pass

class Teaspoon:
    def measure(self) -> Union[int, float]:
        pass
    def clean(self) -> None:
        pass

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
