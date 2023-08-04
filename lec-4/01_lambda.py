def f(x):
    return x * x

sum2 = lambda a, b: a + b

def funk(op, x, y):
    print(op(x, y))

a = f
print(type(a))
print(a(5))
print(sum2(5, 45))
funk(lambda a, b: a + b, 5, 45)