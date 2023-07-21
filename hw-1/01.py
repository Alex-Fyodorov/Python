n = 421
n1 = n % 10
n2 = int(n / 10) % 10
n3 = int(n / 100) % 10
res = n1 + n2 + n3
print(res)