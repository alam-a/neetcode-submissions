class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        wl = 0
        for c in s:
            if c == " ":
                if wl:
                    res = max(res, wl)
                    wl = 0
                continue
            wl += 1
        return max(res, wl)