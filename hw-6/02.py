# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint
print(list_init := [randint(-20, 20) for _ in range(10)])
print(min_value := randint(-20, 0))
print(max_value := randint(1, 20))
print(list_res := [i for i in range(len(list_init)) if min_value <= list_init[i] <= max_value])