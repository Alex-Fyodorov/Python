count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]
print(count_all)

def calc_count(sp):
    total = 0
    for item in sp:
        # if str(type(item)) == "<class 'list'>":
        if isinstance(item, list):
            total = total + calc_count(item)
        else:
            total += item
    return total