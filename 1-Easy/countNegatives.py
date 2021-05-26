"""
90.58% faster
"""

def countNegatives(list[list[int]]) -> int:
    return sum(map(lambda x: sum(map(lambda y: 1 if y < 0 else 0, x)), grid))


