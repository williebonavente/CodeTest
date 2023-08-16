import time

def fast_inverse_square_root(x):
    i = x
    i = 0x5f3759df - (i >> 1)
    y = i
    y = y * (1.5 - 0.5 * x * y * y)
    return y

def calculate_distance(x, y):
    # Calculate the distance using the fast inverse square root approximation
    approx_distance = fast_inverse_square_root(x*x + y*y)
    return approx_distance

# Example usage
x = 3.0
y = 4.0
start_time = time.time()
approx_distance = calculate_distance(x, y)
end_time = time.time()

print(f"Approximate Distance: {approx_distance}")
print(f"Calculation Time: {end_time - start_time} seconds")
