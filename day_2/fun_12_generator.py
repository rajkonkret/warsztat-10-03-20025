# generator - generuje wartość w momencie kiedy jej potrzebuje

def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


# generator
def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # zwraca wartośc obliczoną, zapamiętuje na której skończył


kwa = kwadrat2(5)  # inicjalizacja generatora
print(next(kwa))  # 0
print(next(kwa))  # 1
print(next(kwa))  # 4
print("Zrób cokolwiek")
print(next(kwa))
# Zrób cokolwiek
# 9
print(next(kwa))
# print(next(kwa))  # StopIteration - koniec działania generatora

kwa2 = kwadrat2(10)
kwa3 = kwadrat2(20)

print(next(kwa2))
print(next(kwa3))
print(next(kwa2))
print(next(kwa3))

print(list(kwa3))
# [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
# print(next(kwa3))  # StopIteration
