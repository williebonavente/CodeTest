def binary_search(arr, target):
    """
    Binary search algorithm to find the first occurrence of the target element in the array.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            # Handle duplicate elements, find the first occurrence
            while mid > 0 and arr[mid - 1] == target:
                mid -= 1
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def fractional_cascading_search(lists, targets):
    """
    Fractional Cascading algorithm for efficient searching in multiple lists with sorted data.

    Args:
        lists: A list of sorted lists in ascending order.
        targets: A list of target elements to search for in the lists.

    Returns:
        A list of indices where the target elements are found in the corresponding lists.
    """
    results = []

    # Preprocess the first list to store indices of targets in each list
    index_map = {}
    for target in targets:
        indices = []
        for i, element in enumerate(lists[0]):
            if element == target:
                indices.append(i)
        index_map[target] = indices

    # Perform binary search in subsequent lists using the indices from the previous list
    for i in range(1, len(lists)):
        previous_list = lists[i - 1]
        current_list = lists[i]
        indices = []

        for target in targets:
            for prev_index in index_map[target]:
                if prev_index + 1 < len(previous_list) and previous_list[prev_index + 1] == target:
                    indices.append(prev_index + 1)

            # Find the position to start binary search in the current list
            start_index = binary_search(current_list, target)

            for curr_index in range(start_index, len(current_list)):
                if current_list[curr_index] == target:
                    indices.append(curr_index)

            index_map[target] = indices

        results.append(indices)

    return results


# Example usage
lists = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]
targets = [3, 6, 9]

result_indices = fractional_cascading_search(lists, targets)
print("Indices where targets are found in each list:")
for i, indices in enumerate(result_indices):
    print(f"List {i + 1}: {indices}")
