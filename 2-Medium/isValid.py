class Solution:
    def isValid(self, s: str) -> bool:
        i, s = 0, list(s)
        while i < len(s):
            if (l := len(s)) < 3:
                return False
            elif l == 3:
                return s == ["a", "b", "c"]
            if s[i:i+3] == ["a", "b", "c"]:
                del s[i:i+3]
                i -= 2
                continue
            i += 1
        return "".join(s) == "abc"
