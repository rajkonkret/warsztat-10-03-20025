class Contact:
    all_contacts = []  # lista wspólna dla wszystkich obiektów klasy

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
