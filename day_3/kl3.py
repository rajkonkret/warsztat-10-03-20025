from pprint import pprint


class ContactList(list['Contact']):
    def search(self, name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts


class Contact:
    all_contacts = ContactList()  # lista wspólna dla wszystkich obiektów klasy

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):  # naspisanie __repr__ nadpisuje __str__
        return f"{self.name} {self.email}"


class Suplier(Contact):
    """
    Klasa Suplier dziedziczy po klasie Contact
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


class Friend(Suplier):
    """
    Klasa dziedziczy po Suplier
    """

    def __init__(self, name, email, phone="000000000"):
        super().__init__(name, email)  # super() - musimy wywołać konstruktor klasy wyzszej
        self.phone = phone

    def __repr__(self):  # naspisanie __repr__ nadpisuje __str__
        return f"{self.name!r} {self.email!r}, +48{self.phone!r}"


lista = []
# lista.search() # AttributeError: 'list' object has no attribute 'search'
lista_contact = ContactList()
print(lista_contact.search("Radek"))  # []
#   ---- z kl2
c1 = Contact("Adam", "admin@wp.pl")
print(c1)  # Adam admin@wp.pl
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contacts)
print(c2.all_contacts)
# Adam admin@wp.pl
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(Contact.all_contacts)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]

sup1 = Suplier("Marek", "marek@wp.pl")
print(Contact.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@wp.pl]
sup1.order("kawa")  # kawa zamówiono od Marek

print(Contact.all_contacts.search("Radek"))  # [Radek radek@wp.pl]

# [Radek radek@wp.pl]
f1 = Friend("Kasia", "kasia@wp.pl")
f2 = Friend("Aneta", "aneta@wp.pl", "790876543")
print(Contact.all_contacts)
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@wp.pl, Kasia kasia@wp.pl, Aneta aneta@wp.pl]
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@wp.pl, Kasia kasia@wp.pl, +48000000000, Aneta aneta@wp.pl, +48790876543]
# !r doda '' przy wypisywaniu

pprint(Contact.all_contacts)
# [Adam admin@wp.pl,
#  Radek radek@wp.pl,
#  Tomek tomek@wp.pl,
#  Marek marek@wp.pl,
#  'Kasia' 'kasia@wp.pl', +48'000000000',
#  'Aneta' 'aneta@wp.pl', +48'790876543']

# kolejnośc rozwiązywania metod dla obiektu
pprint(Friend.__mro__)
# (<class '__main__.Friend'>,
#  <class '__main__.Suplier'>,
#  <class '__main__.Contact'>,
#  <class 'object'>)
