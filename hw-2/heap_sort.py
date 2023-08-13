# Пирамидальная сортировка (сортировка кучей)

from random import randint

def heap_sort(lst):
    index = (len(lst) - 2) // 2
    for i in range(index, -1, -1):        
        tree_sort(lst, i)    
    res_lst = list()
    for j in range(len(lst) - 1, -1, -1):
        lst[0], lst[j] = lst[j], lst[0]
        res_lst.insert(0, lst.pop(j))
        if len(lst) > 1:
            tree_sort(lst, 0)        
    print(res_lst)

def tree_sort(lst, index):
    index_left = (index + 1) * 2 - 1
    index_right = (index + 1) * 2    
    if index_left < len(lst):
        max_left = lst[index_left]
    else: max_left = lst[index]
    if index_right < len(lst):
        max_right = lst[index_right]
    else: max_right = lst[index]
    if max_left > lst[index] and max_left >= max_right: 
        lst[index_left], lst[index] = lst[index], lst[index_left]
        tree_sort(lst, index_left)
    if max_right > max_left and max_right > lst[index]:
        lst[index_right], lst[index] = lst[index], lst[index_right]
        tree_sort(lst, index_right)

print(lst := [randint(1, 100) for _ in range(20)])
heap_sort(lst)