class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l, r = 0, 0
        res = 0
        while r < len(s):
            freq[ord(s[r]) - ord('A')] += 1
            c, m = r - l + 1, max(freq)
            while c - m > k and l <= r:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
                m = max(freq)
                c -= 1
            res = max(res, r-l+1)
            r += 1
        return res