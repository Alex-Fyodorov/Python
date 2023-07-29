# 1. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# *Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)*
def is_simple(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, num // 2 + 1, 2):
        if num % i == 0:
            return False
    return True

from random import randint
num = randint(1, 20)
print(num)
print(is_simple(num))
