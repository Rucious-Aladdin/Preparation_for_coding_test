def quicksort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    return quicksort([x for x in tail if x <= pivot]) + [pivot] + quicksort([x for x in tail if x > pivot])

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
arr = quicksort(array)
print(arr)