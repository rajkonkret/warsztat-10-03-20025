# klasy - element programowania obiektowego
# szablon, przepis, stempel, matryca
# obiekt (instancja) - zbudowany wg przepisu element
# hermetyzacja, polimorfizm, dziedziczenie, abstrakcja
# klasa nakreśla cechy (zmienne) i funkcję jakie posiada obiekt (metody)
import math


class MyFirstClass:
    """
    Klasa w Pythonie
    """

    def __init__(self, x=0, y=0):
        """
        Funkcja inicjalizująco (konstruktor)
        :param x:
        :param y:
        """
        # self
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calulate(self, other: "MyFirstClass") -> float:
        """
        Obliczenie odległosci między dwoma punktami
        using the Pythagorean theorem:  sqrt(x*x + y*y)
        :param other:
        :return: float
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"{self.x, self.y}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.x, self.y}"


point1 = MyFirstClass(5, 9)
point2 = MyFirstClass()

# print(MyFirstClass.__doc__)  # Klasa w Pythonie
# help(MyFirstClass)
# pydoc -b
print(point1)
print(point1.x)
print(point1.y)
# 5
# 9
# po nadpisaniu metody __str__ (5, 9)
point1.reset()
print(point1)  # (0, 0)
point1.move(67, 98)
print(point1)  # (67, 98)

print(point1.calulate(point2))  # 118.71394189394942
# print(point1.calulate(200))  # Pychamr sugeruje, ze pomyliliśmy typy
print(point2.calulate(point1))  # 118.71394189394942
print(point2.calulate(point2))  # 0.0

lista = [point1, point2]
print(lista)
# [<__main__.MyFirstClass object at 0x0000025D3A4A7CB0>, <__main__.MyFirstClass object at 0x0000025D3A737250>]
# po nadpisaniu __repr__
# [Point((67, 98), Point((0, 0)]

for p in lista:
    print(p)
    # (67, 98)
    # (0, 0)

# print(globals())
