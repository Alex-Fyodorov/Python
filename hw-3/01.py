from random import randint
print(list_1 := [randint(-10, 10) for _ in range(10)])
k = int(input('vvedite chislo: '))
count = 0
for i in list_1:
    if i == k:
        count += 1
print(count)