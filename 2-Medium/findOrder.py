from bisect import insort
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses, prereq):
        courses = defaultdict(set)
        {insort(courses[c], p) for c, p in prereq}
        return sorted(range(numCourses), key=lambda x: len(courses[x]))


if __name__ == '__main__':
    Solution().findOrder(1, [])
