"""
Given two arrays, write a function to compute their intersection.
"""


def intersection(nums1: list[int], nums2: list[int]):
    inters = set(nums1) & set(nums2)
    res = []
    for n in inters:
        res += [n] * (nums1.count(n) + nums2.count(n))
    return res


if __name__ == '__main__':
    print(
        intersection(
            [1, 2, 2, 1],
            [2, 2, 1]
        )
    )
