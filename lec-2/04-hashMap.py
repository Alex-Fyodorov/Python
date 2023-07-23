d = {}
d = dict()

d['q'] = 'qwerty'
print(d)
d['w'] = 'werty'
print(d)
print(d['q'])
print()

di = {'q': 'qwerty', 'w': 'wertyu', 'e': 'ertyui', 'r': 'rtyuio', 't': 'tyuiop'}
print(di)
del(di['t'])
print(di)
print()

for i in di:
#    print(i)
    print('{}: {}'.format(i, di[i]))
print()

for (k, v) in di.items():
    print(k, v)
print()

print(di.items())