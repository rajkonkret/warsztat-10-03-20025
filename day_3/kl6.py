# dziedziczenie po wielu klasach
class A:
    def method(self):
        print("Metoda z klasy A")


a = A()
a.method()  # Metoda z klasy A


class B:
    def method(self):
        print("Metoda z klasy B")


b = B()
b.method()  # Metoda z klasy B


class C(B, A):
    """
    Klasa dziedziczy po kalsie A i B
    """


c = C()
c.method()
print(C.__mro__)  # Metoda z klasy B


# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

class D(A, B):
    """
    Klasa dziedziczy po A , B
    """


d = D()
d.method()  # Metoda z klasy A
print(D.__mro__)  # (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)


class E(A, B):
    def method(self):
        print("Metoda z klasy E")


e = E()
e.method()  # Metoda z klasy E


class F(A, B):
    def method(self):
        B.method(self)  # jawne wskazanie z której klasy metoda


f = F()
f.method()  # Metoda z klasy B


class G(A, B):
    def method(self):
        super().method()  # super() - klasa nadrzędna tutaj: A
        print("Dopisane")


g = G()  # Metoda z klasy A
g.method()  # Dopisane
