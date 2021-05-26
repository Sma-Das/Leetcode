from collections import defaultdict, deque


def maximumRequests(n: int, requests: list[list[int]]) -> int:

    delta = [0 for _ in range(n)]
    accepted = defaultdict(list)

    while requests:
        curr, new = requests.pop()

        delta[curr] -= 1
        delta[new] += 1

        accepted[curr].append(new)
    print(accepted, delta)


if __name__ == '__main__':
    maximumRequests(5,
                    [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]])
