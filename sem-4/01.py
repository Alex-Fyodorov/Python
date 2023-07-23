# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.

str = 'zxczxczxczxczxc'
str = list(str)
s = set(str)
for i in s:
    count = 0
    for j in range(len(str)):
        if str[j] == i and count > 0:
            str[j] = f'{str[j]}_{count}'
            count += 1
        if str[j] == i:
            count += 1
print(str)