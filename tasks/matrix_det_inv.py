import numpy as np

# Ask the user to enter the matrix elements
matrix_str = input("Enter the matrix elements separated by spaces: ")
matrix_list = matrix_str.split()
n = int(np.sqrt(len(matrix_list)))
matrix = np.array(matrix_list, dtype=float).reshape(n, n)

# Check if the matrix is 3x3
if matrix.shape != (3, 3):
    print("Error: The matrix must be a 3x3 matrix.")
else:
    # Calculate the determinant and inverse of the matrix
    det = np.linalg.det(matrix)
    if det == 0:
        print("Error: The matrix is singular and does not have an inverse.")
    else:
        inverse = np.linalg.inv(matrix)

        # Output the determinant and inverse of the matrix
        print("The determinant of the matrix is:", det)
        print("The inverse of the matrix is:\n", inverse)

