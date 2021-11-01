class Solution:
    def lengthOfLongestSubstring(self, input_string: str) -> int:
        seen, count, queue, max_len = {None}, 0, collections.deque(), 0
        for s in input_string:
            if s not in seen:
                count += 1
                seen.add(s), queue.append(s)
            else:
                while queue and not queue[0] == s:
                    seen.remove(queue.popleft())
                    count -= 1
            max_len = max(max_len, count)
        return max_len
