def peasant_multiplication(a, b):
    result = 0
    while b > 0:
        if b % 2 == 1:
            result += a
        a = a << 1
        b = b >> 1
    return result
