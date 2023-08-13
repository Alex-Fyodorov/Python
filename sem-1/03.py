# Найти все простые числа от 1 до N, где N вводится пользователем.
# Реализовать три различных алгоритма, включая решето Эратосфена.
# Оценить эффективность каждого подхода.

import time

def eratosphen(n):
    start = time.time()
    lst = [x for x in range(2, n + 1)]
    index = 0
    while 2 * lst[index] <= n:
        p = lst[index]
        mult = 2
        while mult * p <= n:
            if mult * p in lst:
                lst.remove(mult * p)
            mult += 1
        index += 1
    print(lst)
    print(f'Время: {time.time() - start}')

def add_simple(n):
    start = time.time()
    lst = [2]
    for i in range(3, n + 1):
        if i % 2 == 1:
            count = 0
            for j in range(3, i//2 + 1):
                if i % j == 0:
                    count += 1
            if count == 0:
                lst.append(i)
    print(lst)
    print(f'Время: {time.time() - start}')

def remove_not_simple(n):
    start = time.time()
    lst = [x for x in range(2, n + 1)]
    for i in range(3, n + 1):        
        if i % 2 == 0:
            lst.remove(i)
        else:            
            for j in range(3, i//2 + 1):
                if i % j == 0:
                    lst.remove(i) 
                    break           
    print(lst)
    print(f'Время: {time.time() - start}')

n = 100 # int(input('Введите число: '))
eratosphen(n)
add_simple(n)
remove_not_simple(n)
