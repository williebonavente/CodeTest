def euclidean_algorithm(a, b):
    while b != 0:
        a, b = b, a % b
    return a
