"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса;
методы: нахождение периметра и площади окружности),
Triangle (атрибуты: три точки, методы: нахождение площади и периметра),
Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""

import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure:
    def find_perimeter(self):
        raise NotImplementedError

    def find_square(self):
        raise NotImplementedError

    @staticmethod
    def find_length(point1: Point, point2: Point):
        return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5

    @staticmethod
    def find_semi_perimeter(len1: float, len2: float, len3: float):
        return (len1 + len2 + len3) / 2


class Circle(Figure):
    def __init__(self, centre: Point, radius: int):
        self.centre = centre
        self.radius = radius

    def find_perimeter(self) -> float:
        return 2 * math.pi * self.radius

    def find_square(self) -> float:
        return math.pi * self.radius ** 2


class Triangle(Figure):
    def __init__(self, point1: Point, point2: Point, point3: Point):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def find_perimeter(self):
        return self.find_length(self.point1, self.point2) + self.find_length(self.point1, self.point3) \
         + self.find_length(self.point2, self.point3)

    def find_square(self):
        len1 = self.find_length(self.point1, self.point2)
        len2 = self.find_length(self.point2, self.point3)
        len3 = self.find_length(self.point1, self.point3)
        semi_perimeter = self.find_semi_perimeter(len1, len2, len3)
        return (semi_perimeter * (semi_perimeter - len1) * (semi_perimeter - len2) * (semi_perimeter - len3)) ** 0.5


class Square(Figure):
    def __init__(self, point1: Point, point2: Point):
        self.point1 = point1
        self.point2 = point2

    def find_perimeter(self):
        return (abs(self.point2.x - self.point1.x)) * 2 + (abs(self.point2.y - self.point1.y)) * 2

    def find_square(self):
        return (abs(self.point2.x - self.point1.x)) * (abs(self.point2.y - self.point1.y))


def main():
    a = Point(3, 4)
    b = Point(2, 5)
    c = Point(6, 8)
    centre = Point(0, 0)
    t = Triangle(a, b, c)
    s = Square(a, b)
    k = Circle(centre, 4)
    print("Circle")
    print(k.find_perimeter())
    print(k.find_square())
    print("------------------")
    print("Triangle")
    print(s.find_perimeter())
    print(s.find_square())
    print("------------------")
    print("Square")
    print(t.find_perimeter())
    print(t.find_square())


if __name__ == "__main__":
    main()


