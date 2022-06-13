"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
Переопределить магические методы сложения, вычитания, умножения на число.
Создать метод, который выводит на экран отформатированное время (HH:MM:SS).
Создать объект класса MyTime, умножить его на 2 и вывести на печать результат.
Создать второй объект класса MyTime, найти разницу с первым,
добавить к нему 7 часов и 45 минут, вывести на печать результат.
"""
from __future__ import annotations


class MyTime:

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self) -> int:
        return self.seconds + self.minutes * 60 + self.hours * 60 * 60

    def __eq__(self, other: MyTime):
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other: MyTime):
        return self.to_seconds() != other.to_seconds()

    def __ge__(self, other: MyTime):
        return self.to_seconds() >= other.to_seconds()

    def __le__(self, other: MyTime):
        return self.to_seconds() <= other.to_seconds()

    def __lt__(self, other: MyTime):
        return self.to_seconds() < other.to_seconds()

    def __gt__(self, other: MyTime):
        return self.to_seconds() > other.to_seconds()

    @staticmethod
    def seconds_to_time(seconds) -> MyTime:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return MyTime(hours=hours, minutes=minutes, seconds=seconds)

    def __str__(self) -> str:
        return f"{self.hours}H:{self.minutes}M:{self.seconds}S"

    def __add__(self, other: MyTime) -> MyTime:
        seconds = self.to_seconds() + other.to_seconds()
        return MyTime.seconds_to_time(seconds)

    def __sub__(self, other) -> MyTime:
        seconds = self.to_seconds() - other.to_seconds()
        return MyTime.seconds_to_time(seconds)

    def __mul__(self, other) -> MyTime:
        seconds = self.to_seconds() * other
        return MyTime.seconds_to_time(seconds)


def main():
    a = MyTime(hours=3, minutes=20, seconds=45)
    b = MyTime(hours=3, minutes=21, seconds=45)
    c = MyTime(hours=7, minutes=45, seconds=0)
    print(a * 2)
    print((b - a) + c)


if __name__ == "__main__":
    main()
