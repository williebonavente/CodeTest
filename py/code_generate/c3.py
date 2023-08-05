def fibonacci(n):
    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib[n - 1]  # Change the index here from n to n - 1

print(fibonacci(10))
