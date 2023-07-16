# Поиск индекса в последовательности Фибоначчи

a = int (input('введите число: '))
count = 0
number1 = 0
number2 = 1
while number2 < a:    
    number1, number2 = number2, number2 + number1    
    count += 1
if number2 == a:
    print (count)
if number2 != a:
    print(-1)