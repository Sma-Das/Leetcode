from collections import deque
from string import ascii_lowercase as letters


def alphabetBoardPath(target: str):
    board = {l: [i//5, i % 5] for i, l in enumerate(letters)}
    res = deque([])
    r0, c0 = 0, 0
    for l in target:
        r, c = board[l]
        if r0 < r:
            res.append("D" * (r-r0))
        elif r0 > r:
            res.append("U" * (r0-r))
        if c0 < c:
            res.append("R" * (c-c0))
        elif c0 > c:
            res.append("L" * (c0-c))
        r0, c0 = r, c
        res.append("!")
    return "".join(res)


if __name__ == '__main__':
    print(alphabetBoardPath("leet"))
