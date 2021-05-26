from functools import cache


def minOperations(n, t):
    @cache
    def find_sum(nums, x, count=0):
        lo = float('inf')
        if x == 0:
            return count
        elif x < 0:
            return lo
        for i, v in enumerate(nums, start=1):
            r = find_sum(nums[i:], x-v, count+1)
            if r:
                lo = min(lo, r)
        return lo
    return v if (v := find_sum(tuple(n), t)) != float('inf') else -1


if __name__ == '__main__':
    print(minOperations([1, 1, 4, 2, 3], 5))
