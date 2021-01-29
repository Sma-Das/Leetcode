def checkPossibility(nums: list):
    i, c = 0, None
    while i < (l := len(nums))-1:
        if nums[i] > nums[i+1]:
            if c is not None:
                print(c, "c")
                return False
            c = i
        i += 1
    return c is None or c == 0 or c == l-2 or nums[c-1] <= nums[c+1] or nums[c] <= nums[c+2]


if __name__ == '__main__':
    nums = [3, 4, 2, 3]
    print(checkPossibility(nums))
