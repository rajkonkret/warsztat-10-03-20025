class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)


def my_function(x: int, y: int) -> float:
    if not isinstance(x, int):
        raise MyTypeError("X must be integer")
    if not isinstance(y, int):
        raise MyTypeError("Y must be integer")
    if y == 0:
        raise MyValueError("y cannot be zero")

    return x / y


while True:
    try:
        a = input("Podaj pierwszą liczbę")
        b = input("Podaj drugą liczbę")
        if a == "q" or b == "q":
            break
        result = my_function(a, b)
    except MyTypeError:
        print("MyTypeError")
    except MyValueError:
        print("Dzielenie przez zero!!!")
    except Exception as e:
        print("Bład", e)
    else:
        print(f"Wynik wynosi {result}")
    finally:
        print("Koniec")
# Podaj pierwszą liczbę5
# Podaj drugą liczbę3
# MyTypeError
# Koniec
# Podaj pierwszą liczbęKoniec