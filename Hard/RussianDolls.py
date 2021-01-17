"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both:
the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)
"""

from bisect import bisect_left


def maxEnvelopes(envelopes: list[list[int, int]]) -> int:
    envelopes.sort(key=lambda val: (val[0], -val[1]))
    nums, ls = [h for _, h in envelopes], []
    for n in nums:
        i = bisect_left(ls, n)
        ls[i:i+1] = [n]
    return len(ls)


if __name__ == '__main__':
    print(maxEnvelopes([[2, 100], [3, 200], [4, 300], [5, 500], [5, 400], [5, 250], [6, 370], [6, 360], [7, 380]]
                       ))
    print(maxEnvelopes([[5, 4], [6, 4], [6, 7], [2, 3]]))
