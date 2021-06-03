from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = collections.defaultdict(list)
        for c, p in prerequisites:
            stack = [p]
            while stack:
                curr = stack.pop()
                stack += (n := courses[curr])
                if c == curr or c in n:
                    return False
            courses[c].append(p)
        return True


if __name__ == '__main__':
    tests = [
        [20,
         [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]],  # False
        [2,
         [[1, 0]]],  # True
        [2,
         [[1, 0], [0, 1]]],  # False
        [3,
         [[1, 0], [0, 2], [2, 3], [3, 1]]],  # False
    ]
    for num, courses in tests:
        print(Solution().canFinish(num, courses))
