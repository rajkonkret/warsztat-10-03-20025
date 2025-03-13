class Matematyka:

    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b


# metod statycznych używamy bez tworzenia obiektu klasy (instancja)
print(Matematyka.dodaj(67, 90))
