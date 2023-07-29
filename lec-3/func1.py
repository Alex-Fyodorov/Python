def sum_numbers(n, y = 'hello'):
    print(y)
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

a = sum_numbers(int(input('Vvedite chislo: ')))
print(a)
a = sum_numbers(1, 'stop')