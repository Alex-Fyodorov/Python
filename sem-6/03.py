# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

from random import randint
print(list_1 := [randint(0, 10) for _ in range(10)])

print(sum([list_1.count(i)//2 for i in set(list_1)]))

dic = {}
for i in list_1:
    value = dic.get(i, 0) + 1
    dic[i] = value
count = 0
for i in dic.values():
    count += i//2
print(count)
