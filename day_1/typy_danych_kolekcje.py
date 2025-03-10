# kolekcja
# lista, krotka (tupla), zbiór (set), słownik

# lista  - dowolna ilosc danych, dowolnego typu na raz
# zachowuje kolejność przy dodawaniu elementów
lista = []
print(lista)  # []
lista = list()
print(lista)  # []
print(type(lista))  # <class 'list'>

lista.append("Radek")
lista.append("Radek")
lista.append("Radek")
lista.append("Radek")
lista.append("Radek")
print(lista)  # ['Radek', 'Radek', 'Radek', 'Radek', 'Radek']

lista2 = lista  # kopia referencji, adres w pamięci
print(lista2)
print(lista)
# ['Radek', 'Radek', 'Radek', 'Radek', 'Radek']
# ['Radek', 'Radek', 'Radek', 'Radek', 'Radek']
lista_copy = lista.copy()  # kopia wszystkich elementów listy
lista.clear()  # usunięcie wszystkich elementów z listy
print(lista2)
print(lista)
print(lista_copy)
# []
# []
# ['Radek', 'Radek', 'Radek', 'Radek', 'Radek']
print(id(lista))
print(id(lista2))
print(id(lista_copy))
# 2816861257664
# 2816861257664
# 2816858611968

# krotka, tupla - niemutowalna kolekcja, tylko do odczytu
# krotka pozwala lepiej zarzadzać pamięcią
krotka = tuple(lista_copy)  # tuple() - rzutowanie na krotkę
print(krotka)  # ('Radek', 'Radek', 'Radek', 'Radek', 'Radek')
print(type(krotka))  # <class 'tuple'>

krotka_liczby = 6, 7, 8, 9, 200
print(krotka_liczby)  # (6, 7, 8, 9, 200)
print(type(krotka_liczby))  # <class 'tuple'>

krotka_jeden = ("Radek")
print(type(krotka_jeden))  # <class 'str'>
krotka_jeden = "Radek",
print(type(krotka_jeden))  # <class 'tuple'>
# PEP8 zaleca przy jednoelementowej krotce używać nawiasów
krotka_jeden = ("Radek",)
print(type(krotka_jeden))
print(krotka_liczby.count(9))  # występuje 1 raz
print(krotka_liczby.index(9))  # index numer 3 (pozycja 4)
# krotka_liczby[0] = 7  # TypeError: 'tuple' object does not support item assignment
# garbage collector - automatyczne usunięcie zbednych danych z pamięci
del krotka_jeden  # usuniecie calej krotki
# print(krotka_jeden)  # NameError: name 'krotka_jeden' is not defined

# rozpakowanie krotki
a, b = 1, 2
print(f"{a=}, {b=}")
tupla = 1, 2
a, b = tupla
print(f"{a=}, {b=}")
tupla = 1, 2, 3
# a, b = tupla # ValueError: too many values to unpack (expected 2)
a, *b = tupla  # * pozostałe
print(f"{a=}, {b=}")  # a=1, b=[2, 3]

# zbiór (set) - przechowuje unikalne wartości
# nie posiada indeksu, nie zachowuje kolejności przy dodawaniu elementów
lista = [44, 55, 66, 77, 33, 31, 33, 55, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 11, 44, 77, 55, 31}
pusty_zbior = set()
print(pusty_zbior)  # set()
pusty_zbior.add(18)
pusty_zbior.add(18)
pusty_zbior.add(18)
pusty_zbior.add(33)
pusty_zbior.add(55)
pusty_zbior.add(76)
print(pusty_zbior)  # {33, 18, 76, 55}

# suma zbiorów, zwraca nowy zbiór
print(zbior | pusty_zbior)  # {33, 66, 11, 44, 77, 76, 18, 55, 31}
print(zbior.union(pusty_zbior))  # {33, 66, 11, 44, 77, 76, 18, 55, 31}

# frozenset() - niemutowalny zbiór, może być zagnieżdzony
imm_set = frozenset([1, 2, 3, 4])
print(imm_set)  # frozenset({1, 2, 3, 4})
nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(nested_set)  # {frozenset({3, 4}), frozenset({1, 2})}

# słownik
# para klucz-wartosc
# {"name": "Radek", 'age':89}
# klucze nie mogą się powtórzyc

slownik = {}
print(slownik)  # {}
print(type(slownik))  # <class 'dict'>

slownik = dict()
print(slownik)  # {}
print(type(slownik))  # <class 'dict'>

slownik['name'] = "Radek"
slownik['age'] = 90
print(slownik)  # {'name': 'Radek', 'age': 90}

print(slownik.keys())  # dict_keys(['name', 'age'])
print(slownik.values())  # dict_values(['Radek', 90])
print(slownik.items())  # dict_items([('name', 'Radek'), ('age', 90)])

print(slownik['name'])  # Radek
# print(slownik['namE'])  # KeyError: 'namE'

print(slownik.get("NAme"))  # None
print(slownik.get("NAme", 'default'))  # default

lista_duplikaty = [33, 66, 11, 44, 77, 45, 18, 54, 31, 55]
print(dict.fromkeys(lista_duplikaty))
# {33: None, 66: None, 11: None, 44: None, 77: None, 45: None, 18: None, 54: None, 31: None, 55: None}
print(list(dict.fromkeys(lista_duplikaty)))
# [33, 66, 11, 44, 77, 45, 18, 54, 31, 55] usunięte duplikaty, zachowana kolejnośc
