# funkcje - fragment kodu, który możemy wykonać w dowolnym momencie
# funkcja musi zostać najpierw zadeklarowana
# wywołanie funkcji uruchamia kod

a = 10
b = 90


# nie zwracają wyniku
# dekalracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):  # obowiązkowe do przekazania
    print(a + b)


def odejmij(a, b, c=0):  # argumenty z wartością domyslną
    print(a - b - c)


# funkcja zwraca wynik
def mnozenie(a, b):
    return a * b  # zwróc wynik


def mnozenie2(a: int, b: int) -> (int, int, int):
    return a, b, a * b


# wywołanie funkcji
print(dodaj)  # <function dodaj at 0x000002D6C5613A60>
print(type(dodaj))  # <class 'function'>
dodaj()  # 100
# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

# parametry rzekazane po pozycji
dodaj2(10, 78)  # 88
dodaj2(23, 44)  # 67
odejmij(1, 2)  # -1
odejmij(1, 2, 8)  # -9
# print(dodaj() + dodaj())  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(mnozenie(6, 7))  # 42
print(mnozenie2(6, 9))  # (6, 9, 54)
# wynik działania _ * _ = _
c = mnozenie2(8, 9)
print(f"{c[0]} * {c[1]} = {c[2]}")
a, b, wynik = mnozenie2(8, 9)  # rozpakowanie krotki
print(f"{a} * {b} = {wynik}")
# 8 * 9 = 72
# 8 * 9 = 72

# parametry przekazane po nazwi
odejmij(b=9, c=89, a=87)  # -11
print(mnozenie2(b=98, a=87))  # (87, 98, 8526)

# parametry mieszane
odejmij(1, b=8, c=87)  # -94
# po argumencie nazwanym nie wolno podowac argumentó pozycyjnych. muszą juz byc po nazwie
# odejmij(a=9, 2, 3)  # SyntaxError: positional argument follows keyword argument

print(mnozenie(5, 6) + mnozenie(5, 6))  # 60
