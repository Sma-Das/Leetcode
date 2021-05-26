from collections import deque


def maximumUniqueSubarray(nums: list[int]) -> int:
    hi, hold = 0, deque([])
    for num in nums:
        if num not in hold:
            hold.append(num)
        else:
            while (curr := hold.popleft()) != num:
                pass
            hold.appendleft(num)
        hi = max(hi, sum(hold))
    return hi
