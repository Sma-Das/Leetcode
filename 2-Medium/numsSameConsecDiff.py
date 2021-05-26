from functools import cache


def numsSameConsecDiff(n, k):
    @cache
    def builder(curr, rem, delta, string=""):
        if not 0 <= curr <= 9:
            return ""
        elif not rem:
            return string
        return builder(curr+delta, rem-1, delta, string + str(curr)) + builder(curr-delta, rem-1, -delta, string + str(curr))
    res = set()
    for i in range(1, 10):
        v = builder(i, n, k)
        [res.add(v[c:c+n]) for c in range(0, len(v), n)]
    return res


if __name__ == '__main__':
    print(numsSameConsecDiff(8, 1))
