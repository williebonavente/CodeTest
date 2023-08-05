def is_in_arithmetic_progression(first_term, common_difference, number):
    if (number - first_term) % common_difference == 0:
        return True
    else:
        return False

# Example usage
first_term = 2
common_difference = 3
number = 8
is_in_progression = is_in_arithmetic_progression(first_term, common_difference, number)
if is_in_progression:
    print(f"{number} is in the arithmetic progression.")
else:
    print(f"{number} is not in the arithmetic progression.")
