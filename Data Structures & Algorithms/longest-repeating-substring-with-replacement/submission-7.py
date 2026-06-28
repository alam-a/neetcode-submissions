class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, res = 0, 0, 1
        freq = [0] * 26
        while r < len(s):
            freq[ord(s[r]) - ord('A')] += 1
            while (r - l + 1) - max(freq) > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
            res = max(res, r - l + 1)
            r += 1
        return res