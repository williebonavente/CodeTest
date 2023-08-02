def sum_arithmetic_progression(first_term, common_difference, num_terms):
    last_term = first_term + (num_terms - 1) * common_difference
    sum_of_terms = (num_terms / 2) * (first_term + last_term)
    return sum_of_terms

# Example usage
first_term = 2
common_difference = 3
num_terms = 5
sum_of_terms = sum_arithmetic_progression(first_term, common_difference, num_terms)
print(f"The sum of the arithmetic progression is: {sum_of_terms}")
