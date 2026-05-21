class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, pos, curr, maximum = 0, {}, 0, 0
        while i < len(s):
            if s[i] in pos:
                maximum = max(curr, maximum)
                pos[s[i]] = i
                curr = i - pos[s[i-1]] + 1
            else:
                curr += 1
                pos[s[i]] = i
            i += 1

        return max(curr, maximum)
        