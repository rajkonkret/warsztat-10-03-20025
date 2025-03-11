# napisać funkcję, która przyjmuje argumenty age, first, last
# age powinien mmieć ustawioną wartość domyślną
# zbudowac słownik z podanych argumentó
# wykorzystac pętlę while
# zastosować "sposób ucieczki"

def build_dict(first, last, age=None):
    person = {"first": first, "last": last}
    if age:
        person['age'] = age

    return person


while True:  # pętla nieskońćzona
    print("Podaj imię i nazwisko")
    print("wpisz q by wyjść")

    f_name = input("Podaj imię")
    if f_name == "q":
        break

    l_name = input("Podaj nazwisko")
    if l_name == "q":
        break

    age = input("Podaj wiek")
    if age == "q":
        break

    print(build_dict(f_name, l_name, age))

# Podaj imię i nazwisko
# wpisz q by wyjść
# Podaj imięradek
# Podaj nazwiskokowalski
# Podaj wiek32
# {'first': 'radek', 'last': 'kowalski', 'age': '32'}
# Podaj imię i nazwisko
# wpisz q by wyjść
# Podaj imiętomek
# Podaj nazwiskozelan
# Podaj wiek67
# {'first': 'tomek', 'last': 'zelan', 'age': '67'}
# Podaj imię i nazwisko
# wpisz q by wyjść
# Podaj imięq
