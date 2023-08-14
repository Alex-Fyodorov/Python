# Аналитически обосновать в каких случаях эффективнее применять быструю сортировку, а когда сортировку подсчетом. Произвести ряд экспериментов с различной длиной массивов и различным диапазоном значений. Оценить и интерпретировать результаты экспериментов, соотнести с теоретическими выкладками.

from random import randint
import time

def counting_sort(sp):    
    max_item = max(sp)
    min_item = min(sp)
    lst=[0 for _ in range(min_item, max_item+1)]
    for i in sp:
        lst[i - min_item] = lst[i - min_item] + 1    
    index=0    
    res_sp = []
    for i in range(len(lst)):
        if lst[i]:
            res_sp.extend([i + min_item] * lst[i])
    return res_sp

def quick_sort(sp):    
    if len(sp) == 1 or len(sp) == 0:
        return sp
    midl = sp[0]
    min_lst = [i for i in sp[1:] if i <= midl]
    max_lst = [i for i in sp[1:] if i > midl]
    # min_lst, max_lst = [], []
    # for i in range (1, len(sp)):
    #     if sp[i] <= midl: min_lst.append(sp[i])
    #     if sp[i] > midl: max_lst.append(sp[i])
    return quick_sort(min_lst) + [midl] + quick_sort(max_lst)

def time_of_method(funk, arr):
    start = time.time()
    result = funk(arr)
    # print(result)
    print(time.time() - start)

sp = [randint(-10000000, 10000000) for _ in range(2000000)]
# print(sp)
time_of_method(counting_sort, sp)
time_of_method(quick_sort, sp)  

# Вывод: Чем больше разброс между максимальным и минимальным элементами, тем медленнее работает сортировка подсчётом, и чем больше количество самих элементов, тем медленнее работает быстрая сортировка.
# Поэтому быструю сортировку эффективнее применять, если самих элементов не очень много, сортировку подсчётом, если не слишком большая разница между максимумо и минимумом данных.
# Однако при прочих равных почти всегда быстрее работает сортировка подсчётом.
# При диапазоне 20.000.000 и длине списка 2.000.000 подсчёт работает быстрее.
# Быстрая сортировка работает быстрее только если дан короткий список с очень большим разбросом данных. 