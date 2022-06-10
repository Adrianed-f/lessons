"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
отображение скорости, задний ход (изменение знака скорости)
"""


class Car:
    mark: str = None
    model: str = None
    year_of_issue: int = None
    speed: int = 0

    def __init__(self, *args, **kwargs):
        self.mark = kwargs.get("mark")
        self.model = kwargs.get("model")
        self.year_of_issue = kwargs.get("year_of_issue")
        if kwargs.get("speed") is not None:
            self.speed = kwargs.get("speed")

    def speed_up(self):
        self.speed += 5
        self.view_speed()

    def speed_down(self):
        self.speed -= 5
        self.view_speed()

    def stop(self):
        self.speed = 0
        self.view_speed()

    def view_speed(self):
        print(f"car speed - {self.speed}k/h")

    def reverse(self):
        self.speed = 0 - self.speed
        self.view_speed()
