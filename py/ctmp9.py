import math


def factorial(n):
    """
    Calculates the factorial of a number.

    Args:
      n: The number to calculate the factorial of.

    Returns:
      The factorial of the number.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    """
    Calculates the Fibonacci number for a given index.

    Args:
      n: The index of the Fibonacci number to calculate.

    Returns:
      The Fibonacci number for the given index.
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    print(factorial(5))
    print(fibonacci(10))


if __name__ == "__main__":
    main()
