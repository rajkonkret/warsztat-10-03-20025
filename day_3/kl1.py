# klasy - element programowania obiektowego
# szablon, przepis, stempel, matryca
# obiekt (instancja) - zbudowany wg przepisu element
# hermetyzacja, polimorfizm, dziedziczenie, abstrakcja
# klasa nakreśla cechy (zmienne) i funkcję jakie posiada obiekt (metody)

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
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x, self.y}"


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