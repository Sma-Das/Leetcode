def minFallingPathSum():
    if not matrix:
         return 0

    for row in range(1, len(matrix)):
        prev_row = matrix[row-1]
        for column in range(c := len(matrix[0])):
            v = matrix[row][column]
            ops = []
            if column > 0:
                ops.append(prev_row[column-1] + v)
            if column < c-1:
                ops.append(prev_row[column+1] + v)
            ops.append(prev_row[column] + v)
            matrix[row][column] = min(ops)
    return min(matrix[-1])
