from collections import deque


def canReach(arr: list[int], start: int):
    stack, visited = deque([start]), set()
    l, r = 0, len(arr) - 1

    while stack:
        i = stack.pop()
        if i in visited:
            continue
        if l <= (L := i + arr[i]) <= r:
            stack.append(L)
        if l <= (R := i - arr[i]) <= r:
            stack.append(R)
        visited.add(i)

    return all(i in visited for i in (j for j, v in enumerate(arr) if v == 0))
