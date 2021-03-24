"""
Given an array of intervals where intervals[i] = [start, end],
merge all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.
"""

from collections import deque


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals = sorted(intervals)
    merged = deque()
    for start, end in intervals:
        flag = False
        for i, (s, e) in enumerate(merged):
            if (s <= start <= e) or (s <= end <= e):
                merged[i] = [min(start, s), max(end, e)]
                flag = True
                break
        if not flag:
            merged.append([start, end])
    return merged


if __name__ == '__main__':
    test1 = [[1, 3], [2, 6], [8, 10], [15, 18], [2, 4]]
    test2 = [[1, 4], [4, 5]]
    test3 = [[1, 4], [0, 5]]
    print(merge(test1))
