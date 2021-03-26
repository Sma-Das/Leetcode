# from functools import lru_cache


def numRollsToTarget(d: int, f: int, target: int):

    numbers = [*range(1, f+1)]

    return howSum(target, numbers, d)


# @lru_cache
def howSum(target, nums, d, count=0):
    if target == 0:
        return True
    elif target < 0:
        return False
    elif count == d:
        return False

    total = 0

    for i in range(len(nums)):
        curr = nums[i]
        if howSum(target-curr, nums, d, count+1):
            total += 1

    return total


if __name__ == '__main__':
    f = 4
    d = 2
    target = 10
    print(numRollsToTarget(d, f, target))
