# Напишите программу для печати всех уникальных значений в словаре.

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

uniq_el = set()
for i in list_1:
    for key in i:
        element = i[key]
        uniq_el.add(element)
print(uniq_el)  

uniq_el = set(list(i.values())[0] for i in list_1) 
print(uniq_el)