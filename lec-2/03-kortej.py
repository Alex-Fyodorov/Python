t = ()
print(type(t))
t = (1)
print(type(t))
t = (1,)
print(type(t))

v = [2, 8, 57]
print(v)
print(type(v))

v = tuple(v)
print(v)
print(type(v))

a, b, c = v
print(a, b, c)

t = (2, 5, 9, 4, 6,)
print(t[2])