from random import randint 
print(init := [randint(0, 20) for _ in range(20)])
print(res := list(filter(lambda x: x % 5 == 0, init)))