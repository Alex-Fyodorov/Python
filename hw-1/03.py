n = 123456
n1 = int(n / 1000)
n2 = n % 1000
m1 = n1 % 10
m2 = int(n1 / 10) % 10
m3 = int(n1 / 100) % 10
res1 = m1 + m2 + m3
m1 = n2 % 10
m2 = int(n2 / 10) % 10
m3 = int(n2 / 100) % 10
res2 = m1 + m2 + m3
if res1 == res2:
    print('yes')
else:
    print('no')
