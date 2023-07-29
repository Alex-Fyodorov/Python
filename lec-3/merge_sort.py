def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if  left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else: 
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

from random import randint
print(list_1 := [randint(0, 20) for _ in range(10)])
merge_sort(list_1)
print(list_1)