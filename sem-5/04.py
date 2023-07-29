# 1. Дано натуральное число *N* и последовательность из *N* элементов. Требуется вывести эту последовательность в обратном порядке.
# ***Примечание.*** В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# def print_str(num):
#     if num < 1:
#         return
#     i = int(input())
#     print_str(num - 1)
#     print(i, end = ' ')

# num = int(input())
# print_str(num)

def print_str(num, str_1):
    if num < 1:        
        return str_1
    i = input()
    str_1 = str(i) + ' ' + str_1    
    return print_str(num - 1, str_1)
    
num = int(input())
print(print_str(num, ''))