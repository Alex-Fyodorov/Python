# 1. Необходимо написать алгоритм поиска всех доступных комбинаций
# (посчитать количество) для количества кубиков K с количеством граней N.
# 2. У вас есть 2 варианта на выбор – количество кубиков может быть строго
# ограничено (4 кубика, например), либо их количество будет динамическим. Выбор за вами.
# 3. Если вы реализуете простой вариант, обращает внимание, что данное решение имеет сложность O(n4), но если количество кубиков сделать переменной, то она трансформируется в O(nk), что будет представлять собой экспоненциальную сложность. 
# Для второго решения очевидно, что его сложность O(nk) с самого начала.

import time
import math

def recomb(n, k):
    start = time.time()
    lst = [str(x) for x in range(1, n + 1)]
    for _ in range(1, k):        
        for _ in range(len(lst)):
            item = lst.pop(0)            
            for i in range(n):
                lst.append(item + str(i + 1))
    lst_set = set()
    for item in lst:        
        item = ''.join(sorted(list(item)))
        lst_set.add(item)
    print(f'Результат: {len(lst_set)} Время: {time.time() - start}')
    
def comb_form(n, k):
    start = time.time()
    res = int(math.factorial(n + k - 1) / (math.factorial(k) * math.factorial(n - 1)))
    print(f'Результат: {res} Время: {time.time() - start}')

n = int(input('Введите кол-во граней: '))
k = int(input('Введите кол-во кубиков: '))

recomb(n, k)
comb_form(n, k)
