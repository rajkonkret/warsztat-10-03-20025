# print(2 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat-10-03-20025\day_4\kl_16.py", line 1, in <module>
#     print(2 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero

# raise ZeroDivisionError("Bład dzielenia")


# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\warsztat-10-03-20025\day_4\kl_16.py", line 8, in <module>
#     raise ZeroDivisionError("Bład dzielenia")
# ZeroDivisionError: Bład dzielenia

class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę calkowitą większą od zera"))
    if x <= 0:
        raise MyException("Liczba musi być większa od zera")
except MyException:
    print("Wartość musi być większa od zera")
except Exception as e:
    print("Błąd", e)
else:  # tylko gdy nie ma błedu
    print("Podana waartość", x)
finally:  # wykonuje się zawsze
    print("Koniec")
