def characterReplacement(s, k):
    max_length, i, seen = 0, 0, set()

    while i < (l := len(s)):
        curr, j, rem, length = s[i], i, k, 0
        while rem and j < l:
            if s[j] != curr or j in seen:  # if we've already seen it, then it isn't the same letter
                rem -= 1
            else:
                seen.add(j)
            length += 1
            j += 1
        max_length = max(max_length, length)
        i += 1
    return max_length


def characterReplacement2(s, k):
    maxLength, s_len = 0, len(s)
    for i, char in enumerate(s):
        length, rem = 0, k
        for j in range(i+1, s_len):
            if not rem:
                break
            if s[j] != char:
                rem -= 1
            length += 1
        maxLength = max(maxLength, length)
    return maxLength
