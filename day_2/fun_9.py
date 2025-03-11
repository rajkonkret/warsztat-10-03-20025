import time
import tracemalloc
from unittest.mock import magic_methods

import numpy as np

# pip install numpy

print(np.iinfo(np.int32))
print(np.iinfo(np.int64))
# Machine parameters for int32
# ---------------------------------------------------------------
# min = -2147483648
# max = 2147483647
# ---------------------------------------------------------------
#
# Machine parameters for int64
# ---------------------------------------------------------------
# min = -9223372036854775808
# max = 9223372036854775807
# ---------------------------------------------------------------
# tracemalloc.start()
array1 = np.arange(10_000_000, dtype=np.int64)
array2 = np.arange(10_000_000, dtype=np.int64)
# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB;")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB;")
# print(array1.dtype)
# Current memory usage: 76.29412841796875 MB;
# Peak memory usage: 76.29412841796875 MB;
# int32
# Current memory usage: 152.58807373046875 MB;
# Peak memory usage: 152.58807373046875 MB;
# int64
# Current memory usage: 762.9238739013672 MB;
# Peak memory usage: 762.9239807128906 MB;

# tracemalloc.start()
lista1 = list(range(10_000_000))
lista2 = list(range(10_000_000))


# current, peak = tracemalloc.get_traced_memory()
# tracemalloc.stop()
# print(f"Current memory usage: {current / 1024 ** 2} MB;")
# print(f"Peak memory usage: {peak / 1024 ** 2} MB;")
# Current memory usage: 762.9238739013672 MB;
# Peak memory usage: 762.9239807128906 MB;

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")

        return result

    return wrapper


@measure_time
def add_without_np():
    result = [lista1[i] + lista2[i] for i in range(len(lista1))]
    return "ok"


@measure_time
def add_np():
    result = array1 + array2
    return "ok np"


@measure_time
def add_zip():
    res = [a + b for a, b in zip(lista1, lista2)]
    return "ok zip"


print("Start")
print(add_without_np())
# Start
# Czas wykonania funkcji add_without_np: 0.8918530941009521
# ok
print(add_np())
# Start
# Czas wykonania funkcji add_without_np: 0.9448955059051514
# ok
# Czas wykonania funkcji add_np: 0.02257561683654785
# ok np
print(add_zip())
# Start
# Czas wykonania funkcji add_without_np: 0.9705913066864014
# ok
# Czas wykonania funkcji add_np: 0.022069931030273438
# ok np
# Czas wykonania funkcji add_zip: 0.8639748096466064
# ok zip
