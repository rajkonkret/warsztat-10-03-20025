from abc import ABC, abstractmethod


# klasa abstarkcyjna
# posiada metode abstrakcyjna
# nie mozna stworzyc obiektu tej klasy
class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod
    def drukuj(self):
        pass

    @staticmethod
    def from_string():
        print("Metoda statyczna")

    @classmethod
    def from_counter(cls, counter):  # zamiennik konstruktorówm, przeciązania
        return cls(counter.values)


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values):
        if values > self.MAX:
            raise ValueError(f"Wartość nie może przekroczyc max {self.MAX}")
        super().__init__(values)

    def drukuj(self):
        print("Drukuje", self.values)


class NewCounter(Counter):
    """
    Klasa NewCounter
    """


class SecondCounter(Counter):

    def drukuj(self):
        print("Drukuj second:", self.values)


# po oznaczeniu klasy jako abstrakcyjna
# TypeError: Can't instantiate abstract class Counter without an implementation for abstract method 'drukuj'
# c1 = Counter()
# c1.increment()
# c1.drukuj()

bc = BoundedCounter(1)
bc.increment()
bc.drukuj()  # Drukuje 2

# nc = NewCounter() # TypeError: Can't instantiate abstract class NewCounter without an implementation for abstract method 'drukuj'
sc = SecondCounter()
sc.drukuj()

# metoda statyczna nie ma konieczności tworzenia obiektu
Counter.from_string()  # Metoda statyczna

bc2 = BoundedCounter(bc.values)
# polimorfizm - klasy róznych typów posiadają wspólne elementy
# możn aje traktować jak jedna klasa w zakresie wspólnych elementów
lista = [bc, sc, bc2]
for i in lista:
    i.drukuj()
    # Drukuje 2
    # Drukuj second: 0
    # Drukuje 2

# classmethod - zamiennik konstruktora
bc3 = BoundedCounter.from_counter(bc2)
bc3.increment()
bc3.drukuj()  # Drukuje 3
