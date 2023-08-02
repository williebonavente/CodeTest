def aliquot_sum(n, i=1, sum=0):
    if i == n:
        return sum
    if n % i == 0:
        sum += i
    return aliquot_sum(n, i+1, sum)

# Test the function
number = 12
print(f"The Aliquot Sum of {number} is {aliquot_sum(number)}")
