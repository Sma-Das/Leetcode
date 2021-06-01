from collections import deque
from heapq import nsmallest


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        header, target, s = deque(nsmallest(k, s)), deque(
            s), deque([s[i] for i in range(k)])
        while header != target:
            s.remove((v := max(header)))
            header.remove(v)
            s.append(v)
            header.append(s[k-1])
        return "".join(s)

    def orderlyQueue2(self, S, K):
        return "".join(sorted(S)) if K > 1 else min(S[i:] + S[:i] for i in range(len(S)))
