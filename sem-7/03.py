# Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов отличается - то False. 
# Для пустого набора объектов, функция должна возвращать True. 
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.

def same_by(func, array):
    # if len(array) == 0:
    #     return True
    # buf = list(map(func, array))
    # if len(list(filter(lambda x: x == buf[0], buf))) == len(buf):
    #     return True
    # return False
    return len(set(map(func, array))) < 2


values = [0, 4, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
