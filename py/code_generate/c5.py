def aliquot_sum(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors)

# Test the function
number = 12
print(f"The Aliquot Sum of {number} is {aliquot_sum(number)}")
