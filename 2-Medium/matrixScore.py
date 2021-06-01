from functools import reduce
from math import ceil
from collections import Counter
'''
94.61% // 61.95%
'''


class Solution:
    def matrixScore(self, grid) -> int:
        rows, columns = len(grid), len(grid[0])
        grid = [[0 if v else 1 for v in row]
                if not row[0] else row for row in grid]

        def num_one(col: int):
            return Counter(1 for r in range(rows) if grid[r][col] == 1)[1]

        def invert_col(col: int):
            for r in range(rows):
                grid[r][col] = 0 if grid[r][col] else 1

        tar = ceil(rows/2)
        [invert_col(col) for col in range(1, columns) if num_one(col) < tar]
        return sum(int(reduce(lambda x, y: str(x) + str(y), row+[""]), base=2) for row in grid)

    def matrixScore2(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        total, rows = (1 << n-1) * m, range(m)
        for col in range(1, n):
            curr_row = sum(grid[row][col] for row in rows)
            total += max(curr_row, m-curr_row) * (1 << n-1-col)
        return total

    def matrixScore(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])

        for i, row in enumerate(grid):
            if row[0] == 0:
                grid[i] = [int(not bool(v)) for v in row]

        def num_one(col: int):
            return len([1 for r in range(rows) if grid[r][col] == 1])

        def invert_col(col: int):
            for r in range(rows):
                grid[r][col] = int(not bool(grid[r][col]))

        tar = ceil(rows/2)
        for col in range(1, columns):
            if num_one(col) < tar:
                invert_col(col)
        return sum(int(reduce(lambda x, y: str(x) + str(y), row+[""]), base=2) for row in grid)


if __name__ == '__main__':
    print(Solution().matrixScore([[0]]))
    print(Solution().matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
