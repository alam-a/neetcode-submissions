class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l, r = 0, 0
        res = 1
        while r < len(s):
            freq[ord(s[r]) - ord('A')] += 1
            while (r - l + 1) - max(freq) > k and l <= r:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res