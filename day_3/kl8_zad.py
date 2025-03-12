# stworzenie ksiązki telefonicznej z wykorzystaniem pętli while
# dodaj kontakt, usun kontakt, wyszukaj kontakt, wyswietl kontakt

# --------
# Stworzyc system zarządzania biblioteką
# Book
# dodanie ksiazek, wypozyczenie ksiązki, zwrot ksiazki
# obsłużyć błedy
# dodac kalsę Library i usera
# title, author, isbn
contacts = {}
while True:
    print(f"""
1. Dodaj kontakt
2. Usuń kontakt
3. Wyszukaj kontakt
4. wyświetl kontakt
5. Koniec
""")
    try:
        odp = input("Wybierz opcję")

        if odp == "1":
            name = input("Podaj imię kontaktu")
            number = input("Podaj numer telefonu (tylko cyfry)")
            if not number.isdigit():
                # print("Numer telefonu powinien zawierać cyfry")
                raise ValueError("Numer telefonu powinien zawierac cyfry")  # rzucanie wyjątku
            else:
                contacts[name.lower()] = number
                print("Kontakt został dodany")
        elif odp == "2":
            name = input("Podaj imię kontaktu do usunięcia")
            if name.lower() in contacts:
                # del contacts[name.lower()]
                contacts.pop(name.lower())
                print(f"Kontakt {name} został usunięty")
        elif odp == "3":
            name = input("Podaj imię kontaktu do wyszukania")
            if name.lower() in contacts:
                print(f"Kontakt {name.capitalize()} nr telefonu: {contacts[name.lower()]}")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "4":
            print(f"Lista kontaktów: {contacts}")
        elif odp == "5":
            break
        else:
            print("Błędny wybór")
    except Exception as e:
        print("Bład", e)
