def mobius(n):
    if n == 1:
        return 1
    count = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    if count % 2 == 0:
        return 1
    else:
        return -1
