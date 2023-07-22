# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.

from random import randint

print(lst := [randint(-5, 5) for _ in range(10)])

shift = int(input('Введите сдвиг: '))

# print(lst[-shift:] + lst[:-shift])

# for i in range(shift):
#     item = lst.pop()
#     lst.insert(0, item)
# print(lst)

new_list = []
for i in range(100):
    print(lst[i%len(lst)])