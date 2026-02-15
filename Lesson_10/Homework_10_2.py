

"""Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру. 
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру. 
Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор. 
Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної."""

import math
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, r):
        self.__r = r
    def area(self):
        return math.pi * self.__r**2
    def perimeter(self):
        return 2 * math.pi * self.__r

class Square(Figure):
    def __init__(self, a):
        self.__a = a
    def area(self):
        return self.__a ** 2
    def perimeter(self):
        return 4 * self.__a


class Rectangle(Figure):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    def area(self):
        return self.__a * self.__b
    def perimeter(self):
        return 2 * (self.__a + self.__b)

figures = [
    Circle(5),
    Square(4),
    Rectangle(5, 3)
]

for f in figures:
    print(f"{f.__class__.__name__}: Площа = {f.area():.2f}, Периметр = {f.perimeter():.2f}")

