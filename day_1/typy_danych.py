import sys

print("Nazywam się Radek")
# ctrl d - powielenie lini
print('Nazywam się Radek')
# ctrl / - komentarz linijki z kursorem
# print('Nazywam się Radek")
#   File "C:\Users\CSComarch\PycharmProjects\warsztat-10-03-20025\day_1\typy_danych.py", line 4
#     print('Nazywam się Radek")
#           ^
# SyntaxError: unterminated string literal (detected at line 4)
print("Dalej")
print(type("Radek"))  # <class 'str'> dane tekstowe

print(39)
print(type(39))  # <class 'int'>, liczba całkowita
print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300, str_digits_check_threshold=640)

print("93")  # 93
print(type("93"))  # <class 'str'>
print("93" + "93")  # 9393
print(93 + 93)  # 186
print(5 * "93")  # 9393939393

# silne typowanie - nie zamienia typów samodzielnie
# print("93" + 45) # TypeError: can only concatenate str (not "int") to str

# rzutowanie
print("93" + str(45))  # str() - rzutowanie na string, 9345
print(int("93") + 45)  # 138

print(34 * "168")

# zmienna - pudełko na dane, posuida nazwę
# PEP8 snake_case
# powinna podpowiadac co zawiera

# typowanie dynamiczne - zmienna przyjmuje typ na podstawie danych w niej zawartych
name = "Radek"
print(name)  # str

name = 90
print(type(name))  # int

# hinty - podpowiedzi
name: str = "Tomek"
print(name)
name = 89
print(name)
# mypy narzedzie do sprawdzannia typów
#  pip install mypy
# (.venv) PS C:\Users\CSComarch\PycharmProjects\warsztat-10-03-20025> mypy .\day_1\typy_danych.py
# day_1\typy_danych.py:43: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# day_1\typy_danych.py:47: error: Name "name" already defined on line 40  [no-redef]
# day_1\typy_danych.py:49: error: Incompatible types in assignment (expression has type "int", variable has type "str")  [assignment]
# Found 3 errors in 1 file (checked 1 source file)
# (.venv) PS C:\Users\CSComarch\PycharmProjects\warsztat-10-03-20025>

temp = 36.6
print(type(temp))  # <class 'float'>, zmmiennoprzecinkowe
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

print(0.1 + 0.5)  # 0.6
print(0.1 + 0.7)  # 0.7999999999999999
# the sum 12.345 + 1.0001 = 13.3451 might be rounded to 13.345.

wiek = 50
rok = 2025
# decimal
print(wiek + rok)  # 2075
print(wiek - rok)  # -1975
print(wiek * rok)  # 101250
print(wiek / rok)  # 0.024691358024691357 -> float

print(rok // wiek)  # częśc całkowita z dielenia 2025 // 50 = 40 i reszty 25
print(rok % wiek)  # reszta z dzielenia 25
print(10 % 3)  # 3 całe r 1, 1
print(4 % 2)  # r=2, parzysta

print(wiek ** rok)  # potęgowanie
# len() - długość kolekcji
print(len(str(wiek ** rok)))  # 3441
# print(len(str(wiek ** rok ** 2)))
# ValueError: Exceeds the limit (4300 digits) for integer string conversion;
# use sys.set_int_max_str_digits() to increase the limit

print(54 - 5 * 43 / 2 + 4 / 2)  # -51.5
print(54 - 5 * 43 / (2 + 4) / 2)  # 36.08333333333333

# name ="Radek"
# Witaj Radek!
name = "Radek"
# f-string
print(f"Witaj {name}!")  # Witaj Radek!
print("Witaj", name)  # Witaj Radek
# sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
print("Witaj", name, sep="%%%%")  # Witaj%%%%Radek

print("Witaj %s!" % name)  # Witaj Radek!# %s str

wersja = 3.900001
print("Używamy %f" % wersja)  # Używamy 3.900001 %f - float
print("Używamy %s" % wersja)  # Używamy 3.900001 # Używamy 3.900001
# print("Używamy %f" % "Radek")  # TypeError: must be real number, not str - sprawdza typy danych

print("Uzywamy wersji {}".format(wersja))  # Uzywamy wersji 3.900001

print("""Tekst
wielolinijkowy""")
# Tekst
# wielolinijkowy
"""
Komentarz
wielolinijkowy
"""

# zaokrągla dla wyswietlenia
print(f"Uzywamy wersji pythona {wersja}")  # Uzywamy wersji pythona 3.900001
print(f"Uzywamy wersji pythona {wersja:.2f}")  # Uzywamy wersji pythona 3.90
print(f"Uzywamy wersji pythona {wersja:.1f}")  # Uzywamy wersji pythona 3.9
print(f"Uzywamy wersji pythona {wersja:.0f}")  # Uzywamy wersji pythona Uzywamy wersji pythona 4

print(wersja)  # 3.900001
a = round(wersja)
b = round(wersja, 2)
print(a, b)

name = "Radek"
print(f"{name:<10}")  # "Radek     "
print(f"{name:>20}")  # "               Radek"
print(f"{name:^25}")  # "          Radek          "

# teksty są niemutowalne
imie = "Radek Radek"
# nie zmienia oryginalnej zmiennej
print(imie)  # Radek Radek
print(imie.upper())  # RADEK RADEK
name_upper = imie.upper()
print(name_upper)  # RADEK RADEK

liczba = 9087896543123
print(type(liczba))
print(f"Nasza duża liczba {liczba}")
print(f"Nasza duża liczba {liczba:,}")
print(f"Nasza duża liczba {liczba:_}")
# Nasza duża liczba 9087896543123
# Nasza duża liczba 9,087,896,543,123
# Nasza duża liczba 9_087_896_543_123

liczba = 9_087_896_543_123
print(type(liczba))  # <class 'int'>
# Nasza duża liczba 9,087,896,543,123
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 9.087.896.543.123

# boolean, typ logiczny
# 1, 0
# prawda, falsz
# True, False

print(int(True))  # 1
print(int(False))  # 0

#  bool() - rzutowaniena boolean - typ logiczny
print(bool(0))  # False
print(bool(1))  # True

print(bool(100))  # True
print(bool(-100))  # True
print(bool("radek"))  # True

print(bool(""))  # False
print(bool(None))  # False, nie wiem, wartość nieokreslony, odpowiednik null

tekst = "    Tekst    "
# usunąć spacje z przodu i z tyłu
print(tekst.strip())  # "Tekst"
print(tekst.lstrip())  # "Tekst    "
print(tekst.rstrip())  # "    Tekst"

a = 10
print(f"Zmienna a = {a}")
print(f"Zmienna {a = }")
# Zmienna a = 10
# Zmienna a = 10

name_1 = "Radek"
name_2 = "Radek"
print(name_1 == name_2)  # True

name_1 = "radek"
name_2 = "Radek"
print(name_1 == name_2)  # False
print(name_1.lower() == name_2.lower())  # True

name_1 = "groẞ"
name_2 = "GROSS"
print(name_1.lower() == name_2.lower())  # False

# """ Return a version of the string suitable for caseless comparisons. """
print(name_1.casefold() == name_2.casefold())  # True

text = "Witaj Świecie"
encode_s = text.encode("utf-8")
print(encode_s)  # b'Witaj \xc5\x9awiecie' postac bajtów
print(type(encode_s))  # class 'bytes'>
# \xc5\x9a wartość bajtów w systemie szesnatków c5 = 197 dziesietnie

print(encode_s.decode("utf-8"))  # Witaj Świecie
