# Function to calculate the width w in terms of A, l, and h
def calculate_width(A, l, h):
    w = (A - 4 * l * h) / (2 * l)
    return w

# Example usage:
A = 100  # Replace with the actual value of A
l = 5    # Replace with the actual value of l
h = 4    # Replace with the actual value of h

width = calculate_width(A, l, h)
print(f"The width w is: {width}")
