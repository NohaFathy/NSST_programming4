# Ask the user to enter the dimensions of the first matrix
rows1 = int(input("Enter the number of rows of the first matrix: "))
cols1 = int(input("Enter the number of columns of the first matrix: "))

# Ask the user to enter the dimensions of the second matrix
rows2 = int(input("Enter the number of rows of the second matrix: "))
cols2 = int(input("Enter the number of columns of the second matrix: "))

# Check if the matrices can be multiplied
if cols1 != rows2:
    print("Error: The number of columns of the first matrix must be equal to the number of rows of the second matrix.")
else:
    # Initialize the first matrix with zeros
    matrix1 = [[0 for j in range(cols1)] for i in range(rows1)]

    # Initialize the second matrix with zeros
    matrix2 = [[0 for j in range(cols2)] for i in range(rows2)]

    # Ask the user to enter the elements of the first matrix
    print("Enter the elements of the first matrix:")
    for i in range(rows1):
        for j in range(cols1):
            matrix1[i][j] = int(input("Enter element ({},{}): ".format(i, j)))

    # Ask the user to enter the elements of the second matrix
    print("Enter the elements of the second matrix:")
    for i in range(rows2):
        for j in range(cols2):
            matrix2[i][j] = int(input("Enter element ({},{}): ".format(i, j)))

    # Multiply the matrices
    result = [[0 for j in range(cols2)] for i in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    # Display the result
    print("The product of the matrices is:")
    for row in result:
        print(row)

