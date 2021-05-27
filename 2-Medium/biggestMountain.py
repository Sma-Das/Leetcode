class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        length = len(arr)

        def search(i, step):
            nonlocal length, arr
            prev, l = arr[i], 0
            while 0 <= (i := i + step) < length:
                if arr[i] < prev:
                    l += 1
                    prev = arr[i]
            return l
        return max([dist if (dist := search(i, -1) + search(i, 1) + 1) >= 3 else 0 for i in range(1, length-1)])


if __name__ == '__main__':
    print(Solution().longestMountain([2, 1, 4, 7, 3, 2, 5]))
