from collections import defaultdict
from operator import itemgetter
from math import gcd


def getCoprimes(nums, edges):
    tree = defaultdict(list)
    for prev, nxt in edges:
        tree[nxt] += [prev, *tree[prev]]
    return [max([p for p in tree[i] if gcd(v, nums[p]) == 1] + [-1]) for i, v in enumerate(nums)]


if __name__ == '__main__':
    print(getCoprimes([5, 6, 10, 2, 3, 6, 15],
                      [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]))
