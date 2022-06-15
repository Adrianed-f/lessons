"""
Создать генератор простой геометрической прогрессии.
Пользователь вводит два числа N и M, рассчитать последовательность  N + NN + NNN + ... + N^M.

"""


class GeoIterator:
    def __init__(self, power, limit):
        self.power = power
        self.limit = limit
        self.current_value = 1

    def __next__(self):
        previous_value = self.current_value
        self.current_value *= self.power
        if self.current_value <= self.limit:
            return self.current_value
        else:
            raise StopIteration

    def __iter__(self):
        self.current_value = 1
        return self


if __name__ == "__main__":
    my_geo = GeoIterator(2, 16)
    for item in my_geo:
        print(item)
    #   while True:
    #   try:
    #       print(next(my_geo))
    #  except StopIteration:
    #     break
