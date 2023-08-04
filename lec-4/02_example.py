# from random import randint 
# print(list_init := [randint(0, 20) for _ in range(10)])
# list_res = []
# for i in list_init:
#     if i % 2 == 0:
#         list_res.append((i, i * i))
# print(list_res)

# /////////////////////////////////////////////////////////////////

# def select(f, col):
#     return [f(x) for x in col]

# def where(f, col):
#     return[x for x in col if f(x)]

# from random import randint 
# print(list_init := [randint(0, 20) for _ in range(10)])
# print(list_res := select(int, list_init))
# print(list_res := where(lambda x: x % 2 == 0, list_res))
# print(list_res := select(lambda x: (x, x**2), list_res))

# /////////////////////////////////////////////////////////

from random import randint 
print(list_init := [randint(0, 20) for _ in range(10)])
print(list_res := list(map(int, list_init)))
print(list_res := list(filter(lambda x: x % 2 == 0, list_res)))
print(list_res := list(map(lambda x: (x, x**2), list_res)))