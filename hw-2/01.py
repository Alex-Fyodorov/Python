# Доработать алгоритм сортировки подсчетом для и отрицательных чисел

from random import randint
import time

def counting_sort(sp):
    start = time.time()
    max_item = max(sp)
    min_item = min(sp)
    lst=[0 for _ in range(min_item, max_item+1)]
    for i in sp:
        lst[i - min_item] = lst[i - min_item] + 1
    print(lst)
    index=0
    # for i in range(len(lst)):
    #     for j in range(lst[i]):
    #         sp[index]=i
    #         index+=1
    res_sp = []
    for i in range(len(lst)):
        if lst[i]:
            res_sp.extend([i + min_item] * lst[i])
    print(res_sp)    
    print(time.time() - start)

    def quick_sort(sp):    
        if len(sp) == 1 or len(sp) == 0:
            return sp
        midl = sp[0]
        min_lst = [i for i in sp[1:] if i <= midl]
        max_lst = [i for i in sp[1:] if i > midl]
        return quick_sort(min_lst) + [midl] + quick_sort(max_lst)


print(sp := [randint(-10, 10) for _ in range(20)])
counting_sort(sp)