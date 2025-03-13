# class Person:
#     def __init__(self, fn,ln,id):
#         self.fn = fn
#         self.ln = ln
#         self.id = id
#
# p1 = Person("Jan", "Kowalski", 1)
# print(p1)
import pickle
from dataclasses import dataclass

from mypyc.primitives.float_ops import pow_op


@dataclass
class Person:
    first_name: str
    last_name: str
    id: int

    def greets(self):
        print("My name is", self.first_name)


print(__name__)
if __name__ == '__main__':
    p2 = Person("Jan", "Kowalski", 1)
    print(p2)
    # Person(first_name='Jan', last_name='Kowalski', id=1)
    p2.greets()

    p3 = Person("Maciej", "Nowak", 2)
    print(p3)  # Person(first_name='Maciej', last_name='Nowak', id=2)

    people = [p2, p3]
    print(people)
    # [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]

    with open('dane.pckl', "wb") as f:
        pickle.dump(people, f)
