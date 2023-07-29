def sieve_of_eratosthenes(n):
  """
  Finds all of the prime numbers less than a given number.

  Args:
    n: The number to find the prime numbers for.

  Returns:
    A list of the prime numbers less than n.
  """

  primes = []
  composite = [False] * (n + 1)

  for i in range(2, n + 1):
    if not composite[i]:
      primes.append(i)
      for j in range(i * i, n + 1, i):
        composite[j] = True

  return primes


if __name__ == "__main__":
  primes = sieve_of_eratosthenes(100)
  print(primes)
