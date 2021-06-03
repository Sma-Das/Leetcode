class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def builder(s, history=dict(), log=set()):
            if s == "0":
                return "01"
            elif s == "1":
                return "10"
            elif s in log:
                return history[s]
            l = len(s)
            history[s] = builder(s[:l//2], history, log) + builder(s[l//2:], history, log)
            log.add(s)
            return history[s]
        s, l = "0", 1
        while k >= l:
            s = builder(s)
            l <<= 1
        return s[k-1]

    def kthGrammar2(self, n, k):
        '''
        My improved solution. O(log2(k)) // O(2^k)
        '''
        c, curr = 1, "01"
        while k >= c:
            curr = curr + curr[c//2:] + curr[:c//2]
            c <<= 1  # log2 since we are increasing by ^2
        return curr[k+1]

    def kthGrammar3(self, n, k):
        '''
        Given solution. O(k) // O(log2(k))
        '''
        return bin(k-1).count("1") & 1  # Count is an O(n) operation


if __name__ == '__main__':
    n, k = 30, 1 << 25-1
    print(Solution().kthGrammar(n, k))
    print(Solution().kthGrammar2(n, k))
    print(Solution().kthGrammar3(n, k))
