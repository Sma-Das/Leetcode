"""
Given an array of integers arr and an integer k.
Find the least number of unique integers after removing exactly k elements.
"""


from collections import Counter


def findLeastUniqueInts(arr: list[int], k: int):
    c = Counter(arr)
    s = sorted(arr, key=lambda v: (c[v], v))
    return len(set(s[k:]))


if __name__ == "__main__":
    print(findLeastUniqueInts(
        [24, 119, 157, 446, 251, 117, 22, 168, 374, 373, 323, 311, 441, 213, 120, 412, 200, 236, 328, 24, 164, 104, 331,
            32, 19, 223, 89, 114, 152, 82, 456, 381, 355, 343, 157, 245, 443, 368, 229, 49, 82, 16, 373, 142, 240, 125, 8],

        41
    ))
