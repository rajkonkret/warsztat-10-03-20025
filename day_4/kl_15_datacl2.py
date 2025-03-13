import pickle
from dataclasses import dataclass
from kl_14_dataclass import Person

# @dataclass
# class Person:
#     first_name: str
#     last_name: str
#     id: int
#
#     def greets(self):
#         print("My name is", self.first_name)


with open('dane.pckl', "rb") as file:
    p = pickle.load(file)

print("------")
print(p)
# [Person(first_name='Jan', last_name='Kowalski', id=1), Person(first_name='Maciej', last_name='Nowak', id=2)]
for person in p:
    person.greets()
# My name is Jan
# My name is Maciej
