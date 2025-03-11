# lambda - skrócony zapis funkcji
# lambda ma return
# funkcja anonimowa - mozliwosc uzycia funkcji w miejscu deklaracji
from functools import reduce, lru_cache


def liczymy(x, y):
    return x * y


print(liczymy(5, 9))  # 45

liczmy2 = lambda x, y: x * y
print(liczmy2(7, 9))  # 63

lista = [1, 2, 5, 56, 78, 90, 100, 200, 500]
# mapowanie danych
lista_wyn = []
for i in lista:
    lista_wyn.append(i ** 2)
print(lista_wyn)  # [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]

# list comprehensions
print([i ** 2 for i in lista])  # [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]


def zmien(x):
    return x ** 2


lista_wyn_2 = []
for i in lista:
    lista_wyn_2.append(zmien(i))
print(lista_wyn_2)  # [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]

# funkcje wyższego rzędu - jako argument przyjmują inną funkcję

# map()
print(f"Zastosowanie map() {list(map(zmien, lista))}")
# Zastosowanie map() [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]

# zastosowanie lambdy jako funkcja anonimowa
print(f"Zastosowanie map() {list(map(lambda x: x ** 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x / 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 2, lista))}")
print(f"Zastosowanie map() {list(map(lambda x: x * 4, lista))}")
# Zastosowanie map() [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]
# Zastosowanie map() [1, 4, 25, 3136, 6084, 8100, 10000, 40000, 250000]
# Zastosowanie map() [0.5, 1.0, 2.5, 28.0, 39.0, 45.0, 50.0, 100.0, 250.0]
# Zastosowanie map() [2, 4, 10, 112, 156, 180, 200, 400, 1000]
# Zastosowanie map() [4, 8, 20, 224, 312, 360, 400, 800, 2000]

for _ in range(10):  # niema zmienna
    # print(_)
    print("Test _")

# filtrowanie danych
for i in lista:
    if i < 10:
        print(i)

# filter()
print(f"Uzycie filter() {list(filter(lambda x: x < 10, lista))}")  # Uzycie filter() [1, 2, 5]
print(f"Uzycie filter() {list(filter(lambda x: x < 5, lista))}")  # Uzycie filter() [1, 2, 5]
print(f"Uzycie filter() {list(filter(lambda x: x > 100, lista))}")  # Uzycie filter() [1, 2, 5]
print(f"Uzycie filter() {list(filter(lambda x: x > 55, lista))}")  # Uzycie filter() [1, 2, 5]
# Uzycie filter() [1, 2, 5]
# Uzycie filter() [1, 2]
# Uzycie filter() [200, 500]
# Uzycie filter() [56, 78, 90, 100, 200, 500]
# x > 5 i x < 200
print(f"Uzycie filter() {list(filter(lambda x: x > 5 and x < 200, lista))}")  # Uzycie filter() [56, 78, 90, 100]
print(f"Uzycie filter() {list(filter(lambda x: 5 < x < 200, lista))}")  # Uzycie filter() [56, 78, 90, 100]

r0 = {'miasto': "Kielce"}
r1 = {'miasto': "Kielce", "ZIP": "25-900"}

print(r0['miasto'])
print(r1['miasto'])
# Kielce
# Kielce
print(r1['ZIP'])
# print(r0['ZIP']) # KeyError: 'ZIP'

print(r0.get('ZIP', "00-000"))
# 25-900
# 00-000

d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
# 00-000
# 25-900
print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}

lata = [(2000, 29.7), (2001, 33.12), (2010, 32.92)]
print(max(lata))
print(min(lata))
# (2010, 32.92)
# (2000, 29.7)

print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
print(max(map(lambda c: c[1], lata)))  # 33.12
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)

# reduce()
liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda a, b: a + b, liczby)  # ((((1 + 2) + 3) + 4) + 5).
# """
#     reduce(function, iterable[, initial], /) -> value
#
#     Apply a function of two arguments cumulatively to the items of an iterable, from left to right.
#
#     This effectively reduces the iterable to a single value.  If initial is present,
#     it is placed before the items of the iterable in the calculation, and serves as
#     a default when the iterable is empty.
#
#     For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
#     calculates ((((1 + 2) + 3) + 4) + 5).
#     """
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
print(wynik)  # 15

wynik = reduce(lambda a, b: a * b, liczby)
print(wynik)  # 120, ((((1 * 2) * 3) * 4) * 5)


@lru_cache(maxsize=1000)  # dekorator
def fib_cached(n):
    if n < 2:
        return n
    return fib_cached(n - 1) + fib_cached(n - 2)


print(fib_cached(10))  # 55
print(fib_cached.cache_info())  # CacheInfo(hits=8, misses=11, maxsize=1000, currsize=11)
print(fib_cached(10))
print(fib_cached.cache_info())  # CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
fib_cached.cache_clear()
print(fib_cached.cache_info())  # CacheInfo(hits=0, misses=0, maxsize=1000, currsize=0)
