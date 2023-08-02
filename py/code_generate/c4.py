def aliquot_sum(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

# Test the function
number = 12
print(f"The Aliquot Sum of {number} is {aliquot_sum(number)}")
