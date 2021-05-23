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
        max_length = max(max_length, length)
        i += 1
    return max_length
