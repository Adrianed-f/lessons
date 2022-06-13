"""
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""

from homework_01 import Point, Circle, Triangle, Square


def main():
    point1 = Point(3, 4)
    point2 = Point(2, 5)
    point3 = Point(6, 8)
    centre = Point(0, 0)
    t = Triangle(point1, point2, point3)
    s = Square(point1, point2)
    k = Circle(centre, 4)
    figures = [t, s, k]
    for item in figures:
        print(item.find_square())


if __name__ == "__main__":
    main()