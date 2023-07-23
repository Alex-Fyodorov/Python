a = {1, 2, 4, 6, 8, 5}
b = {1, 3, 5, 7, 9, 4}
c = a.copy()
u = a.union(b)
print(u)

i = a.intersection(b)
print(i)

da = a.difference(b)
db = b.difference(a)
print(da)
print(db)

f = frozenset(a)
print(f)