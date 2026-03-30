class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        left, right = 0, 0
        pos = defaultdict(int)
        res = 0
        while right < len(s):
            while pos[s[right]] != 0:
                pos[s[left]] -= 1
                left += 1
            pos[s[right]] = 1

            if (right - left + 1) > res:
                res = right - left + 1
            right += 1
        return res