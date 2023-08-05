def is_quadratic_residue(a, p):
    return pow(a, (p - 1) // 2, p) == 1
