def f(a, b):
    if b == 0:
        return 1
    return a * f(a, b-1)

a = 3
b = 5
print(f(a, b))