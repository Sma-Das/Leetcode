from functools import reduce

"""
memory : 99.81% --> Best memory usage yet
"""


class Solution:
    def removeDuplicates(self, s: str) -> str:
        """
        memory : 99.81% --> Best memory usage yet // runtime is 18.28% though lol
        """
        return reduce(lambda x, y: x[:-1] if x and x[-1:] == y else x+y, s)

    def recur_removeDuplicates(self, s: str) -> str:
        def remove_duplicates(string: list) -> list:
            for i in range(len(string)-1):
                if string[i] == string[i+1]:
                    string.pop(i)
                    string.pop(i)
                    return remove_duplicates(string)
            return string
        return "".join(remove_duplicates(list(s)))

    def iter_removeDuplicates(self, s: str) -> str:
        stack = ""
        for letter in s:
            stack = stack[:-
                          1] if stack and stack[-1] == letter else stack+letter
        return stack
