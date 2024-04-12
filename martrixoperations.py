def matrix_addition(A, B):
    """
    Perform matrix addition.
    A and B are matrices represented as lists of lists.
    """
    print(len(A))
    print(len(A[0]))
    print(A[0])
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return "Matrices must have the same dimensions for addition."
    
    result = []
    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] + B[i][j])
        result.append(row)
    return result


# Example matrices
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Matrix addition
print("Matrix Addition:")
print(matrix_addition(matrix1, matrix2))

