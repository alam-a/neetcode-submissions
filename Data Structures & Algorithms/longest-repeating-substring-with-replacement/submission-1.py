class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = len(s)
        freq = [0 for _ in range(26)]
        res = 0
        l, r = 0, 0
        while r < L:
            freq[ord(s[r]) - ord('A')] += 1
            def give_count_and_max():
                c, m = 0, 0
                for i in range(26):
                    c += freq[i]
                    if m < freq[i]:
                        m = freq[i]
                return c, m
            c, m = give_count_and_max()
            while c - m > k and l <= r:
                c, m = give_count_and_max()
                c -= 1
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, sum(freq))
            r += 1
        return res
