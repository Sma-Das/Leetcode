class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort(reverse=True)
        l, r = 0, len(people)-1
        while l <= r:  # Prioritise fatasses
            if people[l] + people[r] <= limit:
                r -= 1  # fatty + thinny
            l += 1
        return l
