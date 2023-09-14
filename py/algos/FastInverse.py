def fast_inverse_square_root(x):
    i = x
    i = 0x5f3759df - (i >> 1)
    y = i
    y = y * (1.5 - 0.5 * x * y * y)
    return y
