"""
Создать общий класс Animal, содержащий все общие методы классов Dog и Cat. Унаследовать Dog и Cat от класса Animal и
Удалить в дочерних классах те методы, которые имеются у родительского класса.
Создать объект каждого класса и вызвать все его методы.
"""


class Animal:
    height: int = None
    weight: int = None
    name: str = None
    age: int = 10

    def __init__(self, height: int, weight: int, name: str, age: int = None):
        self.height = height
        self.weight = weight
        self.name = name
        if age is not None:
            self.age = age

    def jump(self):
        print(f"{self.name} is jumping")

    def run(self):
        print(f"{self.name} is running")

    def talk(self):
        raise NotImplementedError


def main():
    dog = Animal(30, 20, "Bonya", 2)
    print(dog.age, dog.name, dog.weight, dog.height)
    dog.jump()
    dog.run()


if __name__ == "__main__":
    main()
