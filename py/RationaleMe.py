from sympy import sqrt, simplify

# Original expression
expression = 9 / (sqrt(2)**(1/4))

# Rationalize the denominator
rationalized_expression = expression * (sqrt(2)**(3/4)) / (sqrt(2)**(3/4))
simplified_expression = simplify(rationalized_expression)

print("Original Expression:", expression)
print("Rationalized Expression:", simplified_expression)
