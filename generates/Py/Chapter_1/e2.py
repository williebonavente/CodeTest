def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def is_valid_pin(pin, valid_pins):
    index = binary_search(valid_pins, pin)
    return index != -1

def main():
    # List of valid PINs
    valid_pins = [1234, 5678, 9876, 4321, 5555]

    # Get the PIN from the user
    pin = int(input("Enter your PIN: "))

    # Check if the PIN is valid
    if is_valid_pin(pin, valid_pins):
        print("Access granted. Welcome!")
    else:
        print("Invalid PIN. Access denied.")

if __name__ == "__main__":
    main()
