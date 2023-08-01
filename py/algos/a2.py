import cmath

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

# Example usage
s = 1 + 2j
result = riemann_zeta(s)
print(f"zeta({s}) =", result)
