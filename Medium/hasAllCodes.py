from itertools import product
from functools import cache


@cache
def hasAllCodesOG(s, k):
    return any("".join(c) not in s for c in product("01", repeat=2))


def hasAllCodes(s, k):
    ''' updated solution, timespeed error'''
    return len({s[i - k: i] for i in range(k, len(s) + 1)}) == 1 << k


if __name__ == '__main__':
    print(hasAllCodes("00110110", 2))
