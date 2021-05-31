"""
85.86% // 72.88%
"""


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for x in reversed(range(16)):
            if n >= (s := 3 ** x):
                print(n, s)
                n -= s
        return n == 0


if __name__ == '__main__':
    for i in [12, 91, 21, 1536]:
        print(Solution().checkPowersOfThree(i))
