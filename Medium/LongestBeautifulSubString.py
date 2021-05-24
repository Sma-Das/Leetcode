from re import findall


def longestBeautifulSubstring(word: str) -> int:
    return len(max(findall(r'a+e+i+o+u+', word)+[''], key=len))
