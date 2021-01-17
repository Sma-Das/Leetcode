"""
Given two arrays, write a function to compute their intersection.
"""


def intersection(nums1: list[int], nums2: list[int]) -> set:
    return set(nums1) & set(nums2)


if __name__ == '__main__':
    print(
        intersection(
            [1, 2, 2, 1],
            [2, 2, 1]
        )
    )
