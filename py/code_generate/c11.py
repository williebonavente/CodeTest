from math import gcd

def gcd_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

numbers = [12, 18, 24, 36, 48]

result = gcd_list(numbers)
print(f"The GCD of {numbers} is {result}")
