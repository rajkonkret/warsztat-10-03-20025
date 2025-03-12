# --------
# Stworzyc system zarządzania biblioteką
# Book
# dodanie ksiazek, wypozyczenie ksiązki, zwrot ksiazki
# obsłużyć błedy
# dodac kalsę Library i usera
# title, author, isbn

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Author: {self.author!r}, Tytuł: {self.title!r}, ISBN: {self.isbn!r}"


book = Book("Pan Tadeusz", "Adam Mickiewicz", "1234567890")
print(book)  # Author: 'Adam Mickiewicz', Tytuł: 'Pan Tadeusz', ISBN: '1234567890'


class Library:
    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dodaj_ksiazke(self, book: "Book"):
        self.dostepne_ksiazki.append(book)

    def fun_ksiazki_do_wypozyczenia(self):
        return self.dostepne_ksiazki

    def fun_wypozycz_ksiazki(self, isbn):
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.remove(book)
                self.wypozyczone_ksiazki.append(book)
                return book
        raise Exception("Nie ma takiej ksiązki")

    def fun_wypozyczone_ksiazki(self):
        return self.wypozyczone_ksiazki

    def fun_zwroc_ksiazke(self, isbn):
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.wypozyczone_ksiazki.remove(book)
                self.dostepne_ksiazki.append(book)
                return True
        raise Exception("Ksiązka nie z naszej biblioteki")


biblioteka = Library()
while True:
    print(f"""
1. Dodaj ksiązkę
2. Wypożycz ksiązkę
3. Pokaż dostępne
4. Pokaż wypożyczone
5. Zwróć ksiązkę
6. Koniec
""")
    try:
        odp = input("Wybierz opcje")

        if odp == "1":
            author = input("Podaj autora")
            title = input("Podaj tytuł")
            isbn = input("Podaj numer ISBN")
            biblioteka.fun_dodaj_ksiazke(Book(title, author, isbn))
        elif odp == "2":
            isbn = input("Podaj ISBN ksiązki, którą chcesz wypożyczyć")
            book = biblioteka.fun_wypozycz_ksiazki(isbn)
            print(f"Ksiązka została wypożyczona")
        elif odp == "3":
            print(f"Dostępne ksiązki {biblioteka.fun_ksiazki_do_wypozyczenia()}")
        elif odp == "4":
            print(f"Wypożyczone ksiązki {biblioteka.fun_wypozyczone_ksiazki()}")
        elif odp == "5":
            isbn = input("Podaj ISBN ksiązki, którą chcesz zwrócic")
            book = biblioteka.fun_zwroc_ksiazke(isbn)
            if book:
                print("Ksiązka została zwrócona")
        elif odp == "6":
            break
        else:
            print("Błędny wybór")
    except Exception as e:
        print("Bład", e)
