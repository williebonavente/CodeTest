import matplotlib.pyplot as plt
import numpy as np

def riemann_zeta(s, terms=100):
    """
    Calculate the Riemann zeta function for a given complex number s.

    Args:
        s (complex): The complex number for which to calculate the Riemann zeta function.
        terms (int, optional): The number of terms to use in the series approximation. Default is 100.

    Returns:
        complex: The value of the Riemann zeta function for the given complex number.
    """
    result = 0
    for n in range(1, terms+1):
        result += 1 / (n**s)
    return result


def prime_gaps(limit):
    primes = [2]
    gaps = []
    for num in range(3, limit):
        if all(num % prime != 0 for prime in primes):
            gaps.append(num - primes[-1])
            primes.append(num)
    return gaps

def zeta_gap_prediction(limit):
    gaps = []
    for num in range(2, limit):
        zeta_value = riemann_zeta(complex(1, num))
        predicted_gap = int(1 / zeta_value.real)
        gaps.append(predicted_gap)
    return gaps

# Calculate prime gaps and zeta-based predictions
limit = 100
observed_gaps = prime_gaps(limit)
zeta_predicted_gaps = zeta_gap_prediction(limit)

# Plot the prime gaps and zeta-based predictions
plt.plot(range(2, limit), observed_gaps, label='Observed Prime Gaps')
plt.plot(range(2, limit), zeta_predicted_gaps, label='Zeta-based Predictions')
plt.xlabel('Prime Index')
plt.ylabel('Gap Size')
plt.title('Prime Gaps and Zeta-based Predictions')
plt.legend()
plt.grid(True)
plt.show()
