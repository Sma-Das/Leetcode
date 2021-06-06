class Solution:
    def isSumEqual(self, fW: str, sW: str, tW: str) -> bool:
        def num(s):
            a = ord("a")
            return int("".join(str(ord(v)-a) for v in s))
        return num(fW) + num(sW) == num(tW)

    def isSumEqual2(self, fW: str, sW: str, tW: str) -> bool:
        def n(s):
            return int("".join(str(ord(v)-ord('a')) for v in s))
        return n(fW) + n(sW) == n(tW)

    def isSumEqual3(self, fW: str, sW: str, tW: str) -> bool:
        l = {"a": "0", "b": "1", "c": "2", "d": "3", "e": "4",
             "f": "5", "g": "6", "h": "7", "i": "8", "j": "9"}

        def num(s):
            return int("".join(l[v] for v in s))
        return num(fW) + num(sW) == num(tW)

    def isSumEqual4(self, fW: str, sW: str, tW: str) -> bool:
        letters = {"a": "0", "b": "1", "c": "2", "d": "3", "e": "4",
                   "f": "5", "g": "6", "h": "7", "i": "8", "j": "9"}
        for l, v in letters.items():
            fW = fW.replace(l, v)
            sW = sW.replace(l, v)
            tW = tW.replace(l, v)
        return int(fW) + int(sW) == int(tW)

    def isSumEqual5(self, fW: str, sW: str, tW: str) -> bool:
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
        for l, v in zip(letters, range(10)):
            fW = fW.replace(l, str(v))
            sW = sW.replace(l, str(v))
            tW = tW.replace(l, str(v))
        return int(fW) + int(sW) == int(tW)

    def isSumEqual6(self, fW: str, sW: str, tW: str) -> bool:
        return int(fW.translate(t := str.maketrans("abcdefghij", "0123456789"))) + int(sW.translate(t)) == int(tW.translate(t))
