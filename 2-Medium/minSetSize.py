from typing import List
import collections


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = collections.Counter(arr)  # speed increse for collections.Counter
        counter = list(counter.values())
        counter.sort(reverse=True)

        count = 0
        total = 0
        for num in counter:
            count += num
            total += 1
            if count >= len(arr)//2:
                break

        return total
