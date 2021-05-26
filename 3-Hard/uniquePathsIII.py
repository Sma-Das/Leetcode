"""
The question is incorrect as it says you can only travserse an open path once but
uses the same path repeatedly, violating its own rules
"""


def uniquePathsIII(grid: list[list[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    index = dict()
    for r in range(rows := len(grid)):
        for c in range(cols := len(grid[0])):
            if not (v := grid[r][c]):
                grid[r][c] = 3
            elif v == 2 or v == 1:
                index[v] = (r, c)

    def coords(r, c):
        yield r+1, c
        yield r-1, c
        yield r, c+1
        yield r, c-1

    paths = float('inf')
    for row, col in index.values():
        paths = min(paths,
                    *sum((1 for r, c in coords(row, col)
                          if (0 <= r < rows and 0 <= c < cols) and grid[r][c] == 3)))

    return paths
