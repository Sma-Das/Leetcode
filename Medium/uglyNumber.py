"""
Given an integer n, return the nth ugly number.

Ugly number is a positive number whose prime factors only include 2, 3, and/or 5.

The test is incorrect and does not correctly calculate ugly numbers

eg.

Example given for first 11 ugly numbers: [1,2,3,4,5,6,8,9,10,12,15]
Correct first 11 ugly numbers: [1,2,3,4,5,6,8,9,10,12,14]
"""


from collections import deque
from bisect import bisect_left


def nthUglyNumber(n: int) -> int:
    res = deque([1])

    factor = 1

    ugly_fac = [2, 3, 5]

    while len(res) < n * max(ugly_fac) / min(ugly_fac):
        for uf in ugly_fac:
            if not (F := uf*factor) in res:
                i = bisect_left(res, F)
                res.insert(i, F)
        factor += 1
    return res[n-1]
