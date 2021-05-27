"""
Given a non-empty array of integers, return the k most frequent elements.
"""
from collections import Counter
# Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


def topKFrequent(nums: list[int], k: int) -> list:
    '''
    Original and slower solution
    '''
    # num_dict = {}
    # for key in set(nums):
    #     num_dict[key] = nums.count(key)

    num_dict = {key: nums.count(key) for key in set(nums)}
    most_freq = sorted(num_dict.values(), reverse=True)[:k]
    return [key for key, val in num_dict.items() if val in most_freq]


def topKFrequent2(nums, k):
    ''' Lol '''
    return [v for v, _ in Counter(nums).most_common(k)]


if __name__ == '__main__':
    print(topKFrequent2(
        [1, 1, 1, 2, 2, 3],
        2
    ))
