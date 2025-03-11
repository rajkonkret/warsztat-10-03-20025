# zrobic dekorator, ktory zamienia wynik działania funkcji (zwraca tekst) na duże litery
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        # *args - dowolna ilosc argumentów pozycyjnych
        # **kwargs - wszystkie argumenty przekazane po nazwie
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return "\033[1m" + result + "\033[0m"

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World!!!"


# kolejność dekoratorów moze mieć znaczenie
@bold_decorator
@uppercase_decorator
def greeting2(string):
    return f"Podałeś {string}"


print(greeting())  # HELLO WORLD!!!
print(greeting2("Radek"))  # PODAŁEŚ RADEK


# \033[1m: Set text style to bold

def wrap(*args):
    print(args)


wrap()  # ()
wrap(1, 2, 3, 4, 5, 6, 10)  # (1, 2, 3, 4, 5, 6, 10)


def wrap_kw(**kwargs):
    print(kwargs)


wrap_kw()  # {}
wrap_kw(q=10, b=78, c=99)  # {'q': 10, 'b': 78, 'c': 99}


def wrap_all(*args, **kwargs):
    print(f"{args = }, {kwargs = }")


wrap_all(1, 2, 3)
wrap_all(a=10, b=11)
wrap_all(1, 2, 3, 4, 5, a=10, b=11)
# args = (1, 2, 3), kwargs = {}
# args = (), kwargs = {'a': 10, 'b': 11}
# args = (1, 2, 3, 4, 5), kwargs = {'a': 10, 'b': 11}
