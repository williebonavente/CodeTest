def is_armstrong(n):
    num = str(n)
    power = len(num)
    return n == sum(int(digit)**power for digit in num)
