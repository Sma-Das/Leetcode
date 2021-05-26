"""
Given a set of non-overlapping intervals,
insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times
"""

from collections import deque


def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    intervals = sorted(intervals + [newInterval])
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
    a = [[1, 3], [6, 9]]
    b = [2, 5]
    c = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    d = [4, 8]
    e = []
    f = [5, 7]
    g = [[1, 5]]
    h = [2, 3]
    i = [[1, 5]]
    j = [2, 7]
    insert(c, d)
