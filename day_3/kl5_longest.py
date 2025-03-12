# longest() - znajduje najdłuższy klucz w słowniku

class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


# print(len(None)) # TypeError: object of type 'NoneType' has no len()
dictionary = LongestKeyDict()
print(dictionary.longest_key())  # None
dictionary["tomasz"] = 45
dictionary["abraham"] = 7
dictionary["zen"] = 89
print(dictionary.longest_key())  # abraham najdłuższy klucz
