"""
Given a positive integer n,
generate an n x n matrix filled with elements from 1 to n^2 in spiral order.
"""

# from collections import deque


def generateMatrix(n: int):
    matrix = [
        [0 for _ in range(n)] for _ in range(n)
    ]
    i, j, d_i, d_j = 0, 0, 0, 1
    m = 1
    for v in range(1, n*n):
        print(i, j, d_i, d_j)
        print(matrix)
        matrix[i][j] = v
        if i == j and (i or j):
            m *= -1
        if i+j == n-1 or i+j == 2*(n-1):
            d_i, d_j = d_j*m, d_i*m
        i, j = i+d_i, j+d_j

    return matrix


if __name__ == '__main__':
    [[1, 2, 3, 4, 5],
     [16, 17, 18, 19, 6],
     [15, 24, 25, 20, 7],
     [14, 23, 22, 21, 8],
     [13, 12, 11, 10, 9]]

    print(generateMatrix(5))
