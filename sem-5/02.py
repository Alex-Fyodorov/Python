# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

from random import randint
print(list_1 := [randint(1, 5) for _ in range(5)])
max_1 = max(list_1)
min_1 = min(list_1)
for i in range(len(list_1)):
    if list_1[i] == max_1:
        list_1[i] = min_1
print(list_1)
