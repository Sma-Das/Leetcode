def pprint(arr):
    [print(row) for row in arr]


def rotateBox(box: list[list[str]], free: str = "#", fixed: str = "*"):
    m, n = len(box), len(box[0])
    box = [[box[j][i] for j in reversed(range(m))] for i in range(n)]
    for r in reversed(range(n)):
        for c in reversed(range(m)):
            if box[r][c] == "#":
                p = r+1
                while p < n and (v := box[p][c]) != fixed:  # and v != free:
                    box[p-1][c], box[p][c] = v, box[p-1][c]
                    p += 1
    return box


if __name__ == '__main__':
    pprint(rotateBox(
        [
            ["#", "#", "*", ".", "*", "."],
            ["#", "#", "#", "*", ".", "."],
            ["#", "#", "#", ".", "#", "."]
        ]
    ))
    pprint(rotateBox([["#", ".", "*", "."],
                      ["#", "#", "*", "."]]))
