def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Args:
        n (int): The number for which to calculate the factorial.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def total_password_combinations(character_set, password_length):
    """
    Calculates the total number of possible password combinations.

    Args:
        character_set (int): The number of characters in the character set.
        password_length (int): The length of the password.

    Returns:
        int: The total number of possible password combinations.
    """
    total_combinations = character_set ** password_length
    return total_combinations

if __name__ == "__main__":
    character_set_size = 62  # 26 lowercase letters + 26 uppercase letters + 10 digits
    password_length = 8
    total_combinations = total_password_combinations(character_set_size, password_length)
    print(f"There are {total_combinations} possible password combinations.")
