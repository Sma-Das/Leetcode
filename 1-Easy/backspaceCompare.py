from functools import reduce


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:  # O(n) / O(n)
        def perform_edits(string):
            string_list = list()
            for i, letter in enumerate(string):
                if letter == "#" and string_list:
                    string_list.pop()
                else:
                    string_list.append(letter)
            return string_list
        return perform_edits(s) == perform_edits(t)

    def backspaceCompare2(self, s, t):  # O(n) / O(1)
        def func(res, l): return res[:-1] if l == "#" else res + l
        return reduce(func, s, "") == reduce(func, t, "")
