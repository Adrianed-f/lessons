"""
Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при инициализации
устанавливает марку Mercedes, модель E500, год выпуска 2000.
Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""

from homework_01 import Car


def main():
    car = Car(mark="Mercedes", model="E500", year_of_issue="2000")
    car.view_speed()
    while car.speed != 100:
        car.speed_up()


if __name__ == "__main__":
    main()