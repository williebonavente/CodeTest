def binary_search(arr, target):
    # Input validation
    if not isinstance(arr, list) or not all(isinstance(elem, int) for elem in arr):
        raise ValueError("Input 'arr' must be a list of integers.")
    if not isinstance(target, int):
        raise ValueError("Input 'target' must be an integer.")

    # Check if the list is sorted (assumed to be in ascending order)
    if arr != sorted(arr):
        raise ValueError(
            "Input 'arr' must be sorted in ascending order for binary search.")

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example usage
numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target_number = 12

try:
    result = binary_search(numbers, target_number)
    if result != -1:
        print(f"Element {target_number} found at index {result}.")
    else:
        print(f"Element {target_number} not found in the list.")
except ValueError as e:
    print(f"Error: {e}")
