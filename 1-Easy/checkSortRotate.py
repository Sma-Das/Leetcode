class Solution:
    def check(self, nums: list[int]) -> bool:
        return sum(a > b for a, b in zip(nums, nums[1:] + nums[:1])) < 2


if __name__ == '__main__':
    for test in [
        [3, 4, 5, 1, 2],
        [2, 1, 3, 4],
        [1, 2, 3],
        [1, 1, 1],
        [2, 1],
        [2, 7, 4, 1, 2, 6, 2],
    ]:
        print(Solution().check(test))
