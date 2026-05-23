class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        wl = 0
        for c in s:
            if c == " ":
                if wl:
                    res = wl
                    wl = 0
                continue
            wl += 1
        return wl if wl else res