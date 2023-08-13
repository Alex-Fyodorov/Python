# 1.Необходимо написать один из простых алгоритмов сортировки,
# имеющий сложность O(n2).
# 2.Можно выбрать из пузырьковой сортировки, сортировки вставками и
# сортировки выбором.
# 3.Следует обратить внимание на сложность данных алгоритмов и
# указать признаки квадратичной сложности для каждого из них.

from random import randint
import time

def bubble(sp):
    start = time.time()
    for i in range(len(sp)-1):
        for j in range(len(sp)-i-1):
            if sp[j] > sp[j+1]:
                sp[j], sp[j+1] = sp[j+1],sp[j]
    print(sp)
    print(time.time() - start)

def counting_sort(sp):
    start = time.time()
    max_item=max(sp)
    lst=[0 for _ in range(max_item+1)]
    for i in sp:
        lst[i]=lst[i]+1
    print(lst)
    index=0
    # for i in range(len(lst)):
    #     for j in range(lst[i]):
    #         sp[index]=i
    #         index+=1
    res_sp = []
    for i in range(len(lst)):
        if lst[i]:
            res_sp.extend([i] * lst[i])
    print(res_sp)    
    print(time.time() - start)

print(sp := [randint(0, 10) for _ in range(20)])
bubble(sp)
counting_sort(sp)