
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

# one liner to create a zero matrix from a given matrix
# Assumes that the matrix is non-empty
zero_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]


def printRows(matrix):
    for row in matrix:
        print(row)

def printColumns(matrix):
    num_columns = len(matrix[0])
    num_rows = len(matrix)
    for i in range(num_columns):
        column = []
        for j in range(num_rows):
            column.append(matrix[j][i])
        print(column)


def printColumnsV2(matrix):
    transposed_matrix = [list(row) for row in zip(*matrix)]
    printRows(transposed_matrix)

print("Rows:")
printRows(matrix)

print("Columns:")
printColumns(matrix)

print("Columns V2:")
printColumnsV2(matrix)
