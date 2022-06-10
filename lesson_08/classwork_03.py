"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""

from classwork_04 import Animal


class Cat(Animal):

    def talk(self):
        print(f"{self.name} is meowing.")


def main():
    cat = Cat(30, 20, "Boris", 2)
    cat.talk()


if __name__ == "__main__":
    main()
