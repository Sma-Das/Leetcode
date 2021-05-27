from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    def search_string(string1, i, string2):
        l2, c2 = len(string2), Counter(string2)
        l1 = len(string1)
        if i + l2 < l1 and Counter(string1[i:i+l2]) == c2:
            return True
        elif i - l2 > 0 and Counter(string1[i-l2:i]) == c2:
            return True
        return False
    return bool(sum(search_string(s2, i, s1) for i, v in enumerate(s2) if v in s1))
