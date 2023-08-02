from math import gcd

def simplify_fraction(numerator, denominator):
    gcd_value = gcd(numerator, denominator)
    simplified_numerator = numerator # gcd_value
    simplified_denominator = denominator # gcd_value
    return simplified_numerator, simplified_denominator

numerator = 24
denominator = 36

simplified_numerator, simplified_denominator = simplify_fraction(numerator, denominator)
print(f"The simplified fraction of {numerator}/{denominator} is {simplified_numerator}/{simplified_denominator}")
