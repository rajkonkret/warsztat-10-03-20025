import pickle

# serializacja i deserializacja

lista = [1, 2, 3, 4, 5]
print(type(lista))
# context manager - ułatwia prace z pliakmi
# ========= ===============================================================
#     Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('lista.txt', 'w') as fh:  # truncating - kasuje plik jeśli istnieje
    fh.write(str(lista))

with open("lista.txt", "r") as f:
    lines = f.read()

print(lines)  # [1, 2, 3, 4, 5]
print(lines[0])  # [
print(type(lines))  # <class 'str'>

# serializacja - zamiana na postać bajtową
with open('lista.pckl', "wb") as f:
    pickle.dump(lista, f)

# deserializacja - zamiana z postaci bajtowej na postac własciwą
with open('lista.pckl', "rb") as fh:
    p = pickle.load(fh)

print(p)
print(type(p))
# [1, 2, 3, 4, 5]
# <class 'list'>

lista_ser = pickle.dumps(lista)
print(lista_ser)
# b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
print(type(lista_ser))  # <class 'bytes'>

print(pickle.loads(lista_ser))  # [1, 2, 3, 4, 5]

for i in pickle.loads(lista_ser):
    print(i, sep=" : ", end=" : ")
# 1 : 2 : 3 : 4 : 5 :
