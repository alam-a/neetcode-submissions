class Solution:
    def scoreOfString(self, s: str) -> int:
        acc = 0
        for i in range(len(s)-1):
            diff = abs(ord(s[i+1]) - ord(s[i]))
            acc += diff
        return acc