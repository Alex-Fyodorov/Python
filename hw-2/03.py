# Надо сделать имитацию БД по хранению чисел.
# шаг 1 - генерируем список со случайной длиной , со случайным минимальных значением и случайным максимальным. Можно вывести на экран.
# шаг 2 - ваша программа выбирает наилучший вариант сортировки исходя из параметров входного массива - как минимум, из двух вариантов - из сортировки подсчетом и из быстрой сортировки.
# шаг 3 - производится сортировка и создается некая коллекция данных, которая хранит в себе первоначальное расположение элементов. Засекаем время выполнения и выводим на экран.
# шаг 4 - вы вводите число с клавиатуры, далее выполняется бинарный поиск всех таких значений. Засекаем время выполнения и выводим на экран.
# шаг 5 - вам выводятся индексы первоначального списка с шага 1, где находились такие числа.
# шаги 4-5 можно сделать внутри цикла while True.
# Мораль этого задания - можно помучиться один раз, выполнить сортировку, зато потом будет очень быстрый поиск элементов.

from random import randint
import time
import math

def create_database(lst):
    dic = {}
    for i in range(len(lst)):
        if lst[i] in dic:
            dic.get(lst[i]).append(i)
        else: dic[lst[i]] = [i]
    return dic

def create_datalist(lst):
    data_lst = []
    for i in range(len(lst)):
        data_lst.append([lst[i], i])
    return data_lst

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
    return quick_sort(min_lst) + [midl] + quick_sort(max_lst) 

#def binary_find(lst, num)

max_item = randint(1, 1000)
min_item = randint(-1000, 0)
lst_size = randint(10, 100)
sp = [randint(min_item, max_item) for _ in range(lst_size)]
dic = create_database(sp)
# data_lst = create_datalist(sp)
# Даже при не очень большом количестве элементов рандом занимает весь или почти весь диапазон, поэтому разницей между максимумом и минимумом списка в данном случае можно пренебречь. Гораздо большую роль играет количество элементов. Скорость сортировки обоих методов сравнивается, примерно, при длине списка, равной 500. Поэтому:
# if lst_size <= 500:
#     lst_sort = quick_sort(data_lst)
# else: lst_sort = counting_sort(data_lst)
print(dic) 
i = int(input('xcbxcvb'))
print(dic[i])

