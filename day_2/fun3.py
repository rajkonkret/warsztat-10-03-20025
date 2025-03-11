# lambda - skrócony zapis funkcji
# lambda ma return
# funkcja anonimowa - mozliwosc uzycia funkcji w miejscu deklaracji

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