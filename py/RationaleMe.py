import sympy as sp

# Define the variables
x = sp.symbols('x')

# Define the expression
expr = 9 / (2 ** (1/4))

# Rationalize the expression
rationalized_expr = sp.Rationalize(expr)

# Print the result in sqrt format
sp.pretty(rationalized_expr, use_unicode=True)
