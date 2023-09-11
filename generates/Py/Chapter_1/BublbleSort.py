def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Track if any elements were swapped in this pass
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Set swapped to True if elements were swapped
        if not swapped:
            break  # If no elements were swapped, the list is already sorted, so exit the loop

def print_list(arr):
    print("Sorted List:", arr)

def main():
    # Get the list of numbers from the user
    items = input("Enter a list of numbers (separated by commas): ")
    num_list = [int(num) for num in items.split(',')]

    # Perform bubble sort to sort the list
    bubble_sort(num_list)

    # Display the sorted list
    print_list(num_list)

if __name__ == "__main__":
    main()
