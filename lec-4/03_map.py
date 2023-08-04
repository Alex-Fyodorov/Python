from random import randint 
print(list_init := [randint(0, 20) for _ in range(10)])
print(list_init := list(map(lambda x: x + 10, list_init)))