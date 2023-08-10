def binary_search(arr, x):
    """
    Searches for the given value in the given array using the binary search algorithm

    Args:
        arr: The array to search in.
        x: The value to search for.

    Returns:
        The index of the value in the array, or -1 if the value is not found.
    """
    arr.sort()  # sort the array first

    i = 0
    j = len(arr) - 1

    while i <= j:
        mid = (i + j) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] < x:
            i = mid + 1
        else:
            j = mid - 1

    return -1

def main():
    arr = [1, 5, 3, 2, 7]
    x = 5
    
    location = binary_search(arr,x)
    
    if location != -1:
        print(f"The value of {x} is found at index: {location}")
    else:
        print(f"The value {x} is not found")
        
        
if __name__ == "__main__":
    main()
