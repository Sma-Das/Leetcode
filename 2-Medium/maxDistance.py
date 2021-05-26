def maxDistanceBrute(nums1, nums2):
    max_dis = 0
    for i, v in enumerate(nums1):
        max_dis = max(max_dis, max(
            [j-i for j, val in enumerate(nums2[i:], start=i) if val >= v]+[0]))
    return max_dis


def maxDistance(nums1, nums2):
    maxval = i = j = 0
    len_nums1, len_nums2 = len(nums1), len(nums2)
    while i < len_nums1 and j != len_nums2:
        if (l := nums1[i]) <= (r := nums2[j]):
            j += 1
        elif l > r:
            i += 1
        maxval = max(maxval, j-i-1)
    return maxval
