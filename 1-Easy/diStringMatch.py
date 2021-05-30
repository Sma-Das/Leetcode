class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        numbers = deque(range(len(s)+1))
        return [numbers.popleft() if l  == "I" else numbers.pop() for l in s+"A"]
