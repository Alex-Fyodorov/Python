# Необходимо сравнить скорость работы 2 алгоритмов вычисления чисел
# Фибоначчи и определить, какой из них работает быстрее. Так различия
# начнутся уже с 40 члена последовательности.

import time

def alg1(n):
    start = time.time()
    a1 = 0
    a2 = 1    
    i = 3
    if n == 1:
        return 0
    if n == 2:
        return 1
    while i <= n + 1:
        a2, a1 = a2 + a1, a2
        i += 1
    
    print(time.time() - start)
    return a2


def fib(n):    
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)


print(alg1(40))

start = time.time()
print(fib(39))
print(time.time() - start)   