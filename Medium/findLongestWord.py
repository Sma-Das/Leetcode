def findLongest(s: str, dictionary: list) -> str:
    def inDic(word: str) -> bool:
        it = iter(s)
        return all(c in it for c in word)
    return min(
        filter(inDic, dictionary + ['']),
        key=lambda x: (-len(x), x)
    )
