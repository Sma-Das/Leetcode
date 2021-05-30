from functools import reduce
from math import ceil


class Solution:
    def matrixScore(self, grid: list[list[int]]) -> int:
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

    def matrixScore2(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        total, rows = (1 << n-1) * m, range(m)
        for col in range(1, n):
            curr_row = sum(grid[row][col] for row in rows)
            total += max(curr_row, m-curr_row) * (1 << n-1-col)
        return total


if __name__ == '__main__':
    print(Solution().matrixScore2([[0]]))
    print(Solution().matrixScore2([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]]))
