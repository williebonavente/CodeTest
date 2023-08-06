def gaussian_elimination(matrix, mod):
    n = len(matrix)
    for i in range(n):
        # Make the diagonal element 1
        inv = pow(matrix[i][i], -1, mod)
        for j in range(i, n + 1):
            matrix[i][j] = (matrix[i][j] * inv) % mod

        # Eliminate other elements in the column
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n + 1):
                    matrix[k][j] = (matrix[k][j] - factor * matrix[i][j]) % mod

    return [row[-1] for row in matrix]
