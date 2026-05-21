class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        pos = [0] * 26
        res = 0
        while right < len(s):
            index = ord(s[right]) - ord('a')
            while pos[index] != 0:
                pos[ord(s[left]) - ord('a')] -= 1
                left += 1
            pos[index] = 1

            if (right - left + 1) > res:
                res = right - left + 1
            right += 1
        return res