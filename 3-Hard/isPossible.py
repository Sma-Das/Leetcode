"""
Given an array of integers target.
 From a starting array, A consisting of all 1's, you may perform the following procedure :

let x be the sum of all elements currently in your array.
choose index i, such that 0 <= i < target.size and set the value of A at index i to x.
You may repeat this procedure as many times as needed.
Return True if it is possible to construct the target array from A otherwise return False.

"""

import heapq


def isPossible(target: list[int]) -> bool:
    t = sum(target)
    target = [-v for v in target]
    heapq.heapify(target)
    while True:
        v = -heapq.heappop(target)
        t -= v
        if v == 1 or t == 1:
            return True
        elif v < t or t == 0 or v % t == 0:
            return False
        v %= t
        t += v
        heapq.heappush(target, -v)


if __name__ == '__main__':
    trials = [
        [9, 3, 5],
        [1, 1, 1, 2],
        [8, 5],
        [1],
        [2],
        [1, 2],
        [1, 1, 2],
        [1, 1000000000],
        [5, 50],
    ]
    for trial in trials:
        print(isPossible(trial))
