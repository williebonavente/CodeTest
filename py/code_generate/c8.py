def nth_term_arithmetic_progression(first_term, common_difference, n):
    nth_term = first_term + (n - 1) * common_difference
    return nth_term

# Example usage
first_term = 2
common_difference = 3
n = 5
nth_term = nth_term_arithmetic_progression(first_term, common_difference, n)
print(f"The {n}th term of the arithmetic progression is: {nth_term}")
