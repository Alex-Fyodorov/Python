from random import randint
print(list_1 := [randint(-10, 10) for _ in range(10)])
k = int(input('vvedite chislo: '))
delta, res = float('inf'), 0
for i in list_1:
    div = abs(k - i)
    if div < delta:
        delta, res = div, i        
print(res)