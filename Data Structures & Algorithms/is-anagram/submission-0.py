class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sf, tf = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            sf[s[i]] += 1
            tf[t[i]] += 1
        return sf == tf
