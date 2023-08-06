def proximal_gradient_algorithm(gradient_func, prox_func, initial_x, learning_rate, max_iterations):
    x = initial_x

    for i in range(max_iterations):
        gradient = gradient_func(x)
        prox = prox_func(x - learning_rate * gradient, learning_rate)
        x = prox

    return x
