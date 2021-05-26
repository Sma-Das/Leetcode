"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
"""

from itertools import accumulate


def runningSum(nums: list[int]) -> list[int]:
    return accumulate(nums)


if __name__ == '__main__':
    runningSum([*range(9)])
