def heap_sort(array):
    build_max_heap(array)

    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_heapify(array, 0, i)


def build_max_heap(array):
    for i in range(len(array) // 2 - 1, -1, -1):
        max_heapify(array, i, len(array))


def max_heapify(array, i, heap_size):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < heap_size and array[left] > array[largest]:
        largest = left

    if right < heap_size and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        max_heapify(array, largest, heap_size)
