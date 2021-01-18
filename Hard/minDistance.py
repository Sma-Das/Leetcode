"""
Given the array houses and an integer k.
Where houses[i] is the location of the ith house along a street,
your task is to allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.
"""


def minDistance(houses: list[int], k: int):
    houses.sort()
    n = len(houses)

    def closest(i, j):
        median_loc = houses[(i + j) // 2]
        dist = 0
        for h_idx in range(i, j + 1):
            dist += abs(houses[h_idx] - median_loc)
        return dist

    def allocate(i, k, memo={}):
        if i == n:
            return 0
        elif (i, k) in memo:
            return memo[(i, k)]
        elif k == 1:
            memo[(i, k)] = closest(i, n - 1)
            return memo[(i, k)]
        min_dist = float('inf')
        for j in range(i, n):
            dist = closest(i, j) + allocate(j + 1, k - 1, memo)
            min_dist = min(min_dist, dist)

        memo[(i, k)] = min_dist
        return min_dist

    return allocate(0, k)


if __name__ == '__main__':
    print(minDistance(
        [2973, 9950, 709, 7492, 6043, 9053, 2839, 5183, 3894, 1151, 7039, 4145, 2710, 179, 9365, 1798, 1643, 3138, 8886, 5935, 2507, 8727, 4128, 6065, 2746, 319, 5074, 822, 8739, 1536, 7450, 272, 6181, 1511, 1645, 745, 1001,
            2947, 5308, 3599, 677, 8064, 8654, 1533, 2519, 1686, 5940, 5913, 848, 154, 3683, 8091, 3846, 6847, 2367, 5822, 9141, 1894, 9898, 3390, 1165, 7150, 5955, 2326, 9114, 1025, 5994, 4713, 7339, 2854, 2338, 7611, 747, 7963],
        27
    ))
