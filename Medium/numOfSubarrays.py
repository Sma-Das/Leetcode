from collections import deque


def numOfSubarrays(arr: list[int], k: int, threshold: int):
    dp = deque([0])
    [dp.append(v + dp[-1]) for v in arr]
    return sum((1 for i in range(len(arr) - k + 1) if dp[i+k] - dp[i] >= k * threshold))


if __name__ == '__main__':
    numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4)
