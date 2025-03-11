# lista
from itertools import zip_longest

generator_x = [x for x in range(5)]
print(generator_x)
print(type(generator_x))  # <class 'list'>

# generator
generator_2 = (x for x in range(5))
print(generator_2)
print(type(generator_2))
# <generator object <genexpr> at 0x000001B950F96800>
# <class 'generator'>
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))


# 0
# 1
# 2

def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))
print(next(g3))


def gen4():
    i = 1
    while True:
        yield i * i
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def gen5():
    i = 1
    while True:
        command = yield i * i
        print(command)
        i += 1
        if command == "stop":
            break


g5 = gen5()
print(next(g5))
print(next(g5))
print(next(g5))
print(next(g5))
g5.send("ok")  # ok
try:
    g5.send('stop')  # StopIteration
except Exception as e:
    print("Koniec", e)
    # stop
    # Koniec


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


fib2 = fibo_with_index(10)
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))
# (3, 2) -> i, n
for i, n in fibo_with_index(10):
    print(f"Pozycja {i}, element{n}")
# Pozycja 0, element0
# Pozycja 1, element1
# Pozycja 2, element1
# Pozycja 3, element2
# Pozycja 4, element3
# Pozycja 5, element5
# Pozycja 6, element8
# Pozycja 7, element13
# Pozycja 8, element21
# Pozycja 9, element34

person = ['Radek', "Tomek", "Zenek", "Agnieszka"]
wiek = [34, 56, 78]
# Radek 34

# zip() łaczenie kolekcji
for p, w in zip(person, wiek):
    print(p, w)
# Radek 34
# Tomek 56
# Zenek 78

zipped = zip_longest(person, wiek, fillvalue="Brak danych")
print(zipped)  # <itertools.zip_longest object at 0x000001A2F1F7D7B0>
lista = list(zipped)
# dane z generatora wyczerpane,
# moge odczytac tylko z mojej listy
print(lista)  # [('Radek', 34), ('Tomek', 56), ('Zenek', 78), ('Agnieszka', 'Brak danych')]
for imie, wiek in zipped:
    print(imie, wiek)
# Radek 34
# Tomek 56
# Zenek 78
# Agnieszka Brak danych
print("--------------")
for imie, wiek in zipped:
    print(imie, wiek)
