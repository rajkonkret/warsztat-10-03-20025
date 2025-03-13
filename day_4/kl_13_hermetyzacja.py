# hermetyzacja
class Boat:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        # pole prywatne widoczne tylko wewnątrz klasy
        self.__speed = 0

    def sail(self):
        self.__speed += 10
        self.__test()

    def speedometer(self):
        print(f"Speed is {self.__speed} knots")

    def __test(self):
        print("All tested")


boat = Boat("Maxus", 2024)
boat.sail()
boat.sail()
boat.sail()
boat.sail()
boat.sail()
# pole prywatne
# AttributeError: 'Boat' object has no attribute '__speed'
# print(boat.__speed)  # 50
boat.speedometer()  # Speed is 50 knots, metoda do odczytu pola prywatnego

# hermetyzacja - pola prywatne
# enkapsulacja - wystawianie metod do odczytu, zapisu pol prywatnych
boat.__speed = 0  # stworzyl pole publiczne o tej samej nazwie
boat.speedometer()  # Speed is 50 knots
# All tested
# All tested
# All tested
# All tested
# All tested
# Speed is 50 knots
# Speed is 50 knots
