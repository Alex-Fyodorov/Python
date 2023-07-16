# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

# from random import randint
# num = randint(0, 9)
# print (num)

from random import randint
n = int(input ('Введите общее колличество'))
m = 0
min_weight = 30001 #(+бесконечность)
max_weight = 0 #(-бесконечность)
while m < n:
    mass=randint(1,30000)
    print(mass)
    if max_weight < mass:
        max_weight = mass
    if min_weight > mass:
        min_weight = mass
    m+=1
print(f'*** Максимальный вес арбуза: {max},Минимальный вес арбуза: {min}')


# Учительское решение:

# from random import randint
# count_wm = int(input('Введите количество арбузов: '))
# max_wm = float('-inf')
# min_wm = float('inf')
# print(f'Перед вами {count_wm} арбузов:')
# for _ in range(count_wm):
#     current_wm = randint(1000, 30000)
#     print(current_wm, end=' ')
#     if max_wm < current_wm:
#         max_wm = current_wm
#     if min_wm > current_wm:
#         min_wm = current_wm
# print(f'\nСамый тяжелый арбуз - {max_wm} гр\nСамый легкий арбуз - {min_wm} гр')
