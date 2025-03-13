# lazy - leniwy
# dane tylko gdy potrzebne

lista = [1, 2, 3, 4, 5]
iterator = iter(lista)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# 1
# 2
# 3
print("Coś innego")
print(next(iterator))


class Count:
    def __init__(self, lows, high):
        """
        metoda inicjalizacyjna
        :param lows: start
        :param high: stop
        """
        self.current = lows
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


print("--------")
counter = Count(1, 5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
try:
    print(next(counter))
except StopIteration as e:
    print("Koniec", e)
