#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# ADD YOUR CODE HERE

def print_matrix_join(matrix):

    for row in matrix:
            print(' '.join(map(str, row)))

print_matrix_join(matrix)
