class Insect:
    """Базовый класс, представляющий насекомых."""

    def __init__(self, name: str, color: str):
        """
        Инициализация насекомого.

        Args:
            name (str): Имя насекомого.
            color (str): Цвет насекомого.
        """
        self._name = name
        self._color = color

    def make_sound(self) -> str:
        """
        Издать звук.

        Возвращает:
            str: Строка, представляющая звук, который издает насекомое.
        """
        return "Беззвучно"

    def move(self) -> str:
        """
        Движение.

        Возвращает:
            str: Строка, представляющая движение насекомого.
        """
        return "Медленно двигается"

    def __str__(self) -> str:
        """
        Возвращает строковое представление насекомого.

        Возвращает:
            str: Строковое представление насекомого.
        """
        return f"{self._color} {self._name}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление насекомого для отладки.

        Возвращает:
            str: Строковое представление насекомого.
        """
        return f"Насекомое({self._name}, {self._color})"


class Butterfly(Insect):
    """Класс, представляющий бабочку, наследующий от Insect."""

    def __init__(self, name: str, color: str, wingspan: float):
        """
        Инициализация бабочки.

        Args:
            name (str): Имя бабочки.
            color (str): Цвет бабочки.
            размах крыльев (float): Размах крыльев бабочки.
        """
        super().__init__(name, color)
        self._wingspan = wingspan

    def fly(self) -> str:
        """
        Полет.

        Возвращается:
            str: Строка, представляющая действие полета бабочки.
        """
        return "Бабочка грациозно порхает в воздухе."

    def __str__(self) -> str:
        """
        Возвращает строковое представление бабочки.

        Возвращает:
            str: Строковое представление бабочки.
        """
        return f"Бабочка ({self._color} {self._name}, размах крыльев: {self._wingspan} см)"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление бабочки для отладки.

        Возвращает:
            str: Строковое представление бабочки.
        """
        return f"Бабочка({self._name}, {self._color}, {self._wingspan})"


class Grasshopper(Insect):
    """Класс, представляющий кузнечика, наследующий от Insect."""

    def __init__(self, name: str, color: str, jump_distance: float):
        """
        Инициализация кузнечика.

        Args:
            name (str): Имя кузнечика.
            color (str): Цвет кузнечика.
            jump_distance (float): Максимальное расстояние, на которое может прыгнуть кузнечик.
        """
        super().__init__(name, color)
        self._jump_distance = jump_distance

    def jump(self) -> str:
        """
        Прыжок.

        Возвращает:
            str: Строка, представляющая прыжок кузнечика.
        """
        return "Кузнечик прыгает в воздух."

    def __str__(self) -> str:
        """
        Возвращает строковое представление кузнечика.

        Возвращает:
            str: Строковое представление кузнечика.
        """
        return f"Кузнечик ({self._color} {self._name}, длина прыжка: {self._jump_distance} метров)"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление кузнечика для отладки.

        Возвращает:
            str: Строковое представление кузнечика.
        """
        return f"Кузнечик({self._name}, {self._color}, {self._jump_distance})"


class Cockroach(Insect):
    """Класс, представляющий таракана, наследующий от Insect."""

    def __init__(self, name: str, color: str, speed: float):
        """
        Инициализация таракана.

        Args:
            name (str): Имя таракана.
            color (str): Цвет таракана.
            speed (float): Скорость таракана.
        """
        super().__init__(name, color)
        self._speed = speed

    def hide(self) -> str:
        """
        Прятаться.

        Возвращает:
            str: Строка, представляющая действие таракана прятаться.
        """
        return "Таракан убегает, скрываясь во тьме."

    def __str__(self) -> str:
        """
        Возвращает строковое представление таракана.

        Возвращает:
            str: Строковое представление таракана.
        """
        return f"Таракан ({self._color} {self._name}, скорость: {self._speed} м/с)"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление таракана для отладки.

        Возвращает:
            str: Строковое представление таракана.
        """
        return f"Таракан({self._name}, {self._color}, {self._speed})"
