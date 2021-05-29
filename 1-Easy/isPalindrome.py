'''
86.85% Speed and 91.47% Memory
'''
from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = deque(str(x))
        while x and len(x) > 1:
            if not x.popleft() == x.pop():
                return False
        return True

    def isPalindrome2(self, x: int) -> bool:
        return (x := str(x)) == x[::-1]
