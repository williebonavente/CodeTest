def radix_sort(arr):
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        count = [0] * 10

        for num in arr:
            count[(num // exp) % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        output = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1

        for i in range(len(arr)):
            arr[i] = output[i]

        exp *= 10
