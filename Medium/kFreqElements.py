"""
Given a non-empty array of integers, return the k most frequent elements.
"""

# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


def topKFrequent(nums: list[int], k: int):
    num_dict = {}
    for key in set(nums):
        num_dict[key] = nums.count(key)
    most_freq = sorted(num_dict.values(), reverse=True)[:k]
    return [key for key, val in num_dict.items() if val in most_freq]


if __name__ == '__main__':
    print(topKFrequent(
        [1, 1, 1, 2, 2, 3],
        1
    ))
