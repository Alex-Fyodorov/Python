# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)

from random import randint

print(lst := [randint(-5, 5) for i in range(8)])
count = 0

for i in range(len(lst)-1):
    if lst[i] < lst[i+1]:
        count += 1
print(count)