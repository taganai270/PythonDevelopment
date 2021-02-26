"""
2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Dress(ABC):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    @abstractmethod
    def get_square_c(self):
        pass

    @abstractmethod
    def get_square_s(self):
        pass

    @property
    def get_sq_full(self):
        return str(f'Общая площадь ткани\t'
                   f'{round((self.width / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}')


class Coat(Dress):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.square_c = round((self.width / 6.5 + 0.5), 2)

    def get_square_c(self):
        return round(self.width / 6.5 + 0.5, 2)

    def get_square_s(self):
        return round(self.height * 2 + 0.3, 2)

    def __str__(self):
        return f'Расход ткани на пальто {self.square_c}'


class Suit(Dress, ABC):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.width = width
        self.height = height
        self.square_s = round(self.height * 2 + 0.3, 2)

    def get_square_s(self):
        return round(self.height * 2 + 0.3, 2)

    def get_square_c(self):
        return round(self.width / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Расход ткани на костюм {self.square_s}'


coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
