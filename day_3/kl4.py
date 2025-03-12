# __missing__ gdy nie znajdzie klucza w słowniku

class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


# słownik w którym jak nie ma klucza tworzy taki klucz z wartością domyślną np.: 0
class AutoKeyDict(dict):
    def __missing__(self, key):
        self[key] = 0
        return key


class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        return self.get(key.lower())


d_python = {}
print(type(d_python))
# print(d_python["name"]) # KeyError: 'name'

d1 = DefaultDict()
print(d1["name"])  # default

a1 = AutoKeyDict()
print(a1)  # {}
print(a1['name'])
print(a1)  # {'name': 0}

c1 = CaseInsensitiveDict()
c1["name"] = "Radek"
print(c1["NAme"])  # Radek
