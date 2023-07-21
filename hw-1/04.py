a, b, c = 3, 2, 4

if c % a == 0 and c / a <= b:
    print('yes')
elif c % b == 0 and c / b <= a:
    print('yes')
else:
    print('no')