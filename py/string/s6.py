def contains_only_digits(input_string):
    """
    Check if the input string contains only digits.

    Args:
        input_string (str): The string to be checked.

    Returns:
        bool: True if the input string contains only digits, False otherwise.
    """
    try:
        # Attempt to convert the input string to an integer
        # If successful, it means the string contains only digits
        int(input_string)
        return True
    except ValueError:
        # If there's a ValueError, it means the conversion to int failed
        # and the string contains non-digit characters
        return False

if __name__ == "__main__":
    user_input = input("Enter a string to check if it contains only digits: ")
    if contains_only_digits(user_input):
        print("The input string contains only digits.")
    else:
        print("The input string contains non-digit characters.")
