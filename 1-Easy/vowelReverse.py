def reverseVowels(s: str = ""):
    if not s:
        return ""
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    l, r = 0, len(s)-1
    left, right = False, False
    s = list(s)
    while l < r:
        if s[l] in vowels:
            left = True
        else:
            l += 1

        if s[r] in vowels:
            right = True
        else:
            r -= 1

        if left and right:
            s[l], s[r] = s[r], s[l]
            left, right = False, False
            l += 1
            r -= 1
    return "".join(s)


if __name__ == '__main__':
    reverseVowels("Hello")
    reverseVowels("Aa")
