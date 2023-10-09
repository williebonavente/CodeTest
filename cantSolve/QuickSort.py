def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    less = [x for x in array[1:] if x < pivot]
    greater = [x for x in array[1:] if x >= pivot]

    return quicksort(less) + [pivot] + quicksort(greater)