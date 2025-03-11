# funkcja zagniezdzona, wewnętrzna
# dekorator - funkcja, ktora przyjmuje inną funkcje
# wykorzystuje zasady funkcji wewnętrznej

def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2  # zwracamy referencje, adres funkcji


fun1()  # To jest fun1
# print(fun1()) # None
new_fun = fun1()
print(new_fun)  # <function fun1.<locals>.fun2 at 0x000002D9BC4E3A60>
print(type(new_fun))  # <class 'function'>
new_fun()  # To jest fun2


# zrobic funkcję plik
# funkcja przyjmuje parametr: zapis, odczyt
# w zależności od parametru zwróci funkcję do oczytu lub zapisu pliku
def plik(arg):
    print("Sprawdzam czy plik istnieje")

    def zapis():
        print("Zapisałem do pliku")

    def odczyt():
        print('Odczytałem plik')

    if arg == "zapis":
        return zapis  # zwracamy adres funkcji, referencję
    else:
        return odczyt


zapis_plik = plik("zapis")
zapis_plik()
zapis_plik()
zapis_plik()
zapis_plik()
zapis_plik()

oczyt_plik = plik("odczyt")
oczyt_plik()
oczyt_plik()
oczyt_plik()
oczyt_plik()
oczyt_plik()

fh = open('../text.txt', "w")
fh.write("Zapiano\n")
fh.close()
