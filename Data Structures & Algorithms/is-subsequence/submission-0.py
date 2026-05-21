class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si, ti = 0, 0
        while si < len(s):
            while ti < len(t) and s[si] != t[ti]:
                ti += 1
            if ti == len(t) or s[si] != t[ti]:
                return False
            si += 1
        return True