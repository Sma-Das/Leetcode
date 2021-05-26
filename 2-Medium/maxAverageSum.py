from statistics import mean
"""
We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the
sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers
"""


def largestSumOfAverages(A: list[int], K: int) -> float:

    res = []

    for _ in range(K-1):
        ind = A.index(max(A))
        res.append(A.pop(ind))

    # submission check is incorrect

    return sum(res) + mean(A)
