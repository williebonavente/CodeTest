def heap_sort(array):
    build_max_heap(array)

    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, 0, i)