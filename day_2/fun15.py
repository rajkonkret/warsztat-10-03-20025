def count_down(min):
    count = min
    while count > 0:
        yield count
        count -= 1


def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1


c_u = count_up_to(3)
c_d = count_down(3)


def combined(gen1, gen2):
    yield from gen1  # najpierw wszystko z tego
    yield from gen2  # potem wszystko z tego


c = combined(c_u, c_d)
# c_u
print(next(c))  # 1
print(next(c))  # 2
print(next(c))  # 3
# c_d
print(next(c))  # 3
print(next(c))  # 2
print(next(c))  # 1

c_u = count_up_to(3)
c_d = count_down(3)
for i in c_u:
    print(i)
# 1
# 2
# 3
for i in c_d:
    print(i)
# 3
# 2
# 1
