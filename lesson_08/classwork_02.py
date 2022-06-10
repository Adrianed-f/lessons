"""
Добавить в класс Dog метод change_name.
Метод принимает на вход новое имя и меняет атрибут имени у объекта.
Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
"""

from classwork_01 import Dog


class NewDog(Dog):

    def __init__(self, height: int, weight: int, name: str, age: int = None):
        super().__init__(height, weight, name, age)
        self.age += 10

    def change_name(self, new_name: str):
        self.name = new_name



def main():
    new_dog = NewDog(30, 20, "Bonya", 2)
    print(new_dog.name)
    new_dog.change_name("Boris")
    print(new_dog.name)


if __name__ == "__main__":
    main()
